# **Description of Week 1 Lab**

In this lab, we learned the basic structure and workflow of the ROS 2 environment. We created a ROS 2 workspace and built our first package using Python. A simple node was implemented that prints a message to the terminal and runs using ROS 2 commands. The purpose of this lab was to understand how nodes, packages, and workspaces work together in the ROS 2 ecosystem. We also learned how to build packages and run nodes using ROS 2 command-line tools.

## Commands used
- mkdir -p ~/faiq_ros2_ws/src
- cd ~/faiq_ros2_ws
- cd src
- ros2 pkg create my_first_package --build-type ament_python
- chmod +x my_first_node.py
- colcon build
- source install/setup.bash
- ros2 pkg list
- ros2 run my_first_package my_first_node


## Problems Faced and How They Were Solved

One problem faced during the lab was the **“No executable found”** error when trying to run the node. This occurred because the node was not correctly added in the setup.py file under entry_points. The issue was solved by adding the correct mapping for the Python node.

Another issue occurred when ROS 2 could not detect the package. This happened because the workspace environment was not sourced. The problem was fixed by running the command source install/setup.bash before executing ROS 2 commands.

Additionally, indentation errors occurred in the Python file, which i resolved by properly formatting the code in the editor.

## Reflection

This lab helped in understanding the basic structure of ROS 2 and how different components interact with each other. Creating a workspace and package gave practical experience with the ROS 2 development workflow. Running a node through the terminal helped in understanding how ROS executes programs within packages. The lab also highlighted the importance of proper configuration files like setup.py. Troubleshooting errors during the lab improved problem-solving skills. Overall, this lab provided a strong foundation for beginning with ROS 2 .