import rclpy

from camille_arbault_rob1.wall_follow import TurtlebotWallFollow


def main(args=None):
    rclpy.init(args=args)
    turtlebot3_obstacle_detection = TurtlebotWallFollow()
    rclpy.spin(turtlebot3_obstacle_detection)

    turtlebot3_obstacle_detection.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
