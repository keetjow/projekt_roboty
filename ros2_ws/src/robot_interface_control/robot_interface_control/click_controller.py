#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np


class ClickController(Node):
    def __init__(self):
        super().__init__('click_controller')
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.image_sub = self.create_subscription(Image, '/camera/image_raw', self.image_callback, 10)
        self.bridge = CvBridge()
        self.current_image = None
        cv2.namedWindow('Camera')
        cv2.setMouseCallback('Camera', self.mouse_callback)

    def image_callback(self, msg):
        self.current_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        cv2.imshow('Camera', self.current_image)
        cv2.waitKey(1)

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and self.current_image is not None:
            height = self.current_image.shape[0]
            center_y = height // 2
            
            twist_msg = Twist()
            if y < center_y:
                twist_msg.linear.x = 0.2  # Do przodu
            else:
                twist_msg.linear.x = -0.2  # Do tyłu
            
            self.cmd_vel_pub.publish(twist_msg)


def main(args=None):
    rclpy.init(args=args)
    node = ClickController()
    rclpy.spin(node)
    cv2.destroyAllWindows()
    rclpy.shutdown()


if __name__ == '__main__':
    main()