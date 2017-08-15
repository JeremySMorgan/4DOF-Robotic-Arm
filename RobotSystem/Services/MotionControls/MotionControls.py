#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import time
import math


class MotionController(object):

    def __init__(self, motors, RobotUtils):

        self.motors = motors
        self.j1 = motors[0]
        self.j2 = motors[1]
        self.j3 = motors[2]
        self.j4 = motors[3]

        self.RobotUtils = RobotUtils

        # self.MotionCalculator = MotionCalculator

    def stop(self):
        if not self.stopped:
            self.move_to_base_position()
            self.stopped = True
            self.RobotUtils.ColorPrinter(self.__class__.__name__, 'Stop'
                    , 'OKBLUE')

    def reset(self):
        self.j1.move_to_base_position()
        self.j2.move_to_base_position()
        self.j3.move_to_base_position()
        self.j4.move_to_base_position()

        def set_motor_to_abs_angle(self, motor_num, angle):
            motor = self.motors[motor_num - 1]
            motor.move_to_abs_angle(angle)

            debug_str = 'Set motor ' + motor.name + ' to angle: ' \
                + str(angle)

        self.RobotUtils.ColorPrinter(self.__class__.__name__,
                debug_str, 'OKBLUE')



			
