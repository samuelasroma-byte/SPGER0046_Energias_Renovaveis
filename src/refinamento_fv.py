"""Diagnostics and publication outputs for v1.2; the physical baseline is unchanged."""
from pathlib import Path
import json
import html
import io
import base64
import hashlib
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from PIL import Image as PILImage
from matplotlib.patches import Arc, FancyArrowPatch, FancyBboxPatch, Polygon, Rectangle
import projeto_fv as fv
import editorial_fv as editorial

THEMES = {
    'claro': dict(bg='#FFFFFF', fg='#161616', grid='#CDD3D8',
                  colors=['#0072B2','#D55E00','#009E73','#7A3E9D','#AA7200','#444444']),
    'escuro': dict(bg='#101820', fg='#F5F7FA', grid='#536773',
                   colors=['#70E5FF','#FFB570','#7BE0AA','#DBA7FF','#FFE477','#F5F7FA'])
}
FIGURE_SOURCE='elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026).'


def analytics(ctx):
    d, a, cfg = ctx['data'], ctx['model_a'], ctx['config']
    mask = d.paired_daylight
    p = pd.DataFrame({'observed_kW':d.ac_meter_W/1000,
                      'modeled_kW':a.ac_final_W/1000,
                      'POA_Wm2':d.poa_measured_Wm2,
                      'temp_air_C':d.temp_air_C,'wind_ms':d.wind_ms,
                      'temp_operational_model_C':a.temp_cell_proxy_C}, index=d.index)
    p['residual_kW'] = p.modeled_kW-p.observed_kW
    p['empirical_kW'] = p.modeled_kW*ctx['empirical_scale_april']
    p = p.loc[mask].copy()
    local = p.index.tz_convert(cfg['site']['timezone'])
    p['month_local'] = local.month
    p['hour_local'] = local.hour
    variables = [('POA_Wm2','POA medida','W/m²'),
        ('temp_air_C','Temperatura do ar','°C'),('wind_ms','Velocidade do vento','m/s'),
        ('temp_operational_model_C','Temperatura operacional estimada','°C'),
        ('observed_kW','Potência AC observada','kW'),
        ('modeled_kW','Potência AC simulada','kW'),('residual_kW','Resíduo simulado − observado','kW')]
    descriptive = []
    expected = int(d.daylight.sum())
    for key, label, unit in variables:
        s = p[key].dropna()
        descriptive.append(dict(variable=label,unit=unit,expected=expected,valid=len(s),
            coverage_percent=100*len(s)/expected,mean=s.mean(),median=s.median(),std_sample=s.std(ddof=1),
            minimum=s.min(),Q1=s.quantile(.25),Q3=s.quantile(.75),maximum=s.max(),
            IQR=s.quantile(.75)-s.quantile(.25),
            window='mesmos intervalos diurnos pareados; elevação NOAA ≥10°',
            std_convention='amostral, ddof=1'))
    monthly, hourly, irradiance = [], [], []
    for month, group in p.groupby('month_local'):
        row=fv.metrics(group.observed_kW,group.modeled_kW,f'Mês {month:02d}: físico')
        expected_m=int((d.daylight & (d.index.tz_convert(cfg['site']['timezone']).month==month)).sum())
        row.update(month=int(month),expected_intervals=expected_m,coverage_percent=100*len(group)/expected_m,
                   role={4:'ajuste apenas do fator empírico',5:'verificação',6:'teste temporal separado'}[int(month)])
        monthly.append(row)
    for hour, group in p.groupby('hour_local'):
        row=fv.metrics(group.observed_kW,group.modeled_kW,f'Hora local {hour:02d}')
        exp=int((d.daylight & (d.index.tz_convert(cfg['site']['timezone']).hour==hour)).sum())
        row.update(hour_local=int(hour),expected_intervals=exp,coverage_percent=100*len(group)/exp)
        hourly.append(row)
    bins=pd.cut(p.POA_Wm2,[0,200,400,600,800,1000,1200,1800],include_lowest=True,right=False)
    for interval, group in p.groupby(bins,observed=True):
        row=fv.metrics(group.observed_kW,group.modeled_kW,str(interval))
        exp=int((d.daylight & d.poa_measured_Wm2.ge(interval.left) & d.poa_measured_Wm2.lt(interval.right)).sum())
        row.update(POA_bin_Wm2=str(interval),expected_intervals=exp,
                   coverage_percent=100*len(group)/exp if exp else np.nan)
        irradiance.append(row)
    daily=fv.daily_paired_energy(ctx)
    q=pd.DataFrame(index=d.index)
    q['H_POA_paired_kWh_m2']=d.poa_measured_Wm2.where(mask)*.25/1000
    h=q.tz_convert(cfg['site']['timezone']).resample('D').sum(min_count=1)
    daily=daily.join(h)
    daily['PSH_POA_paired_h']=daily.H_POA_paired_kWh_m2/1.0
    daily['period_label']='janela diurna pareada, não dia completo'
    daily['E_error_kWh']=daily.E_modeled_kWh-daily.E_measured_kWh
    monthly_energy=[]
    for month in [4,5,6]:
        use=mask & (d.index.tz_convert(cfg['site']['timezone']).month==month)
        full=(d.index.tz_convert(cfg['site']['timezone']).month==month)
        H=d.loc[use,'poa_measured_Wm2'].sum()*.25/1000
        obs=d.loc[use,'ac_meter_W'].sum()*.25/1000
        mod=a.loc[use,'ac_final_W'].sum()*.25/1000
        p0=cfg['system']['metadata_p0_kw']
        monthly_energy.append(dict(month=month,n_paired=int(use.sum()),
            n_daylight_expected=int((full & d.daylight).sum()),
            coverage_percent=100*use.sum()/(full & d.daylight).sum(),
            E_observed_paired_kWh=obs,E_modeled_paired_kWh=mod,H_POA_paired_kWh_m2=H,
            Yf_observed_paired_kWh_kWp=obs/p0,PR_observed_paired=obs/p0/H,PR_modeled_paired=mod/p0/H,
            E_observed_full_month_kWh=d.loc[full,'ac_meter_W'].sum()*.25/1000,
            meter_full_month_records=int(d.loc[full,'ac_meter_W'].notna().sum()),
            meter_full_month_expected=int(full.sum())))
    day_variation=[]
    for day, group in p.tz_convert(cfg['site']['timezone']).groupby(lambda t:t.date()):
        cover=daily.loc[pd.Timestamp(day,tz=cfg['site']['timezone']),'coverage_percent']
        if cover>=99 and len(group)>20 and group.POA_Wm2.mean()>0:
            score=float(np.abs(np.diff(group.POA_Wm2)).mean()/group.POA_Wm2.mean())
            day_variation.append({'day':str(day),'relative_mean_absolute_step':score,'n':len(group),'coverage_percent':cover})
    days=pd.DataFrame(day_variation).sort_values('relative_mean_absolute_step')
    selected=[days.iloc[0].day,days.iloc[-1].day]
    exp_cfg=cfg['assumptions']
    array=a.loc[mask,['v_mp_module_V','i_mp_module_A','p_mp_module_W']].copy()
    array['V_mp_equivalent_string_V']=array.v_mp_module_V*exp_cfg['illustrative_modules_in_series']
    array['I_mp_equivalent_group_A']=array.i_mp_module_A*exp_cfg['illustrative_parallel_strings']
    array['P_mp_equivalent_group_W']=array.p_mp_module_W*cfg['system']['modules_per_group']
    array['configuration_status']='20 série × 6 paralelo: exemplo equivalente, não cabeamento comprovado'
    power=pd.Series(np.linspace(0,42000,160))
    inv=fv.inverter_pvwatts_stages(power,exp_cfg['inverter_capacity_baseline_w_each'],
        exp_cfg['inverter_eta_nom'],exp_cfg['inverter_eta_ref'])
    inv['P_DC_W']=power
    inv['efficiency_before_clipping']=inv.ac_before_clip_W/power.where(power>0)
    tables={'estatistica_descritiva':pd.DataFrame(descriptive),'metricas_por_mes':pd.DataFrame(monthly),
        'metricas_por_hora':pd.DataFrame(hourly),'metricas_por_faixa_POA':pd.DataFrame(irradiance),
        'energia_e_indicadores_mensais':pd.DataFrame(monthly_energy),
        'energia_e_HSP_diurna_pareada':daily.reset_index(names='day_local'),
        'criterio_dias_ilustrativos':days,'curva_inversor_modelada':inv,
        'arranjo_equivalente_diurno':array.reset_index(names='interval_start_UTC')}
    ctx.update(analytics_tables=tables,paired=p,selected_days=selected,figures=[])
    return ctx


