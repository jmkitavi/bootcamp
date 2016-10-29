import unittest
import try1

class TestTry(unittest.TestCase):
    def test_small_booleans_type(self):
        self.assertEqual(True, try1.data_type(True))
