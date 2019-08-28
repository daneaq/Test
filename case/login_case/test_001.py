#Author : Danea

import unittest
import time

class Test(unittest.TestCase):

    def setUp(self):
        print("start....")

    def tearDown(self):
        time.sleep(1)
        print("end....")

    def test_001(self):
        print("test001")

    def test_002(self):
        print("test002")

if __name__ == '__main__':
    unittest.main()