#!/usr/bin/env python

"""
Test for calculator app.
"""

from calc import add,subtract


class TestCalcApp:
    def test_add(self):
        assert 5 == add(3, 2)

    def test_subtract(self):
        assert 5 == subtract(7, 2)
        
    def test_add2(self):
        assert 7 == add(add(3,2), 2)