def compute_curves(ctx, variation):
    pairs=[(g,25) for g in [300,600,1000]] if variation=='irradiance' else [(1000,t) for t in [15,25,45]]
    curves=[]
    m=ctx['module']
    for g,t in pairs:
        par=fv.pvlib.pvsystem.calcparams_cec(g,t,m['alpha_sc'],m['a_ref'],m['I_L_ref'],
            m['I_o_ref'],m['R_sh_ref'],m['R_s'],m['Adjust'])
        sd=fv.pvlib.pvsystem.singlediode(*par)
        v=np.linspace(0,float(sd['v_oc']),180)
        current=fv.pvlib.pvsystem.i_from_v(v,*par)
        curves.append((g,t,v,current,sd))
    return curves


def style(theme):
    t=THEMES[theme]
    return {'figure.facecolor':t['bg'],'axes.facecolor':t['bg'],'savefig.facecolor':t['bg'],
        'text.color':t['fg'],'axes.labelcolor':t['fg'],'axes.edgecolor':t['fg'],
        'xtick.color':t['fg'],'ytick.color':t['fg'],'grid.color':t['grid'],
        'font.family':'DejaVu Sans','font.size':13,'axes.labelsize':14,
        'axes.titlesize':14,'legend.fontsize':11.5,'xtick.labelsize':12,'ytick.labelsize':12,
        'legend.facecolor':t['bg'],'legend.edgecolor':t['grid'],'pdf.fonttype':42,'ps.fonttype':42,
        'figure.constrained_layout.use':True,
        'axes.prop_cycle':mpl.cycler(color=t['colors']),'axes.spines.top':False,
        'axes.spines.right':False,'grid.alpha':.35,'lines.linewidth':1.8}


def axes_finish(ax, xlabel=None, ylabel=None, zero=False):
    if xlabel:ax.set_xlabel(xlabel)
    if ylabel:ax.set_ylabel(ylabel)
    ax.grid(True,alpha=.25)
    ax.set_axisbelow(True)
    if zero:ax.axhline(0,color=mpl.rcParams['text.color'],lw=1,ls='--')


def export_figure(ctx, ident, category, subsections, title, caption, refs, drawer, status, size=(6.3,4.1)):
    record=dict(id=ident,category=category,subsections=subsections,title=title,caption=caption,
                refs=refs,status=status,files={},source=FIGURE_SOURCE)
    editorial.assign_figure(ctx['root'],record)
    signatures=[]
    for theme in THEMES:
        with mpl.rc_context(style(theme)):
            fig=drawer(THEMES[theme])
            fig.set_size_inches(*size)
            paths={}
            for fmt in ['pdf','png']:
                path=editorial.figure_path(ctx['root'],ident,theme,fmt)
                if path is None:path=ctx['root']/'outputs'/category/theme/fmt/(ident+'.'+fmt)
                path.parent.mkdir(parents=True,exist_ok=True)
                buffer=io.BytesIO()
                fig.savefig(buffer,format=fmt,dpi=600,facecolor=THEMES[theme]['bg'])
                content=buffer.getvalue()
                if fmt=='png':
                    with PILImage.open(io.BytesIO(content)) as im:im.verify()
                temporary=path.with_suffix(path.suffix+'.tmp')
                temporary.write_bytes(content);temporary.replace(path)
                assert path.stat().st_size==len(content)
                paths[fmt]=path.relative_to(ctx['root']).as_posix()
            preview=ctx['root']/'outputs/_previews'/theme/(ident+'.png')
            preview.parent.mkdir(parents=True,exist_ok=True)
            fig.savefig(preview,dpi=150,facecolor=THEMES[theme]['bg'])
            paths['preview']=preview.relative_to(ctx['root']).as_posix()
            signatures.append([(ax.get_xlim(),ax.get_ylim(),
                [(np.asarray(line.get_xdata()).tolist(),np.asarray(line.get_ydata()).tolist()) for line in ax.lines])
                for ax in fig.axes])
            plt.close(fig)
            record['files'][theme]=paths
    # Colors may differ, numerical coordinates and axis limits must agree.
    assert repr(signatures[0])==repr(signatures[1]),'Temas com dados/eixos divergentes: '+ident
    record['same_numeric_geometry_between_themes']=True
    ctx['figures'].append(record)
    print('Figura exportada:',ident,flush=True)
    return record


