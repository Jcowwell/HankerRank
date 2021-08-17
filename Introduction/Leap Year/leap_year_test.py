from leap_year import *
import unittest

class TestLeapYear(unittest.TestCase):
    def test_leap_year(self):
        true_msg = "Should be True"
        false_msg = "Should be False"
        # DN: Leap Years are any year that can be exactly divided by 4
        self.assertAlmostEqual(is_leap(2016), True, msg= true_msg)
        self.assertAlmostEqual(is_leap(2020), True, msg= true_msg)
        self.assertAlmostEqual(is_leap(2024), True, msg= true_msg)
        # DN: except if it can be exactly divided by 100, then it isn't (such as 2100, 2200, etc)
        self.assertAlmostEqual(is_leap(2100), False, msg= false_msg)
        self.assertAlmostEqual(is_leap(2200), False, msg= false_msg)
        # DN: except if it can be exactly divided by 400, then it is (such as 2000, 2400)
        self.assertAlmostEqual(is_leap(2000), True, msg= true_msg)
        self.assertAlmostEqual(is_leap(2400), True, msg= true_msg)

unittest.main()