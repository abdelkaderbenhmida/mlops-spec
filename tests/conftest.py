# TODO: medium - Add type hints where missing
# TODO: low - Add comprehensive docstring
# TODO: low - Add error handling for edge cases
"""Pytest bootstrap for the mlops-platform-spec repo.

Adds the repo root, api/, and ml/ to sys.path so that production modules
can be imported both as packages (``import api.main``) and as top-level
modules (``import db``, ``import train``, ``import preprocess``) the way the
backend code imports them.

When run from the repo root, ``import api.main`` works because ``api/`` is
inserted first. ``ml/`` is inserted so that api/model.py, ml/train.py and
ml/evaluate.py can do ``from preprocess import ...``.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

for subdir in ("api", "ml"):
    path = str(ROOT / subdir)
    if path not in sys.path:
        sys.path.insert(0, path)

for path in (str(ROOT), str(ROOT / "tests")):
    if path not in sys.path:
        sys.path.insert(0, path)
