import unittest
from sqrt import square_root_function, builtin_sqrt

class SqrtTests(unittest.TestCase):
    """obligatory test
    """
    def test_sqrt9(self):
        self.assertEqual(builtin_sqrt(9), 3)
        self.assertEqual(square_root_function(9), 3)

    def test_sqrt2(self):
        self.assertGreaterEqual(square_root_function(2), 1.414)


class SquaringTests(unittest.TestCase):
    def test_thing(self):
        pass

if __name__ == '__main__':
    unittest.main()
