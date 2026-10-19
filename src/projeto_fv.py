"""SPGER0046: local measurements, electrical evaluation and exploratory reverse POA.

Measured, derived, estimated and hypothetical quantities remain distinguishable.
No missing daytime observations are interpolated. All internal powers are W.
"""
from pathlib import Path
import hashlib
import io
import json
import platform
import urllib.request
import zipfile

import numpy as np
import pandas as pd
import pvlib
import matplotlib.pyplot as plt


def load_config(root):
    root = Path(root)
    return json.loads((root / 'config/projeto.json').read_text())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def read_sources(root, include_nasa=False):
    """Read verified original bytes; recreate the raw ZIP from official URLs if needed."""
    root = Path(root)
    raw = root / 'data/raw'
    raw.mkdir(parents=True, exist_ok=True)
    manifest = json.loads((raw / 'fontes_pvdaq.json').read_text())
    archive = raw / 'pvdaq_2107_2024_originais.zip'
    if not archive.exists():
        temporary = archive.with_suffix('.download')
        with zipfile.ZipFile(temporary, 'w', zipfile.ZIP_DEFLATED) as z:
            for item in manifest:
                with urllib.request.urlopen(item['url'], timeout=60) as response:
                    content = response.read()
                assert len(content) == item['bytes'] and digest(content) == item['sha256'], item['file']
                z.writestr(item['file'], content)
        temporary.replace(archive)
    frames = {}
    with zipfile.ZipFile(archive) as z:
        for item in manifest:
            content = z.read(item['file'])
            assert len(content) == item['bytes'] and digest(content) == item['sha256'], item['file']
            if item['file'].endswith('.json'):
                metadata = json.loads(content)
            else:
                frames[item['file']] = pd.read_csv(io.BytesIO(content), index_col=0, parse_dates=True)
    if not include_nasa:
        return frames, metadata, None
    nasa_source = json.loads((raw / 'fonte_nasa.json').read_text())
    nasa_file = raw / nasa_source['file']
    if not nasa_file.exists():
        with urllib.request.urlopen(nasa_source['url'], timeout=60) as response:
            content = response.read()
        assert digest(content) == nasa_source['sha256']
        nasa_file.write_bytes(content)
    content = nasa_file.read_bytes()
    assert digest(content) == nasa_source['sha256']
    return frames, metadata, json.loads(content)


def geometry(index, cfg, minutes=15):
    """Use interval midpoints for SPA; restore interval-start index explicitly."""
    mid = index + pd.Timedelta(minutes=minutes/2)
    site = cfg['site']
    location = pvlib.location.Location(site['latitude'], site['longitude'], tz='UTC', altitude=site['altitude_m'])
    result = location.get_solarposition(mid)
    result.index = index
    result['dni_extra_Wm2'] = np.asarray(pvlib.irradiance.get_extra_radiation(mid, method='spencer'))
    result['extraterrestrial_horizontal_Wm2'] = result.dni_extra_Wm2 * np.maximum(np.cos(np.deg2rad(result.zenith)), 0)
    result['aoi_deg'] = pvlib.irradiance.aoi(site['tilt_deg'], site['azimuth_deg'], result.apparent_zenith, result.azimuth)
    return result


def noaa_elevation(index, cfg, minutes=15):
    """Reproduce the initial availability denominator, independent of power."""
    t = (index + pd.Timedelta(minutes=minutes/2)).tz_convert('UTC')
    n = np.where(t.is_leap_year, 366, 365)
    g = 2*np.pi/n*(t.dayofyear-1+(t.hour-12)/24)
    eot = 229.18*(.000075+.001868*np.cos(g)-.032077*np.sin(g)-.014615*np.cos(2*g)-.040849*np.sin(2*g))
    dec = .006918-.399912*np.cos(g)+.070257*np.sin(g)-.006758*np.cos(2*g)+.000907*np.sin(2*g)-.002697*np.cos(3*g)+.00148*np.sin(3*g)
    solar = t.hour*60+t.minute+t.second/60+eot+4*cfg['site']['longitude']
    hour_angle = np.deg2rad(solar/4-180)
    lat = np.deg2rad(cfg['site']['latitude'])
    return np.rad2deg(np.arcsin(np.sin(lat)*np.sin(dec)+np.cos(lat)*np.cos(dec)*np.cos(hour_angle)))


