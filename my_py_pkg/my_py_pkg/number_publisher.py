#!/usr/bin/env python3
import rclpy 
import random
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberPublisherNode(Node):
    
    def __init__(self):
        super().__init__("number_publisher")
        
        self.declare_parameter("max_rand_number_to_publish", 2)
        self.declare_parameter("publish_frequency", 1.0)
        
        self.max_number_ = self.get_parameter("max_rand_number_to_publish").value
        self.publish_frequency_  = self.get_parameter("publish_frequency").value

        self.publisher_ = self.create_publisher(Int64, "number", 10)
        self.timer_ = self.create_timer(1.0 / self.publish_frequency_, self.publish_number)
        self.get_logger().info("Random Generator has started.")

    def publish_number(self):
        num_data = random.choice(list(range(1,self.max_number_)))
        num = Int64()
        num.data = num_data
        self.publisher_.publish(num)
        

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisherNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()