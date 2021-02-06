#!/usr/bin/python
# -*- coding: utf-8 -*-

from Services import *
import json

class Hypervisor(object):

    def __init__(self):


        self.pwm = None
        if RobotUtils.PWM_ENABLED:
            if RobotUtils.RUNNING_ON_RPI:
                self.pwm = PWM()
                self.pwm.setPWMFreq(RobotUtils.SERVO_FREQUENCY)
        
        self.current_data = None

        self.data_file_name = RobotUtils.DATA_FILE

        self.j1 = None
        self.j2 = None
        self.j3 = None
        self.j4 = None

        self.create_motor_drivers()

        self.motors = [self.j1, self.j2, self.j3, self.j4]

        self.MotionController = MotionController(self.motors,
                RobotUtils, Kinematics)
        RobotUtils.ColorPrinter(self.__class__.__name__,
                                'Hypervisor initialization finished',
                                'OKBLUE')

    def testSuite(self, operation):
        pass

    def create_motor_drivers(self):
        with open(self.data_file_name) as data_file:
            data = json.load(data_file)
            motors = data['motors']
            for i in range(len(data['motors'])):
                self.add_motor(data['motors'][i])

    def add_motor(self, motor_data):

        name = motor_data['name']
        pin = motor_data['pin']
        base_angle = motor_data['base_val']
        min_angle = motor_data['min_angle']
        max_angle = motor_data['max_angle']
        max_min_swapped = bool(motor_data['min_max_swapped'])

        motor = Motor(
            RobotUtils,
            pin,
            min_angle,
            max_angle,
            base_angle,
            name,
            max_min_swapped,
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

    def shutdown(self):
        self.set_base_position()



            
