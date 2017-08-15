#!/usr/bin/env python
import os
import sys
from RobotSystem.Hypervisor import Hypervisor
from RobotSystem.Services.Utilities.RobotUtils import RobotUtils

if __name__ == '__main__':
    
    robot_arm_hypervisor = Hypervisor()

    try:
        robot_arm_hypervisor.set_base_position()

    except KeyboardInterrupt:
        RobotUtils.ColorPrinter("app.py", "Server shutting down", 'FAIL')
        robot_arm_hypervisor.shutdown()
        
        try: 
            sys.exit(0)
        except SystemExit:
            os._exit(0)
    