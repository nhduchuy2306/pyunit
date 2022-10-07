import unittest

from app.check_date_time import is_valid_date

class MyTestCase(unittest.TestCase):
    def test_normal_29_2_2020_should_return_tru(self):
        """Success"""
        self.assertEqual(is_valid_date(2020, 2, 29), True)
        
    def test_normal_29_2_2000_should_return_tru(self):
        """Success"""
        self.assertEqual(is_valid_date(2000, 2, 29), True)
        
    def test_abnormal_31_4_2009_should_return_false(self):
        """Day is out of range"""
        self.assertEqual(is_valid_date(2009, 4, 31), False)

    def test_boundary_30_4_2009_should_return_true(self):
        """Success"""
        self.assertEqual(is_valid_date(2009, 4, 30), True)

    def test_boundary_31_3_2020_should_return_true(self):
        """Success"""
        self.assertEqual(is_valid_date(2020, 3, 31), True)

    def test_normal_30_3_2009_should_return_true(self):
        """Success"""
        self.assertEqual(is_valid_date(2009, 3, 30), True)

    def test_abnormal__4_2000_should_return_false(self):
        """Day is null"""
        self.assertEqual(is_valid_date(2009, 3, None), False)

    def test_boundary_28_2_1700_should_return_true(self):
        """Success"""
        self.assertEqual(is_valid_date(1700, 2, 28), True)

    def test_abnormal_31_2_2009_should_return_false(self):
        """Day is out of range"""
        self.assertEqual(is_valid_date(2009, 2, 31), False)

    def test_boundary_29_2_1700_should_return_false(self):
        """Day is out of range"""
        self.assertEqual(is_valid_date(1700, 2, 29), False)

    def test_abnormal_30_13_3000_should_return_false(self):
        """Month is out of range"""
        self.assertEqual(is_valid_date(3000, 13, 30), False)

    def test_abnormal_0_4_2009_should_return_false(self):
        """Day is out of range"""
        self.assertEqual(is_valid_date(2009,4,0), False)

    def test_abnormal_29_3_999_should_return_false(self):
        """Year is out of range"""
        self.assertEqual(is_valid_date(999,3,29), False)

    def test_normal_28_4_1700_should_return_true(self):
        """Success"""
        self.assertEqual(is_valid_date(1700,4,28), True)

    def test_abnormal_28_13_3001_should_return_false(self):
        """Year is out of range, Month is out of range"""
        self.assertEqual(is_valid_date(3001,13,28), False)

    def test_abnormal_29__1700_should_return_false(self):
        """Month is null"""
        self.assertEqual(is_valid_date(1700,None,29), False)

    def test_abnormal_28_4__should_return_false(self):
        """Year is null"""
        self.assertEqual(is_valid_date(None,4,28), False)

