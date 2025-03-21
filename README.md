# Installing and Running the Project
## Installing Required packages. 
```
sudo apt update

sudo apt install ros-humble-nav2-bringup

sudo apt install ros-humble-navigation2

sudo apt install ros-humble-ros2-controllers

sudo apt install ros-humble-ros2-control

sudo apt install gazebo

sudo apt install ros-humble-gazebo-ros-pkgs

sudo apt install ros-humble-gazebo-ros2-control

sudo apt install ros-humble-xacro
```

## After Installing 
You can either move the items in the src/ directory into the src directory of a pre-existing ros2 workspace, via 
```
mv /path/to/git/directory/src/* /path/to/ros2_ws/src/
```
Or, treat the git repository as its own ros2 workspace. 
For more information on ros2 workspaces read https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html.

Or https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-Your-First-ROS2-Package.html for ros2 packages.

Next, build the project via colcon build. see this link for more information. 
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Colcon-Tutorial.html

If you are treating the repository as its own ros2 workspace, you can, in the base repository directory, run:
```
colcon build
```
After running, the directory should include, 
```
build install log src
```

Next, open two seperate terminals and navigate to the base ros2 workspace, or base repository directory. run the following code to launch the robots and control nodes. Launch the robots(the first script) before the control nodes.
### First terminal
```
source install/setup.bash

ros2 launch robot_gazebo many_spawn_main.launch.py 
```

### Second terminal
```
source install/setup.bash

ros2 run robot_control robot_control.py
```
