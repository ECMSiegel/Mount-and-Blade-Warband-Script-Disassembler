"""Makes `python3 -m unittest tests.test_wbops` work as well as `discover -s tests`.

The test files import each other's helpers by bare name (`import _support`), which
works under `discover -s tests` because that puts this folder on sys.path. When the
folder is imported as a package instead, put it there here.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
