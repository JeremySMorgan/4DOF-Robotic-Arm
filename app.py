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
        xyz_d = [0, -2.5, 20]
        print
        print "desired xyz:", xyz_d
        print 

        start_t = time.time()        
        res = robot_arm_hypervisor.MotionController.MotionCalculator.inverse_kinematics( xyz_d )
        elapsed_t = time.time() - start_t

        print "inverse k calculated in:", elapsed_t, "seconds"

        if type(res.x) != type(None):
            thetas_d = list(res.x)
            print "inv kin solution: ", thetas_d

            print "calculated location of solution:",robot_arm_hypervisor.MotionController.MotionCalculator.forward_kinematics_xyz(thetas_d)
        else:
            print "no solution"

        #robot_arm_hypervisor.MotionController.setMotorAngles(thetas)
        #end_coord = robot_arm_hypervisor.MotionController.getXYZfromThetas(thetas)
        #print "End effector position: ",end_coord

    except KeyboardInterrupt:

        #robot_arm_hypervisor.shutdown()
        RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
