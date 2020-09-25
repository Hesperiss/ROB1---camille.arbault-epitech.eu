# ROB1 Project

## Pre-requisites
- ROS2 Foxy (preferably on Ubuntu 20.4)
- Rosdep
- Colcon
- Turtlebot3
- vcstools

## Setup steps

download and install the contents of this repository:
```
wget https://raw.githubusercontent.com/Hesperiss/ROB1---camille.arbault-epitech.eu/project.repos
vcs import < project.repos
```

Install the package of the project:

**Note:** If using zsh shell instead of bash, replace every instance of "bashrc" by "zshrc" on zsh in the above commands.
```
rosdep install -i --from-path camille_arbault_rob1 --rosdistro foxy -y
colcon build --packages-select camille_arbault_rob1
. install/setup.bash
. install/local_setup.bash
source ~/.bashrc    
```

Export the turtlebot3 model and launch turtlebot 3:
```
export TURTLEBOT3_MODEL=burger && ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

Launch the project node in another terminal:
```
ros 2 run camille_arbault_rob1 start
```