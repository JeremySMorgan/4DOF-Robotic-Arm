import numpy as np
from scipy import optimize
import scipy

class Kinematics(object):

    def __init__(self,RobotUtils,angle_ranges):
        
        self.RobotUtils = RobotUtils
        
        self.joint_lengths = [RobotUtils.L0, RobotUtils.L1, RobotUtils.L2, RobotUtils.L3, RobotUtils.L4]
        self.min_angles = angle_ranges[0]
        self.max_angles = angle_ranges[1]
        self.bounds = self.get_bounds(self.min_angles,self.max_angles)        

    
    def get_bounds(self,min_angs,max_angs):
        bounds = []
        for i in range(len(min_angs)):
            bound = (min_angs[i], max_angs[i])
            bounds.append(bound)
        return bounds

    def forward_kinematics_xyz(self, thetas ):
        
        x = self.forward_kinematics_x(thetas)
        y = self.forward_kinematics_y(thetas)
        z = self.forward_kinematics_z(thetas)

        if np.abs(x) <  self.RobotUtils.FK_EPSILON:
            x = 0

        if np.abs(y) <  self.RobotUtils.FK_EPSILON:
            y = 0

        if np.abs(z) <  self.RobotUtils.FK_EPSILON:
            z = 0

        return [x,y,z]
        

    def set_num_to_zero_if_vsmall(self,num):
        if np.abs(num) < self.RobotUtils.FK_EPSILON:
            num = 0
        return num


    def forward_kinematics_x(self,thetas):

        theta1, theta2, theta3, theta4 = thetas[0],thetas[1],thetas[2],thetas[3]

        theta_1_adjusted = theta1 + 90

        j2_x = self.RobotUtils.L1 * np.cos( np.deg2rad( theta_1_adjusted ))
        j3_x = self.RobotUtils.L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.cos( np.deg2rad( 90 + theta_1_adjusted ))
        j4_x = self.RobotUtils.L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
        j5_x = self.RobotUtils.L4 * np.cos( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 )) * np.cos( np.deg2rad( 270 + theta_1_adjusted ))
        
        x = j2_x + j3_x + j4_x + j5_x;

        return x

    def forward_kinematics_y(self,thetas):
        
        theta1, theta2, theta3, theta4 = thetas[0],thetas[1],thetas[2],thetas[3]

        theta_1_adjusted = theta1 + 90
        j2_y = self.RobotUtils.L1 * np.sin( np.deg2rad( theta_1_adjusted ))
        j3_y = self.RobotUtils.L2 * np.cos( np.deg2rad( 180 - theta2 )) * np.sin( np.deg2rad( 90 + theta_1_adjusted  ))
        j4_y = self.RobotUtils.L3 * np.cos( np.deg2rad( theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
        j5_y = self.RobotUtils.L4 * np.cos( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 )) * np.sin( np.deg2rad( 270 + theta_1_adjusted ))
       
        y = j2_y + j3_y + j4_y + j5_y

        return y

    def forward_kinematics_z(self,thetas):
        
        theta1, theta2, theta3, theta4 = thetas[0],thetas[1],thetas[2],thetas[3]

        j1_z = self.RobotUtils.L0
        theta_1_adjusted = theta1 + 90
        j2_z = 0
        j3_z = self.RobotUtils.L2 * np.sin( np.deg2rad( theta2 ))
        j4_z = self.RobotUtils.L3 * np.sin( np.deg2rad( theta2 + theta3 - 180 ))
        j5_z = self.RobotUtils.L4 * np.sin( np.deg2rad( (180 - theta4) + theta3 + theta2 - 180 ))

        z = j1_z + j2_z + j3_z + j4_z + j5_z 

        return z


    def ik_kin_solution_valid(self,error):
        if np.abs(error) > self.RobotUtils.MAX_ALLOWABLE_IK_KIN_ERROR:
            return False    
        return True

    def ik_kin_solution_error(self,xyz_d,thetas_calculated):
        
        xyz_act = self.forward_kinematics_xyz(thetas_calculated)

        if len(xyz_d) != len(xyz_act):
            raise ValueError("array lengths are not equal")
            
        else:
            cumulative_error = 0
            for i in range(len(xyz_d)):
                cumulative_error += np.abs(xyz_d[i] - xyz_act[i])
            if cumulative_error < self.RobotUtils.MAX_ALLOWABLE_IK_KIN_ERROR:
                return 0
            else:
                return cumulative_error

    def inverse_kinematics(self,xyz_d):
        
        xyz_d = tuple(xyz_d)

        def inv_kin_cost_function(thetas):
            
            x_dif = self.forward_kinematics_x( thetas ) - xyz_d[0]   
            y_dif = self.forward_kinematics_y( thetas ) - xyz_d[1] 
            z_dif = self.forward_kinematics_z( thetas ) - xyz_d[2] 
            
            cost = np.sqrt(( x_dif**2 + y_dif**2 + z_dif**2 ))
            return cost

        ret_val = scipy.optimize.minimize ( inv_kin_cost_function, [180,90,180,180], bounds=self.bounds )   

        if not ret_val.x is None:            
            thetas_calc = list(ret_val.x)
            for i in range(len(thetas_calc)):
                thetas_calc[i] % 360
            return thetas_calc

        else:
            return None
