import unittest
import main

class Test_Main(unittest.TestCase):

    def test_find_missing(self):
        l1 = [4,12,9,5,6]
        l2 = [4,9,12,6]
        self.assertEqual(main.find_missing(l1, l2), [5])
    
    def test_find_missing_with_sets(self):
        l1 = [4,12,9,5,6]
        l2 = [4,9,12,6]
        self.assertEqual(main.find_missing_with_sets(l1, l2), [5])

    def test_find_missing_xor(self):
        l1 = [4,12,9,5,6]
        l2 = [4,9,12,6]
        self.assertEqual(main.find_missing_xor(l1, l2), 5)

if __name__ == '__main__':
    unittest.main()