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
        #robot_arm_hypervisor.set_base_position()
        
        #robot_arm_hypervisor.set_motor_to_angle(1, 270)
        #robot_arm_hypervisor.set_motor_to_angle(2, 45)
        #robot_arm_hypervisor.set_motor_to_angle(3, 225)
        
        delay = 2
        motor_num = 4
        d_angle = 180
        
        robot_arm_hypervisor.set_motor_to_min_angle(motor_num)
        time.sleep(delay)
        robot_arm_hypervisor.set_motor_to_max_angle(motor_num)
        time.sleep(delay)
        robot_arm_hypervisor.set_motor_to_angle(motor_num, d_angle)
        time.sleep(delay)
    
    except KeyboardInterrupt:

        #robot_arm_hypervisor.shutdown()
        RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
