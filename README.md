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

Setup the project and launch the map in gazebo simulator:

**Note:** If using zsh shell instead of bash, replace every instance of "bashrc" by "zshrc" on zsh in the below commands.
```
rosdep install -i --from-path camille_arbault_rob1 --rosdistro foxy -y
colcon build --packages-select camille_arbault_rob1
. install/setup.bash
source ~/.bashrc
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$PWD/resource/models:$GAZEBO_MODEL_PATH    
ros2 launch camille_arbault_rob1 rob1.launch.py 
```
In another terminal, launch the wall follower node:
```
. install/setup.bash
source ~/.bashrc
export TURTLEBOT3_MODEL=burger
export GAZEBO_MODEL_PATH=$PWD/resource/models:$GAZEBO_MODEL_PATH 
ros2 launch camille_arbault_rob1 rob1.launch.py    
```