#!/usr/bin/env python
PKG = 'rospy_test_bug'
NAME = 'unittest_path'

import unittest
import rospy
import sys, os
import logging


# Unit tests to print out the python path
class TestPath(unittest.TestCase):

    def __init__(self, *args):
        unittest.TestCase.__init__(self, *args)
        rospy.init_node(NAME)

    def test_path(self):
        self.assertEquals(1, 2, msg="Python Path: \n{}".format('\n'.join(sys.path)))


if __name__ == '__main__':
    import rosunit
    rosunit.unitrun(PKG, NAME, TestPath)
