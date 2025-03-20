#!/usr/bin/python3

import rclpy
from rclpy.node import Node
import math
from std_msgs.msg import Float64MultiArray
import numpy as np

class Commander(Node):

    def __init__(self):
        super().__init__('commander')
        self.wheel_vel1 = np.array([0,0,0,0], float)
        self.wheel_vel2 = np.array([0,0,0,0], float)
        self.wheel_vel3 = np.array([0,0,0,0], float)
        self.publisher_robot1 = self.create_publisher(Float64MultiArray, '/robot_1/forward_velocity_controller/commands', 10)
        self.publisher_robot2 = self.create_publisher(Float64MultiArray, '/robot_2/forward_velocity_controller/commands', 10)
        self.publisher_robot3 = self.create_publisher(Float64MultiArray, '/robot_3/forward_velocity_controller/commands', 10)

        self.timer_period = 0.005
        self.L = 0.125 # distance from the robot center to the wheel
        self.Rw = 0.03 # Radius ot the wheel

        self.t = 0

        self.timer = self.create_timer(self.timer_period, self.timer_callback)

    def timer_callback(self):

        # robot1
        vel_x1 = 0
        vel_y1 = 0
        vel_w1 = -0.7
        self.wheel_vel1[0] = (vel_x1*math.sin(math.pi/4            ) + vel_y1*math.cos(math.pi/4            ) + self.L*vel_w1)/self.Rw
        self.wheel_vel1[1] = (vel_x1*math.sin(math.pi/4 + math.pi/2) + vel_y1*math.cos(math.pi/4 + math.pi/2) + self.L*vel_w1)/self.Rw
        self.wheel_vel1[2] = (vel_x1*math.sin(math.pi/4 - math.pi)   + vel_y1*math.cos(math.pi/4 - math.pi)   + self.L*vel_w1)/self.Rw
        self.wheel_vel1[3] = (vel_x1*math.sin(math.pi/4 - math.pi/2) + vel_y1*math.cos(math.pi/4 - math.pi/2) + self.L*vel_w1)/self.Rw

        # robot2
        vel_x2 = -math.sin(math.pi*self.t/5)
        vel_y2 = math.cos(math.pi*self.t/5)
        vel_w2 = 0
        self.wheel_vel2[0] = (vel_x2*math.sin(math.pi/4            ) + vel_y2*math.cos(math.pi/4            ) + self.L*vel_w2)/self.Rw
        self.wheel_vel2[1] = (vel_x2*math.sin(math.pi/4 + math.pi/2) + vel_y2*math.cos(math.pi/4 + math.pi/2) + self.L*vel_w2)/self.Rw
        self.wheel_vel2[2] = (vel_x2*math.sin(math.pi/4 - math.pi)   + vel_y2*math.cos(math.pi/4 - math.pi)   + self.L*vel_w2)/self.Rw
        self.wheel_vel2[3] = (vel_x2*math.sin(math.pi/4 - math.pi/2) + vel_y2*math.cos(math.pi/4 - math.pi/2) + self.L*vel_w2)/self.Rw        

        # robot3
        vel_x3 = -math.sin(math.pi*self.t/5)
        vel_y3 = math.cos(math.pi*self.t/5)
        vel_w3 = 0
        self.wheel_vel3[0] = (vel_x3*math.sin(math.pi/4            ) + vel_y3*math.cos(math.pi/4            ) + self.L*vel_w3)/self.Rw
        self.wheel_vel3[1] = (vel_x3*math.sin(math.pi/4 + math.pi/2) + vel_y3*math.cos(math.pi/4 + math.pi/2) + self.L*vel_w3)/self.Rw
        self.wheel_vel3[2] = (vel_x3*math.sin(math.pi/4 - math.pi)   + vel_y3*math.cos(math.pi/4 - math.pi)   + self.L*vel_w3)/self.Rw
        self.wheel_vel3[3] = (vel_x3*math.sin(math.pi/4 - math.pi/2) + vel_y3*math.cos(math.pi/4 - math.pi/2) + self.L*vel_w3)/self.Rw        


        self.t += self.timer_period

        array_forPublish1 = Float64MultiArray(data=self.wheel_vel1)    
        array_forPublish2 = Float64MultiArray(data=self.wheel_vel2) 
        array_forPublish3 = Float64MultiArray(data=self.wheel_vel3) 
        rclpy.logging._root_logger.info(f"wheel vel : {self.wheel_vel1}")
        self.publisher_robot1.publish(array_forPublish1)     
        self.publisher_robot2.publish(array_forPublish2)  
        self.publisher_robot3.publish(array_forPublish3)  

if __name__ == '__main__':
    rclpy.init(args=None)
    commander = Commander()
    rclpy.spin(commander)
    commander.destroy_node()
    rclpy.shutdown()

