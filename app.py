#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
from RobotSystem.Hypervisor import Hypervisor
from RobotSystem.Services.Utilities.RobotUtils import RobotUtils

if __name__ == '__main__':

    robot_arm_hypervisor = Hypervisor()

    try:
        thetas = [180, 45, 270, 225]
        print
        print "thetas:", thetas
        print
        robot_arm_hypervisor.MotionController.setMotorAngles(thetas)
        end_coord = robot_arm_hypervisor.MotionController.getXYZfromThetas(thetas)
        print "End effector position: ",end_coord

    except KeyboardInterrupt:

        #robot_arm_hypervisor.shutdown()
        RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