def prepare(root, cfg, include_nasa=False):
    frames, metadata, nasa_json = read_sources(root, include_nasa=include_nasa)
    tz = cfg['site']['timezone']
    start = pd.Timestamp(cfg['period']['start_local'], tz=tz).tz_convert('UTC')
    end = pd.Timestamp(cfg['period']['end_exclusive_local'], tz=tz).tz_convert('UTC')
    index = pd.date_range(start, end, freq='15min', inclusive='left')
    local_start = start.tz_convert(tz).tz_localize(None)
    local_end = end.tz_convert(tz).tz_localize(None)
    def subset(frame):
        # Select the quarter before localizing: the full year contains DST transitions.
        frame = frame.loc[(frame.index >= local_start) & (frame.index < local_end)].copy()
        assert not frame.index.duplicated().any()
        assert frame.index.is_monotonic_increasing
        frame.index = frame.index.tz_localize(tz, ambiguous='raise', nonexistent='raise').tz_convert('UTC')
        return frame
    env = subset(frames['2107_environment_data_2024.csv'])
    irradiance = subset(frames['2107_irradiance_data_2024.csv'])
    meter = subset(frames['2107_meter_15m_data_2024.csv'])
    electrical = subset(frames['2107_electrical_data_2024.csv'])
    power_cols = [c for c in electrical if 'ac_power' in c]
    assert len(power_cols) == cfg['system']['n_inverters']
    d = pd.DataFrame(index=index)
    d['temp_air_C'] = (env.iloc[:, 0].reindex(index)-32)*5/9
    d['wind_ms'] = env.iloc[:, 1].reindex(index)*0.44704
    d['wind_direction_deg'] = env.iloc[:, 2].reindex(index)
    counts_irr = irradiance.iloc[:, 0].resample('15min').count().reindex(index).fillna(0)
    d['poa_measured_Wm2'] = irradiance.iloc[:, 0].resample('15min').mean().reindex(index)
    d['irradiance_3_samples'] = counts_irr.eq(3)
    ac_samples = electrical[power_cols].resample('15min').count().reindex(index).fillna(0)
    d['inverters_3_samples'] = ac_samples.eq(3).all(axis=1)
    d['ac_meter_W'] = meter.iloc[:, 0].reindex(index)*1000
    inv = electrical[power_cols].resample('15min').mean().reindex(index)*1000
    inv.columns = [f'inv_{n:02d}_ac_W' for n in range(1, 25)]
    d['ac_sum_inverters_W'] = inv.sum(axis=1, min_count=24)
    dc = []
    for n in range(1, 25):
        current = next(c for c in electrical if c.startswith(f'inv_{n:02d}_dc_current'))
        voltage = next(c for c in electrical if c.startswith(f'inv_{n:02d}_dc_voltage'))
        dc.append(electrical[current]*electrical[voltage])
    # Derived from V*I, not an independently measured DC power channel.
    d['dc_VI_derived_W'] = pd.concat(dc, axis=1).sum(axis=1, min_count=24).resample('15min').mean().reindex(index)
    d['noaa_elevation_deg'] = noaa_elevation(index, cfg)
    d['daylight'] = d.noaa_elevation_deg.ge(cfg['period']['daylight_elevation_deg'])
    d['availability'] = (d[['temp_air_C','wind_ms','wind_direction_deg','poa_measured_Wm2','ac_meter_W']].notna().all(axis=1)
        & d.irradiance_3_samples & d.inverters_3_samples)
    d['physical_bounds'] = (d.temp_air_C.between(-30, 60) & d.wind_ms.between(0, 60)
        & d.poa_measured_Wm2.between(0, 1800) & d.ac_meter_W.between(0, 893000*1.05))
    d['paired_daylight'] = d.daylight & d.availability & d.physical_bounds
    d = d.join(geometry(index, cfg))
    hourly_obs = d[['poa_measured_Wm2','ac_meter_W','ac_sum_inverters_W','temp_air_C','wind_ms']].resample('h').mean()
    full = d[['irradiance_3_samples','inverters_3_samples','availability']].resample('h').sum().eq(4).all(axis=1)
    hourly_obs['full_hour'] = full
    stats = {'expected_daylight_15m':int(d.daylight.sum()),'available_daylight_15m':int((d.daylight & d.availability).sum()),
        'paired_daylight_after_bounds':int(d.paired_daylight.sum()),'quarter_days':int((end-start)/pd.Timedelta(days=1)),
        'meter_records':int(d.ac_meter_W.notna().sum()),'NASA_used':False}
    ctx = {'data':d,'hourly_obs':hourly_obs,'inverters':inv,'metadata':metadata,'audit':stats,'config':cfg,'root':Path(root),
           'module':json.loads((Path(root)/'config/modulo_cec.json').read_text())}
    if nasa_json is None:
        return ctx
    # Hourly POWER energy per unit area / 1 hour = hourly mean irradiance.
    source = pd.DataFrame(nasa_json['properties']['parameter'])
    source.index = pd.to_datetime(source.index, format='%Y%m%d%H', utc=True)
    source = source.replace(nasa_json['header']['fill_value'], np.nan).astype(float)
    source.index += pd.Timedelta(hours=cfg['assumptions']['nasa_hour_label_offset_hours'])
    ren = {'ALLSKY_SFC_SW_DWN':'ghi_Wm2','ALLSKY_SFC_SW_DNI':'dni_Wm2','ALLSKY_SFC_SW_DIFF':'dhi_Wm2','T2M':'temp_air_C','WS10M':'wind_ms'}
    nasa = source.rename(columns=ren).loc[(source.index >= start) & (source.index < end)].copy()
    expected = pd.date_range(start, end, freq='h', inclusive='left')
    nasa = nasa.reindex(expected)
    assert len(nasa) == 91*24
    nasa = nasa.join(geometry(nasa.index, cfg, minutes=60))
    nasa['daylight'] = noaa_elevation(nasa.index, cfg, minutes=60) >= cfg['period']['daylight_elevation_deg']
    nasa['ghi_closure_residual_Wm2'] = nasa.ghi_Wm2-(nasa.dni_Wm2*np.maximum(np.cos(np.deg2rad(nasa.apparent_zenith)),0)+nasa.dhi_Wm2)
    nasa['clearness_index'] = nasa.ghi_Wm2/nasa.extraterrestrial_horizontal_Wm2.where(nasa.extraterrestrial_horizontal_Wm2>20)
    hourly_obs = d[['poa_measured_Wm2','ac_meter_W','ac_sum_inverters_W','temp_air_C','wind_ms']].resample('h').mean()
    full = d[['irradiance_3_samples','inverters_3_samples','availability']].resample('h').sum().eq(4).all(axis=1)
    hourly_obs['full_hour'] = full
    stats = {'expected_daylight_15m':int(d.daylight.sum()),'available_daylight_15m':int((d.daylight & d.availability).sum()),
        'paired_daylight_after_bounds':int(d.paired_daylight.sum()),'quarter_days':91,
        'meter_records':int(d.ac_meter_W.notna().sum()),'nasa_hours':len(nasa),
        'nasa_complete_hours':int(nasa[list(ren.values())].notna().all(axis=1).sum())}
    stats['NASA_used'] = True
    ctx.update({'nasa':nasa,'audit':stats})
    return ctx


def transpose(nasa, cfg, tilt=None, azimuth=None, albedo=None, model=None):
    tilt = cfg['site']['tilt_deg'] if tilt is None else tilt
    azimuth = cfg['site']['azimuth_deg'] if azimuth is None else azimuth
    albedo = cfg['assumptions']['albedo'] if albedo is None else albedo
    columns = ['poa_global','poa_direct','poa_diffuse','poa_sky_diffuse','poa_ground_diffuse']
    out = pd.DataFrame(np.nan, index=nasa.index, columns=columns)
    valid = nasa[['ghi_Wm2','dni_Wm2','dhi_Wm2']].notna().all(axis=1)
    zcolumn = 'zenith' if nasa.attrs.get('origin')=='reverse_POA' else 'apparent_zenith'
    sun = valid & nasa[zcolumn].lt(90)
    am = pvlib.atmosphere.get_relative_airmass(nasa.loc[sun,'apparent_zenith'])
    modeled = pvlib.irradiance.get_total_irradiance(tilt, azimuth, nasa.loc[sun,zcolumn],
        nasa.loc[sun,'azimuth'], nasa.loc[sun,'dni_Wm2'], nasa.loc[sun,'ghi_Wm2'], nasa.loc[sun,'dhi_Wm2'],
        dni_extra=nasa.loc[sun,'dni_extra_Wm2'], airmass=am, albedo=albedo,
        model=model or ('perez-driesse' if nasa.attrs.get('origin')=='reverse_POA' else 'perez'))
    out.loc[sun, columns] = modeled[columns]
    out.loc[valid & ~sun, columns] = 0
    return out


