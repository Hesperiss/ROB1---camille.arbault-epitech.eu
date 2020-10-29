import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='camille_arbault_rob1',
            executable='rob1',
            output='screen'
        )
    ])