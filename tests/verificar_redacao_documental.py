"""Check source traceability and scientific invariants across document formats."""
from pathlib import Path
import ast
import base64
import hashlib
import io
import json
import re
import subprocess
import sys
import zipfile

from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
from integridade_documental import records,verify_record

BASE='85390a506c95a45436c0bfdaab1e2715d255cb9f'
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'm':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
PATTERN=re.compile(r'solicitad[oa].{0,35}usuári|nesta (?:tarefa|missão)|a pedido do usuário|Material atualizado|No inventário geral os quatro quadros|não retornou repositórios acessíveis',re.I)


def source(path):
    return subprocess.check_output(['git','-C',str(ROOT),'show',BASE+':'+path])


def notebook_code(text):
    text=re.sub(r'(b64decode\([\'\"])[^\'\"]{100,}([\'\"]\))',r'\1PAYLOAD\2',text)
    text=re.sub(r'(hashlib.sha256\(support\).hexdigest\(\)==[\'\"])[a-f0-9]{64}',r'\1DIGEST',text)
    return ast.dump(ast.parse(text),include_attributes=False)


def main():
    changed=subprocess.check_output(['git','-C',str(ROOT),'diff',BASE,'--name-only'],text=True).splitlines()
    assert not [p for p in changed if p.startswith(('src/','config/','data/processed/','data/raw/','outputs/series/','outputs/avaliacao/','outputs/tabelas/csv/'))]
    registry=records();assert registry
    for path,record in registry.items():verify_record(path,record)
    docx_count=0;maths=0;notebooks=0
    for path in subprocess.check_output(['git','-C',str(ROOT),'ls-files'],text=True).splitlines():
        p=ROOT/path
        if p.suffix=='.docx':
            with zipfile.ZipFile(p) as current,zipfile.ZipFile(io.BytesIO(source(path))) as original:
                new=etree.fromstring(current.read('word/document.xml'))
                old=etree.fromstring(original.read('word/document.xml'))
                original_math=[etree.tostring(n,method='c14n') for n in old.xpath('//m:oMath',namespaces=NS)]
                actual_math=[etree.tostring(n,method='c14n') for n in new.xpath('//m:oMath',namespaces=NS)]
                assert original_math==actual_math,path
                maths+=len(actual_math);docx_count+=1
                # All scientific tables retain every original cell value.
                if path!='docs/planejamento/Plano_Equipe_SPGER0046.docx':
                    def cells(tree):return [''.join(n.xpath('.//w:t/text()',namespaces=NS)).replace('N Fórmula no notebook','N Fórmula do notebook') for n in tree.xpath('//w:tbl//w:tc',namespaces=NS)]
                    assert cells(old)==cells(new),path
                for text in new.xpath('//w:t/text()',namespaces=NS):assert not PATTERN.search(text),(path,text)
        elif p.suffix=='.ipynb':
            old=json.loads(source(path));new=json.loads(p.read_text());notebooks+=1
            assert len(old['cells'])==len(new['cells']),path
            for before,after in zip(old['cells'],new['cells']):
                assert before.get('outputs')==after.get('outputs'),path
                assert before.get('execution_count')==after.get('execution_count'),path
                text=''.join(after['source'])
                if before['cell_type']=='code':
                    assert notebook_code(''.join(before['source']))==notebook_code(text),path
                    match=re.search(r'b64decode\([\'\"]([^\'\"]{100,})[\'\"]\)',text)
                    if match:
                        data=base64.b64decode(match[1],validate=True)
                        assert hashlib.sha256(data).hexdigest() in text,path
                        with zipfile.ZipFile(io.BytesIO(data)) as archive:
                            assert archive.testzip() is None
                            for name in archive.namelist():
                                local=ROOT/name
                                if path.startswith('bibliografia/'):local=ROOT/'bibliografia'/name
                                if name.endswith('.py') and local.is_file() and not name.startswith('src/'):
                                    assert archive.read(name)==local.read_bytes(),(path,name)
                else:assert not PATTERN.search(text),(path,text[:200])
        elif p.suffix in {'.md','.txt'}:
            assert not PATTERN.search(p.read_text()),path
    # Citation strings, IDs and subsection associations retain their identity.
    old=json.loads(source('bibliografia/principal/Referencias_B01_B39.json'))
    new=json.loads((ROOT/'bibliografia/principal/Referencias_B01_B39.json').read_text())
    assert len(new)==39
    for a,b in zip(old,new):
        assert {k:v for k,v in a.items() if k!='observacao'}=={k:v for k,v in b.items() if k!='observacao'}
    print(json.dumps({'Word_documents':docx_count,'native_equations_preserved':maths,
                      'notebooks_with_code_and_outputs_preserved':notebooks,
                      'scientific_files_unchanged':True,'references':39,
                      'document_sources_verified':len(registry)},ensure_ascii=False))


if __name__=='__main__':main()