def generate_graphs(ctx):
    d,a,p=ctx['data'],ctx['model_a'],ctx['paired']
    tb=ctx['analytics_tables'];tz=ctx['config']['site']['timezone'];mask=d.paired_daylight
    def add(i,sec,title,caption,refs,draw,status='medição e modelo identificados',size=(6.3,4.1)):
        return export_figure(ctx,i,'graficos',sec,title,caption,refs,draw,status,size)
    selected=ctx['selected_days']
    day=selected[0]
    def resource(t):
        fig,axs=plt.subplots(2,1,sharex=True)
        local=d.index.tz_convert(tz);use=local.strftime('%Y-%m-%d')==day
        hour=local[use].hour+local[use].minute/60
        axs[0].plot(hour,d.loc[use,'poa_measured_Wm2'],label='POA medida')
        axes_finish(axs[0],ylabel='Irradiância (W/m²)');axs[0].legend()
        axs[1].plot(hour,d.loc[use,'zenith'],label='Zenital SPA')
        axs[1].plot(hour,d.loc[use,'aoi_deg'],label='Incidência',ls='--')
        axes_finish(axs[1],'Hora local','Ângulo (°)');axs[1].legend()
        return fig
    add('G01_recurso_geometria',['1.1','1.2'],'Recurso solar medido e geometria calculada',
        f'Dia {day}, selecionado pela menor variação relativa da POA entre dias com cobertura ≥99%. Ângulos calculados no meio dos intervalos; POA medida.',
        ['R01','R03','R05'],resource,size=(6.3,6.2))
    def variability(t):
        q=tb['energia_e_HSP_diurna_pareada']
        fig,ax=plt.subplots();ax.plot(q.day_local.dt.dayofyear,q.H_POA_paired_kWh_m2)
        axes_finish(ax,'Dia do ano de 2024','Irradiação POA pareada (kWh/m²)')
        return fig
    add('G02_variabilidade_recurso',['1.3'],'Variabilidade diária do recurso solar',
        'Integração somente nos intervalos diurnos pareados. Oscilações não identificam isoladamente nuvens, aerossóis ou vapor d’água.',
        ['R01','R12'],variability)
    def environments(t):
        fig,axs=plt.subplots(2,1)
        axs[0].hist(p.temp_air_C,bins=25,color=t['colors'][0]);axes_finish(axs[0],'Temperatura do ar (°C)','Intervalos')
        axs[1].hist(p.wind_ms,bins=25,color=t['colors'][1]);axes_finish(axs[1],'Velocidade do vento (m/s)','Intervalos')
        return fig
    add('G03_condicoes_ambientais',['2.1'],'Distribuições das condições ambientais',
        'Temperatura do ar e vento medidos; mesma janela diurna pareada da avaliação elétrica. Sem interpolação.',
        ['R01','R07'],environments,size=(6.3,6.2))
    def thermal(t):
        fig,ax=plt.subplots()
        sc=ax.scatter(p.POA_Wm2,p.temp_operational_model_C-p.temp_air_C,c=p.wind_ms,cmap='viridis',s=8,alpha=.55)
        axes_finish(ax,'POA medida (W/m²)','Elevação térmica estimada (°C)')
        colorbar=fig.colorbar(sc,ax=ax,label='Vento medido (m/s)')
        if colorbar.solids is not None:colorbar.solids.set_rasterized(False)
        return fig
    add('G04_temperatura_estimada',['2.1','3.2'],'Resposta térmica estimada pelo modelo',
        'Elevação térmica por Faiman com U₀=25 W/(m² K) e U₁=6,84 W s/(m³ K). Temperatura operacional usada como aproximação da célula; sem medição térmica independente.',
        ['R07'],thermal)
    for variation,ident,title,sec in [
        ('irradiance','G05_curvas_irradiancia','Curvas elétricas para diferentes irradiâncias','3.3'),
        ('temperature','G06_curvas_temperatura','Curvas elétricas para diferentes temperaturas','3.3')]:
        curves=compute_curves(ctx,variation)
        def draw(t,curves=curves,variation=variation):
            fig,axs=plt.subplots(2,1,sharex=True)
            for n,(g,temp,v,current,sd) in enumerate(curves):
                label=f'{g} W/m²' if variation=='irradiance' else f'{temp} °C'
                color=t['colors'][n]
                axs[0].plot(v,current,label=label,color=color,ls=['-','--',':'][n])
                axs[1].plot(v,v*current,color=color,ls=['-','--',':'][n])
                axs[0].plot(sd['v_mp'],sd['i_mp'],'o',color=color,ms=5)
                axs[1].plot(sd['v_mp'],sd['p_mp'],'o',color=color,ms=5)
            axes_finish(axs[0],ylabel='Corrente (A)');axs[0].legend(ncol=3,loc='upper right')
            axes_finish(axs[1],'Tensão (V)','Potência (W)')
            return fig
        add(ident,[sec],title,
            ('Temperatura fixa de 25 °C; ' if variation=='irradiance' else 'Irradiância fixa de 1.000 W/m²; ')+
            'modelo de diodo único com parâmetros CEC do módulo. Círculos indicam MPP. Curvas calculadas, não ensaios I–V da instalação.',
            ['R08','R10'],draw,'curvas calculadas',size=(6.3,6.3))
    def inverter(t):
        q=tb['curva_inversor_modelada'];fig,axs=plt.subplots(2,1)
        axs[0].plot(q.P_DC_W/1000,100*q.efficiency_before_clipping)
        axes_finish(axs[0],'Potência DC por inversor (kW)','Eficiência antes do limite (%)')
        axs[1].plot(q.P_DC_W/1000,q.ac_before_clip_W/1000,label='Antes do limite')
        axs[1].plot(q.P_DC_W/1000,q.ac_modeled_W/1000,label='AC limitada',ls='--')
        axs[1].axhline(30,color=t['fg'],ls=':',lw=1)
        axes_finish(axs[1],'Potência DC por inversor (kW)','Potência AC (kW)');axs[1].legend()
        return fig
    add('G07_inversor',['3.5'],'Eficiência e limitação de potência do inversor',
        'Curva PVWatts com limite assumido de 30 kW por inversor e η nominal de 98%. O valor de pdc0 do inversor é Paco/ηnom; não é a potência STC do arranjo. Configuração real do limite AC ainda não comprovada.',
        ['R11','R13'],inverter,'modelo de inversor e limite assumido',size=(6.3,6.3))
    def time_series(t):
        fig,axs=plt.subplots(2,1,sharex=True)
        for ax,day in zip(axs,selected):
            loc=p.index.tz_convert(tz);q=p.loc[loc.strftime('%Y-%m-%d')==day]
            h=q.index.tz_convert(tz).hour+q.index.tz_convert(tz).minute/60
            ax.plot(h,q.observed_kW,label='Medida')
            ax.plot(h,q.modeled_kW,label='Simulada',ls='--')
            ax.set_title(day);axes_finish(ax,ylabel='Potência AC (kW)')
        axs[0].legend(ncol=2);axs[1].set_xlabel('Hora local')
        return fig
    add('G08_series_potencia',['3.6','4.4'],'Potência em dias de menor e maior variabilidade',
        f'Dias {selected[0]} e {selected[1]}. Seleção pelo passo absoluto médio da POA dividido por sua média, com cobertura ≥99%; sem seleção pelo erro do modelo. Mesmos intervalos medidos/simulados.',
        ['R01','R08','R11'],time_series,size=(6.3,6.3))
    def daily_energy(t):
        q=tb['energia_e_HSP_diurna_pareada'];fig,ax=plt.subplots()
        x=q.day_local.dt.dayofyear
        ax.plot(x,q.E_measured_kWh/1000,label='Medida');ax.plot(x,q.E_modeled_kWh/1000,label='Simulada',ls='--')
        axes_finish(ax,'Dia do ano de 2024','Energia pareada (MWh)');ax.legend()
        return fig
    add('G09_energia_diaria',['3.6','4.4'],'Energia diária em intervalos pareados',
        'Soma de potência média × 0,25 h sobre intervalos com os mesmos dados disponíveis. Não é a energia observada do dia inteiro.',
        ['R12'],daily_energy)
    def monthly_energy(t):
        q=tb['energia_e_indicadores_mensais'];fig,ax=plt.subplots();x=np.arange(3)
        ax.bar(x-.18,q.E_observed_paired_kWh/1000,.36,label='Medida')
        ax.bar(x+.18,q.E_modeled_paired_kWh/1000,.36,label='Simulada')
        ax.set_xticks(x,['Abril','Maio','Junho']);axes_finish(ax,ylabel='Energia diurna pareada (MWh)');ax.legend()
        return fig
    add('G10_energia_mensal',['3.6'],'Energia mensal na janela de comparação',
        'Energia simulada e observada calculadas sobre a mesma máscara diurna pareada. Totais integrais medidos do mês são fornecidos separadamente nas tabelas.',
        ['R12'],monthly_energy)
    def stages(t):
        q=ctx['energy_stages'];fig,ax=plt.subplots()
        labels=['Referência STC','Diodo único a 25 °C','Hipótese óptica','Temperatura estimada','Perdas DC assumidas','Conversão sem limite','Após clipping','Perdas AC assumidas']
        ax.barh(labels[::-1],q.energy_kWh.iloc[::-1]/1000)
        axes_finish(ax,'Energia modelada pareada (MWh)')
        ax.tick_params(axis='y',labelsize=11.5)
        return fig
    add('G11_cadeia_energetica',['4.1'],'Cadeia de energia calculada',
        'Estágios integrados na mesma janela. Diferenças são decomposição do modelo, não identificação independente das perdas reais. Ganhos relativos sob frio não são forçados a perdas positivas.',
        ['R08','R11','R12'],stages,size=(6.3,5.2))
    def yields(t):
        q=ctx['yields'].iloc[0];fig,axs=plt.subplots(2,1)
        axs[0].bar(['Yr','Ya modelo','Yf modelo','Yf medida'],[q.Yr_h,q.Ya_model_h,q.Yf_model_kWh_kWp,q.Yf_observed_kWh_kWp])
        axes_finish(axs[0],ylabel='Produtividade equivalente (h)')
        axs[1].bar(['PR modelo','PR observado'],100*np.array([q.PR_model,q.PR_observed_paired]))
        axes_finish(axs[1],ylabel='PR pareado (%)')
        return fig
    add('G12_produtividades_PR',['4.2','4.3'],'Produtividades e razão de desempenho',
        'Normalização por 893 kWp declarados. Yr, Ya e Yf estão na mesma janela pareada; Ya é modelada. Numericamente, kWh/kWp corresponde a horas equivalentes. PR observado não representa automaticamente todo o trimestre.',
        ['R12','R30'],yields,size=(6.3,6.2))
    def validation(t):
        fig,ax=plt.subplots()
        ax.scatter(p.observed_kW,p.modeled_kW,s=7,alpha=.35)
        limit=max(p.observed_kW.max(),p.modeled_kW.max())*1.03
        ax.plot([0,limit],[0,limit],color=t['fg'],ls='--',label='Igualdade 1:1')
        ax.set(xlim=(0,limit),ylim=(0,limit));ax.set_aspect('equal',adjustable='box')
        m=ctx['metrics'].iloc[0]
        ax.text(.03,.97,f"n = {int(m.n):,}\nr = {m.r:.4f}\nR² = {m.R2:.4f}\nnRMSE = {m.nRMSE_percent:.2f}%",transform=ax.transAxes,va='top',fontsize=12)
        axes_finish(ax,'Potência medida (kW)','Potência simulada (kW)')
        return fig
    add('G13_validacao',['4.4'],'Comparação entre potência simulada e medida',
        'Modelo físico original, sem ajuste empírico; 4.401 pares diurnos. R²=1−SSE/SST e r calculado separadamente. nRMSE normalizado pela média observada dos pares.',
        ['R27'],validation,size=(6.3,5.7))
    def residual_time(t):
        fig,ax=plt.subplots();local=p.index.tz_convert(tz)
        x=local.dayofyear+(local.hour+local.minute/60)/24
        ax.scatter(x,p.residual_kW,s=5,alpha=.4);axes_finish(ax,'Dia do ano de 2024','Resíduo (kW)',zero=True)
        return fig
    add('G14_residuos_temporais',['4.4'],'Resíduos ao longo do trimestre',
        'Resíduo = potência simulada − medida, sobre os pares diurnos. Valores positivos representam superestimação. Nenhum ponto foi removido pelo tamanho do erro.',
        ['R27'],residual_time)
    def residual_power(t):
        fig,ax=plt.subplots();ax.scatter(p.observed_kW,p.residual_kW,s=7,alpha=.35)
        axes_finish(ax,'Potência medida (kW)','Resíduo (kW)',zero=True);return fig
    add('G15_residuos_potencia',['4.4'],'Resíduos em função da potência observada',
        'Diagnóstico de dependência do erro com o nível de potência; não identifica isoladamente causas operacionais, ópticas ou térmicas.',
        ['R27'],residual_power)
    def residual_hist(t):
        fig,ax=plt.subplots();ax.hist(p.residual_kW,bins=35,color=t['colors'][0])
        ax.axvline(0,color=t['fg'],ls='--',label='Erro zero')
        ax.axvline(p.residual_kW.mean(),color=t['colors'][1],label='MBE')
        axes_finish(ax,'Resíduo (kW)','Intervalos');ax.legend();return fig
    add('G16_distribuicao_residuos',['4.4'],'Distribuição dos resíduos',
        'Histograma dos mesmos 4.401 resíduos. MBE mantém o sinal; MAE e RMSE resumem magnitudes diferentes do erro e são apresentados em tabela.',
        ['R27'],residual_hist)
    def monthly_errors(t):
        q=tb['metricas_por_mes'];fig,axs=plt.subplots(2,1);x=np.arange(len(q));width=.23
        for n,key in enumerate(['MBE','MAE','RMSE']):
            axs[0].bar(x+(n-1)*width,q[key],width,label=key)
        axs[0].set_xticks(x,['Abril','Maio','Junho']);axes_finish(axs[0],ylabel='Erro (kW)',zero=True)
        axs[0].legend(ncol=3)
        for n,key in enumerate(['nMBE_percent','nRMSE_percent']):
            axs[1].bar(x+(n-.5)*.32,q[key],.32,label=key.replace('_percent',''))
        axs[1].set_xticks(x,['Abril','Maio','Junho']);axes_finish(axs[1],ylabel='Erro normalizado (%)',zero=True)
        axs[1].legend(ncol=2)
        return fig
    add('G17_metricas_mensais',['4.4'],'Erros mensais do modelo físico',
        'Mesma definição de erro; normalização pela média observada de cada mês. n e cobertura estão nas tabelas. Modelos com ajuste empírico são relatados separadamente.',
        ['R27'],monthly_errors,size=(6.3,6.3))
    def stratified(t):
        q=tb['metricas_por_hora'];fig,axs=plt.subplots(2,1,sharex=True)
        axs[0].plot(q.hour_local,q.MBE,'o-');axes_finish(axs[0],ylabel='MBE por hora (kW)',zero=True)
        axs[1].bar(q.hour_local,q.n,color=t['colors'][1]);axes_finish(axs[1],'Hora local','Pares disponíveis')
        return fig
    add('G18_vies_horario',['4.4'],'Viés por hora local e tamanho da amostra',
        'Médias condicionadas à janela diurna selecionada; cada faixa tem n e cobertura próprios. O padrão horário não prova uma causa única.',
        ['R27'],stratified,size=(6.3,6.0))
    def meters(t):
        fig,ax=plt.subplots();x=d.loc[mask,'ac_meter_W']/1000;y=d.loc[mask,'ac_sum_inverters_W']/1000
        ax.scatter(x,y,s=7,alpha=.35)
        lim=max(x.max(),y.max())*1.03;ax.plot([0,lim],[0,lim],ls='--',color=t['fg'])
        ax.set(xlim=(0,lim),ylim=(0,lim));ax.set_aspect('equal',adjustable='box')
        axes_finish(ax,'Medidor AC (kW)','Soma dos 24 inversores (kW)');return fig
    add('G19_consistencia_medicoes',['1.4','4.4'],'Consistência entre referências elétricas',
        'Comparação entre dois registros observacionais locais; não é previsão do modelo. Divergências entre medidor e inversores integram os limites da referência.',
        ['R01','R25'],meters,size=(6.3,5.5))
    def soiling(t):
        q=ctx['environment_sensitivity'];fig,ax=plt.subplots();x=np.arange(3)
        for n,(label,group) in enumerate(q.groupby('thermal_scenario',sort=False)):
            ax.bar(x+(n-.5)*.34,group.E_AC_paired_kWh/1000,.34,label=label.replace(', cenário',''))
        ax.set_xticks(x,['0%','2%','5%']);axes_finish(ax,'Sujidade adicional assumida','Energia AC pareada (MWh)')
        ax.legend(fontsize=10.5);return fig
    add('G20_sujidade_ventilacao',['2.1','2.3'],'Sensibilidade à sujidade e à ventilação',
        'Cenários, não perdas medidas. Sujidade representa atenuação adicional do módulo em relação à leitura POA; considerar a condição do sensor evita dupla contagem. Ventilação reduzida usa U₀=15 e U₁=3.',
        ['R07','R28'],soiling,'cenários hipotéticos')
    def psh(t):
        q=tb['energia_e_HSP_diurna_pareada'];fig,ax=plt.subplots()
        ax.plot(q.day_local.dt.dayofyear,q.PSH_POA_paired_h)
        axes_finish(ax,'Dia do ano de 2024','PSH da janela POA pareada (h)')
        return fig
    add('G21_HSP_POA_pareada',['4.2'],'Horas equivalentes de sol na janela pareada',
        'HSP/PSH=H_POA/(1 kW/m²), correspondente a Yr na janela. Não é duração medida de brilho solar nem HSP integral do dia. A cobertura diária está no CSV.',
        ['R12','R30'],psh)
    if 'resource_for_scenarios' in ctx:
        def albedo(t):
            q=ctx['environment_scenarios'].iloc[:3];fig,ax=plt.subplots()
            ax.bar(['0,10','0,20','0,40'],q.H_POA_kWh_m2)
            axes_finish(ax,'Albedo assumido','Irradiação POA estimada (kWh/m²)');return fig
        add('G22_albedo',['2.2','3.1'],'Sensibilidade ao albedo assumido',
            'Transposição das mesmas componentes reconstruídas com albedo-base 0,20. A variação isola o parâmetro da transposição e não valida albedo. Apenas 1.037 horas elegíveis; não é trimestre integral. A POA medida da cadeia principal não recebe reflexão novamente.',
            ['R14','R15','R29'],albedo,'componentes estimadas e hipótese de albedo')
        def components(t):
            q=ctx['resource_for_scenarios'];local=q.index.tz_convert(tz)
            use=local.strftime('%Y-%m-%d')==day
            h=local[use].hour+.5
            fig,ax=plt.subplots()
            for n,(key,label) in enumerate([('ghi_Wm2','GHI estimada'),('dni_Wm2','DNI estimada'),('dhi_Wm2','DHI estimada')]):
                ax.plot(h,q.loc[use,key],label=label,ls=['-','--',':'][n],marker=['o','s','^'][n],ms=4)
            axes_finish(ax,'Hora local no meio do intervalo','Irradiância estimada (W/m²)');ax.legend(fontsize=11);return fig
        add('G23_componentes_estimadas',['1.2','3.1'],'Componentes reconstruídas da POA',
            f'Exemplo de {day}, em horas elegíveis. Driesse 2024 e Erbs–Driesse; não são três sensores independentes. O fechamento pelo modelo não prova exatidão das componentes.',
            ['R14','R15','R16','R18'],components,'estimativa exploratória')
        def bipv(t):
            q=ctx['bipv_comparison'];fig,ax=plt.subplots()
            labels=['Inclinado','Sul vertical','Leste vertical','Oeste vertical']
            ax.barh(labels[::-1],q.E_AC_for_1kWp_kWh.iloc[::-1])
            axes_finish(ax,'Energia específica simulada (kWh/kWp)');return fig
        add('G24_BIPV_orientacoes',['2.4','4.5'],'Cenários de orientação e integração',
            'Mesmo recorte de componentes estimadas, meteorologia e capacidade de normalização. Cenários verticais incluem menor ventilação; portanto a comparação combina orientação e condição térmica. Sem medições de fachada.',
            ['R14','R19'],bipv,'cenários BIPV, 1.037 horas elegíveis')
        def partition(t):
            q=ctx['bipv_energy_summary'].iloc[1:6];fig,ax=plt.subplots()
            labels=['Refletida','Transmitida','Elétrica DC','Calor para dentro','Calor para fora']
            ax.barh(labels[::-1],q.energy_kWh.iloc[::-1]/1000)
            axes_finish(ax,'Energia solar particionada (MWh)');return fig
        add('G25_BIPV_balanco',['4.5'],'Partição solar do exemplo semitransparente',
            'Área hipotética de 100 m²; ρsolar=0,12, τsolar=0,25, α=0,63, eficiência de referência=0,10. Soma das cinco parcelas igual à energia incidente. SHGC equivalente simplificado, sem certificação.',
            ['R19','R20'],partition,'balanço solar hipotético')
    return ctx['figures']


