# ROB1 Project

## Pre-requisites
- ROS2 Foxy (preferably on Ubuntu 20.4)
- Rosdep
- Colcon
- vcstools

## Setup steps

download and install the contents of this repository:
```
wget https://raw.githubusercontent.com/Hesperiss/ROB1---camille.arbault-epitech.eu/project.repos
vcs import < project.repos
```

Setup and launch the project:

**Note:** If using zsh shell instead of bash, replace every instance of "bashrc" by "zshrc" on zsh in the above commands.
```
rosdep install -i --from-path camille_arbault_rob1 --rosdistro foxy -y
colcon build --packages-select camille_arbault_rob1
. install/setup.bash
. install/local_setup.bash
source ~/.bashrc
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$PWD/resource/models:$GAZEBO_MODEL_PATH 
ros2 launch camille_arbault_rob1 map.launch.py    
ros2 launch camille_arbault_rob1 rob1.launch.py 
```
