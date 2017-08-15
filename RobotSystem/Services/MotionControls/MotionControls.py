#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import time
import math

class MotionController(object):

    def __init__( self, motors, RobotUtils):
        
        self.j1 = motors[0]
        self.j2 = motors[1]
        self.j3 = motors[2]
        self.j4 = motors[3]

        self.RobotUtils = RobotUtils

    def stop(self):
        if not self.stopped:
            self.reset()
            self.stopped = True
            self.RobotUtils.ColorPrinter(self.__class__.__name__, 'Stop', 'OKBLUE')
        

    def autonomous(self):
        if not self.stopped:
            self.reset()
            self.stopped = True
            self.RobotUtils.ColorPrinter(self.__class__.__name__, 'Autonomous', 'OKBLUE')

    def reset(self):
        self.j1.reset()
        self.j2.reset()
        self.j3.reset()
        self.j4.reset()

	# Refer to stand()
	def reset(self):
		self.stand()

	# resets legs to default position
	def stand(self):
		self.front_left.reset()
		self.front_right.reset()
		self.back_left.reset()
		self.back_right.reset()

	def setAllHoriz(self):
		self.front_right.setMidAndLegHoriz()
		self.front_left.setMidAndLegHoriz()
		self.back_right.setMidAndLegHoriz()
		self.back_left.setMidAndLegHoriz()
		time.sleep(5)

	def setMidsToMin(self):
		self.front_right.middle.moveTo(self.front_right.middle.min)
		self.front_left.middle.moveTo(self.front_left.middle.min)
		self.back_left.middle.moveTo(self.back_left.middle.min)
		self.back_right.middle.moveTo(self.back_right.middle.min)
		time.sleep(10)

	def setMidsToMax(self):
		self.front_right.middle.moveTo(self.front_right.middle.max)
		self.front_left.middle.moveTo(self.front_left.middle.max)
		self.back_left.middle.moveTo(self.back_left.middle.max)
		self.back_right.middle.moveTo(self.back_right.middle.max)


# old forward command

'''
if (self.forwardSide==0):

	self.back_left.standardPivotStep(turnDegree, stepHeightMid, stepHeightLeg, motion_increment_delay, mid_step_time_delay)
	time.sleep(step_time_delay)

	self.front_left.standardPivotStep(turnDegree/2.0, stepHeightMid, stepHeightLeg, motion_increment_delay, mid_step_time_delay)
	time.sleep(step_time_delay)

	self.back_right.standardPivotStep(-turnDegree, stepHeightMid, stepHeightLeg, motion_increment_delay, mid_step_time_delay)
	time.sleep(step_time_delay)

	self.forwardSide = 1



else:
	self.back_right.standardPivotStep(-turnDegree, stepHeightMid, stepHeightLeg, motion_increment_delay, mid_step_time_delay)
	time.sleep(step_time_delay)
	
	self.front_right.standardPivotStep(-turnDegree/2.0, stepHeightMid, stepHeightLeg, motion_increment_delay, mid_step_time_delay)
	time.sleep(step_time_delay)
	
	self.back_left.standardPivotStep(turnDegree, stepHeightMid, stepHeightLeg, motion_increment_delay, mid_step_time_delay)
	time.sleep(step_time_delay)

	self.forwardSide = 0
'''

