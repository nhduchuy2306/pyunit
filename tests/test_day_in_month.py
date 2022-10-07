import unittest
from app.check_date_time import days_in_month

class MyTestCase(unittest.TestCase):
    def test_boundary_1_2020_should_return_31(self):
        """Success"""
        self.assertEqual(days_in_month(2020,1),31)
    def test_boundary_2_2021_should_return_28(self):
        """Success"""
        self.assertEqual(days_in_month(2021,2),28)
    def test_boundary_2_2000_should_return_28(self):
        """Success"""
        self.assertEqual(days_in_month(2000,2),29)
    def test_normal_4_2019_should_return_30(self):
        """Success"""
        self.assertEqual(days_in_month(2019,4),30)
    def test_abnormal_null_2021_should_return_0(self):
        """Input is null"""
        self.assertEqual(days_in_month(2021,None),0)

if __name__ == '__main__':
    unittest.main()