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

		self.base_val = centerValue
		self.current_angle = self.base_val
		self.name = name
		self.pwm = pwm

	def moveTo(self,d_angle):
		if d_angle > self.min_angle and d_angle < self.max_angle:
			self.value = d_angle

		elif d_angle >= self.max_angle:
			self.value = self.max_angle
			debug_str = "Error: Desired angle of ",str(d_angle)," is greater than max_angle of ",str(self.max_angle)
			self.RobotUtilities.ColorPrinter(self.name, debug_str, 'FAIL')

		elif d_angle <= self.min_angle:
			self.value = self.min_angle
			debug_str = "Error: Desired angle of ",str(d_angle)," is less than min_angle of ",str(self.min_angle)
			self.RobotUtilities.ColorPrinter(self.name, debug_str, 'FAIL')

		#def scale(OldValue, OldMin, OldMax, NewMin, NewMax):
		scaled_value = int( self.RobotUtilities.scale( self.value, self.min_angle, self.max_angle,  self.min_pwm, self.max_pwm ))

		if scaled_value < self.min_pwm:
			self.RobotUtilities.ColorPrinter(self.name, "Error: scaled pwm duty value < min allowable pwm", 'FAIL')
			
		elif scaled_value > self.max_pwm:
			self.RobotUtilities.ColorPrinter(self.name, "Error: scaled pwm duty value > max allowable pwm", 'FAIL')
			
		else:
			if self.pwm != None:
				self.pwm.setPWM(self.pin_number, 0, scaled_value)

	def move_to_base_position(self):
		self.moveTo(self.center_value)
