import datetime

class RobotUtils(object):

    R1                 = 11.5                    # length of curved leg portion of bot
    R2                 = 6.5                    # length of junction between middle and leg servos

    DEG_TO_RAD        = 0.0174533                # Constant to convert degrees to radians
    
    L0 = 1.7
    L1 = 2.5
    L2 = 11.45
    L3 = 9.54
    L4 = 7.64

    SERVO_MIN        = 165                    # Minumum tick count for duty cycle
    SERVO_MAX        = 480                     # Maximum tick count for duty cycle
    SERVO_FREQUENCY    = 50                     # 50 Hz creates a 20 ms period, which servos operate with
    DATA_FILE         = "/home/pi/Desktop/4DOF-Robotic-Arm/RobotSystem/Services/MotorCalibration.json"#"RobotSystem/Services/MotorCalibration.json"     # path to data file

    MOTOR_DEBUG     		= False                    # Debug Motors
    PWM_ENABLED     	   	= True                    # Dictates whether to write to pwm
    RUNNING_ON_RPI    		= True

    AGENDA_UPDATE_SPEED = .1                # Time delay between polls of new agenda

    FK_EPSILON = .000001
    MAX_ALLOWABLE_IK_KIN_ERROR = .01

    COLORS = {                                # Unix codes for special priting
        "HEADER"        :     {"value":'\033[95m', "code":0},
        "OKBLUE"         :     {"value":'\033[94m', "code":1},
        "OKGREEN"         :     {"value":'\033[92m', "code":2},
        "WARNING"         :     {"value":'\033[93m', "code":3},
        "FAIL"             :     {"value":'\033[91m', "code":4},
        "ENDC"             :     {"value":'\033[0m', "code":5},
        "BOLD"             :     {"value":'\033[1m', "code":6},
        "UNDERLINE"     :     {"value":'\033[4m', "code":7},
        "STANDARD"        :    {"value":'', "code":8}
    }

    # takes any numer and returns 1 if positive, -1 if negative, and 0 if input is 0
    @staticmethod
    def PositiveOrNegative(n):
        if (n>0):
            return 1
        elif (n<0):
            return -1
        else:
            return 0

    @staticmethod
    def scale(OldValue, OldMin, OldMax, NewMin, NewMax):
        NewValue = (((OldValue - OldMin) * (NewMax - NewMin)) / (OldMax - OldMin)) + NewMin
        return NewValue

    @staticmethod
    def ColorPrinter( caller, message, color):
        # [03/Apr/2017 18:37:10]
        time = datetime.datetime.now()
        prefix = "["+str(time.day)+"/"+str(time.month)+ "/" + str(time.year) + " " + str(time.hour) + ":" + str(time.minute) + ":" + str(time.second) +  " ] "
        prefix = prefix +  RobotUtils.COLORS["BOLD"]["value"]+ RobotUtils.COLORS["UNDERLINE"]["value"]+ caller+ RobotUtils.COLORS["ENDC"]["value"]+ ":"
        print  prefix, RobotUtils.COLORS[color]["value"] ,message , RobotUtils.COLORS["ENDC"]["value"]

