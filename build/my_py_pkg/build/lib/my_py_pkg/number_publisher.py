#!/usr/bin/env python3
import rclpy 
import random
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    
    def __init__(self):
        super().__init__("number_publisher")

        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(1, self.publish_number)
        self.get_logger().info("Random Generator has started.")

    def publish_number(self):
        num_list = [1, 2, 3, 4, 5, 6]

        num = Int64()
        num_data = random.choice(num_list)

        num.data = num_data
        self.publisher_.publish(num)
        

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()