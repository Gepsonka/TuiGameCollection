import unittest


class BasicTestMethod(unittest.TestCase):
    
    def test_is_strings_are_equal(self):
        self.assertEqual("cscs", "cscs")
        
        
        
if __name__=="__main__":
    unittest.main()