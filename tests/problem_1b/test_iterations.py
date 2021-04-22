# -*- coding: utf-8 -*-
# ASSIGNMENT: Makeup 02
# PROBLEM NUMBER: 1b

# place as problem_x/test_name.py so that relative imports work

import pytest

from ..tst import _test_filecontent

FILENAME = 'iterations.txt'
POINTS = 4

def test_iterations():
    return _test_filecontent(FILENAME,
                             r"""[0-9][0-9][0-9]+""",
                             regex=True)


