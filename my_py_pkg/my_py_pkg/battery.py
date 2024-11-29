#!usr/bin/ env python
import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import ChangeLedState

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery")

    
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()