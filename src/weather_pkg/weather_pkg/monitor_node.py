#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class MonitorNode(Node):
    def __init__(self):
        super().__init__('monitor_node')

        self.temperature=0
        self.pressure=0
        self.humidity=0

        self.create_subscription(Int32,'temperature',self.temperature_callback,10)
        self.create_subscription(Int32,'pressure',self.pressure_callback,10)
        self.create_subscription(Int32,'humidity',self.humidity_callback,10)

        self.create_timer(1.0,self.timer_callback)

        self.file=open("weather_readings.txt",'w')


    def temperature_callback(self, msg):
        self.temperature=msg.data
    def pressure_callback(self, msg):
        self.pressure=msg.data
    def humidity_callback(self, msg):
        self.humidity=msg.data
    def timer_callback(self):
        msg = f'Temperature = {self.temperature} °C, Humidity = {self.humidity} %, Pressure = {self.pressure} hPa'
        self.get_logger().info(msg)
        self.file.write(msg+'\n')
    def destroy_node(self):
        self.file.close()
        super().destroy_node()
    

def main():
    rclpy.init()
    node = MonitorNode()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()