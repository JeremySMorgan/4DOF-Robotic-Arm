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
        thetas = [180, 90, 270, 180 ]
        print
        print "thetas:", thetas
        print
        robot_arm_hypervisor.MotionController.setMotorAngles(thetas)
        end_coord = robot_arm_hypervisor.MotionController.getXYZfromThetas(thetas)
        print
        print "X:",end_coord[0],"Y:",end_coord[1],"Z:",end_coord[2]

    except KeyboardInterrupt:

        #robot_arm_hypervisor.shutdown()
        RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