def box(ax,xy,width,height,text,t,color=0,fs=12):
    patch=FancyBboxPatch(xy,width,height,boxstyle='round,pad=0.012,rounding_size=0.015',
        facecolor=t['bg'],edgecolor=t['colors'][color],lw=1.8)
    ax.add_patch(patch);ax.text(xy[0]+width/2,xy[1]+height/2,text,ha='center',va='center',fontsize=fs)
    return patch


def arrow(ax,start,end,t,color=0,dashed=False):
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,
        lw=1.7,color=t['colors'][color],linestyle='--' if dashed else '-'))


def generate_schematics(ctx):
    def flow(t):
        fig,ax=plt.subplots();ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
        nodes=[(.83,'1 Recurso solar\nPOA e geometria'),(.65,'Controle de qualidade\nPareamento temporal'),
               (.47,'2 Ambiente\nTemperatura e vento'),
               (.29,'3 Conversão\nTemperatura → DC → AC'),(.11,'4 Desempenho\nEnergia e erros')]
        for y,label in nodes:box(ax,(.06,y),.50,.13,label,t,0)
        for (y,_),(next_y,_) in zip(nodes[:-1],nodes[1:]):arrow(ax,(.31,y),(.31,next_y+.13),t)
        box(ax,(.68,.11),.28,.13,'AC medida\nReferência',t,1,11.5)
        arrow(ax,(.68,.175),(.57,.175),t,1)
        box(ax,(.68,.72),.28,.15,'Inversão POA\nGHI/DNI/DHI\nestimadas',t,2,11)
        arrow(ax,(.57,.895),(.68,.80),t,2,True)
        box(ax,(.68,.44),.28,.13,'4.5 BIPV\nCenário',t,2,12)
        arrow(ax,(.82,.71),(.82,.58),t,2,True)
        ax.text(.70,.35,'Ramo exploratório',fontsize=10.5)
        ax.text(.06,.025,'Dados locais → cálculo → comparação observacional',fontsize=10.5)
        return fig
    export_figure(ctx,'FL01_fluxo_projeto','fluxogramas',['1.4','3.1','4.4','4.5'],
        'Fluxo do estudo com medições locais',
        'As observações AC são referência para comparação, não entrada da previsão física. Controle de qualidade e pareamento precedem a análise. Setas tracejadas identificam a extensão exploratória.',
        ['R01','R09','R14'],flow,'esquema do método',(6.3,6.5))
    def plane(t):
        fig,axs=plt.subplots(2,1)
        ax=axs[0];ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-2.2,2.1),ylim=(-.3,2.6))
        ax.plot([-2,2],[0,0],color=t['fg'],lw=1.5)
        start=np.array([-1.,0]);end=start+2.6*np.array([np.cos(np.deg2rad(25)),np.sin(np.deg2rad(25))])
        ax.plot([start[0],end[0]],[start[1],end[1]],lw=6,color=t['colors'][0])
        center=(start+end)/2
        for angle,label,c,length in [(90,'Vertical',5,1.7),(115,'Normal',2,1.9),(145,'Direção do Sol',1,2.0)]:
            tip=center+length*np.array([np.cos(np.deg2rad(angle)),np.sin(np.deg2rad(angle))])
            arrow(ax,center,tip,t,c);ax.text(tip[0],tip[1]+.07,label,fontsize=10.5,ha='center')
        for r,a1,a2 in [(.9,90,145),(.62,115,145)]:
            ax.add_patch(Arc(center,2*r,2*r,theta1=a1,theta2=a2,color=t['fg'],lw=1.1))
        ax.add_patch(Arc(start,1.3,1.3,theta1=0,theta2=25,color=t['fg']))
        ax.text(-.26,.10,'β = 25°',fontsize=11)
        ax.text(-.25,1.64,'θz = 55°',fontsize=10.5)
        ax.text(-.70,1.18,'θi = 30°',fontsize=10.5)
        ax.text(1.2,-.22,'Horizontal',fontsize=10.5,ha='center')
        ax=axs[1];ax.set_aspect('equal');ax.axis('off');ax.set(xlim=(-1.6,1.8),ylim=(-1.45,1.5))
        for x,y,label in [(0,1.2,'N 0°'),(1.2,0,'L 90°'),(0,-1.2,'S 180°'),(-1.2,0,'O 270°')]:
            ax.plot([0,x],[0,y],color=t['grid'],lw=1);ax.text(x*1.12,y*1.12,label,ha='center',va='center',fontsize=11)
        arrow(ax,(0,0),(0,-.95),t,0)
        ax.add_patch(Arc((0,0),1.6,1.6,theta1=-90,theta2=90,color=t['colors'][0]))
        ax.text(.55,.35,'Azimute do\narranjo 180°',fontsize=11)
        return fig
    export_figure(ctx,'F01_plano_angulos','figuras',['1.1','2.4','3.1'],'Plano do arranjo e convenções angulares',
        'Corte coplanar didático: β=25° documentado; θz=55° e θi=30° são valores ilustrativos coerentes nesse corte. Abaixo, azimute medido a partir do norte no sentido horário; arranjo orientado ao sul. Não é um levantamento tridimensional da usina.',
        ['R03','R09'],plane,'geometria documentada e exemplo solar hipotético',(6.3,7.0))
    def components(t):
        fig,ax=plt.subplots();ax.axis('off');ax.set_aspect('equal');ax.set(xlim=(0,10),ylim=(0,6.5))
        ax.plot([.3,9.5],[.5,.5],color=t['fg'],lw=1.5)
        module=np.array([[3,1],[7,2.9]])
        ax.plot(module[:,0],module[:,1],lw=9,color=t['colors'][0])
        ax.text(5.4,.62,'Plano do módulo',fontsize=12)
        arrow(ax,(1.0,5.8),(4.4,2.0),t,1);ax.text(.45,5.9,'Direta',fontsize=13)
        for x,tx in [(4,4.8),(6,5.7),(8.5,6.4)]:arrow(ax,(x,5.7),(tx,2.9),t,2)
        ax.text(6.2,6.02,'Difusa do céu',fontsize=13)
        arrow(ax,(8.8,.55),(6.4,2.75),t,3);ax.text(7.5,.1,'Refletida pelo solo',fontsize=11.5,ha='center')
        ax.text(.4,.1,'Solo',fontsize=12)
        ax.text(.5,2.45,'POA no módulo',fontsize=12)
        return fig
    export_figure(ctx,'F02_componentes_POA','figuras',['1.2','2.2','3.1'],'Componentes incidentes no plano do módulo',
        'Representação esquemática das contribuições à POA. Não atribui medições locais de GHI/DNI/DHI nem albedo. O sensor POA da cadeia principal já recebe a contribuição refletida do entorno.',
        ['R06','R29'],components,'esquema radiativo',(6.3,4.6))
    def array(t):
        fig,ax=plt.subplots();ax.axis('off');ax.set(xlim=(0,1),ylim=(0,1))
        for y,text in [(.78,'Módulos FV\n2.880 no sistema'),(.56,'24 grupos de 120 módulos\nExemplo: 20 em série × 6 strings'),
                       (.34,'24 inversores\nDC → AC'),(.12,'Medidor AC\nGeração observada')]:
            box(ax,(.08,y),.84,.14,text,t,0,12)
        for y in [.78,.56,.34]:arrow(ax,(.50,y),(.50,y-.08),t)
        ax.text(.08,.02,'Topologia 20 × 6 apenas equivalente didático',fontsize=11)
        return fig
    export_figure(ctx,'F03_arranjo_eletrico','figuras',['3.3','3.4','3.5'],'Organização elétrica do sistema de referência',
        'Número de módulos, inversores e módulos por grupo documentados. Associação 20 em série por 6 strings é um equivalente didático de 120 módulos, não confirmação da fiação/MPPT real. Tensões e correntes desse equivalente são calculadas em CSV.',
        ['R01','R10','R13'],array,'metadados e associação equivalente hipotética',(6.3,6.0))
    def facade(t):
        fig,axs=plt.subplots(1,2)
        for ax in axs:ax.axis('off');ax.set_aspect('equal');ax.set(xlim=(0,4),ylim=(0,5))
        ax=axs[0];ax.plot([.2,3.8],[.6,.6],color=t['fg'])
        ax.plot([.7,3.4],[1.0,2.26],lw=8,color=t['colors'][0])
        ax.text(.5,3.9,'Arranjo inclinado',fontsize=12)
        ax.text(1.1,.9,'25°',fontsize=12)
        arrow(ax,(.4,3.5),(1.5,1.8),t,1)
        ax=axs[1];ax.add_patch(Rectangle((2.0,.6),1.3,3.4,facecolor=t['grid'],alpha=.35))
        ax.plot([2,2],[.6,4],lw=8,color=t['colors'][2])
        ax.plot([.2,3.8],[.6,.6],color=t['fg'])
        ax.text(.35,4.35,'Fachada BIPV',fontsize=12)
        ax.text(2.1,.30,'90°',fontsize=12)
        arrow(ax,(.2,3.6),(1.9,2.8),t,1)
        arrow(ax,(2.05,2.6),(3.2,2.6),t,3)
        ax.text(.0,1.3,'Transmissão\ne partição\nelétrica/térmica',fontsize=10.5)
        return fig
    export_figure(ctx,'F04_geometrias_BIPV','figuras',['2.4','4.5'],'Arranjo inclinado e extensão de fachada',
        'Comparação geométrica didática. A fachada e suas propriedades semitransparentes são hipotéticas. O painel inclinado corresponde à referência geométrica; não existe fachada BIPV monitorada nos dados.',
        ['R19','R20'],facade,'esquema BIPV hipotético',(6.3,4.4))


