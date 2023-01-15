import unittest
from generator import password, password_strong, password_strong_simple

class TestGenerator(unittest.TestCase):
    def test_generator(self):
        self.assertEqual(len(password(5, 2, 2)), 9)  # add assertion here

    def test_generator_strong(self):
        self.assertEqual(len(password_strong(5, 2, 2)), 9)


    def test_generator_simple_strong(self):
        self.assertEqual(len(password_strong_simple(5, 2, 2)), 9)


if __name__ == '__main__':
    unittest.main()
