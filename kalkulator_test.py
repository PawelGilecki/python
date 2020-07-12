import unittest
import kalkulator

class TestKalkulator(unittest.TestCase):
    def setUp(self):
        self.x  = kalkulator.kalkulator()
    def test_dummy(self):
        self.assertEqual(2,2)
    def test_dodwania_malych_liczb(self):
        x = kalkulator.kalkulator()
        self.assertEqual(4, x.dodawanie(2, 2))
    def test_odejmownaia_malych_liczb(self):
        self.assertEqual(5, self.x.odejmowanie(7, 2))