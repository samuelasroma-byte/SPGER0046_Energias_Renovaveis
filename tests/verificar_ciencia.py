"""Focused physical and numerical verification, without network access."""
from pathlib import Path
import sys,json
import numpy as np
import pandas as pd
import pvlib
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import projeto_fv as f
cfg=f.load_config(ROOT)
m=json.loads((ROOT/'config/modulo_cec.json').read_text())

# Reference STC and temperature response are independent physical expectations.
r=f.module_mpp(pd.Series([0.,1000.,1000.]),pd.Series([25.,25.,45.]),m)
assert r.loc[0,'p_mp']==0
assert np.isclose(r.loc[1,'p_mp'],m['STC'],atol=.002)
assert r.loc[2,'p_mp']<r.loc[1,'p_mp']

# Cross-check custom loss-stage accounting against pvlib's independent AC implementation.
p=pd.Series([0.,10.,3000.,50000.,400000.,750000.,900000.])
ours=f.inverter_pvwatts_stages(p,720000).ac_modeled_W
ref=pvlib.inverter.pvwatts(p,pdc0=720000/.98,eta_inv_nom=.98,eta_inv_ref=.9637)
assert np.allclose(ours,ref,atol=1e-8)

# R² must not be substituted by squared correlation.
q=f.metrics(pd.Series([1.,2.,3.]),pd.Series([3.,2.,1.]),'known counterexample')
assert np.isclose(q['r'],-1) and np.isclose(q['R2'],-3)

from unittest.mock import patch
with patch.object(f.urllib.request,'urlopen',side_effect=AssertionError('Network forbidden in local workflow')):
    c=f.complete_pipeline(ROOT,make_plots=False,include_nasa=False)
assert c['audit']['available_daylight_15m']==4401
assert c['audit']['NASA_used'] is False and 'nasa' not in c
assert len(c['reverse_diagnostics'])==2184
assert c['reverse_summary']['converged_hours']>1000
assert c['reverse_diagnostics'].loc[lambda t:t.converged,'numerical_closure_residual_Wm2'].abs().max()<.1
assert len(c['data'])==8736
st=c['energy_stages']
assert np.isclose(st.change_to_next_kWh.dropna().sum(),st.energy_kWh.iloc[0]-st.energy_kWh.iloc[-1])
assert c['bipv_balance'].balance_residual_W.abs().max()<1e-7
assert c['bipv_balance'].SHGC_equivalent_simplified.between(0,1).all()
assert (c['bipv_comparison'].n_input_hours==c['reverse_summary']['converged_hours']).all()
assert (c['bipv_comparison'].resource_origin=='reverse_POA').all()
assert np.isclose(c['metrics'].iloc[0].nRMSE_percent,14.991130565767405)
assert c['full_quarter']['meter_available_15min']==c['full_quarter']['meter_expected_15min']
# Synthetic inverse-model consistency is a numerical check, not observational validation.
parts=pvlib.irradiance.erbs_driesse(800.,25.,dni_extra=1366.1)
poa=pvlib.irradiance.get_total_irradiance(25.,180.,25.,180.,parts['dni'],800.,parts['dhi'],dni_extra=1366.1,model='perez-driesse',albedo=.2)['poa_global']
recovered,ok,_=pvlib.irradiance.ghi_from_poa_driesse_2024(25.,180.,25.,180.,poa,1366.1,albedo=.2,full_output=True)
assert ok and abs(recovered-800)<.02
print('PASS: source integrity, STC, temperature response, inverter reference, R², paired coverage, energy conservation and BIPV bounds.')
