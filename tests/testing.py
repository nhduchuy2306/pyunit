import unittest
import app.dao,app.rectangle

class TestData(unittest.TestCase):
    def test_area(self):
        rect1 = app.rectangle.Rectangle(2,3)
        self.assertEqual(rect1.area(),6)
        # self.assertEqual(rect1.area(),9)
        
    def test_circum(self):
        rect = app.rectangle.Rectangle(4,5)
        self.assertEqual(rect.circumference(),18)
    
    def test_data_get_by_id(self):
        d = app.dao.DAO()
        data = d.get_user_by_id("SE130363")
        self.assertGreater(len(data),0)
    
    def test_get_all_data(self):
        d = app.dao.DAO()
        data = d.get_all_user()
        self.assertEqual(len(data), 8)
        
if __name__ == '__main__':
    unittest.main(verbosity=2)