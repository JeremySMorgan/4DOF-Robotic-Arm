from RobotSystem.Services.Utilities.RobotUtils import RobotUtils

# MotionPlanner provides target values given a desired end state

# math.cos(X) - return the cosine of x radians
# math.cos(math.radians(X)) - return the cosine of x radians

#                         _ _ _
#                     /        \
#                   /    / ---   \
#     R1 /      /    /        \  \
#                 /    /   theta2  \  \   \ R2
#           /   /               \  \
#        /    /                \  \
#        (   )                    \  \
#    __ |   /  theta1              |__|
#  ____   |
#

# Input desired x, y cooredinates, output mid, leg angle, or -1

class MotionCalc(object):

    def __init__(self):
        pass