def module_mpp(g, temperature, module):
    g = pd.Series(g)
    temp = pd.Series(temperature, index=g.index)
    out = pd.DataFrame(np.nan, index=g.index, columns=['p_mp','v_mp','i_mp','i_sc','v_oc'])
    valid = g.notna() & temp.notna()
    positive = valid & g.gt(0)
    out.loc[valid & ~positive] = 0
    if positive.any():
        params = pvlib.pvsystem.calcparams_cec(g.loc[positive], temp.loc[positive], module['alpha_sc'], module['a_ref'],
            module['I_L_ref'], module['I_o_ref'], module['R_sh_ref'], module['R_s'], module['Adjust'])
        result = pvlib.pvsystem.singlediode(*params, method='lambertw')
        out.loc[positive] = result[out.columns]
    return out


def inverter_pvwatts_stages(pdc, capacity, eta_nom=.98, eta_ref=.9637):
    pdc = pd.Series(pdc)
    pdc0 = capacity/eta_nom
    zeta = pdc/pdc0
    eta = (eta_nom/eta_ref)*(-.0162*zeta-.0059/zeta.where(zeta>0)+.9858)
    before_clip = (eta*pdc).clip(lower=0)
    before_clip.loc[pdc.eq(0)] = 0
    pac = before_clip.clip(upper=capacity)
    return pd.DataFrame({'ac_before_clip_W':before_clip,'ac_modeled_W':pac,'clipping_W':before_clip-pac},index=pdc.index)


def simulate(poa, temp, wind, cfg, module, ac_each=None, thermal=None):
    a = cfg['assumptions']
    poa = pd.Series(poa)
    temp = pd.Series(temp, index=poa.index)
    wind = pd.Series(wind, index=poa.index)
    u0,u1 = (a['faiman_u0'],a['faiman_u1']) if thermal is None else thermal
    effective = poa*(1-a['soiling_fraction'])
    tcell = pvlib.temperature.faiman(effective,temp,wind,u0=u0,u1=u1)
    at25 = module_mpp(poa,pd.Series(25.,index=poa.index),module)
    optical25 = module_mpp(effective,pd.Series(25.,index=poa.index),module)
    hot = module_mpp(effective,tcell,module)
    n = cfg['system']['n_modules']
    p0 = cfg['system']['metadata_p0_kw']*1000
    loss_dc = 1-(1-a['dc_wiring_fraction'])*(1-a['dc_mismatch_fraction'])*(1-a['dc_connections_fraction'])
    out = pd.DataFrame({'poa_Wm2':poa,'effective_poa_Wm2':effective,'temp_cell_proxy_C':tcell,
        'ideal_linear_W':p0*poa/1000,'sdm25_W':at25.p_mp*n,'optical25_W':optical25.p_mp*n,
        'dc_gross_W':hot.p_mp*n,'dc_net_W':hot.p_mp*n*(1-loss_dc)},index=poa.index)
    capacity = cfg['system']['n_inverters']*(a['inverter_capacity_baseline_w_each'] if ac_each is None else ac_each)
    stages = inverter_pvwatts_stages(out.dc_net_W,capacity,a['inverter_eta_nom'],a['inverter_eta_ref'])
    out = out.join(stages)
    out['ac_final_W'] = out.ac_modeled_W*(1-a['ac_wiring_fraction'])
    out['pvwatts_dc_comparison_W'] = pvlib.pvsystem.pvwatts_dc(effective,tcell,module['STC']*n,module['gamma_r']/100)*(1-loss_dc)
    out['p_mp_module_W'] = hot.p_mp
    out['v_mp_module_V'] = hot.v_mp
    out['i_mp_module_A'] = hot.i_mp
    return out


def metrics(observed, modeled, label, normalization='mean_observed'):
    pair = pd.concat([pd.Series(observed).rename('obs'),pd.Series(modeled).rename('mod')],axis=1).dropna()
    if pair.empty:
        raise ValueError(f'No paired data: {label}')
    y,p = pair.obs.to_numpy(),pair['mod'].to_numpy()
    error = p-y
    mse = float(np.mean(error**2))
    denom = np.mean(y)
    sst = float(np.sum((y-y.mean())**2))
    return {'comparison':label,'n':len(pair),'MBE':float(error.mean()),'MAE':float(np.abs(error).mean()),'RMSE':mse**.5,
        'nMBE_percent':float(100*error.mean()/denom) if denom else np.nan,
        'nRMSE_percent':float(100*mse**.5/denom) if denom else np.nan,
        'r':float(np.corrcoef(y,p)[0,1]) if np.std(y)>0 and np.std(p)>0 else np.nan,
        'R2':float(1-np.sum(error**2)/sst) if sst else np.nan,'normalization':'mean of paired observations'}


def run_models(ctx):
    cfg = ctx['config']
    module = json.loads((ctx['root']/'config/modulo_cec.json').read_text())
    d,nasa,obs = ctx['data'],ctx.get('nasa'),ctx['hourly_obs']
    a = simulate(d.poa_measured_Wm2,d.temp_air_C,d.wind_ms,cfg,module)
    mask = d.paired_daylight
    rows = [metrics(d.loc[mask,'ac_meter_W']/1000,a.loc[mask,'ac_final_W']/1000,'A: POA e meteorologia locais → medidor AC [kW]'),
        metrics(d.loc[mask,'ac_sum_inverters_W']/1000,a.loc[mask,'ac_final_W']/1000,'A: POA e meteorologia locais → soma dos inversores [kW]')]
    if nasa is not None:
        poa = transpose(nasa,cfg)
        b = simulate(poa.poa_global,nasa.temp_air_C,nasa.wind_ms,cfg,module)
        ctx.update({'model_b':b,'poa_nasa':poa})
        common = nasa.daylight & obs.ac_meter_W.notna() & b.ac_final_W.notna()
        rows.append(metrics(obs.loc[common,'ac_meter_W']/1000,b.loc[common,'ac_final_W']/1000,'B: recurso e meteorologia NASA → medidor AC [kW]'))
        check = nasa.daylight & obs.full_hour & obs.poa_measured_Wm2.notna() & poa.poa_global.notna()
        rows.append(metrics(obs.loc[check,'poa_measured_Wm2'],poa.loc[check,'poa_global'],'NASA/Perez → POA medida [W/m²]'))
    # Empirical adjustment is fitted only on April; report June separately.
    month = d.index.tz_convert(cfg['site']['timezone']).month
    train = mask & (month==4)
    k = float(np.dot(a.loc[train,'ac_final_W'],d.loc[train,'ac_meter_W'])/np.dot(a.loc[train,'ac_final_W'],a.loc[train,'ac_final_W']))
    for m,label in [(4,'Abril (ajuste)'),(5,'Maio (verificação)'),(6,'Junho (avaliação separada)')]:
        use = mask & (month==m)
        rows.append(metrics(d.loc[use,'ac_meter_W']/1000,a.loc[use,'ac_final_W']*k/1000,f'A × k empírico: {label} [kW]'))
    # Compare capacity assumptions without selecting one on the test set.
    sensitivities = []
    for capacity in [27600,30000]:
        s = simulate(d.poa_measured_Wm2,d.temp_air_C,d.wind_ms,cfg,module,ac_each=capacity)
        sensitivities.append(metrics(d.loc[mask,'ac_meter_W']/1000,s.loc[mask,'ac_final_W']/1000,f'Paco = {capacity/1000:g} kW/inversor'))
    ctx.update({'module':module,'model_a':a,'metrics':pd.DataFrame(rows),
        'capacity_sensitivity':pd.DataFrame(sensitivities),'empirical_scale_april':k})
    return ctx


