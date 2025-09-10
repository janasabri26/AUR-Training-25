#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from random import randint

class HumidityNode(Node):
    def __init__(self):
        super().__init__('humidity_node')
        self.publisher_ = self.create_publisher(Int32, 'humidity', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        

    def timer_callback(self):
        msg = Int32()
        msg.data = randint(20,100)
        self.publisher_.publish(msg)
        self.get_logger().info(f'Humidity: {msg.data}%')
        
        
def main():
    rclpy.init()
    node = HumidityNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()