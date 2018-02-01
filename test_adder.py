import unittest
import adder

class TestAdder(unittest.TestCase):

    def test_two_positive(self):
        actual = adder.add(2, 4)
        expect = 6
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()
