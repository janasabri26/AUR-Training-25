#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim_msgs.srv import Spawn,Kill
from turtlesim_msgs.msg import Pose     
from std_msgs.msg import Int32
from random import uniform
import math
import time

class TurtleChase(Node):
    def __init__(self):
        super().__init__('turtle_chase')

        self.score=0
        self.score_pub=self.create_publisher(Int32,'score',10)

        self.player_pose=None
        self.enemy1_pose=None
        self.enemy2_pose=None
        self.enemy3_pose=None

        self.create_subscription(Pose,'/turtle1/pose',self.player_callback,10)
        self.create_subscription(Pose, '/enemy1/pose', self.enemy1_callback, 10)
        self.create_subscription(Pose, '/enemy2/pose', self.enemy2_callback, 10)
        self.create_subscription(Pose, '/enemy3/pose', self.enemy3_callback, 10)

        self.spawn_enemy("enemy1")
        self.spawn_enemy("enemy2")
        self.spawn_enemy("enemy3")
        
        self.create_timer(0.1,self.check_collision)
    
    def player_callback(self,msg):
        self.player_pose=msg
    def enemy1_callback(self,msg):
        self.enemy1_pose=msg
    def enemy2_callback(self,msg):
        self.enemy2_pose=msg
    def enemy3_callback(self,msg):
        self.enemy3_pose=msg

    def spawn_enemy(self,name):
        spawn_client=self.create_client(Spawn,'/spawn')
        spawn_client.wait_for_service()
        spawn_request=Spawn.Request()
        spawn_request.x=uniform(1.0,10.0)
        spawn_request.y=uniform(1.0,10.0)
        spawn_request.theta=0.0
        spawn_request.name=name
        future = spawn_client.call_async(spawn_request)
        future.add_done_callback(lambda f: self.get_logger().info(f'spawned {name}'))
        self.get_logger().info(f'spawned {name}')

        
        
    def kill_enemy(self,name):
        kill_client=self.create_client(Kill,'/kill')
        kill_client.wait_for_service()
        kill_request=Kill.Request()
        kill_request.name=name
        future = kill_client.call_async(kill_request)
        future.add_done_callback(lambda f: self.get_logger().info(f'killed {name}'))
        self.get_logger().info(f'killed {name}')

    
    def check_collision(self):
        if self.player_pose is None:
            return None
        
        if self.enemy1_pose and self.distance(self.player_pose,self.enemy1_pose)<1.2:
                self.score+=1
                self.score_pub.publish(Int32(data=self.score))
                self.kill_enemy("enemy1")
                self.enemy1_pose=None
                time.sleep(0.2)
                self.spawn_enemy("enemy1")

        if self.enemy2_pose and self.distance(self.player_pose,self.enemy2_pose)<1.2:
                self.score+=1
                self.score_pub.publish(Int32(data=self.score))
                self.kill_enemy("enemy2")
                self.enemy2_pose=None
                time.sleep(0.2)
                self.spawn_enemy("enemy2")

        if self.enemy3_pose and self.distance(self.player_pose,self.enemy3_pose)<1.2:
                self.score+=1
                self.score_pub.publish(Int32(data=self.score))
                self.kill_enemy("enemy3")
                self.enemy3_pose=None
                time.sleep(0.2)
                self.spawn_enemy("enemy3")
                
    def distance(self,p1,p2):
        return math.sqrt((p1.x-p2.x)**2+(p1.y-p2.y)**2)


def main(args=None):
    rclpy.init(args=args)
    node = TurtleChase()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()