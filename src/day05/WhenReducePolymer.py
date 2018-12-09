import unittest

from src.day05.day05 import reduce


class WhenReducePolymer(unittest.TestCase):
    def test_aA_reduces_to_empty(self):
        self.assertEqual("", reduce("aA"))

    def test_Aa_reduces_to_empty(self):
        self.assertEqual("", reduce("Aa"))

    def test_xAax_reduces_to_xx(self):
        self.assertEqual("xx", reduce("xAax"))

    def test_XAax_reduces_to_empty(self):
        self.assertEqual("", reduce("XAax"))
