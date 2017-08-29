import time
import sys
import os
import random
import numpy as np
import pickle
from RobotSystem.Hypervisor import Hypervisor
from RobotSystem.Services.Utilities.RobotUtils import RobotUtils

def main():

    robot_arm_hypervisor = Hypervisor()
    print

    try:
        x_des = 5
        y_des = 5
        z_des = 5


        trials = 250 

        start_t = time.time()
        last_t = start_t
        sum_t = 0
        
        sum_err = 0

        for i in range(1,trials):

            rand_x = random.randint(5,15)
            rand_y = random.randint(-5,5)
            rand_z = random.randint(-5,5)
            xyz_d = [ rand_x, rand_y, rand_z ]
                   
            res = robot_arm_hypervisor.MotionController.MotionCalculator.inverse_kinematics( xyz_d )
            error = robot_arm_hypervisor.MotionController.MotionCalculator.ik_kin_solution_error(xyz_d,res)

            sum_err += error
            t_elapsed = time.time() - last_t
            sum_t += t_elapsed
            ave_t = sum_t/i

            print "Trial:",i,"\tof",trials,"\t xyz_d:",xyz_d,"\t Error:",error," operation time:",t_elapsed,"\tave time:",ave_t

            last_t = time.time()

        ave_t = ( time.time() - start_t ) / trials
        print "Average operation time: ",ave_t, "s"

    except KeyboardInterrupt:
        print "\nexiting"
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)



if __name__ == '__main__':
    main()





'''
    robot_arm_hypervisor = Hypervisor()

    file_name = "calc_ik_values.pckl"
    ik_values = {}

    try:
        x_min = -280
        x_max = 280
        x_step = 1

        y_min = -280
        y_max = 280
        y_step = 1

        z_min = -280
        z_max = 280
        z_step = 1
        
        sum_points = (x_max - x_min) * (y_max - y_min) * (z_max - z_min)
        iterator = 1

        for x in range(x_min,x_max,x_step):
            for y in range(y_min, y_max, y_step):
                for z in range(z_min, z_max, z_step):

                    print "Calculating Point",iterator,"\tof",sum_points
                    iterator += 1 

                    xyz_d = [int(x/10), int(y/10), int(z/10)]
                   
                    res = robot_arm_hypervisor.MotionController.MotionCalculator.inverse_kinematics( xyz_d )
                    
                    if not res is None:
                        thetas_calc = res
                        solution_error = robot_arm_hypervisor.MotionController.MotionCalculator.ik_kin_solution_error( xyz_d, thetas_calc)
                        if robot_arm_hypervisor.MotionController.MotionCalculator.ik_kin_solution_valid(solution_error):
                            xyz = tuple(xyz_d)
                            thetas_calc = tuple(thetas_calc)
                            ik_values[xyz] = thetas_calc    
                    else:
                        print "no solution: result is None"
                        
        f = open(file_name, 'wb')
        pickle.dump(ik_values, f)
        f.close()
                   
    except KeyboardInterrupt:
        print "\nexiting"
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
'''