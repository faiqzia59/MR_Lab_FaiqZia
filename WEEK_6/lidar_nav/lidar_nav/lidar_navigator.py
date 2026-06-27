import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import numpy as np


class LidarNavigator(Node):

    def __init__(self):
        super().__init__('lidar_navigator')

        # Subscriber
        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        # Publisher
        self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)

        # Safety thresholds
        self.SAFE_DIST = 0.7      # start reacting early
        self.CRITICAL_DIST = 0.4  # emergency stop/turn
        self.WALL_DIST = 0.5      # side wall avoidance

    def scan_callback(self, msg):

        # Convert to numpy array
        ranges = np.array(msg.ranges)

        # Clean invalid values
        ranges[np.isinf(ranges)] = 3.5
        ranges[np.isnan(ranges)] = 0.0

        # Define regions
        front_region = np.concatenate((ranges[0:20], ranges[340:359]))
        left_region = ranges[60:140]
        right_region = ranges[220:300]

        # Get minimum distances
        front_dist = np.min(front_region)
        left_dist = np.min(left_region)
        right_dist = np.min(right_region)

        twist = Twist()

        # -----------------------------
        # MAIN CONTROL LOGIC
        # -----------------------------

        if front_dist < self.CRITICAL_DIST:
            # 🚨 VERY CLOSE → STOP + HARD TURN
            twist.linear.x = 0.0

            if left_dist > right_dist:
                twist.angular.z = 1.2
            else:
                twist.angular.z = -1.2

        elif front_dist < self.SAFE_DIST:
            # ⚠️ CLOSE → SLOW + TURN
            twist.linear.x = 0.05

            if left_dist > right_dist:
                twist.angular.z = 0.6
            else:
                twist.angular.z = -0.6

        else:
            # ✅ CLEAR PATH → MOVE FORWARD
            twist.linear.x = 0.18

            # Wall avoidance (stay centered)
            if left_dist < self.WALL_DIST:
                twist.angular.z = -0.2
            elif right_dist < self.WALL_DIST:
                twist.angular.z = 0.2
            else:
                twist.angular.z = 0.0

        # Publish velocity
        self.publisher.publish(twist)


def main(args=None):
    rclpy.init(args=args)

    node = LidarNavigator()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
    