import numpy as np

class Kinematics(object):

    def __init__(self,RobotUtils):
        self.RobotUtils = RobotUtils
    
    def forward_kinematics_xy(self, theta1, theta2, theta3, theta4 ):
        
        
        theta_1_adjusted = theta1 + 90
        j2_x = L1 * np.cos( np.deg2rad( theta_1_adjusted ))
        j2_y = L1 * np.sin( np.deg2rad( theta_1_adjusted ))
        j2_z = 0

        j3_x = L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.cos( np.deg2rad( 90 + theta_1_adjusted ))
        j3_y = L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.sin( np.deg2rad( 90 + theta_1_adjusted  ))
        j3_z = L2 * np.sin( np.deg2rad( theta2 ))

        j4_x = L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
        j4_y = L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
        j4_z = L3 * np.sin( np.deg2rad( theta2 + theta3 - 180 ))

        j5_x = L4 * np.cos( np.deg2rad( theta4 + theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
        j5_y = L4 * np.cos( np.deg2rad( theta4 + theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
        j5_z = L4 * np.sin( np.deg2rad( theta4 + theta3 + theta2 - 180 ))
        
        x = j1_x + j2_x + j3_x + j4_x + j5_x
        y = j1_y + j2_y + j3_y + j4_y + j5_y
        z = j1_z + j2_z + j3_z + j4_z + j5_z

        if ( np.abs(x) < self.RobotUtils.FK_EPSILON ):
            x = 0
        if ( np.abs(y) < self.RobotUtils.FK_EPSILON ):
            y = 0
        if ( np.abs(x) < self.RobotUtils.FK_EPSILON ):
            y = 0

        return [x,y,z]
        
    

    def inverse_kinematics(self,x,y):
        return [0,0,0,0]


        