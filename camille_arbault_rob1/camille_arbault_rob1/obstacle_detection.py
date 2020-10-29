import numpy

from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

MAX_DISTANCE = 0.6

FRONT = 0
LEFT = 1
RIGHT = 2

BASE_LINEAR_SPEED = 0.2
TURN_LINEAR_SPEED = 0.1
ROTATION_SPEED = 0.4


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
            self.handle_obstacles()

    def handle_obstacles(self):

        walls_dist = self.scan_ranges
        
        # if no wall too close in front, keep going straight
        if (walls_dist[FRONT] > MAX_DISTANCE):
            self.go_straight()

        # else go towards nearest wall to follow it
        elif (walls_dist[LEFT] < walls_dist[RIGHT]):
            self.turn_left()   
        else:
            self.turn_right()     

    def go_straight(self):
        twist = Twist()
        twist.linear.x = BASE_LINEAR_SPEED
        twist.angular.z = self.angular_velocity
        self.cmd_vel_pub.publish(twist)
    
    def turn_left(self):
        twist = Twist()
        twist.linear.x = TURN_LINEAR_SPEED
        twist.angular.z = -ROTATION_SPEED
        self.get_logger().info("going left !")
        self.cmd_vel_pub.publish(twist)
    
    def turn_right(self):
        twist = Twist()
        twist.linear.x = TURN_LINEAR_SPEED
        twist.angular.z = ROTATION_SPEED
        self.get_logger().info("going right !")
        self.cmd_vel_pub.publish(twist)
