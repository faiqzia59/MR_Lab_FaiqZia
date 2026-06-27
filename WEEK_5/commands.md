source /opt/ros/humble/setup.bash
source /usr/share/gazebo/setup.sh
export TURTLEBOT3_MODEL=burger
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
ros2 launch turtlebot3_cartographer cartographer.launch.py
use_sim_time:=true (write these both commands in single line)
ros2 run lab5_slam cmd_pub
ros2 run lab5_slam odom_sub
