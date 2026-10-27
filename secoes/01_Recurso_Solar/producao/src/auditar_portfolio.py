"""Conferência do recorte existente; não consulta bases nem repete a bibliometria."""
from pathlib import Path
from collections import Counter,defaultdict
import json,re,unicodedata
ROOT=Path(__file__).resolve().parents[1]
def normalized(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()
def run(root=ROOT):
    root=Path(root);p=json.loads((root/'bibliografia/Manifesto_Corpus_Secao_01.json').read_text())
    inv=json.loads((root/'bibliografia/Inventario_Fontes_Conferidas.json').read_text())
    associations=Counter(code for s in p['subsections'] for code in s['B_codes'])
    dois=defaultdict(list);titles=defaultdict(list);files=defaultdict(list)
    for code,r in p['refs'].items():
        url=r['source_url'];m=re.search(r'doi\.org/(.+)',url,re.I)
        if m:dois[m[1].lower().rstrip('/ .')].append(code)
        titles[normalized(r['title'])].append(code)
    for r in inv:files[r['sha256']].append(r['codigo'])
    result={
      'escopo':'12 referências B herdadas; seis PDFs locais inventariados; sem nova busca',
      'associacoes':sum(associations.values()),'obras_B_distintas':len(associations),
      'repeticoes_entre_subsecoes':sum(associations.values())-len(associations),
      'associacoes_por_codigo':dict(associations),
      'duplicatas_por_DOI_normalizado':[v for v in dois.values() if len(v)>1],
      'candidatos_por_titulo_normalizado':[v for v in titles.values() if len(v)>1],
      'duplicatas_binarias_SHA256':[v for v in files.values() if len(v)>1],
      'decisoes':[{'codigos':['B31','B32'],'acao':'manter distintos','motivo':'Artigo de 2004 e relatório revisado em 2008; mesmo título não implica mesma versão.'},
                  {'codigos':['B19','A003'],'acao':'manter distintos','motivo':'Obras/edições diferentes; A003 não substitui a edição B19 ausente.'},
                  {'codigos':['B36','A045'],'acao':'manter distintos','motivo':'Terceira edição de 2021 e quarta edição de 2024; leitura não transferível.'}],
      'limites':'DOIs são metadados herdados, sem validar automaticamente conteúdo ou acesso. Repetições entre subseções são associações legítimas, não documentos adicionais.'}
    (root/'documentacao/Conferencia_Duplicatas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
