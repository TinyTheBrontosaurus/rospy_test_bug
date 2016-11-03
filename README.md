Overview
========
This repository is meant to demonstrate confusion in running unit tests with catkin.

Reproducible test case
======================
To reproduce:

        # Setup the workspace
        mkdir -p test_case/src
        cd test_case/src
        catkin_init_workspace

        # Check out this package into test_case/src
        git clone git@github.com:TinyTheBrontosaurus/rospy_test_bug.git

        # Build it
        cd ..
        catkin_make

        # Try to run the test. It fails.
        catkin_make test

Looking at build/test_results/rospy_test_bug shows that it didn't produce output. and it only has

        cat build/test_results/rospy_test_bug/rostest-tests_unittest_sample.xml

And running catkin_make with more details shows it failed on importing the messages:

        # from rospy_test_bug.msg import * ImportError:
        # No module named rospy_test_bug.msg
        env CTEST_OUTPUT_ON_FAILURE=1 catkin_make test


Note that the test works when running with rostest

        catkin_make
        . devel/setup.bash
        rostest rospy_test_bug unittest_sample.test


A little more digging
=====================
By uncommenting tests/unittest_sample.py's xtest_path, the PYTHON_PATH will be printed to the console via a failed test.
This shows that path does not match between catkin_make test and rostest. The difference is the local workspace's
dist_packages.

So this shows that *the python path is wrong*


and make it work using this one weird trick...
=================================================
By changing the rospy_test_bug/CMakeLists.txt so that it rebuilds the test causes it to work. Specifically uncomment
line 190:

        add_rostest(tests/unittest_path.test DEPENDENCIES ${rospy_test_bug_EXPORTED_TARGETS})

Note that unittest_path will fail, but that's on purpose to print out the path. But after changing it, call again

        catkin_make test

You'll see that the original test passes now. Reproducible every time