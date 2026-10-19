"""Check scientific dataset contracts and chapter completeness after export."""
from pathlib import Path
import csv
import json
import re
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
cfg = json.loads((ROOT / 'config/projeto.json').read_text())


def read(path):
    return pd.read_csv(ROOT / path, index_col=0, parse_dates=True)


meteorology = read('data/processed/meteorologia/meteorologia_15min.csv')
poa = read('data/processed/irradiancia/poa_15min.csv')
electrical = read('data/processed/eletrica_observada/potencias_15min.csv')
features = read('data/processed/base_modelagem/entradas_e_mascaras_15min.csv')
model = read('outputs/series/potencias_modeladas_15min.csv')
start = pd.Timestamp(cfg['period']['start_local'], tz=cfg['site']['timezone']).tz_convert('UTC')
end = pd.Timestamp(cfg['period']['end_exclusive_local'], tz=cfg['site']['timezone']).tz_convert('UTC')
expected = pd.date_range(start, end, freq='15min', inclusive='left', name='interval_start_UTC')
for frame in [meteorology, poa, electrical, features, model]:
    assert frame.index.equals(expected), 'The four sections must use the same UTC grid.'
    assert frame.index.is_unique and frame.index.is_monotonic_increasing
assert len(expected) == 8736
assert 'ac_meter_W' not in features and 'ac_sum_inverters_W' not in features
assert int(features.paired_daylight.sum()) == 4401
assert int(features.daylight.sum()) == 4421
assert electrical.ac_meter_W.notna().sum() == 8736
assert np.allclose(poa.poa_measured_Wm2, features.poa_measured_Wm2, equal_nan=True)
assert np.allclose(meteorology.temp_air_C, features.temp_air_C, equal_nan=True)

# Recalculate the validation indicators from the exported model and reference,
# instead of only checking that output files exist.
mask = features.paired_daylight
obs = electrical.loc[mask, 'ac_meter_W'].to_numpy() / 1000
sim = model.loc[mask, 'ac_final_W'].to_numpy() / 1000
err = sim - obs
metrics = pd.read_csv(ROOT / 'outputs/avaliacao/metricas.csv').iloc[0]
assert np.isclose(metrics['RMSE'], np.sqrt(np.mean(err ** 2)))
assert np.isclose(metrics['MBE'], np.mean(err))
assert np.isclose(metrics['R2'], 1 - (err ** 2).sum() / ((obs - obs.mean()) ** 2).sum())

modules = pd.read_csv(ROOT / 'data/equipamentos/grupos_de_modulos.csv')
inverters = pd.read_csv(ROOT / 'data/equipamentos/inversores.csv')
channels = pd.read_csv(ROOT / 'data/equipamentos/dicionario_completo_125_canais.csv')
assert modules.quantity.sum() == cfg['system']['n_modules'] == 2880
assert inverters.quantity.sum() == cfg['system']['n_inverters'] == 24
assert len(channels) == 125 and channels.metric_id.is_unique

with (ROOT / 'references/acervo_disponivel.csv').open(encoding='utf-8-sig') as handle:
    records = list(csv.DictReader(handle))
assert all(None not in row and all(value is not None for value in row.values()) for row in records), 'Malformed bibliographic CSV row.'
assert len(records) == len({r['id'] for r in records}) == 91
matrix = (ROOT / 'docs/Matriz_19_Subsecoes.md').read_text()
topics = re.findall(r'^## ([1-4]\.\d+) ', matrix, flags=re.M)
assert len(topics) == len(set(topics)) == 19
assert [sum(t.startswith(str(i) + '.') for t in topics) for i in range(1, 5)] == [4, 4, 6, 5]
print('PASS: shared time grid, target separation, exported metrics, equipment counts, 125 channels, 91 documents and 19 subsections.')
