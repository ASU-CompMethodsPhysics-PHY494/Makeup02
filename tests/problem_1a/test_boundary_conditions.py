import numpy as np
from numpy.testing import (assert_equal,
                           assert_almost_equal)

import pytest

from ..tst import get_attribute


FILENAME = "capacitor.py"



@pytest.fixture(scope="class")
def Phi0(Nmax=100):
    set_boundaries = get_attribute("set_boundaries", FILENAME)

    _Phi0 = np.zeros((Nmax, Nmax))
    _Phi0 = set_boundaries(_Phi0)
    return _Phi0

class TestBoundaryConditions(object):
    # correct values for the given problem
    plate_size = 50
    voltage = 100.

    def test_voltage(self, Phi0):
        assert_almost_equal(Phi0.min(), -self.voltage)
        assert_almost_equal(Phi0.max(), self.voltage)

    def test_plate_size(self, Phi0):
        plus_plate = Phi0 > 0
        minus_plate = Phi0 < 0
        assert np.sum(plus_plate) == self.plate_size
        assert np.sum(minus_plate) == self.plate_size

    def test_plus_plate_position(self, Phi0):
        x, y = np.where(Phi0 > 0)
        assert x.min() == 25
        assert y.min() == 40
        assert x.max() == 74
        assert y.max() == 40

    def test_minus_plate_position(self, Phi0):
        x, y = np.where(Phi0 < 0)
        assert x.min() == 25
        assert y.min() == 60
        assert x.max() == 74
        assert y.max() == 60

    def test_box_boundary(self, Phi0):
        assert_equal(Phi0[:, 0], 0)
        assert_equal(Phi0[:, -1], 0)
        assert_equal(Phi0[0, :], 0)
        assert_equal(Phi0[-1, :], 0)


