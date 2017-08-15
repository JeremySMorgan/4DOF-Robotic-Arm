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
        robot_arm_hypervisor.set_base_position()

        # accepts motor# 1-4
        # robot_arm_hypervisor.set_motor_to_min(1)
        # time.sleep(4)
        # robot_arm_hypervisor.set_motor_to_max(1)
        # time.sleep(4)

        robot_arm_hypervisor.set_motor_to_abs_angle(1, 180)
        time.sleep(4)
    except KeyboardInterrupt:

        robot_arm_hypervisor.shutdown()
        RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)


			
