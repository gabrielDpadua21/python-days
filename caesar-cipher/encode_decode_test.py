import unittest
from encoder import encode
from decoder import decode

class MyTestCase(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode("message", 13), "zrffntr")

    def test_decode(self):
        self.assertEqual(decode("zrffntr", 13), "message")


if __name__ == '__main__':
    unittest.main()
