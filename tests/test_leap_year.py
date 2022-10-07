import unittest
from app.leap_year import leap_year

class TestData(unittest.TestCase):  
    def test_leap_year_return_true(self):
        self.assertEqual(leap_year(2000),True)
        self.assertEqual(leap_year(2004),True)
        self.assertEqual(leap_year(1960),True)
        self.assertEqual(leap_year(1920),True)
        
    def test_leap_year_return_false(self):
        self.assertEqual(leap_year(1900),False)
        self.assertEqual(leap_year(2003),False)
        self.assertEqual(leap_year(1962),False)
        self.assertEqual(leap_year(1922),False)

if __name__ == '__main__':
    unittest.main(verbosity=2)