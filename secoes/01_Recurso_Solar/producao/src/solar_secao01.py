"""Geometria da Seção 1, sem recalcular a cadeia elétrica do projeto."""
from pathlib import Path
import hashlib, json, platform
import numpy as np
import pandas as pd
import pvlib
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
BG, FG, YELLOW, CYAN, ORANGE = '#0b1015', '#eef2f6', '#ffd45c', '#70dcf5', '#ffb66f'

def sha256(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def run(root=ROOT):
    root = Path(root)
    assert pvlib.__version__ == '0.16.1', 'Utilize a versão pvlib 0.16.1 fixada no projeto.'
    cfg = json.loads((root/'config/projeto.json').read_text())
    site = cfg['site']
    inp = root/'dados/poa_15min.csv'
    poa = pd.read_csv(inp, index_col=0, parse_dates=True)
    poa.index = pd.to_datetime(poa.index, utc=True)
    assert poa.index.is_unique and poa.index.is_monotonic_increasing
    assert len(poa) == 91*96
    assert np.all(np.diff(poa.index.asi8) == 15*60*10**9)
    mid = poa.index + pd.Timedelta(minutes=7.5)
    loc = pvlib.location.Location(site['latitude'],site['longitude'],tz='UTC',altitude=site['altitude_m'])
    sp = loc.get_solarposition(mid, method='nrel_numpy', temperature=12, delta_t=67)
    sp.index = poa.index
    extra = np.asarray(pvlib.irradiance.get_extra_radiation(mid,solar_constant=1366.1,method='spencer'))
    # Conferência independente da implementação do fator orbital de Spencer.
    b = 2*np.pi*(mid.dayofyear.to_numpy()-1)/365
    factor = 1.00011 + .034221*np.cos(b) + .00128*np.sin(b) + .000719*np.cos(2*b) + .000077*np.sin(2*b)
    assert np.allclose(extra,1366.1*factor,rtol=0,atol=1e-10)
    d = poa.join(sp)
    d['instant_mid_UTC'] = mid
    d['instant_mid_local'] = mid.tz_convert(site['timezone'])
    d['G0n_Wm2'] = extra
    d['G0h_Wm2'] = extra*np.maximum(0,np.cos(np.deg2rad(d.zenith)))
    d['aoi_deg'] = pvlib.irradiance.aoi(site['tilt_deg'],site['azimuth_deg'],d.apparent_zenith,d.azimuth)
    assert np.allclose(d.elevation + d.zenith,90,atol=1e-12)
    assert np.all(d.G0h_Wm2 >= 0)
    assert np.all(d.loc[d.zenith>90,'G0h_Wm2'] == 0)
    assert d.azimuth.between(0,360,inclusive='left').all()
    assert np.all(d.G0h_Wm2 <= d.G0n_Wm2+1e-10)
    # Exemplo publicado do SPA, Reda e Andreas (2008), Tabela A5.1, pp. A-15–A-16.
    ref = pd.DatetimeIndex(['2003-10-17T12:30:30-07:00'])
    test = pvlib.solarposition.spa_python(ref,39.742476,-105.1786,altitude=1830.14,pressure=82000,temperature=11,delta_t=67)
    actual = float(test.apparent_zenith.iloc[0])
    azi = float(test.azimuth.iloc[0])
    assert abs(actual-50.11162)<5e-5 and abs(azi-194.34024)<5e-5
    use = d.instant_mid_local.dt.strftime('%Y-%m-%d').eq('2024-05-17')
    day = d.loc[use].copy()
    assert len(day)==96
    out = root/'resultados';out.mkdir(exist_ok=True)
    day.to_csv(out/'G01_dados_verificados.csv',index_label='interval_start_UTC')
    # Seleção diurna é só uma janela de exibição, sem interpolar observações ausentes.
    figdir=root/'figuras';figdir.mkdir(exist_ok=True)
    for dark in [True,False]:
        bg,fg = (BG,FG) if dark else ('#ffffff','#101820')
        plt.rcParams.update({'font.family':'serif','font.serif':['Times New Roman','Nimbus Roman','DejaVu Serif'],
          'font.size':16,'axes.labelsize':17,'xtick.labelsize':14,'ytick.labelsize':14,
          'figure.facecolor':bg,'axes.facecolor':bg,'axes.edgecolor':fg,'text.color':fg,
          'axes.labelcolor':fg,'xtick.color':fg,'ytick.color':fg,'svg.fonttype':'path','pdf.fonttype':42})
        fig,axs=plt.subplots(2,1,figsize=(8.4,4.7),sharex=True,gridspec_kw={'height_ratios':[1,1]})
        h=day.instant_mid_local.dt.hour+day.instant_mid_local.dt.minute/60+day.instant_mid_local.dt.second/3600
        c1=CYAN if dark else '#00728c';c2=YELLOW if dark else '#8b5700'
        axs[0].plot(h,day.poa_measured_Wm2,color=c1,lw=2.5,label='POA medida')
        axs[0].set(ylabel='POA (W m$^{-2}$)',ylim=(-15,1100),yticks=[0,500,1000])
        axs[0].legend(loc='upper left',frameon=False,fontsize=14,labelcolor=fg)
        axs[1].plot(h,day.zenith,color=c1,lw=2.2,label='Zenital SPA')
        axs[1].plot(h,day.aoi_deg,color=c2,lw=2.2,ls='--',label='Incidência')
        axs[1].set(ylabel='Ângulo (°)',xlabel='Hora local — 17/05/2024 (UTC−7)',ylim=(0,140),yticks=[0,60,120],xlim=(5,21),xticks=[6,9,12,15,18,21])
        axs[1].legend(loc='upper center',bbox_to_anchor=(.5,1.25),ncol=2,frameon=False,fontsize=14,labelcolor=fg)
        for ax in axs:
            ax.spines[['top','right']].set_visible(False);ax.grid(alpha=.16,color=fg);ax.margins(x=0)
        fig.subplots_adjust(left=.14,right=.99,bottom=.18,top=.98,hspace=.43)
        stem=figdir/('G01_recurso_geometria_'+('escuro' if dark else 'claro'))
        for ext in ['pdf','svg','png']:fig.savefig(str(stem)+'.'+ext,dpi=300,facecolor=bg)
        plt.close(fig)
    info={
      'pvlib':pvlib.__version__,'python':platform.python_version(),'period_local':'2024-04-01/2024-07-01 exclusive',
      'n_intervals':len(d),'n_intervals_day':len(day),'date_local':'2024-05-17','timezone':site['timezone'],
      'offset_on_day':'UTC-07:00','site':site,'interval_label':'start','calculation_offset_minutes':7.5,
      'solarposition':'NREL SPA, nrel_numpy','pressure_Pa':float(pvlib.atmosphere.alt2pres(site['altitude_m'])),
      'temperature_for_refraction_C':12,'delta_t_seconds':67,'delta_t_status':'default retained from project; not a measured time-scale correction',
      'extraterrestrial':'Spencer','solar_constant_Wm2':1366.1,'spencer_denominator_days':365,
      'day_of_year':int(mid[use][0].dayofyear),'leap_year_convention':'dayofyear from 2024; denominator 365 follows pvlib',
      'POA_observed_nonmissing_day':int(day.poa_measured_Wm2.notna().sum()),
      'POA_intervals_with_three_samples_day':int(day.irradiance_3_samples.sum()),
      'max_POA_Wm2':float(day.poa_measured_Wm2.max()),
      'min_geometric_zenith_deg':float(day.zenith.min()),
      'G0n_Wm2_day':float(day.G0n_Wm2.iloc[0]),
      'reference_SPA_apparent_zenith_deg':actual,'reference_SPA_azimuth_deg':azi,
      'reference_tolerance_deg':5e-5,'reference_source':'Reda & Andreas 2008, Table A5.1, printed A-15–A-16 / PDF 37–38',
      'input_sha256':sha256(inp),'config_sha256':sha256(root/'config/projeto.json'),
      'checks_passed':['regular cadence','91 days','no duplicate timestamps','Spencer independent expression','elevation+zenith','azimuth convention','night clipping','SPA published example'],
      'limitations':['POA is an interval mean, not an instantaneous value','No local independent GHI/DNI/DHI measurements','No cloud attribution from the curve','Display window 05-21 local; full day retained in CSV','Refraction uses default temperature and altitude-derived pressure','Apparent zenith used for AOI; geometric zenith used for extraterrestrial projection, as in the project']
    }
    (out/'Conferencia_Calculos.json').write_text(json.dumps(info,ensure_ascii=False,indent=2))
    return day,info

if __name__=='__main__':
    _,info=run();print(json.dumps(info,ensure_ascii=False,indent=2))
