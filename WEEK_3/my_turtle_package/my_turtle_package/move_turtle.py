import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

class MultiTurtleController(Node):

    def __init__(self):
        super().__init__('multi_turtle_controller')

        # Publishers for both turtles
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        self.timer = self.create_timer(0.5, self.control_turtles)

        self.step = 0

    def control_turtles(self):
        msg1 = Twist()  # triangle
        msg2 = Twist()  # circle

        # 🔺 Turtle1 → TRIANGLE
        if self.step % 2 == 0:
            msg1.linear.x = 2.0
            msg1.angular.z = 0.0
        else:
            msg1.linear.x = 0.0
            msg1.angular.z = 2.094  # 120 degrees

        # 🔵 Turtle2 → CIRCLE
        msg2.linear.x = 2.0
        msg2.angular.z = 1.0

        self.pub1.publish(msg1)
        self.pub2.publish(msg2)

        self.step += 1
        time.sleep(2)


def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtleController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()