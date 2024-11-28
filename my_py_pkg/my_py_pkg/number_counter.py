#!/usr/bin/env python3
from netaddr import valid_eui64
import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounterNode(Node):
    def __init__(self):
        super().__init__("number_counter")
        
        self.total_count = 0
        
        self.subscriber_ = self.create_subscription(Int64, "number", self.callback_number, 10)
        self.publisher_ = self.create_publisher(Int64, "number_count", 10)

        self.server_ = self.create_service(SetBool, "reset_counter", self.callback_reset_number_count)


        self.get_logger().info("Number Counter has started")

    def callback_number(self, num = Int64):
        previous_total = self.total_count
        total_count = Int64()
        
        self.total_count += num.data
        total_count.data = self.total_count

        self.publisher_.publish(total_count)
        self.get_logger().info(f"{previous_total} + {num.data} = {total_count.data}")

    def callback_reset_number_count(self, request, response):
        response.success = True
        self.get_logger().warn("Reset counter operation")
        
        if (request.data):
            self.get_logger().info("Reseting counter...")
            self.total_count = 0
            response.message = "Operation true"

        return response
        

def main(args=None):
    rclpy.init(args=args)
    node = NumberCounterNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()