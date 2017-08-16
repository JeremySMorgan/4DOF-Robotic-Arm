#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import math


class MotionController(object):

    def __init__(self, motors, RobotUtils, Kinematics):

        self.motors = motors
        self.j1 = motors[0]
        self.j2 = motors[1]
        self.j3 = motors[2]
        self.j4 = motors[3]

        self.RobotUtils = RobotUtils

        self.MotionCalculator = Kinematics( RobotUtils, self.get_angle_ranges() )

    def get_angle_ranges(self):
        min_angs = []
        max_angs = []
        for motor in self.motors:
            min_angs.append(motor.min_angle)
            max_angs.append(motor.max_angle)
        return [min_angs,max_angs]

    def reset(self):
        self.j1.move_to_base_position()
        self.j2.move_to_base_position()
        self.j3.move_to_base_position()
        self.j4.move_to_base_position()

    def setEndEffectorToXY(self,x,y):
        pass
    
    def getXYZfromThetas(self,thetas):
        xyz = self.MotionCalculator.forward_kinematics_xy(thetas[0],thetas[1],thetas[2],thetas[3])
        return xyz

    def setMotorAngles(self,thetas):
        for i in range(4):
            self.set_motor_to_abs_angle(i+1,thetas[i])

    def set_motor_to_abs_angle(self, motor_num, angle):
        motor = self.motors[motor_num - 1]
        motor.move_to_abs_angle(angle)
        debug_str = 'Set motor ' + motor.name + ' to angle: '+ str(angle)
        #self.RobotUtils.ColorPrinter(self.__class__.__name__,debug_str, 'OKGREEN')

    def set_motor_to_min(self, motor_num):
        
        motor = self.motors[motor_num - 1]
        motor.set_minimum_pwm()

        status_str = 'Set motor ' + self.motors[motor_num - 1].name + ' to min pwm'
        #self.RobotUtils.ColorPrinter(self.__class__.__name__, status_str, 'OKGREEN')
        
    def set_motor_to_max(self, motor_num):
        motor = self.motors[motor_num - 1]
        motor.set_maximum_pwm()

        status_str = 'Set motor ' + self.motors[motor_num - 1].name + ' to max pwm'
        self.RobotUtils.ColorPrinter(self.__class__.__name__, status_str, 'OKGREEN')
        