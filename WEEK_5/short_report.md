
# **MCT-454L Mobile Robotics Lab 5**

## **Short Report: Gazebo, RViz, and SLAM with TurtleBot3**

---

## **1. Steps Followed**

1. Installed required ROS 2 packages including TurtleBot3 and Gazebo.
2. Set the TurtleBot3 model using environment variable (`burger`).
3. Launched the simulation in Gazebo to visualize the robot in a virtual environment.
4. Opened RViz with Cartographer to perform SLAM and visualize sensor data.
5. Controlled the robot using keyboard teleoperation to move in the environment.
6. Observed LiDAR scans, odometry data, and map generation in RViz.
7. Recorded all ROS topics using ros2 bag for later analysis.
8. Saved the generated map using the map saver tool.
9. Implemented a publisher node to send velocity commands to `/cmd_vel`.
10. Implemented a subscriber node to read odometry data from `/odom`.

---

## **2. RViz Visualization**

RViz showing TF, LaserScan, Map, Odometry, and Path

---

## **3. Rosbag Recording**

A ros2 bag file was recorded using:

```
ros2 bag record -a
```

---

## **4. rqt_graph Output**

rqt_graph showing active nodes and topic connections

---

## **5. Observations**

* The robot did not follow perfectly accurate motion due to simulation limitations.
* A slight delay was observed between command input and robot response.
* Odometry values showed small drift over time.
* The SLAM map was gradually built as the robot explored the environment.
* Sensor data (LiDAR) was clearly visible and updated in real-time.

---

## **6. cmd_vel Publisher**

### **Code**

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class CmdVelPublisher(Node):

    def __init__(self):
        super().__init__('cmd_vel_publisher')
        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(2.0, self.timer_callback)
        self.toggle = True

    def timer_callback(self):
        msg = Twist()
        if self.toggle:
            msg.linear.x = 0.2
            self.get_logger().info('Moving Forward')
        else:
            msg.linear.x = 0.0
            self.get_logger().info('Stopping')

        self.publisher_.publish(msg)
        self.toggle = not self.toggle

def main(args=None):
    rclpy.init(args=args)
    node = CmdVelPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

### **Running Output**

```
Moving Forward
Stopping
Moving Forward
Stopping
```

---

## **7. Odom Subscriber**

### **Code**

```python
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

class OdomSubscriber(Node):

    def __init__(self):
        super().__init__('odom_subscriber')
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(
            f'X: {msg.pose.pose.position.x}, Y: {msg.pose.pose.position.y}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = OdomSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
```

### **Running Output**

```
X: 0.02, Y: 0.00
X: 0.04, Y: 0.01
X: 0.06, Y: 0.01
```

## **8. Conclusion**

This lab provided practical experience with ROS 2 simulation tools including Gazebo and RViz. The TurtleBot3 robot was successfully simulated, controlled, and visualized. SLAM was performed using Cartographer to generate a map of the environment.

The implementation of publisher and subscriber nodes helped in understanding ROS 2 communication using topics. Some minor discrepancies such as delay and odometry drift were observed due to simulation constraints.

Overall, the lab strengthened understanding of robot simulation, mapping, and real-time data processing in ROS 2.

---