def save_tables(ctx):
    folder=ctx['root']/'outputs/tabelas/csv';folder.mkdir(parents=True,exist_ok=True)
    for key,table in ctx['analytics_tables'].items():table.to_csv(folder/(key+'.csv'),index=False)
    for key in ['metrics','capacity_sensitivity','yields','energy_stages','operational_flags',
                'environment_scenarios','environment_sensitivity','bipv_comparison','bipv_energy_summary']:
        if key in ctx:ctx[key].to_csv(folder/(key+'.csv'),index=False)
    pd.DataFrame([ctx['meter_inverter_consistency']]).to_csv(folder/'consistencia_medidor_inversores.csv',index=False)
    fv.data_status().to_csv(ctx['root']/'outputs/quadros/situacao_dos_dados.csv',index=False)
    if 'reverse_diagnostics' in ctx:
        ctx['reverse_diagnostics'].to_csv(folder/'componentes_estimadas_da_POA_horario.csv',index_label='interval_start_UTC')
    if 'bipv_balance' in ctx:ctx['bipv_balance'].to_csv(folder/'bipv_balanco_solar_horario.csv',index_label='interval_start_UTC')
    ctx['data'].join(ctx['model_a'].add_prefix('model_A_')).to_csv(folder/'series_15min_local_e_modelo.csv',index_label='interval_start_UTC')


