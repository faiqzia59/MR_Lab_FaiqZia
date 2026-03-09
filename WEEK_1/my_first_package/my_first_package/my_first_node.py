#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class HelloWorldNode(Node):
    def __init__(self):
        super().__init__('hello_world_node')
        # this line will emit to the ROS‑2 logger
        self.get_logger().info('WELCOME TO MOBILE ROBOTICS LAB')

def main(args=None):
    rclpy.init(args=args)
    node = HelloWorldNode()
    rclpy.spin(node)          # keep the node alive
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()