"""Validate consultation documents against their identified source snapshots."""
from pathlib import Path
import hashlib
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]


def records():
    path=ROOT/'docs/auditoria/Edicoes_Documentais.json'
    if not path.exists():return {}
    return {r['path']:r for r in json.loads(path.read_text())['files']}


def verify_record(path, record):
    source=subprocess.check_output(['git','-C',str(ROOT),'show',record['source_commit']+':'+path])
    assert hashlib.sha256(source).hexdigest()==record['source_sha256'],path
    assert hashlib.sha256((ROOT/path).read_bytes()).hexdigest()==record['sha256'],path
    return source


def unregistered_changes(paths):
    registry=records();remaining=[]
    for path in paths:
        if path in registry:verify_record(path,registry[path])
        else:remaining.append(path)
    return remaining
