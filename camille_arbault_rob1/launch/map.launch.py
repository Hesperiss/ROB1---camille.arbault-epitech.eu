import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch.actions import ExecuteProcess
from launch.substitutions import LaunchConfiguration

TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']

model = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'models/turtlebot3_burger/model.sdf')

def generate_launch_description():

    launch_file_dir = os.path.join(get_package_share_directory('turtlebot3_gazebo'), 'launch')
    world = os.path.join(get_package_share_directory('camille_arbault_rob1'), 'challenge_maze.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world, '-s', 'libgazebo_ros_init.so'],
            output='screen'),

        ExecuteProcess(
            cmd=['gz', 'model', '-m', model, '-f', model],
            prefix="bash -c 'sleep 5s; $0 $@'",
            output='screen'
        ),    

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([launch_file_dir, '/robot_state_publisher.launch.py']),
            launch_arguments={'use_sim_time': 'true'}.items(),
        ),
    ])
