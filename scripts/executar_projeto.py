"""Execute the existing model and export the team's shared technical datasets.

The physical implementation remains in src/projeto_fv.py and refinamento_fv.py.
"""
from pathlib import Path
import argparse
import hashlib
import json
import platform
import subprocess
import sys
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'src'))


def exportar_estrutura(ctx):
    """Export views of a single computation, without changing its masks or inputs."""
    import pandas as pd
    import refinamento_fv as rf
    d, a = ctx['data'], ctx['model_a']
    root = ctx['root']
    for directory in ['outputs/quadros', 'outputs/tabelas/csv', 'outputs/avaliacao',
                      'outputs/series', 'outputs/logs', 'data/processed/meteorologia',
                      'data/processed/irradiancia', 'data/processed/eletrica_observada',
                      'data/processed/base_modelagem']:
        (root / directory).mkdir(parents=True, exist_ok=True)

    def save(frame, name):
        frame.to_csv(root / name, index_label='interval_start_UTC')

    save(d[['temp_air_C', 'wind_ms', 'wind_direction_deg']],
         'data/processed/meteorologia/meteorologia_15min.csv')
    save(d[['poa_measured_Wm2', 'irradiance_3_samples']],
         'data/processed/irradiancia/poa_15min.csv')
    save(d[['ac_meter_W', 'ac_sum_inverters_W', 'dc_VI_derived_W', 'inverters_3_samples']],
         'data/processed/eletrica_observada/potencias_15min.csv')
    # This table contains physical inputs and quality masks; the measured target
    # is kept in the observational dataset above to make its role explicit.
    save(d[['poa_measured_Wm2', 'temp_air_C', 'wind_ms', 'wind_direction_deg',
            'daylight', 'availability', 'physical_bounds', 'paired_daylight']],
         'data/processed/base_modelagem/entradas_e_mascaras_15min.csv')
    save(a, 'outputs/series/potencias_modeladas_15min.csv')
    ctx['metrics'].to_csv(root / 'outputs/avaliacao/metricas.csv', index=False)
    ctx['yields'].to_csv(root / 'outputs/avaliacao/produtividades_PR_perdas.csv', index=False)
    ctx['energy_stages'].to_csv(root / 'outputs/avaliacao/cadeia_energetica.csv', index=False)
    rf.analytics(ctx)
    rf.save_tables(ctx)
    # Keep the exported small numerical tables alongside the plot index.
    # Large combined tables are generated locally and remain outside Git.
    from importlib.metadata import version
    sources = json.loads((root / 'data/raw/fontes_pvdaq.json').read_text())
    files = {str(p.relative_to(root)): hashlib.sha256(p.read_bytes()).hexdigest()
             for directory in ['src', 'config'] for p in (root / directory).glob('*')
             if p.is_file()}
    try:
        git_revision = subprocess.check_output(
            ['git', '-C', str(root), 'rev-parse', 'HEAD'], stderr=subprocess.DEVNULL,
            text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        git_revision = None
    log = {
        'generated_at_UTC': datetime.now(timezone.utc).isoformat(),
        'project_version': ctx['config']['version'], 'git_revision': git_revision,
        'source_code_and_configuration_sha256': files,
        'period': ctx['config']['period'], 'site_timezone': ctx['config']['site']['timezone'],
        'export_timezone': 'UTC', 'original_sources': sources,
        'audit': ctx['audit'], 'primary_metrics': ctx['metrics'].iloc[0].to_dict(),
        'python': platform.python_version(),
        'packages': {k: version(k) for k in ['numpy', 'pandas', 'scipy', 'pvlib']},
        'observed_generation_role': 'validation reference; not an input to the physical prediction',
        'interpolation': False,
        'missing_metadata': 'See docs/metodos/README.md and config/proveniencia_parametros.csv',
    }
    (root / 'outputs/logs/ultima_execucao.json').write_text(
        json.dumps(log, ensure_ascii=False, indent=2, default=str))
    print(json.dumps({'project_version': log['project_version'], 'audit': ctx['audit'],
                      'metrics': log['primary_metrics']}, ensure_ascii=False, indent=2))
    return log


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--graficos', action='store_true',
                        help='Also regenerate the complete original figure collection.')
    args = parser.parse_args()
    import projeto_fv as fv
    ctx = fv.complete_pipeline(ROOT, make_plots=False, include_nasa=False, reverse=True)
    exportar_estrutura(ctx)
    if args.graficos:
        import refinamento_fv as rf
        rf.generate_all(ctx, reuse_checked=True)


if __name__ == '__main__':
    main()
