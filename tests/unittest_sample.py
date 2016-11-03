#!/usr/bin/env python
PKG = 'rospy_test_bug'
NAME = 'unittest_sample'

import unittest
import rospy
import sys, os
# Pull in src directory for imports
sys.path.insert(0, os.path.dirname(__file__) + '/../src')
from sample import SampleParser


# Unit tests for Sample
class TestSample(unittest.TestCase):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        rospy.init_node(NAME)

    def test_nominal_sample(self):
        input_string = "\x00\x01\x02\x03"

        parser = SampleParser()
        values = parser.parse_sample(input_string)

        self.assertEqual(values.zero, 0, msg="zero")
        self.assertEqual(values.one, 1, msg="one")
        self.assertEqual(values.two, 2, msg="two")
        self.assertEqual(values.three, 3, msg="three")

    # Uncomment (i.e., remove the leading x) to turn on path printing. Note this will cause the test to fail
    def xtest_path(self):
        self.assertEquals(1, 2, msg="Python Path: \n{}".format('\n'.join(sys.path)))

if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, NAME, TestSample)
