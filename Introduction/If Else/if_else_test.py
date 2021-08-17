from if_else import *
import unittest

class TestIfElse(unittest.TestCase):
    def test_if_else(self):
        weird_msg = "Should be Weird"
        not_weird_msg = "Should be Not Weird"

        weird: str = "Weird"
        not_weird: str = 'Not Weird'

        # DN: If  n is odd, print Weird
        self.assertEqual(is_weird(1), weird, msg = weird_msg)
        self.assertEqual(is_weird(17), weird, msg = weird_msg)
        # DN: If  n is even and in the inclusive range of 2 to 5, print Not Weird
        self.assertEqual(is_weird(2), not_weird, msg = not_weird_msg)
        self.assertEqual(is_weird(4), not_weird, msg = not_weird_msg)
        # DN: If  n is even and in the inclusive range of 6 to 20, print Weird
        self.assertEqual(is_weird(6), weird, msg = weird_msg)
        self.assertEqual(is_weird(18), weird, msg = weird_msg)
        self.assertEqual(is_weird(20), weird, msg = weird_msg)
        # DN: If  n is even and greater than 20, print Not Weird
        self.assertEqual(is_weird(26), not_weird, msg = not_weird_msg)
        self.assertEqual(is_weird(100), not_weird, msg = not_weird_msg)

unittest.main()