def save_catalog(ctx):
    dest=ctx['root']/'outputs/relatorios';dest.mkdir(parents=True,exist_ok=True)
    (dest/'catalogo_figuras.json').write_text(json.dumps(ctx['figures'],ensure_ascii=False,indent=2))
    pd.DataFrame([{k:( '; '.join(v) if isinstance(v,list) else v) for k,v in r.items() if k!='files'}
                  for r in ctx['figures']]).to_csv(dest/'catalogo_figuras.csv',index=False)


def show(ctx,ids,theme='escuro'):
    from IPython.display import display,Image,Markdown
    for r in ctx['figures']:
        if r['id'] in ids:
            display(Markdown('**'+r['title']+'**'))
            display(Image(filename=str(ctx['root']/r['files'][theme]['preview']),width=950))
            display(Markdown(r['caption']+'\n\n**Fonte:** '+FIGURE_SOURCE+'\n\nReferências metodológicas: '+', '.join(r['refs'])+'.'))


def figure_cache_signature(ctx):
    root=ctx['root']
    physical={k:ctx['config'][k] for k in ['site','period','system','assumptions','bipv','workflow']}
    digest=lambda path:hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(physical_config=physical,
        physical_code_sha256=digest(root/'src/projeto_fv.py'),
        rendering_code_sha256=digest(root/'src/refinamento_fv.py'),
        numerical_tables={p.name:digest(p) for p in sorted((root/'outputs/tabelas/csv').glob('*.csv'))},
        figures={str(p.relative_to(root)):digest(p) for folder in [root/'outputs',root/'secoes'] for p in sorted(folder.rglob('*'))
                 if p.suffix in ['.pdf','.png'] and '_previews' not in p.parts})


def generate_all(ctx,reuse_checked=False):
    analytics(ctx)
    for name in ['quadros','relatorios']:(ctx['root']/'outputs'/name).mkdir(parents=True,exist_ok=True)
    cache=ctx['root']/'outputs/relatorios/cache_figuras_verificadas.json'
    save_tables(ctx)
    signature=figure_cache_signature(ctx)
    if reuse_checked and cache.exists() and json.loads(cache.read_text())==signature:
        ctx['figures']=json.loads((ctx['root']/'outputs/relatorios/catalogo_figuras.json').read_text())
        for r in ctx['figures']:
            r['source']=FIGURE_SOURCE
            editorial.assign_figure(root=ctx['root'],record=r)
        assert len(ctx['figures'])==30
        print('Reutilizadas 30 figuras: parâmetros, códigos, tabelas numéricas e bytes gráficos conferidos.',flush=True)
        ctx['figure_cache_reused']=True
    else:
        generate_graphs(ctx);generate_schematics(ctx)
        ctx['figure_cache_reused']=False
    save_catalog(ctx)
    cache.write_text(json.dumps(figure_cache_signature(ctx),ensure_ascii=False,indent=2))
    return ctx