def performance(ctx):
    d,a,cfg = ctx['data'],ctx['model_a'],ctx['config']
    use = d.paired_daylight & a.ac_final_W.notna()
    dt = cfg['period']['aggregation_minutes']/60
    p0kw = cfg['system']['metadata_p0_kw']
    energy = lambda v: float(v.loc[use].sum()*dt/1000)
    hpoa = float(d.loc[use,'poa_measured_Wm2'].sum()*dt/1000)
    eac_obs,edc,eac = energy(d.ac_meter_W),energy(a.dc_net_W),energy(a.ac_final_W)
    yr,ya,yf,yfobs = hpoa,edc/p0kw,eac/p0kw,eac_obs/p0kw
    stages = [('Referência linear STC',a.ideal_linear_W),('Resposta SDM a 25 °C',a.sdm25_W),
        ('Após hipótese óptica',a.optical25_W),('Após temperatura modelada',a.dc_gross_W),('Após perdas CC assumidas',a.dc_net_W),
        ('Após conversão, antes do clipping',a.ac_before_clip_W),('Após clipping',a.ac_modeled_W),('Após perdas CA assumidas',a.ac_final_W)]
    stage_df = pd.DataFrame([{'stage':name,'energy_kWh':energy(v)} for name,v in stages])
    stage_df['change_to_next_kWh'] = stage_df.energy_kWh-stage_df.energy_kWh.shift(-1)
    yields = pd.DataFrame([{'scope':'Intervalos pareados, Sol ≥10°; não total do trimestre',
        'n_15min':int(use.sum()),'H_POA_kWh_m2':hpoa,'E_DC_model_kWh':edc,'E_AC_model_kWh':eac,'E_AC_observed_kWh':eac_obs,
        'Yr_h':yr,'Ya_model_h':ya,'Yf_model_kWh_kWp':yf,'Yf_observed_kWh_kWp':yfobs,'PR_model':yf/yr,
        'PR_observed_paired':yfobs/yr,'Lc_model_h':yr-ya,'Ls_model_h':ya-yf}])
    full = {'E_AC_meter_full_quarter_kWh':float(d.ac_meter_W.sum()*.25/1000),'meter_expected_15min':len(d),
        'meter_available_15min':int(d.ac_meter_W.notna().sum()),'Yf_meter_full_quarter_kWh_kWp':float(d.ac_meter_W.sum()*.25/1000/p0kw)}
    if 'model_b' in ctx:
        full.update({'E_AC_NASA_model_full_quarter_kWh':float(ctx['model_b'].ac_final_W.sum()/1000),
                     'NASA_model_hours':int(ctx['model_b'].ac_final_W.notna().sum())})
    inv = ctx['inverters']
    bright = d.poa_measured_Wm2.gt(200) & d.availability
    flags = pd.DataFrame({'inverter':inv.columns,
        'zero_AC_with_POA_gt200_intervals':[(inv[c].le(1)&bright).sum() for c in inv],
        'note':'Operational or acquisition flag; no cause attributed and not removed from validation'})
    consistency = metrics(d.loc[use,'ac_meter_W']/1000,d.loc[use,'ac_sum_inverters_W']/1000,'Soma dos inversores → medidor [kW]')
    ctx.update({'yields':yields,'energy_stages':stage_df,'full_quarter':full,'operational_flags':flags,'meter_inverter_consistency':consistency})
    return ctx


def environmental_scenarios(ctx):
    n,cfg = ctx.get('resource_for_scenarios',ctx.get('nasa')),ctx['config']
    rows=[]
    if n is not None:
        for albedo in [.1,.2,.4]:
            p=transpose(n,cfg,albedo=albedo)
            rows.append({'scenario':f'Albedo {albedo:.1f} (hipótese)','H_POA_kWh_m2':float(p.poa_global.sum()/1000)})
        for tilt,az,label in [(0,180,'Horizontal'),(25,180,'Arranjo real: 25°, sul'),(90,180,'Fachada sul'),(90,90,'Fachada leste'),(90,270,'Fachada oeste')]:
            p=transpose(n,cfg,tilt=tilt,azimuth=az)
            rows.append({'scenario':label,'H_POA_kWh_m2':float(p.poa_global.sum()/1000)})
    d=ctx['data']; mask=d.paired_daylight
    sensitivity=[]
    for soiling in [0,.02,.05]:
        for u0,u1,label in [(25,6.84,'Ventilação de referência'),(15,3,'Menor ventilação, cenário')]:
            c=json.loads(json.dumps(cfg));c['assumptions']['soiling_fraction']=soiling
            m=simulate(d.poa_measured_Wm2,d.temp_air_C,d.wind_ms,c,ctx['module'],thermal=(u0,u1))
            sensitivity.append({'soiling_assumed':soiling,'thermal_scenario':label,'E_AC_paired_kWh':float(m.loc[mask,'ac_final_W'].sum()*.25/1000)})
    return pd.DataFrame(rows),pd.DataFrame(sensitivity)


