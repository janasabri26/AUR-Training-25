#!/usr/bin/env python3

import rclpy
from rclpy.node import Node


class TimerNode(Node):
    def __init__(self):
        super().__init__('timer_node')
        self.count = 10
        self.timer = self.create_timer(1.0, self.timer_callback)
        

    def timer_callback(self):
        if self.count >=0:
            self.get_logger().info(f'{self.count}')
            self.count-=1
        else:
            self.get_logger().info('Time is up!')
            self.timer.cancel()
        
        
        
        
def main():
    rclpy.init()
    node =TimerNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()