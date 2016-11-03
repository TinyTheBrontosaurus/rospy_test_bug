#! /usr/bin/env python

import rospy
from rospy_test_bug.msg import *
import struct

class SampleParser:

    def __init__(self):
        pass

    def parse_sample(self, payload, utc=None):
        if utc is None:
            utc = rospy.Time.now()

        # Page 58 of ICD
        parsed = struct.unpack("<BBBB", payload)
        sample_msg = Sample()
        sample_msg.utc_time = utc
        sample_msg.zero = parsed[0]
        sample_msg.one = parsed[1]
        sample_msg.two = parsed[2]
        sample_msg.three = parsed[3]
        return sample_msg