def bipv_scenario(ctx):
    cfg,n = ctx['config'],ctx.get('resource_for_scenarios',ctx.get('nasa'))
    if n is None:
        raise ValueError('BIPV requires estimated components; run reverse_components first.')
    b=cfg['bipv'];a=cfg['assumptions']
    alpha=1-b['rho_solar']-b['tau_solar']
    assert 0<=alpha<=1 and 0<=b['tau_visible']<=1
    comparisons=[]
    for tilt,az,label,thermal in [(25,180,'Inclinado de referência',(25,6.84)),(90,180,'Fachada sul',(15,3)),
                                  (90,90,'Fachada leste',(15,3)),(90,270,'Fachada oeste',(15,3))]:
        poa=transpose(n,cfg,tilt=tilt,azimuth=az).poa_global
        modeled=simulate(poa,n.temp_air_C,n.wind_ms,cfg,ctx['module'],thermal=thermal)
        # Retain the same module, losses and DC/AC ratio; normalize, do not
        # silently replace the array by a different 1 kW inverter system.
        h=float(poa.sum()/1000)
        e=float(modeled.ac_final_W.sum()/1000/cfg['system']['metadata_p0_kw'])
        comparisons.append({'scenario':label,'H_POA_estimated_kWh_m2':h,'E_AC_for_1kWp_kWh':e,'PR_modeled':e/h,'n_input_hours':len(n),'scope':'selected complete daytime hours; not full-quarter energy' if n.attrs.get('origin')=='reverse_POA' else 'full-quarter NASA scenario','resource_origin':n.attrs.get('origin','NASA'),'status':'hypothetical; no facade observations'})
    poa=transpose(n,cfg,tilt=b['tilt_deg'],azimuth=b['azimuth_deg']).poa_global
    temp=pvlib.temperature.faiman(poa,n.temp_air_C,n.wind_ms,u0=b['faiman_u0'],u1=b['faiman_u1'])
    eta=(b['reference_efficiency']*(1+b['gamma_pdc_per_C']*(temp-25))).clip(0,alpha)
    incident=poa*b['area_m2'];electric=eta*incident;heat_abs=(alpha-eta)*incident
    f=b['inward_heat_fraction']
    out=pd.DataFrame({'incident_W':incident,'reflected_W':b['rho_solar']*incident,'transmitted_W':b['tau_solar']*incident,
        'electrical_DC_W':electric,'absorbed_heat_inward_W':f*heat_abs,'absorbed_heat_outward_W':(1-f)*heat_abs,
        'solar_heat_gain_W':b['tau_solar']*incident+f*heat_abs,
        'SHGC_equivalent_simplified':b['tau_solar']+f*(alpha-eta),'tau_visible_assumed':b['tau_visible']},index=n.index)
    out['balance_residual_W']=out.incident_W-out[['reflected_W','transmitted_W','electrical_DC_W','absorbed_heat_inward_W','absorbed_heat_outward_W']].sum(axis=1)
    assert out.balance_residual_W.abs().max()<1e-7
    summary=pd.DataFrame([{'component':c,'energy_kWh':float(out[c].sum()/1000),'status':'hypothetical solar-only balance'} for c in
        ['incident_W','reflected_W','transmitted_W','electrical_DC_W','absorbed_heat_inward_W','absorbed_heat_outward_W','solar_heat_gain_W']])
    return pd.DataFrame(comparisons),out,summary


def module_curves(ctx):
    m=ctx['module'];curves=[]
    for g,t in [(300,25),(600,25),(1000,25),(1000,45)]:
        par=pvlib.pvsystem.calcparams_cec(g,t,m['alpha_sc'],m['a_ref'],m['I_L_ref'],m['I_o_ref'],m['R_sh_ref'],m['R_s'],m['Adjust'])
        sd=pvlib.pvsystem.singlediode(*par)
        v=np.linspace(0,float(sd['v_oc']),160)
        current=pvlib.pvsystem.i_from_v(v,*par)
        curves.append(pd.DataFrame({'voltage_V':v,'current_A':current,'power_W':v*current,'G_Wm2':g,'T_C':t}))
    return pd.concat(curves,ignore_index=True)


def reverse_components(ctx):
    """Exploratory hourly reverse transposition, never an independent sensor.

    Restrict a priori to complete local inputs, zenith <= 80°, AOI <= 80°.
    This filter limits horizon problems but does not prove uniqueness.
    All excluded/failed hours remain in the diagnostic table.
    """
    cfg,d=ctx['config'],ctx['data']
    h=ctx['hourly_obs'].copy().join(geometry(ctx['hourly_obs'].index,cfg,minutes=60))
    complete=(d[['temp_air_C','wind_ms','poa_measured_Wm2']].notna().resample('h').sum().eq(4).all(axis=1)
              & d.irradiance_3_samples.resample('h').sum().eq(4))
    aoi=pvlib.irradiance.aoi(cfg['site']['tilt_deg'],cfg['site']['azimuth_deg'],h.zenith,h.azimuth)
    candidate=complete & h.zenith.le(80) & aoi.le(80) & h.poa_measured_Wm2.between(0,1800)
    result=h[['poa_measured_Wm2','zenith','apparent_zenith','azimuth','dni_extra_Wm2']].copy()
    result['input_complete']=complete
    result['eligible_geometry']=h.zenith.le(80)&aoi.le(80)
    result['aoi_true_deg']=aoi
    result['status']='excluded_geometry_or_missing_input'
    result['converged']=False
    result[['ghi_estimated_Wm2','dni_estimated_Wm2','dhi_estimated_Wm2','poa_reconstructed_Wm2','iterations']]=np.nan
    use=h.loc[candidate]
    am=pvlib.atmosphere.get_relative_airmass(use.apparent_zenith)
    ghi,converged,niter=pvlib.irradiance.ghi_from_poa_driesse_2024(
        cfg['site']['tilt_deg'],cfg['site']['azimuth_deg'],use.zenith,use.azimuth,
        use.poa_measured_Wm2,use.dni_extra_Wm2,airmass=am,albedo=cfg['assumptions']['albedo'],
        xtol=0.01,full_output=True)
    components=pvlib.irradiance.erbs_driesse(ghi,use.zenith,dni_extra=use.dni_extra_Wm2)
    result.loc[candidate,'ghi_estimated_Wm2']=np.asarray(ghi)
    result.loc[candidate,'dni_estimated_Wm2']=np.asarray(components['dni'])
    result.loc[candidate,'dhi_estimated_Wm2']=np.asarray(components['dhi'])
    result.loc[candidate,'iterations']=np.asarray(niter)
    result.loc[candidate,'converged']=np.asarray(converged)
    result.loc[candidate,'status']=np.where(np.asarray(converged),'converged_estimate_not_observation','failed_no_imputation')
    valid=candidate&result.converged&result[['ghi_estimated_Wm2','dni_estimated_Wm2','dhi_estimated_Wm2']].notna().all(axis=1)
    n=h.loc[valid].copy()
    for source,target in [('ghi_estimated_Wm2','ghi_Wm2'),('dni_estimated_Wm2','dni_Wm2'),('dhi_estimated_Wm2','dhi_Wm2')]:
        n[target]=result.loc[valid,source]
    n.attrs['origin']='reverse_POA'
    reconstructed=transpose(n,cfg)
    result.loc[valid,'poa_reconstructed_Wm2']=reconstructed.poa_global
    result['numerical_closure_residual_Wm2']=result.poa_reconstructed_Wm2-result.poa_measured_Wm2
    result['label']='ESTIMATED from POA; no measured GHI/DNI/DHI; closure is not validation'
    ctx.update({'reverse_diagnostics':result,'resource_for_scenarios':n,
                'reverse_summary':{'candidate_hours':int(candidate.sum()),'converged_hours':int(valid.sum()),
                    'excluded_or_failed_hours':int((~valid).sum()),'total_quarter_hours':len(h),
                    'method':'Driesse 2024 + Erbs-Driesse + Perez-Driesse',
                    'independent_component_validation':False,
                    'max_numerical_closure_residual_Wm2':float(result.numerical_closure_residual_Wm2.abs().max())}})
    return result


