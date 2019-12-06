import unittest
from sqrt import newton_sqrt1, newton_sqrt2, lazy_sqrt, builtin_sqrt

class sqrtTests(unittest.TestCase):
    def test_sqrt9(self):
        self.assertEqual(lazy_sqrt(9), 3)

if __name__ == "__main__":
    unittest.main()