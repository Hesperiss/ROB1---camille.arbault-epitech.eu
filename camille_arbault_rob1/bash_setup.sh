colcon build
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$PWD/resource/models:$GAZEBO_MODEL_PATH
. install/setup.bash
. install/local_setup.bash
ros2 launch camille_arbault_rob1 map.launch.py
ros2 launch camille_arbault_rob1 rob1.launch.py