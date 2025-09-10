#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TurtleNode(Node):
    def __init__(self):
        super().__init__('turtle_node')
        self.pub = self.create_publisher(Twist,'/turtle2/cmd_vel',10)
        

    def move_turtle(self,key):
        msg=Twist()
        if key.lower()=='w':
            msg.linear.x=1.0
        elif key.lower()=='s':
            msg.linear.x=-1.0
        elif key.lower()=='a':
            msg.angular.z=1.0
        elif key.lower()=='d':
            msg.angular.z=-1.0
        self.pub.publish(msg)

        
def main(args=None):
    rclpy.init(args=args)
    node = TurtleNode()

    print("Use arrow keys for Turtle1, WASD for Turtle2, q to quit")
    try:
        while True:
            key = input("Key: ")
            if key.lower() == 'q':
                break
            node.move_turtle(key)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__=='__main__':
    main()

