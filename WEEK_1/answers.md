ANSWERS FILE BY 2022MC59

Q1 Define: node, topic, package, workspace

ANSWER : 
Node:
A node is a single executable program in ROS 2 that performs a specific task, such as controlling a sensor or publishing data.

Topic:
A topic is a named communication channel used by ROS 2 nodes to send and receive messages asynchronously.

Package:
A package is a collection of ROS 2 files including nodes, libraries, configuration files, and dependencies organized together for a specific application.

Workspace:
A workspace is a directory that contains ROS 2 packages and is used to build and manage ROS projects.

QUESTION 2 Why is sourcing required? What happens if you do not source a workspace?
ANSWER:-
Sourcing a workspace loads the environment variables so the terminal can locate ROS 2 packages, executables, and dependencies.
source install/setup.bash

QUESTION 3 What is the purpose of colcon build? What folders does it generate?
ANSWER:-
colcon build is used to compile and build ROS 2 packages inside a workspace.
It generates following folders
build/ → Contains temporary build files used during compilation.

install/ → Contains the installed executables and setup files used to run nodes.

log/ → Contains logs of the build process.

QUESTION 4 Explain what the entry_points console scripts do in setup.py.
ANSWER:-
The entry_points console_scripts section in setup.py tells ROS 2 which Python file should be executed as a node when using the ros2 run command.

QUESTION 5 Diagram showing one publisher and one subscriber connected by a topic
      +----------------+
      |  Publisher Node |
      |  (talker)       |
      +--------+--------+
               |
               |  Topic: /chatter
               |  (String messages)
               v
      +--------+--------+
      | Subscriber Node |
      |   (listener)    |
      +-----------------+