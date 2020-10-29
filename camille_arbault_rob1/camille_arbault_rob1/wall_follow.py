import numpy

from geometry_msgs.msg import Twist
from rclpy.node import Node
from rclpy.qos import QoSProfile
from rclpy.qos import qos_profile_sensor_data
from sensor_msgs.msg import LaserScan

MAX_DISTANCE = 0.8

FRONT = 0
LEFT = 1
RIGHT = 2

BASE_LINEAR_SPEED = 0.3
TURN_LINEAR_SPEED = 0.0
ROTATION_SPEED = 0.5


class TurtlebotWallFollow(Node):

    def __init__(self):
        super().__init__('turtlebot3_obstacle_detection')

        self.angle_increment = 0.0
        self.min_angle = 0.0
        self.walls_dist = []
        self.linear_speed = 0.0
        self.angular_speed = 0.0
                
        self.has_scan_started = False
        self.first_scan = True

        qos = QoSProfile(depth=10)

        # Init publisher
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', qos)

        # Init subscribers
        self.scan_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan,
            qos_profile=qos_profile_sensor_data)
        
        self.vel_raw_sub = self.create_subscription(
            Twist,
            'cmd_vel_raw',
            self.get_speed,
            qos)

        self.update_timer = self.create_timer(
            0.010,
            self.update_callback)

        self.get_logger().info("node initialized.")


    def scan(self, msg: LaserScan):
        self.walls_dist = msg.ranges
        self.angle_increment = msg.angle_increment
        self.min_angle = msg.angle_min
        self.has_scan_started = True


    def get_speed(self, msg):
        self.linear_speed = msg.linear.x
        self.angular_speed = msg.angular.z

    #update linear & angular velocity
    def update_callback(self):
        if (self.has_scan_started is True):
            if (self.first_scan is True):
                self.go_to_nearest_wall()
            else:
                self.follow_walls()
    
    def go_to_nearest_wall(self):    
        nearest_wall_dist = min(self.walls_dist)
        nearest_wall_index = self.walls_dist.index(nearest_wall_dist)
        target_angle = self.min_angle + (nearest_wall_index * self.angle_increment)
     
        # turn to nearest wall
        twist = Twist()
        twist.linear.x = TURN_LINEAR_SPEED
        twist.angular.z = target_angle
        self.get_logger().info("turning to nearest wall")  
        self.first_scan = False
        self.cmd_vel_pub.publish(twist)
           

    def follow_walls(self):        
    
        if (self.walls_dist[FRONT] > MAX_DISTANCE 
            and self.walls_dist[LEFT] > MAX_DISTANCE
            and self.walls_dist[RIGHT] > MAX_DISTANCE):
            self.go_forward()
        elif (self.walls_dist[LEFT] < MAX_DISTANCE):
            self.turn("left")   
        else:
            self.turn("right")     

    def go_forward(self):
        twist = Twist()
        twist.linear.x = BASE_LINEAR_SPEED
        twist.angular.z = self.angular_speed
        self.cmd_vel_pub.publish(twist)


    def turn(self, direction):
        twist = Twist()
        twist.linear.x = TURN_LINEAR_SPEED
        
        if (direction == "left"):
            twist.angular.z = -ROTATION_SPEED
        else:
            twist.angular.z = ROTATION_SPEED
       
        self.get_logger().info("going " + direction)
        self.cmd_vel_pub.publish(twist)

