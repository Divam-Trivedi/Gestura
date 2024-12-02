#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

class KeyPublisher(Node):
    def __init__(self):
        super().__init__('key_publisher')
        self.robot_publisher = self.create_publisher(Twist, '/model/vehicle/cmd_vel2', 10)
        self.gripper_publisher = self.create_publisher(Twist, '/model/vehicle/cmd_vel', 10)
        self.get_logger().info('KeyPublisher node started. Press "a" to publish.')

    def publish_message_robot(self, params):
        msg = Twist()
        msg.linear.x = params[0]
        msg.linear.y = params[1]
        msg.linear.z = params[2]
        msg.angular.x = params[3]
        msg.angular.y = params[4]
        msg.angular.z = params[5]
        self.robot_publisher.publish(msg)
        self.get_logger().info(f'Message published: {msg}')
    
    def publish_message_gripper(self, params):
        msg = Twist()
        msg.linear.x = params[0]
        msg.linear.y = 0.0
        msg.linear.z = 0.0
        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0
        self.gripper_publisher.publish(msg)
        self.get_logger().info(f'Message published: {msg}')

def on_press(key, node):
        print("hello 1")
    # try:
        if key == 'w':  # Check if the "a" key is pressed
            node.publish_message_robot([0.1, 0.0, 0.0, 0.0, 0.0, 0.0])
        if key == 'a':  # Check if the "a" key is pressed
            node.publish_message_robot([0.1, 0.0, 0.0, 0.0, 0.0, 0.1])
        if key == 's':  # Check if the "a" key is pressed
            node.publish_message_robot([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
        if key == 'd':  # Check if the "a" key is pressed
            node.publish_message_robot([0.1, 0.0, 0.0, 0.0, 0.0, -0.1])
        if key == 'z':  # Check if the "a" key is pressed
            node.publish_message_robot([-0.1, 0.0, 0.0, 0.0, 0.0, 0.0])

        if key == 'o':  # Check if the "a" key is pressed
            node.publish_message_gripper([0.05, 0.0, 0.0, 0.0, 0.0, 0.0])
        if key == 'c':  # Check if the "a" key is pressed
            node.publish_message_gripper([-0.05, 0.0, 0.0, 0.0, 0.0, 0.0])
        if key == 'l':  # Check if the "a" key is pressed
            node.publish_message_gripper([0.0 , 0.0, 0.0, 0.0, 0.0, 0.0])

        # if key == 's':  # Check if the "a" key is pressed
        #     node.publish_message_robot([0.1, 0.0, 0.0, 0.0, 0.0, 0.0])
    # except AttributeError:
    #     pass  # Handle special keys (if needed)

def main(args=None):
    rclpy.init(args=args)
    node = KeyPublisher()

    # # Use pynput to listen for keypress events
    # listener = keyboard.Listener(on_press=lambda key: on_press(key, node))
    # listener.start()

    key = 'a'
    while(True):
        key = input("Enter a character: ")
        if key == 'x':
            exit()
        on_press(key, node)
        

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
