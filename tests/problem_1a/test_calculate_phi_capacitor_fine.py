import numpy as np
from numpy.testing import (assert_equal,
                           assert_almost_equal)

import pytest

from ..tst import get_attribute


FILENAME = "capacitor.py"



@pytest.fixture(scope="module")
def phi_long(Max_iter=10000, tol=1e-3):
    calculate_phi_capacitor = get_attribute("calculate_phi_capacitor", FILENAME)
    Phi = calculate_phi_capacitor(Max_iter=Max_iter, tol=tol)
    return Phi

class TestPhiLong(object):
    def test_shape(self, phi_long):
        assert_equal(phi_long.shape, (100, 100))

    def test_min(self, phi_long):
        assert_almost_equal(phi_long.min(), -100)

    def test_max(self, phi_long):
        assert_almost_equal(phi_long.max(), 100)

    def test_diagonal_sum(self, phi_long):
        assert_almost_equal(np.trace(phi_long),
                            72.637059850488143, decimal=2)

    def test_half_sum(self, phi_long):
        Nx, Ny = phi_long.shape
        assert_almost_equal(phi_long[:Nx//2, :].sum(),
                            1127.5308751853702, decimal=2)

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


