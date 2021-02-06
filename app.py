#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import math
from RobotSystem.Hypervisor import Hypervisor
from RobotSystem.Services.Utilities.RobotUtils import RobotUtils

def circle_demo(hypv):

	sleep_t = .0001
	x_b = 5
	y_b = -8
	z_b = 8
	
	c_radius = 3
	
	try:
		for theta in range(0,360):
			
			x = x_b
			y = y_b + c_radius*math.sin(math.radians(theta))
			z = z_b + c_radius*math.cos(math.radians(theta))
			
			xyz_d = [x,y,z]
			
			print "Moving EndAffector to:",xyz_d," theta:",theta
			res = hypv.MotionController.MotionCalculator.inverse_kinematics( xyz_d )
			hypv.MotionController.set_motor_angles(res)
			time.sleep(.05)

	except KeyboardInterrupt:
		RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)


def line_demo(hypv):

	sleep_t = .01
	
	i3 = 114
	i4 = 125
	i2 = 160
	
	try:
	
		for i1 in range(165,300):
			thetas = [i1,i2,i3,i4]
			hypv.MotionController.set_motor_angles(thetas)
			time.sleep(sleep_t)
			print i1
			
		for i1 in xrange(300,165,-1):
			thetas = [i1,i2,i3,i4]
			hypv.MotionController.set_motor_angles(thetas)
			time.sleep(sleep_t)
			print i1

		
	except KeyboardInterrupt:
		RobotUtils.ColorPrinter('app.py', 'Hypervisor shutdown', 'FAIL')
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)

if __name__ == '__main__':

	robot_arm_hypervisor = Hypervisor()
	line_demo(robot_arm_hypervisor)
