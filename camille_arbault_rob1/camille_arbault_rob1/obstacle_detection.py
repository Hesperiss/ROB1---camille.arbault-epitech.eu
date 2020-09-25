import numpy

from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan


class Turtlebot3ObstacleDetection(Node):

    def __init__(self):
        super().__init__('turtlebot3_obstacle_detection')

        self.linear_velocity = 0.0
        self.angular_velocity = 0.0 
        self.scan_ranges = []
        self.has_scan_started = False

        qos = QoSProfile(depth=10)

        # Init publisher
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', qos)

        # Init subscriber
        self.scan_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            qos_profile=qos_profile_sensor_data)
        self.cmd_vel_raw_sub = self.create_subscription(
            Twist,
            'cmd_vel_raw',
            self.cmd_vel_raw_callback,
            qos)

        self.update_timer = self.create_timer(
            0.010,
            self.update_callback)

        self.get_logger().info("node initialised.")


    def scan_callback(self, msg: LaserScan):
        self.scan_ranges = msg.ranges
        self.has_scan_started = True

    def cmd_vel_raw_callback(self, msg):
        self.linear_velocity = msg.linear.x
        self.angular_velocity = msg.angular.z

    def update_callback(self):
        if self.has_scan_started is True:
            self.check_for_obstacles()

    def check_for_obstacles(self):
        obstacle_distance = min(self.scan_ranges)
        safety_distance = 0.2
        if (obstacle_distance > safety_distance):
            self.go_straight()
        else:
            self.turn()         

    def go_straight(self):
        twist = Twist()
        twist.linear.x = 0.2
        twist.angular.z = self.angular_velocity
        self.cmd_vel_pub.publish(twist)
    
    def turn(self):
        twist = Twist()
        twist.linear.x = 0.1
        twist.angular.z = 0.2
        self.get_logger().info("Obstacle nearby !")
        self.cmd_vel_pub.publish(twist)
