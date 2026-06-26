# Week 2 Lab ROS 2 Turtlesim, Topics, Services, and RQT Exploration

## Brief Description

In Week 2 lab, we explored the practical implementation of ROS 2 concepts using the Turtlesim simulator. We learned how to launch a node, control a turtle using keyboard teleoperation, and interact with ROS 2 topics and services. We observed real-time data from topics like `/turtle1/pose` and sent velocity commands to move the turtle. Additionally, we used services such as `/reset` and `/spawn` to manipulate the simulation. The lab also introduced the RQT tool for visualizing nodes, topics, and services. By the end, we successfully controlled multiple turtles and understood how ROS 2 communication works in real-time.

## Commands Used

### Source ROS 2 environment
```bash
source /opt/ros/humble/setup.bash
```

### Launch turtlesim
```bash
ros2 run turtlesim turtlesim_node
```

### Control turtle using keyboard
```bash
ros2 run turtlesim turtle_teleop_key
```

### List all active topics
```bash
ros2 topic list
```

### View turtle position in real-time
```bash
ros2 topic echo /turtle1/pose
```

### Publish velocity command to move turtle
```bash
ros2 topic pub /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.8}}"
```

### Reset simulation
```bash
ros2 service call /reset std_srvs/srv/Empty
```

### Open RQT tool
```bash
rqt
```

### Spawn a second turtle
```bash
ros2 service call /spawn turtlesim/srv/Spawn "{x: 5.0, y: 5.0, theta: 0.0, name: 'turtle2'}"
```

### Control second turtle
```bash
ros2 topic pub /turtle2/cmd_vel geometry_msgs/msg/Twist "{linear: {x: 1.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.0}}"
```

---

## Additional Commands

### Change Background Color

#### Pink
```bash
ros2 param set /turtlesim background_r 255
ros2 param set /turtlesim background_g 105
ros2 param set /turtlesim background_b 180
ros2 service call /clear std_srvs/srv/Empty
```

#### Purple
```bash
ros2 param set /turtlesim background_r 128
ros2 param set /turtlesim background_g 0
ros2 param set /turtlesim background_b 128
ros2 service call /clear std_srvs/srv/Empty
```

#### Sea Green
```bash
ros2 param set /turtlesim background_r 46
ros2 param set /turtlesim background_g 139
ros2 param set /turtlesim background_b 87
ros2 service call /clear std_srvs/srv/Empty
```

#### Bluish
```bash
ros2 param set /turtlesim background_r 70
ros2 param set /turtlesim background_g 130
ros2 param set /turtlesim background_b 180
ros2 service call /clear std_srvs/srv/Empty
```

---

### Teleport Turtle

#### Teleport to a specific position
```bash
ros2 service call /turtle1/teleport_absolute turtlesim/srv/TeleportAbsolute "{x: 2.0, y: 8.0, theta: 1.57}"
```

#### Teleport relative to current position
```bash
ros2 service call /turtle1/teleport_relative turtlesim/srv/TeleportRelative "{linear: 2.0, angular: 1.57}"
```

---

## Problems Faced and How They Were Solved

1. **Problem:** Turtle not moving using topic command  
   **Solution:** Ensured correct topic name `/turtle1/cmd_vel` and proper message format for `geometry_msgs/msg/Twist`.

2. **Problem:** ros2 command not working  
   **Solution:** ROS 2 environment was not sourced. Fixed by running:
```bash
source /opt/ros/humble/setup.bash
```

3. **Problem:** Second turtle not responding  
   **Solution:** Verified correct topic `/turtle2/cmd_vel` and ensured turtle was successfully spawned.

4. **Problem:** RQT not showing nodes or topics  
   **Solution:** Restarted RQT after running turtlesim node and ensured environment was sourced.

---

## Reflection

This lab strengthened my understanding of ROS 2 communication through topics and services. I learned how to control a robot in real-time by publishing velocity commands and observing feedback through topic echo. Using services like `/reset` and `/spawn` helped me understand request-response interactions in ROS 2. The RQT tool provided a clear visualization of how nodes and topics are connected. Controlling multiple turtles demonstrated how independent nodes operate within the same system. Additionally, experimenting with background color changes and teleportation enhanced my understanding of ROS 2 parameters and services. Overall, this lab improved my practical skills in ROS 2 and prepared me for more advanced robotic control and simulations.
