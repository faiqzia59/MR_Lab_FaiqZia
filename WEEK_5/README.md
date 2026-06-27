
# Week 5 Lab ROS 2 Gazebo, RViz, and SLAM with TurtleBot3

## Brief Description

In Week 5 lab, we explored simulation and visualization tools in ROS 2 using the TurtleBot3 platform. We used Gazebo to simulate the robot in a virtual environment and RViz to visualize sensor data such as LiDAR, odometry, and mapping.

We performed SLAM using Cartographer, allowing the robot to build a map of the environment while moving. The robot was controlled using keyboard teleoperation, and its motion and sensor data were analyzed in real-time.

Additionally, we implemented two custom ROS 2 nodes: a publisher that sends velocity commands to the robot and a subscriber that reads odometry data. This lab provided hands-on experience in robot simulation, mapping, and ROS 2 communication.

---

## Commands Used

### Source ROS 2 environment

```bash
source /opt/ros/humble/setup.bash
````

### Build workspace

```bash
cd ~/ros2_ws_alishba
colcon build
source install/setup.bash
```

---

### Set TurtleBot3 model

```bash
export TURTLEBOT3_MODEL=burger
```

---

### Launch Gazebo simulation

```bash
ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
```

---

### Launch RViz with SLAM (Cartographer)

```bash
ros2 launch turtlebot3_cartographer cartographer.launch.py use_sim_time:=true
```

---

### Run Teleoperation

```bash
ros2 run turtlebot3_teleop teleop_keyboard
```

**Controls:**

* `w` → forward
* `s` → backward
* `a` → left
* `d` → right

---

### Record rosbag data

```bash
ros2 bag record -a
```

### Stop recording

Press `CTRL + C`

---

### Save generated map

```bash
mkdir maps
ros2 run nav2_map_server map_saver_cli -f maps/my_map
```

---

## Custom Nodes

### Run cmd_vel Publisher

```bash
ros2 run lab5_slam cmd_pub
```

---

### Run Odom Subscriber

```bash
ros2 run lab5_slam odom_sub
```

---

## Additional Tasks

### View system graph

```bash
rqt_graph
```

---

### Check topic information

```bash
ros2 topic info /odom
```

---

### Observe RViz Plugins

* LaserScan
* Map
* TF
* Odometry
* Path

---

## Problems Faced and Solutions

1. **Problem:** Gazebo not launching properly
   **Solution:** Ensured TurtleBot3 model was set correctly using:

```bash
export TURTLEBOT3_MODEL=burger
```

2. **Problem:** Nodes not running
   **Solution:** Rebuilt workspace and sourced setup file:

```bash
colcon build
source install/setup.bash
```

3. **Problem:** No data in RViz
   **Solution:** Set Fixed Frame to `map` and ensured SLAM was running.

4. **Problem:** Subscriber not receiving data
   **Solution:** Verified topic type and ensured robot was moving.

---

## Reflection

This lab enhanced my understanding of ROS 2 simulation tools such as Gazebo and RViz. I learned how to simulate a mobile robot, visualize sensor data, and perform SLAM for mapping.

Implementing the publisher and subscriber nodes improved my understanding of ROS 2 communication using topics. Observing LiDAR data and coordinate frames in RViz helped in understanding robot perception and localization.

Overall, this lab provided valuable experience in robot simulation, navigation, and real-time data analysis using ROS 2.

---

```

---


```

