"""Conferências analíticas e numéricas; exemplos construídos não são dados PVDAQ."""
from pathlib import Path
import json
import numpy as np
import pvlib

ROOT=Path(__file__).resolve().parents[1]

def run(root=ROOT):
    root=Path(root);checks=[]
    # Convenções: Duffie parte do sul, negativo a leste e positivo a oeste.
    south=np.array([-180.,-90.,0.,90.,180.])
    north=(south+180.)%360.
    assert np.array_equal(north,[0,90,180,270,0])
    checks.append('Conversão azimutal sul→norte e quatro direções cardeais')
    # Casos exatos da relação esférica, sem refração.
    for phi,delta,omega,expected in [(0,0,0,1),(0,0,90,0),(30,0,0,np.cos(np.pi/6)),(30,30,0,1)]:
        p,d,w=np.deg2rad([phi,delta,omega])
        c=np.sin(p)*np.sin(d)+np.cos(p)*np.cos(d)*np.cos(w)
        assert np.isclose(c,expected,rtol=0,atol=1e-14)
    checks.append('Relação esférica em equador, horizonte geométrico e passagem zenital')
    days=np.arange(1,367);b=2*np.pi*(days-1)/365
    factor=1.000110+.034221*np.cos(b)+.001280*np.sin(b)+.000719*np.cos(2*b)+.000077*np.sin(2*b)
    software=np.asarray(pvlib.irradiance.get_extra_radiation(days,solar_constant=1366.1,method='spencer'))
    assert np.allclose(software,1366.1*factor,atol=1e-10,rtol=0)
    assert factor.min()>0
    checks.append('Spencer confrontado com expressão independente nos dias 1–366; denominador 365')
    z=np.array([0,30,60,90,100,180.]);g0=1366.1*factor[137]
    horizontal=g0*np.maximum(0,np.cos(np.deg2rad(z)))
    assert np.isclose(horizontal[0],g0) and np.isclose(horizontal[2],g0/2)
    assert np.all(horizontal[z>90]==0) and np.all(horizontal>=0)
    checks.append('Projeção extraterrestre: normal, 60° e recorte abaixo do horizonte')
    # Exemplo dimensional: quatro médias construídas de 100 W/m² por 15 min.
    mean=np.full(4,100.);duration_h=np.full(4,.25)
    energy_Wh=float(np.sum(mean*duration_h));energy_J=float(np.sum(mean*duration_h*3600))
    assert energy_Wh==100 and energy_J==360000 and energy_J/3600==energy_Wh
    checks.append('Integral discreta de médias de intervalo: Wh/m² ↔ J/m²')
    # Uma equação de fechamento não identifica, sozinha, duas componentes.
    # Dois pares construídos distintos satisfazem a MESMA GHI e o MESMO zenital.
    closure_pairs=[(600.,200.),(400.,300.)]
    assert all(np.isclose(dni*.5+dhi,500) for dni,dhi in closure_pairs)
    assert closure_pairs[0]!=closure_pairs[1]
    checks.append('Subdeterminação do fechamento: dois pares DNI/DHI construídos com mesma GHI')
    result={'verificacoes':checks,'total':len(checks),'falhas':0,
      'exemplos_construidos':'Integração e fechamento são testes didáticos, não medições nem reconstruções PVDAQ.',
      'dominios':'Zenital geométrico; graus convertidos para radianos; massa de ar secante não testada no horizonte.',
      'nao_demonstrado':['incerteza do sensor','validação observacional de componentes reconstruídas','condição de céu claro']}
    (root/'resultados/Conferencia_Relacoes_Fisicas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result

if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
