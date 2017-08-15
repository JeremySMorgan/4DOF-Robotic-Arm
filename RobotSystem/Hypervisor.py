#!/usr/bin/python
# -*- coding: utf-8 -*-

from Services import *
import time
import math
import json
import sys
import threading
import os
import datetime


class Hypervisor:

    def __init__(self):

        if RobotUtils.PWM_ENABLED:
            if RobotUtils.RUNNING_ON_RPI:
                self.pwm = PWM()
                self.pwm.setPWMFreq(RobotUtils.SERVO_FREQUENCY)
        self.pwm = None

        self.current_data = None

        if RobotUtils.MULTI_THREADING_ENABLE:
            self.agendaThreadAlive = True
            self.agendaThread = threading.Thread(group=None,
                    target=self.updateAgendaLoop, name='agendaThread')
            self.agendaThread.start()

        self.data_file_name = RobotUtils.DATA_FILE

        self.j1 = None
        self.j2 = None
        self.j3 = None
        self.j4 = None

        self.create_motor_drivers()

        self.motors = [self.j1, self.j2, self.j3, self.j4]

        self.MotionController = MotionController(self.motors,
                RobotUtils)
        RobotUtils.ColorPrinter(self.__class__.__name__,
                                'Hypervisor initialization finished',
                                'OKBLUE')

    def testSuite(self, operation):
        pass

    # loads json data and creates Leg objects with add_leg()

    def create_motor_drivers(self):
        with open(self.data_file_name) as data_file:
            data = json.load(data_file)
            motors = data['motors']
            for i in range(len(data['motors'])):
                self.add_motor(data['motors'][i])

    # reads dictuanary values from input, creates a Leg object, and adds it to leg variables

    def add_motor(self, motor_data):

        name = motor_data['name']
        pin = motor_data['pin']
        base_angle = motor_data['base_val']
        min_angle = motor_data['min_angle']
        max_angle = motor_data['max_angle']

        motor = Motor(
            RobotUtils,
            pin,
            min_angle,
            max_angle,
            base_angle,
            name,
            self.pwm,
            )

        if name == 'j1':
            self.j1 = motor
        elif name == 'j2':

            self.j2 = motor
        elif name == 'j3':

            self.j3 = motor
        elif name == 'j4':

            self.j4 = motor
        else:

            RobotUtils.ColorPrinter(self.__class__.__name__,
                                    'Error in add_motor(): cannot identify motor'
                                    , 'FAIL')

    def set_base_position(self):
        for i in self.motors:
            i.move_to_base_position()

    def set_motor_to_min(self, motor_num):
        self.motors[motor_num - 1].set_minimum_angle()

        status_str = 'Set motor ' + self.motors[motor_num - 1].name \
            + ' to minimum angle of ' + str(self.motors[motor_num
                - 1].min_angle)
        RobotUtils.ColorPrinter(self.__class__.__name__, status_str,
                                'OKGREEN')

    def set_motor_to_max(self, motor_num):
        self.motors[motor_num - 1].set_maximum_angle()

        status_str = 'Set motor ' + self.motors[motor_num - 1].name \
            + ' to maximum angle of ' + str(self.motors[motor_num
                - 1].max_angle)
        RobotUtils.ColorPrinter(self.__class__.__name__, status_str,
                                'OKGREEN')

    def set_motor_to_abs_angle(self, motor_num, angle):

        self.MotionController.set_motor_to_abs_angle(motor_num, angle)

    def shutdown(self):
        self.set_base_position()



            
