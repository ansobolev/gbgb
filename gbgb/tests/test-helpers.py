# ---------------------------------------------
#
# The file test-helpers is part of the gbgb project.  
# Copyright (c) 2014 Andrey Sobolev  
# License GNU GPL v.2
# See http://github.com/ansobolev/gbgb for details
#
# ---------------------------------------------
__author__ = 'andrey'

from nose.tools import assert_equals, assert_raises
from unittest import TestCase
from gbgb.helpers import *

class TestHelpers(TestCase):

    def test_lcm_pos(self):
        """
        lcm test with positive numbers
        """
        assert_equals(lcm(2, 3, 4), 12)

    def test_lcm_neg(self):
        """
        lcm test with negative numbers
        """
        assert_equals(lcm(-2, -3, 4), 12)

    def test_lcm_zero(self):
        """
        lcm test with negative numbers
        """
        assert_raises(ValueError, lcm, -2, 0, 4)