def daily_paired_energy(ctx):
    d,a=ctx['data'],ctx['model_a']
    q=pd.DataFrame(index=d.index)
    q['E_measured_kWh']=d.ac_meter_W.where(d.paired_daylight)*.25/1000
    q['E_modeled_kWh']=a.ac_final_W.where(d.paired_daylight)*.25/1000
    q['paired_intervals']=d.paired_daylight.astype(int)
    q['expected_daylight_intervals']=d.daylight.astype(int)
    daily=q.tz_convert(ctx['config']['site']['timezone']).resample('D').sum(min_count=1)
    daily['coverage_percent']=100*daily.paired_intervals/daily.expected_daylight_intervals
    daily['scope']='same paired daylight intervals; not complete daily energy'
    return daily


def save_plot(root,name):
    folder=Path(root)/'outputs/figures';folder.mkdir(parents=True,exist_ok=True)
    plt.tight_layout()
    plt.savefig(folder/(name+'.png'),dpi=160,bbox_inches='tight')
    plt.savefig(folder/(name+'.svg'),bbox_inches='tight')


def plot_all(ctx):
    plt.style.use('dark_background')
    plt.rcParams.update({'font.size':15,'axes.labelsize':16,'axes.titlesize':18,'legend.fontsize':12,'figure.figsize':(11,5)})
    d,a=ctx['data'],ctx['model_a'];tz=ctx['config']['site']['timezone']
    day=d.index.tz_convert(tz).strftime('%Y-%m-%d')=='2024-05-15'
    clock=d.index[day].tz_convert(tz)
    fig,axes=plt.subplots(2,1,figsize=(11,7),sharex=True)
    axes[0].plot(clock,d.loc[day,'poa_measured_Wm2'],color='#50e3e6');axes[0].set(ylabel='POA medida (W/m²)',title='1 — Recurso solar medido na instalação')
    axes[1].plot(clock,d.loc[day,'zenith'],color='#ffdb58');axes[1].set(ylabel='Ângulo zenital calculado (°)',xlabel='Hora local — 15/05/2024')
    save_plot(ctx['root'],'01_recurso_solar');plt.show()
    fig,axes=plt.subplots(1,2,figsize=(12,5))
    axes[0].hist(d.loc[d.daylight,'temp_air_C'].dropna(),bins=22,color='#ffdb58');axes[0].set(xlabel='Temperatura do ar (°C)',ylabel='Intervalos',title='2 — Temperatura medida')
    axes[1].hist(d.loc[d.daylight,'wind_ms'].dropna(),bins=22,color='#50e3e6');axes[1].set(xlabel='Vento (m/s)',ylabel='Intervalos',title='2 — Vento medido')
    save_plot(ctx['root'],'02_ambiente');plt.show()
    curves=module_curves(ctx)
    fig,axes=plt.subplots(1,2,figsize=(13,5))
    for (g,t),q in curves.groupby(['G_Wm2','T_C']):
        label=f'{g} W/m²; {t} °C';axes[0].plot(q.voltage_V,q.current_A,label=label);axes[1].plot(q.voltage_V,q.power_W,label=label)
    axes[0].set(xlabel='Tensão (V)',ylabel='Corrente (A)',title='3.3 — Curvas I–V');axes[1].set(xlabel='Tensão (V)',ylabel='Potência (W)',title='3.3 — Curvas P–V');axes[1].legend()
    save_plot(ctx['root'],'03_curvas_modulo');plt.show()
    use=d.paired_daylight
    fig,ax=plt.subplots();ax.scatter(d.loc[use,'ac_meter_W']/1000,a.loc[use,'ac_final_W']/1000,s=8,alpha=.4,color='#50e3e6');ax.plot([0,730],[0,730],color='#ffdb58',label='Igualdade')
    ax.set(xlabel='Potência AC medida (kW)',ylabel='Potência AC modelada (kW)',title='4.4 — Validação elétrica com medições locais');ax.legend()
    save_plot(ctx['root'],'04_validacao_poa_local');plt.show()
    fig,ax=plt.subplots();ax.plot(clock,d.loc[day,'ac_meter_W']/1000,label='Medidor real',linewidth=2);ax.plot(clock,a.loc[day,'ac_final_W']/1000,label='Modelo com POA e meteorologia locais',linewidth=2)
    ax.set(xlabel='Hora local — Califórnia',ylabel='Potência AC (kW)',title='3–4 — Medição e simulação em 15/05/2024');ax.legend()
    save_plot(ctx['root'],'05_series_potencia');plt.show()
    fig,ax=plt.subplots();stage=ctx['energy_stages'];ax.barh(np.arange(len(stage)),stage.energy_kWh/1000,color='#50e3e6');ax.set_yticks(np.arange(len(stage)),['Linear STC','SDM a 25 °C','Hipótese óptica','Temperatura','Perdas CC','Conversão CC–CA','Clipping','Perdas CA']);ax.invert_yaxis();ax.set(xlabel='Energia no recorte pareado (MWh)',title='4.1 — Estágios modelados da cadeia energética')
    save_plot(ctx['root'],'06_cadeia_energetica');plt.show()
    daily=daily_paired_energy(ctx)
    fig,ax=plt.subplots();ax.plot(daily.index,daily.E_measured_kWh,label='Medidor');ax.plot(daily.index,daily.E_modeled_kWh,label='Modelo');ax.set(ylabel='Energia diurna pareada (kWh)',xlabel='Data local',title='4.4 — Energia nos mesmos intervalos de cada dia');ax.legend()
    save_plot(ctx['root'],'07_energia_diaria_pareada');plt.show()
    if 'bipv_comparison' in ctx:
        comparisons=ctx['bipv_comparison'];fig,ax=plt.subplots();ax.bar(comparisons.scenario,comparisons.E_AC_for_1kWp_kWh,color=['#50e3e6','#ffdb58','#e58bff','#a4f28b']);ax.tick_params(axis='x',rotation=15)
        ax.set(ylabel='Energia específica (kWh/kWp)',title='4.5 — BIPV: horas diurnas selecionadas da inversão')
        save_plot(ctx['root'],'08_cenarios_bipv_estimados');plt.show()
    if 'reverse_diagnostics' in ctx:
        q=ctx['reverse_diagnostics'];dayh=q.index.tz_convert(tz).strftime('%Y-%m-%d')=='2024-05-15';fig,ax=plt.subplots()
        for c,label in [('ghi_estimated_Wm2','GHI estimada'),('dni_estimated_Wm2','DNI estimada'),('dhi_estimated_Wm2','DHI estimada')]:
            ax.plot(q.index[dayh].tz_convert(tz),q.loc[dayh,c],marker='.',label=label)
        ax.set(xlabel='Hora local — 15/05/2024',ylabel='Irradiância estimada (W/m²)',title='3.1 — Transposição inversa exploratória; sem validação local');ax.legend()
        save_plot(ctx['root'],'09_componentes_estimadas_da_POA');plt.show()


