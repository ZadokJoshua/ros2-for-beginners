#!/usr/bin/env python3
import rclpy
import sys

from rclpy.node import Node
from geometry_msgs.msg import Twist

class DriverNode(Node):
    def __init__(self):
        super().__init__("turtle_driver")
        self.publisher_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.timer_ = self.create_timer(1, self.timer_callback)
        
    def timer_callback(self):
        msg = Twist()
        linear_vel = float(sys.argv[1])
        radius = float(sys.argv[2])
        msg.linear.x = linear_vel
        msg.linear.y = 0.0
        msg.angular.z = linear_vel/radius
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = DriverNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()