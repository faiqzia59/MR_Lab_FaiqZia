# My Mobile Robot – URDF Description

## Overview
This project implements a simple differential-drive mobile robot using the Unified Robot Description Format (URDF) in ROS 2. The robot was designed and visualized in RViz as part of Mobile Robotics Lab Session 8.

---

## Robot Components

The robot consists of four main links:

### 1. Base Link
- Shape: Box
- Dimensions: 0.4 m × 0.3 m × 0.1 m
- Color: Blue
- Purpose: Serves as the main body and reference frame of the robot.

### 2. Camera
- Shape: Cylinder
- Radius: 0.03 m
- Length: 0.05 m
- Color: Black
- Position: Mounted on top of the robot.
- Purpose: Represents a vision sensor that can be used for future perception tasks.

### 3. Left Wheel
- Shape: Cylinder
- Radius: 0.05 m
- Length: 0.02 m
- Color: Black
- Position: Left side of the base.
- Purpose: Provides locomotion for the differential drive robot.

### 4. Right Wheel
- Shape: Cylinder
- Radius: 0.05 m
- Length: 0.02 m
- Color: Black
- Position: Right side of the base.
- Purpose: Provides locomotion for the differential drive robot.

---

## Joint Configuration

| Joint Name | Type | Parent Link | Child Link | Purpose |
|------------|-------|-------------|------------|----------|
| camera_joint | Fixed | base_link | camera | Mounts the camera on the robot |
| left_wheel_joint | Continuous | base_link | left_wheel | Allows continuous rotation of left wheel |
| right_wheel_joint | Continuous | base_link | right_wheel | Allows continuous rotation of right wheel |

---

## Robot Frame Hierarchy

```text
base_link
├── camera
├── left_wheel
└── right_wheel
```

---

## Customizations Made

The following customizations were implemented:

- Added a camera sensor mounted on top of the robot body.
- Added left and right wheels to create a differential-drive configuration.
- Used multiple geometric shapes:
  - Box for the base.
  - Cylinders for the camera and wheels.
- Implemented different joint types:
  - Fixed joint for the camera.
  - Continuous joints for wheel rotation.
- Added custom materials and colors for improved visualization in RViz.

---

## Package Structure

```text
my_robot_description/
├── launch/
├── rviz/
└── urdf/
    └── my_robot.urdf
```

---

## Building the Workspace

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

---

## Visualizing the Robot in RViz

```bash
ros2 launch urdf_tutorial display.launch.py model:=/home/<username>/ros2_ws/src/my_robot_description/urdf/my_robot.urdf
```

Replace `<username>` with your Linux username.

---

## Viewing the TF Tree

Generate the TF frame diagram using:

```bash
ros2 run tf2_tools view_frames
```

A file named `frames.pdf` will be created showing the relationship between all robot links.

---

## Future Improvements

The robot can be further extended by:

- Adding a LiDAR sensor for mapping and navigation.
- Adding a caster wheel for improved stability.
- Integrating the robot into Gazebo simulation.
- Implementing differential drive controllers.
- Adding autonomous navigation capabilities.

---

## Conclusion

A custom mobile robot was successfully designed using URDF and visualized in RViz. The robot consists of a base, a camera module, and two continuous rotating wheels representing a differential-drive mobile platform. This model provides a foundation for future simulation, control, and navigation tasks in ROS 2 and Gazebo.
