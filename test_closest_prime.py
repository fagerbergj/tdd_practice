import unittest
from closest_prime import closest_prime, is_prime

class TestIsPrime(unittest.TestCase):
    def test_returns_true_when_prime(self):
        inputs = [2, 3, 5, 7, 11, 13]
        for i in inputs:
            self.assertTrue(is_prime(i))

    def test_returns_false_when_not_prime(self):
        inputs = [0, 1, 4, 6, 8, 9, 10, 12]
        for i in inputs:
            self.assertFalse(is_prime(i))

class TestClosestPrime(unittest.TestCase):
    def test_returns_self_if_prime_is_itself(self):
        expect = [2, 3, 5, 7, 11, 13]
        for e in expect:
            self.assertEqual(closest_prime(e),  e, "\ninput: " + str(e))

    def test_returns_expected_prime(self):
        inputs = [1, 4, 6, 8, 9, 10, 12]
        expected = [2, 3, 5, 7, 7, 11, 11]

        for input, e in zip(inputs, expected):
           self.assertEqual(closest_prime(input),  e, "\ninput: " + str(input) + "\nexpected: " + str(e))

    def test_expected_prime_for_large_input(self):
        input = 5615156415618423
        expected =5615156415618389
        self.assertEqual(closest_prime(input), expected)


if __name__ == '__main__':
    unittest.main()
