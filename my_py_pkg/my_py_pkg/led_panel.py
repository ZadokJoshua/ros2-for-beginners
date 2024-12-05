#!usr/bin/env python 
import rclpy

from rclpy.node import Node
from my_robot_interfaces.msg import LedPanelStatus
from my_robot_interfaces.srv import ChangeLedState

class LedPanelNode(Node):
    def __init__(self):
        super().__init__("led_panel")
        
        self.declare_parameter("led_states", [False, False, False])
        self.led_states_ = self.get_parameter("led_states").value
        
        self.led_state_server_ = self.create_service(ChangeLedState, "set_led", self.callback_change_led_state)
        self.led_state_publisher_ = self.create_publisher(LedPanelStatus, "led_panel_state", 10)
        self.timer = self.create_timer(1.0, self.publish_led_states)
        self.get_logger().info("Led panel status publisher has been started.")

    def callback_change_led_state(self, request: ChangeLedState.Request, response: ChangeLedState.Response):
        led_number = request.led_number
        request_action = request.turn_on
        
        match led_number:
            case 1:
                self.process_request(response, led_number, request_action)
            case 2:
                self.process_request(response, led_number, request_action)
            case 3:
                self.process_request(response, led_number, request_action)
            case default:
                response.success = False
                response.message = f"Wrong Led Number {led_number} - Choose between 1 to 3"
                self.get_logger().error(response.message)
                
        return response

    def process_request(self, response, led_number, request_action):
        if (self.led_states_[led_number-1] == request_action):
            response.success = False
            response.message = f"Led {led_number} current state \'{self.get_on_off_str(self.led_states_[led_number-1])}\' can't be equal to command \'{self.get_on_off_str(request_action)}\'"
            self.get_logger().error(response.message)
        else:
            self.led_states_[led_number-1] = request_action
            response.success = True
            response.message = f"Previous state: \'{self.get_on_off_str(not request_action)}\' <--> Current state: \'{self.get_on_off_str(request_action)}\'"
            self.get_logger().info(f"Led {led_number} state changed.")

    def publish_led_states(self):
        msg = LedPanelStatus()
        msg.is_led_on = self.led_states_
        self.led_state_publisher_.publish(msg)
    
    def get_on_off_str(self, is_true: bool):
        return "on" if is_true else "off"

def main(args=None):
    rclpy.init(args=args)
    node = LedPanelNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()
