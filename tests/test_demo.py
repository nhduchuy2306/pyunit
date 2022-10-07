import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('python'.upper(),'PYTHON')
    def test_lower(self):
        self.assertEqual('Python'.lower(),'python') 
    def test_isupper(self):
        self.assertTrue('PYTHON'.isupper())
        self.assertFalse('Python'.isupper())
    def test_islower(self):
        self.assertTrue('PYTHON'.isupper()) 
        self.assertFalse('python'.isupper()) 
    def test_split(self):
        test_string = 'python is the best language'
        self.assertEqual(test_string.split(),
                         ['python','is','the','best','language'])
        with self.assertRaises(TypeError):
            test_string.split(2)        

if __name__ == '__main__':
    unittest.main(verbosity=2)
    
    
