#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# Initialise the PWM device using the default address
pwm = PWM(0x40)
pwm.setPWMFreq(50)

# 50 Hz = 1/50 second = .02 s = 20 milliseconds
# .9 / 20  = min_duty / 4096  -> min_duty = 185
# 2.1 / 20  = max_duty / 4096  -> max_duty = 430 
 
servoMin = 165  # Min pulse length out of 4096
servoMax = 480  # Max pulse length out of 4096

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)


def set_all_to_mid():
	p = (servoMax  + servoMin) / 2
	for i in range(4):
		pwm.setPWM(i, 0, p)

def simple_demo():

	for x in range(3):
		for i in range(servoMin,servoMax):
			pwm.setPWM(0, 0, i)
			pwm.setPWM(1, 0, i)
			pwm.setPWM(2, 0, i)
			pwm.setPWM(3,0, i)
			time.sleep(.01)
		
		for j in range(servoMax,servoMin,-1):
			pwm.setPWM(0, 0, j)
			pwm.setPWM(1, 0, j)
			pwm.setPWM(2, 0, j)
			pwm.setPWM(3, 0, j)
			time.sleep(.01)



def main():
	simple_demo()
	#set_all_to_mid()
	#pwm.setPWM(0, 0, servoMin)
	#pwm.setPWM(0, 0, servoMax)
	

 	
if __name__ == "__main__":
	main()
