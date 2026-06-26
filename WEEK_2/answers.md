# Week 2 Lab Q&A (ROS 2 Turtlesim)

## Q1: What is a node in ROS 2?
A node is a basic unit of execution in ROS 2. It is a process that performs computation, such as controlling a robot or processing data. For example, `turtlesim_node` is a node that runs the turtle simulator.

---

## Q2: What is a topic in ROS 2?
A topic is a communication channel used to exchange data between nodes. One node publishes data, and other nodes can subscribe to it. For example, `/turtle1/cmd_vel` is used to send velocity commands to the turtle.

---

## Q3: What is the difference between topics and services?
Topics are used for continuous data streaming (one-way communication), while services are used for request-response communication (two-way). Topics are asynchronous, whereas services are synchronous.

---

## Q4: What is the purpose of `/turtle1/pose` topic?
The `/turtle1/pose` topic provides real-time information about the turtle’s position, orientation, and velocity. It helps in monitoring the movement of the turtle.

---

## Q5: What message type is used to control turtle movement?
The message type used is `geometry_msgs/msg/Twist`. It contains linear and angular velocity components that control how the turtle moves.

---

## Q6: What does the `/reset` service do?
The `/reset` service resets the simulation. It clears the screen and moves the turtle back to its initial position.

---

## Q7: What is the use of `/spawn` service?
The `/spawn` service is used to create a new turtle in the simulation at a specified position and orientation.

---

## Q8: How can you change the background color in turtlesim?
The background color can be changed using ROS 2 parameters:
- `background_r`
- `background_g`
- `background_b`  
After setting values, call `/clear` service to apply changes.

---

## Q9: What is teleportation in turtlesim?
Teleportation allows the turtle to instantly move to a new position without following a path. It can be done using:
- `teleport_absolute`
- `teleport_relative`

---

## Q10: What is RQT and why is it used?
RQT is a GUI tool in ROS 2 used to visualize nodes, topics, and services. It helps in understanding how different components of the system are connected.

---

## Q11: Why is sourcing the ROS 2 environment important?
Sourcing sets up environment variables required for ROS 2 commands to work. Without it, commands like `ros2` will not run.

---

## Q12: How do multiple turtles work in the same simulation?
Each turtle operates with its own namespace (e.g., `/turtle1`, `/turtle2`). This allows independent control using different topics and services.

---

## Q13: What happens if you publish incorrect data to a topic?
If the message format is incorrect, the command may fail or the turtle may not move properly. ROS 2 requires correct message types and structure.

---

## Q14: What did you learn from this lab?
This lab helped me understand ROS 2 communication using topics and services. I learned how to control a robot in real-time, monitor its state, and use tools like RQT for visualization.

---
