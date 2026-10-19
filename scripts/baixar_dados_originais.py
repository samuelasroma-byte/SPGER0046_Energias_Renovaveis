"""Download/check the official PVDAQ inputs using the original SHA-256 manifest."""
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from projeto_fv import read_sources
if __name__=='__main__':
    frames,metadata,_=read_sources(ROOT,include_nasa=False)
    print('Originais completos conferidos por SHA-256: quatro CSVs e metadados; NASA fora da cadeia principal.')
