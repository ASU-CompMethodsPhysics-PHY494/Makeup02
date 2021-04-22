# -*- coding: utf-8 -*-
# ASSIGNMENT: Makeup 02
# PROBLEM NUMBER: 1b

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_imagefile

FILENAME = 'capacitor_potential_3d.png'
POINTS = 3

def test_potential_3d_plot():
    return _test_imagefile(FILENAME)


