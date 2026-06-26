import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class TurtleMover(Node):
    def __init__(self):
        super().__init__('turtle_mover')
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pose_sub = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.pose = None
        self.target_x = 1.0
        self.target_y = 1.0
        self.timer = self.create_timer(0.1, self.move_turtle)

    def pose_callback(self, msg):
        self.pose = msg

    def move_turtle(self):
        if self.pose is None:
            return
        
        # Compute distance to target
        dx = self.target_x - self.pose.x
        dy = self.target_y - self.pose.y
        distance = math.sqrt(dx**2 + dy**2)
        
        msg = Twist()
        if distance > 0.1:
            # Move linearly toward target
            angle_to_goal = math.atan2(dy, dx)
            msg.linear.x = 1.5 * distance
            msg.angular.z = 4.0 * (angle_to_goal - self.pose.theta)
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0

        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleMover()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()