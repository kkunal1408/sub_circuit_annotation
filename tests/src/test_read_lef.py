import os
import pathlib
from os.path import dirname, abspath, join , isfile
import sys
# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '../../', 'src'))
sys.path.append(CODE_DIR)

from read_lef import read_lef
def test_lef():
    test_path=(pathlib.Path(__file__).parent / 'all_lef').resolve()
    blocks = read_lef(test_path)
    assert len(blocks) == 34
    assert 'CMC_NMOS_S_n12_X3_Y1' in blocks
