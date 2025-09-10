#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class TemperatureNode(Node):
    def __init__(self):
        super().__init__('temperature_node')
        self.publisher_ = self.create_publisher(Int32, 'temperature', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        

    def timer_callback(self):
        msg = Int32()
        msg.data = randint(15,40)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Temperature: {msg.data}°C')
        
        
def main():
    rclpy.init()
    node =TemperatureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()