colcon build
. install/setup.zsh
. install/local_setup.zsh
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$PWD/resource/models:$GAZEBO_MODEL_PATH
ros2 launch camille_arbault_rob1 map.launch.py
ros2 launch camille_arbault_rob1 rob1.launch.py