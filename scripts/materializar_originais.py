"""Recover the exact public originals listed in the provenance manifest.

Existing files must match the manifest. Downloads are never accepted without
the expected byte count and SHA-256, and no scientific output is regenerated.
"""
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import argparse
import hashlib
import json
import os
import tempfile
import time

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/auditoria/Proveniencia_Arquivos_Integrados.json"
REPORT = ROOT / "docs/auditoria/Materializacao_Remota.json"


def sha256(path):
    result = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            result.update(block)
    return result.hexdigest()


def materialize(record, official):
    destination = (ROOT / record["caminho_github"]).resolve()
    if not destination.is_relative_to(ROOT):
        raise ValueError("Path outside the repository")
    expected_size = int(record["bytes"])
    expected_hash = record["sha256"]
    result = {
        "path": record["caminho_github"],
        "bytes": expected_size,
        "sha256": expected_hash,
    }
    if destination.exists():
        if destination.stat().st_size != expected_size or sha256(destination) != expected_hash:
            raise ValueError("Existing original differs: " + result["path"])
        return {**result, "status": "ja_presente_e_conferido"}

    source = official.get(destination.name)
    if source is None:
        source = "https://drive.usercontent.google.com/download?" + urlencode(
            {"id": record["drive_id"], "export": "download", "confirm": "t"}
        )
    destination.parent.mkdir(parents=True, exist_ok=True)
    for attempt in range(3):
        temporary = None
        try:
            request = Request(source, headers={"User-Agent": "SPGER0046-integridade/1.0"})
            with urlopen(request, timeout=45) as response:
                with tempfile.NamedTemporaryFile(dir=destination.parent, delete=False) as output:
                    temporary = Path(output.name)
                    size = 0
                    for block in iter(lambda: response.read(1024 * 1024), b""):
                        size += len(block)
                        if size > expected_size:
                            raise ValueError("Source larger than the manifest")
                        output.write(block)
            if size != expected_size or sha256(temporary) != expected_hash:
                raise ValueError("Download does not match the manifest: " + result["path"])
            os.replace(temporary, destination)
            return {**result, "status": "recuperado_e_conferido"}
        except Exception:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
            if attempt == 2:
                raise
            time.sleep(2 * (attempt + 1))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--workers", type=int, default=4)
    args = parser.parse_args()
    records = json.loads(MANIFEST.read_text())
    official = {
        row["file"]: row["url"]
        for row in json.loads((ROOT / "data/raw/fontes_pvdaq.json").read_text())
    }
    results = []
    with ThreadPoolExecutor(max_workers=max(1, min(args.workers, 8))) as pool:
        tasks = {pool.submit(materialize, row, official): row for row in records}
        for task in as_completed(tasks):
            result = task.result()
            results.append(result)
            print(result["status"] + ": " + result["path"], flush=True)
    results.sort(key=lambda row: row["path"])
    REPORT.write_text(json.dumps({"status": "passed", "source_copies": len(results), "files": results}, ensure_ascii=False, indent=2) + "\n")


if __name__ == "__main__":
    main()
