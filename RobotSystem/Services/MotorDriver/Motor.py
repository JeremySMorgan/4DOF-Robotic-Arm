import time
import math

class Motor(object):

	def __init__(self, RobotUtils, pinNumber, minAngle, maxAngle, centerValue, name, pwm):

		if RobotUtils.MOTOR_DEBUG:
			debug_str = "Motor Init. name: ",name,"	| minAngle: ",minAngle,"	| maxAngle: ",maxAngle,"	| baseValue: ",centerValue
			RobotUtils.ColorPrinter(name, debug_str, 'OKBLUE')

		self.RobotUtilities = RobotUtils

		self.pin_number = pinNumber

		self.min_pwm = self.RobotUtilities.SERVO_MIN
		self.max_pwm = self.RobotUtilities.SERVO_MAX

		self.min_angle = minAngle
		self.max_angle = maxAngle

		self.current_angle = centerValue
		self.base_val = centerValue
		self.current_angle = self.base_val
		self.name = name
		self.pwm = pwm

	def move_to_abs_angle(self,d_angle):
		if d_angle >= self.min_angle and d_angle <= self.max_angle:
			self.current_angle = d_angle

		elif d_angle >= self.max_angle:
			self.current_angle = self.max_angle
			debug_str = "Error: Desired angle of " + str(d_angle) + " is greater than max_angle of " + str(self.max_angle)
			self.RobotUtilities.ColorPrinter(self.name, debug_str, 'FAIL')

		elif d_angle <= self.min_angle:
			self.current_angle = self.min_angle
			debug_str = "Error: Desired angle of " + str(d_angle) + " is less than min_angle of " + str(self.min_angle)
			self.RobotUtilities.ColorPrinter(self.name, debug_str, 'FAIL')

		scaled_value = int( self.RobotUtilities.scale( self.current_angle, self.min_angle, self.max_angle,  self.max_pwm, self.min_pwm ))

		if scaled_value < self.min_pwm:
			self.RobotUtilities.ColorPrinter(self.name, "Error: scaled pwm duty value < min allowable pwm", 'FAIL')
			
		elif scaled_value > self.max_pwm:
			self.RobotUtilities.ColorPrinter(self.name, "Error: scaled pwm duty value > max allowable pwm", 'FAIL')
			
		else:
			if self.pwm != None:
				self.pwm.setPWM(self.pin_number, 0, scaled_value)

	def move_to_base_position(self):
		self.move_to_abs_angle(self.base_val)
		
	def set_minimum_angle(self):
		self.move_to_abs_angle(self.min_angle)
		
	def set_maximum_angle(self):
		self.move_to_abs_angle(self.max_angle)
