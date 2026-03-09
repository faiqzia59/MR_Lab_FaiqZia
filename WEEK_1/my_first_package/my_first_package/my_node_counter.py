import rclpy
from rclpy.node import Node
import os

COUNTER_FILE = '/tmp/simple_node_counter.txt'  # You can choose another path

class SimpleNode(Node):
    def __init__(self):
        super().__init__('simple_node')

        # Load previous counter from file if exists
        self.counter = self.load_counter()

        # Increment immediately since running the node counts as 1
        self.counter += 1
        self.save_counter()

        self.get_logger().info(
            f'WELCOME TO MOBILE ROBOTICS LAB | Run Count: {self.counter}'
        )

        # Timer: runs every 1 second
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        self.get_logger().info(
            f'WELCOME TO MOBILE ROBOTICS LAB | Current Count: {self.counter}'
        )

    def load_counter(self):
        if os.path.exists(COUNTER_FILE):
            with open(COUNTER_FILE, 'r') as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_counter(self):
        with open(COUNTER_FILE, 'w') as f:
            f.write(str(self.counter))


def main(args=None):
    rclpy.init(args=args)
    node = SimpleNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()