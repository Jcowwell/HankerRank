from runner_up import *
from random import sample
import unittest

class TestRunnerUp(unittest.TestCase):
    def test_runner_up(self):
        
        random_list = sample(range(10,30), 5)
        _max = max(random_list)
        msg = f"{random_list}'s max value should not be returned"

        # DN: Let's just test that it's not the Max
        self.assertIsNot(runner_up(random_list), _max, msg=msg )
        

unittest.main()