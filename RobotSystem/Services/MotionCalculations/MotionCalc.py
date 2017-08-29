import numpy as np
from scipy import optimize
import scipy

class Kinematics(object):

    def __init__(self,RobotUtils,angle_ranges):
        
        self.RobotUtils = RobotUtils
        
        self.joint_lengths = [RobotUtils.L0, RobotUtils.L1, RobotUtils.L2, RobotUtils.L3, RobotUtils.L4]
        self.min_angles = angle_ranges[0]
        self.max_angles = angle_ranges[0]
        

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

            #print "In inv_kin_cost_function, thetas:",thetas," x:",self.forward_kinematics_x( thetas )," y:",self.forward_kinematics_y( thetas )," z:",self.forward_kinematics_z( thetas ), "cost:",cost
            return cost

        #ret_val = scipy.optimize.basinhopping ( inv_kin_cost_function, [180,90,180,180] )   
        ret_val = scipy.optimize.minimize ( inv_kin_cost_function, [180,90,180,180] )   


        if not ret_val.x is None:            
            thetas_calc = list(ret_val.x)
            for i in range(len(thetas_calc)):
                thetas_calc[i] % 360
            return thetas_calc

        else:
            return None





'''




#ret_val = scipy.optimize.fmin_slsqp( func=inv_kin_cost_function, x0=self.current_thetas, eqcons=[x_constraint, y_constraint, z_constraint], args=(xyz,), iprint=0)

        def x_constraint(thetas,xyz):
            return self.forward_kinematics_x(thetas) - xyz[0]
            
        def y_constraint(thetas,xyz):
            return self.forward_kinematics_y(thetas) - xyz[1]
            
        def z_constraint(thetas,xyz):
            return self.forward_kinematics_z(thetas) - xyz[2]

    def inv_kin(self, xy):
     
        def distance_to_default(q, *args): 
            # weights found with trial and error, get some wrist bend, but not much
            weight = [1, 1, 1.3] 
            return np.sqrt(np.sum([(qi - q0i)**2 * wi 
                for qi,q0i,wi in zip(q, self.q0, weight)]))
 
        def x_constraint(q, xy):
            x = ( self.L[0]*np.cos(q[0]) + self.L[1]*np.cos(q[0]+q[1]) +
                self.L[2]*np.cos(np.sum(q)) ) - xy[0]
            return x
 
        def y_constraint(q, xy): 
            y = ( self.L[0]*np.sin(q[0]) + self.L[1]*np.sin(q[0]+q[1]) +
                self.L[2]*np.sin(np.sum(q)) ) - xy[1]
            return y
         
        return scipy.optimize.fmin_slsqp( func=distance_to_default, x0=self.q, eqcons=[x_constraint, y_constraint], 
            args=[xy], iprint=0) # iprint=0 suppresses output

'''








''' 
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
'''