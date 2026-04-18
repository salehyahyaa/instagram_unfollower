"""Entry point when running from the repo root: python3 main.py"""
import os
import runpy
import sys
from pathlib import Path

from dotenv import load_dotenv

_root = Path(__file__).resolve().parent
_src = _root / "src"
_src_main = _src / "main.py"
if not _src_main.is_file():
    raise FileNotFoundError(f"Missing {_src_main}")

load_dotenv(_root / ".env")
os.chdir(_src)
sys.path.insert(0, str(_src))
runpy.run_path(str(_src_main), run_name="__main__")
