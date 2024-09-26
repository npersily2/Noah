# ----------------------------------------------------------------------------- #
#                                                                               #                                    
#    Project:        Split Arcade Control                                       #                             
#    Module:         main.py                                                    #
#    Author:         VEX                                                        #
#    Created:        Fri Aug 05 2022                                            #
#    Description:    This example will use the left Y and right X               #
#                    Controller axis to control the Clawbot.                    #
#                                                                               #                                    
#    Configuration:  V5 Clawbot (Individual Motors)                             #
#                    Controller                                                 #
#                    Claw Motor in Port 3                                       #
#                    Arm Motor in Port 8                                        #
#                    Left Motor in Port 1                                       #
#                    Right Motor in Port 10                                     #
#                                                                               #                                                                          
# ----------------------------------------------------------------------------- #

# Library imports
from vex import *
import math

# Brain should be defined by default
brain=Brain()

# Robot configuration code






controller_1 = Controller(PRIMARY)



top_left_motor = Motor(Ports.PORT10, )
bottom_left_motor = Motor(Ports.PORT14)
top_right_motor = Motor(Ports.PORT3)
bottom_right_motor = Motor(Ports.PORT1)

left = MotorGroup(top_left_motor,bottom_left_motor)
right = MotorGroup(top_right_motor,bottom_right_motor)

#driveTrain = DriveTrain(left,right, (7.5  * math.pi), 7.5, 13, DistanceUnits.IN, (60/84))

# Begin project code
# Main Controller loop to set motors to controller axis postiions
while True:
    left.set_velocity(controller_1.axis3.position, PERCENT)
    right.set_velocity(controller_1.axis2.position, PERCENT)


    left.spin(FORWARD)
    right.spin(FORWARD)
    wait(5, MSEC)
