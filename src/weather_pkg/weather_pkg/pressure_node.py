#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class PressureNode(Node):
    def __init__(self):
        super().__init__('pressure_node')
        self.publisher_ = self.create_publisher(Int32, 'pressure', 10)
        self.timer = self.create_timer(3.0, self.timer_callback)
        

    def timer_callback(self):
        msg = Int32()
        msg.data = randint(900,1100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Pressure: {msg.data} hPa')
        
        
def main():
    rclpy.init()
    node = PressureNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()