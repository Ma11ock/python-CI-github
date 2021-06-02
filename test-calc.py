#!/usr/bin/env python

"""
Test for calculator app.
"""

from calc import add,subtract,multiply,divide


class TestCalcApp:
    def test_add(self):
        assert 5 == add(3, 2)

    def test_subtract(self):
        assert 5 == subtract(7, 2)
        
    def test_add2(self):
        assert 7 == add(add(3, 2), 2)

    def test_mult(self):
        assert 12 == multiply(3, 4)

    def test_divide(self):
        assert 12 == divide(144, 12)
