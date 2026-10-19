"""Canonical builder; delegates to the current version."""
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).with_name('build_notebook_v1_2.py')),run_name='__main__')
