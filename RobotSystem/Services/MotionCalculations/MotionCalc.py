import numpy as np

class Kinematics(object):

    def __init__(self,RobotUtils):
        self.RobotUtils = RobotUtils
    
    def forward_kinematics_xy(self, theta1, theta2, theta3, theta4 ):
        
        L0 = 1.7
        L1 = 2.5
        L2 = 11.45
        L3 = 9.54
        L4 = 7.64

        j1_x = 0
        j1_y = 0
        j1_z = L0

        theta_1_adjusted = theta1 + 90
        j2_x = self.RobotUtils.L1 * np.cos( np.deg2rad( theta_1_adjusted ))
        j2_y = self.RobotUtils.L1 * np.sin( np.deg2rad( theta_1_adjusted ))
        j2_z = 0

        j3_x = self.RobotUtils.L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.cos( np.deg2rad( 90 + theta_1_adjusted ))
        j3_y = self.RobotUtils.L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.sin( np.deg2rad( 90 + theta_1_adjusted  ))
        j3_z = self.RobotUtils.L2 * np.sin( np.deg2rad( theta2 ))

        j4_x = self.RobotUtils.L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
        j4_y = self.RobotUtils.L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
        j4_z = self.RobotUtils.L3 * np.sin( np.deg2rad( theta2 + theta3 - 180 ))

        j5_x = self.RobotUtils.L4 * np.cos( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
        j5_y = self.RobotUtils.L4 * np.cos( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
        j5_z = self.RobotUtils.L4 * np.sin( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 ))

        x, y,z = 0, 0, 0
        x += j1_x; y += j1_y; z+=j1_z
        x += j2_x; y += j2_y; z+=j2_z
        x += j3_x; y += j3_y; z+=j3_z
        x += j4_x; y += j4_y; z+=j4_z
        x += j5_x; y += j5_y; z+=j5_z

        return [x,y,z]
        
    

    def inverse_kinematics(self,x,y):
        return [0,0,0,0]


        