def data_status():
    return pd.DataFrame([
        ['Latitude, longitude, altitude, inclinação e azimute','Disponíveis nos metadados','Permitem calcular a geometria solar; não é preciso medir o zenital'],
        ['POA, temperatura do ar, vento e potência AC','Medições locais disponíveis','Permitem comparação elétrica agregada modelo–medidor'],
        ['GHI, DNI e DHI locais','Sem séries medidas nos arquivos obtidos','Não impedem o modelo direto com POA; impedem validação independente das componentes'],
        ['Temperatura medida de módulo/célula','Ausente','Temperatura operacional estimada; etapa térmica sem validação própria'],
        ['Strings, associação aos MPPTs e limite AC efetivo','Documentação incompleta','Modelo agregado possível; reconstrução detalhada não comprovada'],
        ['Albedo, limpeza, sombras e altura do anemômetro','Não documentados suficientemente','Hipóteses e sensibilidades; causas de perdas não identificadas só pelo resíduo'],
        ['Fachada e propriedades de produto BIPV','Sem medições','Extensão simulada; sem validação de fachada'],
    ],columns=['Item','Situação','Consequência para o estudo'])


def export_results(ctx):
    root=ctx['root'];folder=root/'outputs/tabelas/csv';folder.mkdir(parents=True,exist_ok=True)
    keys=['metrics','capacity_sensitivity','yields','energy_stages','operational_flags','bipv_comparison','bipv_energy_summary','environment_scenarios','environment_sensitivity']
    for key in keys:
        if key in ctx and len(ctx[key]):ctx[key].to_csv(folder/(key+'.csv'),index=False)
    ctx['data'].join(ctx['model_a'].add_prefix('model_A_')).to_csv(folder/'series_15min_local_e_modelo.csv',index_label='interval_start_UTC')
    daily_paired_energy(ctx).to_csv(folder/'energia_diaria_pareada.csv',index_label='day_local')
    data_status().to_csv(folder/'situacao_dos_dados.csv',index=False)
    if 'reverse_diagnostics' in ctx:
        ctx['reverse_diagnostics'].to_csv(folder/'componentes_estimadas_da_POA_horario.csv',index_label='interval_start_UTC')
    if 'bipv_balance' in ctx:ctx['bipv_balance'].to_csv(folder/'bipv_balanco_solar_horario.csv',index_label='interval_start_UTC')
    if 'nasa' in ctx:
        ctx['nasa'].join(ctx['poa_nasa'].add_prefix('perez_')).join(ctx['model_b'].add_prefix('model_B_')).to_csv(folder/'series_hourly_NASA_e_modelo.csv',index_label='interval_start_UTC')
    summary={'project_version':ctx['config']['version'],'primary_workflow':'measured POA + local air temperature/wind -> physical model -> measured AC comparison',
        'NASA_used':bool(ctx['audit'].get('NASA_used',False)),'audit':ctx['audit'],'full_quarter':ctx['full_quarter'],
        'primary_validation':ctx['metrics'].iloc[0].to_dict(),'empirical_scale_fitted_only_april':ctx['empirical_scale_april'],
        'reverse_POA':ctx.get('reverse_summary',{'executed':False}),
        'validation_scope':'Preliminary electrical model–observation evaluation; no independent validation of GHI/DNI/DHI, cell temperature or facade',
        'meter_vs_inverters':ctx['meter_inverter_consistency'],'python':platform.python_version(),'pvlib':pvlib.__version__}
    (root/'outputs/resumo_execucao.json').write_text(json.dumps(summary,indent=2,ensure_ascii=False))
    (root/'outputs/LEIA_ME_RESULTADOS.txt').write_text('Versão '+ctx['config']['version']+'\nTabelas: tabelas/csv/ e tabelas/docx/\nQuadros: quadros/docx/\nGráficos, fluxogramas e ilustrações: graficos/, fluxogramas/ e figuras/\nCada figura possui PDF e PNG nos temas claro e escuro.\nRelatório e catálogos: relatorios/\nO caminho principal não usa NASA POWER.\nComponentes obtidas da POA são estimativas exploratórias.\nBIPV usa somente as horas diurnas selecionadas da inversão; não é energia integral do trimestre.\n')
    return summary


