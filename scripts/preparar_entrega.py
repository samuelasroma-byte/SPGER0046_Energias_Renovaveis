"""Generate the current local-measurement results, figures, report and ZIP."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
import projeto_fv as f,refinamento_fv as r,relatorio_fv as rel
import subprocess,os
ctx=f.complete_pipeline(ROOT,make_plots=False,include_nasa=False,reverse=True)
r.generate_all(ctx)
subprocess.run([os.environ.get('CODEX_PRIMARY_RUNTIME_PYTHON',sys.executable),str(ROOT/'scripts/gerar_documentos.py')],check=True)
subprocess.run([os.environ.get('CODEX_PRIMARY_RUNTIME_PYTHON',sys.executable),str(ROOT/'scripts/gerar_dossie_tecnico.py')],check=True)
print(rel.report(ctx))
print(f.zip_results(ctx))
