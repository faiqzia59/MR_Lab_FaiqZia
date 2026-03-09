import rclpy
from rclpy.node import Node


class SimpleNode(Node):

    def __init__(self):
        super().__init__('simple_node')

        # Declare parameter
        self.declare_parameter('student_name', '')

        # Create timer (runs every 1 second)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):

        # Get parameter value
        name = self.get_parameter('student_name').value

        if name != '':
            self.get_logger().info(f"Student Name: {name}")
        else:
            self.get_logger().info("student_name not set")


def main(args=None):

    rclpy.init(args=args)

    node = SimpleNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()