def report_results(ctx):
    """Readable standalone report with actual figures and reproducible scope."""
    import base64,html
    root=ctx['root'];out=root/'outputs';m=ctx['metrics'].iloc[0];cfg=ctx['config']
    body='<p>SPGER0046 · UFPB · versão '+cfg['version']+'</p><h1>Projeto FV com medições locais</h1>'
    body+='<p>Farm Solar Array, Califórnia, abril–junho de 2024. O modelo principal usa POA, temperatura do ar e vento medidos para calcular a potência AC, comparada com o medidor real. NASA POWER não é usado no percurso principal.</p>'
    body+='<p><strong>Resultado principal:</strong> '+str(int(m['n']))+' intervalos; nRMSE '+f'{m.nRMSE_percent:.2f}'+'%; viés '+f'{m.nMBE_percent:+.2f}'+'%; R² '+f'{m.R2:.4f}'+'. A comparação foi executada; adequação, causas dos desvios e incertezas precisam de discussão científica.</p>'
    for title,text in [('1 — Recurso solar','Coordenadas e relógio permitem calcular o zenital pelo SPA. A POA é medida. GHI, DNI e DHI reconstruídas são estimativas, não novas observações.'),
                       ('2 — Ambiente e instalação','Temperatura e vento são locais. Albedo, parâmetros térmicos e perdas genéricas permanecem hipóteses documentadas.'),
                       ('3 — Conversão','Faiman, diodo único/CEC e inversor PVWatts transformam as entradas em potência e energia. A topologia elétrica real não foi integralmente reconstruída.'),
                       ('4 — Desempenho','Produtividades e PR usam os mesmos intervalos pareados. A energia integral observada é apresentada separadamente. A extensão BIPV usa componentes estimadas da POA e não possui observações de fachada.')]:
        body+='<h2>'+title+'</h2><p>'+text+'</p>'
    body+='<h2>Situação dos dados</h2><div class="scroll">'+data_status().to_html(index=False,border=0)+'</div>'
    body+='<h2>Comparações elétricas</h2><div class="scroll">'+ctx['metrics'].to_html(index=False,border=0,float_format=lambda x:f'{x:.4f}')+'</div>'
    if 'reverse_summary' in ctx:
        body+='<h2>Inversão exploratória da POA</h2><p>'+str(ctx['reverse_summary']['converged_hours'])+' horas elegíveis convergiram. O fechamento da POA com o mesmo modelo é uma verificação numérica; não valida GHI, DNI e DHI de forma independente. Os cenários usam apenas esse recorte de horas diurnas.</p>'
    for p in sorted((out/'figures').glob('*.png')):
        body+='<figure><img alt="'+html.escape(p.stem)+'" src="data:image/png;base64,'+base64.b64encode(p.read_bytes()).decode()+'"><figcaption>'+html.escape(p.stem.replace('_',' '))+'</figcaption></figure>'
    body+='<h2>Referências do projeto</h2>'
    refs=json.loads((root/'references/referencias_projeto.json').read_text())
    for ref in refs:
        body+='<p><strong>'+html.escape(ref['id'])+'</strong> — '+html.escape(ref['citation'])+' <a href="'+html.escape(ref['url'])+'">Fonte</a>. '+html.escape(ref['role'])+'</p>'
    css='body{background:#101820;color:#f3f6fa;font:20px/1.65 system-ui,Arial;margin:0}main{max-width:1150px;margin:auto;padding:30px 24px}h1{font-size:2rem}h2,a{color:#73e9ed}table{border-collapse:collapse;font-size:18px}td,th{padding:12px;text-align:left;border-bottom:1px solid #58717d;vertical-align:top}th{background:#27434d}.scroll{overflow-x:auto}img{width:100%;height:auto}figure{margin:30px 0}figcaption{font-size:17px}'
    p=out/'Relatorio_do_Projeto.html';p.write_text('<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Projeto FV — v1.1</title><style>'+css+'</style><main>'+body+'</main></html>')
    return p


def zip_results(ctx):
    folder=ctx['root']/'outputs';target=folder/'Resultados_Execucao_Projeto_FV.zip'
    with zipfile.ZipFile(target,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(folder.rglob('*')):
            if p.is_file() and p!=target:z.write(p,p.relative_to(folder).as_posix())
    return target


def sync_outputs_drive(ctx, parent_id):
    """Called by the user inside Colab, after explicit Google authentication.

    Creates one dated run folder below the verified project-results folder.
    Does not overwrite or delete previous runs or the raw data.
    """
    from datetime import datetime
    from zoneinfo import ZoneInfo
    from google.colab import auth
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    auth.authenticate_user()
    api=build('drive','v3',cache_discovery=False)
    parent=api.files().get(fileId=parent_id,fields='id,name,mimeType').execute()
    if parent['mimeType']!='application/vnd.google-apps.folder':raise ValueError('Destino não é pasta')
    name='Execucao_v'+ctx['config']['version'].replace('.','_')+'_'+datetime.now(ZoneInfo('America/Sao_Paulo')).strftime('%Y%m%d_%H%M%S')
    run=api.files().create(body={'name':name,'mimeType':'application/vnd.google-apps.folder','parents':[parent_id]},fields='id,name,webViewLink').execute()
    folders={'.':run['id']};receipts=[];base=ctx['root']/'outputs'
    paths=[p for p in sorted(base.rglob('*')) if p.is_file()]
    for i,p in enumerate(paths,1):
        relative=p.relative_to(base);parent_path=relative.parent.as_posix()
        current='.'
        for component in relative.parent.parts:
            child=component if current=='.' else current+'/'+component
            if child not in folders:
                sub=api.files().create(body={'name':component,'mimeType':'application/vnd.google-apps.folder','parents':[folders[current]]},fields='id').execute()
                folders[child]=sub['id']
            current=child
        uploaded=api.files().create(body={'name':p.name,'parents':[folders[parent_path]]},media_body=MediaFileUpload(str(p),resumable=True),fields='id,name,size').execute()
        if int(uploaded['size'])!=p.stat().st_size:raise IOError('Tamanho divergente: '+p.name)
        receipts.append(uploaded)
        print(f'Salvo {i}/{len(paths)}: {relative}')
    return {'folder_name':run['name'],'folder_url':run.get('webViewLink','https://drive.google.com/drive/folders/'+run['id']),'files_verified':len(receipts)}


def complete_pipeline(root, make_plots=True, include_nasa=False, reverse=True):
    cfg=load_config(root);ctx=prepare(root,cfg,include_nasa=include_nasa);run_models(ctx);performance(ctx)
    if reverse:reverse_components(ctx)
    ctx['environment_scenarios'],ctx['environment_sensitivity']=environmental_scenarios(ctx)
    if 'resource_for_scenarios' in ctx or 'nasa' in ctx:
        ctx['bipv_comparison'],ctx['bipv_balance'],ctx['bipv_energy_summary']=bipv_scenario(ctx)
    export_results(ctx)
    if make_plots:plot_all(ctx)
    return ctx


