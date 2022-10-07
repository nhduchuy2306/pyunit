
import unittest
from app.rectangle import Rectangle

class TestRangtangle(unittest.TestCase):
    def setUp(self):
        self.rangtangle = Rectangle(0,0)
        
    def test_get_area(self):
        self.rangtangle.width = 2
        self.rangtangle.height = 3
        self.assertEqual(self.rangtangle.get_area(),6)
        
    def test_get_area_with_negative_case(self):
        self.rangtangle.width = -1
        self.rangtangle.height = 2
        # self.assertEqual(self.rangtangle.get_area(),-2)
        self.assertRaises(Exception, self.rangtangle.get_area)

if __name__ == '__main__':
    unittest.main(verbosity=2)