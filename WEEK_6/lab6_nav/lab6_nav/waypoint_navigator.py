import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from nav2_msgs.action import FollowWaypoints
from geometry_msgs.msg import PoseStamped
import math


class WaypointNavigator(Node):
    def __init__(self):
        super().__init__('waypoint_navigator')
        self._client = ActionClient(self, FollowWaypoints, 'follow_waypoints')

    def send_waypoints(self, waypoints):
        self.get_logger().info('Waiting for FollowWaypoints server...')
        self._client.wait_for_server()

        goal_msg = FollowWaypoints.Goal()
        goal_msg.poses = waypoints

        self.get_logger().info(f'Sending {len(waypoints)} waypoints...')
        send_goal_future = self._client.send_goal_async(goal_msg)
        rclpy.spin_until_future_complete(self, send_goal_future)

        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().error('Goal rejected!')
            return

        self.get_logger().info('Goal accepted! Navigating...')

        result_future = goal_handle.get_result_async()
        rclpy.spin_until_future_complete(self, result_future)

        self.get_logger().info('✅ All waypoints reached!')


def quaternion_from_yaw(yaw):
    """Convert yaw to quaternion"""
    qz = math.sin(yaw / 2.0)
    qw = math.cos(yaw / 2.0)
    return qz, qw


def make_pose(x, y, yaw):
    pose = PoseStamped()
    pose.header.frame_id = 'map'

    pose.pose.position.x = x
    pose.pose.position.y = y
    pose.pose.position.z = 0.0

    qz, qw = quaternion_from_yaw(yaw)
    pose.pose.orientation.z = qz
    pose.pose.orientation.w = qw

    return pose


def main(args=None):
    rclpy.init(args=args)

    navigator = WaypointNavigator()

    # 🔥 USE SAFE WAYPOINTS (adjust if needed)
    waypoints = [
        make_pose(0.3,  0.0,  0.0),     # Forward
        make_pose(0.6,  0.3,  1.57),    # Right-up
        make_pose(0.3,  0.6,  3.14),    # Backward
        make_pose(0.0,  0.3, -1.57),    # Left-down
        make_pose(0.0,  0.0,  0.0)      # Back to origin
    ]

    navigator.send_waypoints(waypoints)

    navigator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
