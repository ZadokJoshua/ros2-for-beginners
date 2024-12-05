#!usr/bin/ env python
import rclpy
import random

from rclpy.node import Node
from my_robot_interfaces.srv import ChangeLedState

class BatteryNode(Node):
    def __init__(self):
        super().__init__("battery")
        led_number = random.choice((list(range(1,4))))
        turn_on = bool(random.getrandbits(1))
        self.call_change_led_state(led_number, turn_on)
        
    def call_change_led_state(self, led_number: int, turn_on: bool):
        client = self.create_client(ChangeLedState, "set_led")
        
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for server \'Set Led\'...")
        
        self.get_logger().info("Changing led state randomly")
        
        request = ChangeLedState.Request(led_number = led_number, turn_on = turn_on)
        future = client.call_async(request)
        rclpy.spin_until_future_complete(self, future)
        
        self.get_logger().info(future.result().message)

    
def main(args=None):
    rclpy.init(args=args)
    node = BatteryNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()