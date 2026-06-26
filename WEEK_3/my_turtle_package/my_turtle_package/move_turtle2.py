import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.srv import Spawn

class MultiTurtle(Node):

    def __init__(self):
        super().__init__('multi_turtle')

        # Create spawn client
        self.spawn_client = self.create_client(Spawn, '/spawn')

        # Wait for service
        while not self.spawn_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for /spawn service...')

        # Spawn turtle2
        self.spawn_turtle(5.0, 5.0, 0.0, 'turtle2')

        # Spawn turtle3
        self.spawn_turtle(6.0, 6.0, 0.0, 'turtle3')

        # Publishers
        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)
        self.pub3 = self.create_publisher(Twist, '/turtle3/cmd_vel', 10)

        self.timer = self.create_timer(1.0, self.move_turtles)

        self.step1 = 0
        self.step3 = 0

    def spawn_turtle(self, x, y, theta, name):
        req = Spawn.Request()
        req.x = x
        req.y = y
        req.theta = theta
        req.name = name

        future = self.spawn_client.call_async(req)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            self.get_logger().info(f'{name} spawned successfully')
        else:
            self.get_logger().error(f'Failed to spawn {name}')

    def move_turtles(self):
        msg1 = Twist()
        msg2 = Twist()
        msg3 = Twist()

        # 🔺 TRIANGLE (turtle1)
        if self.step1 % 2 == 0:
            msg1.linear.x = 2.0
            msg1.angular.z = 0.0
        else:
            msg1.linear.x = 0.0
            msg1.angular.z = 2.094   # 120 deg

        self.pub1.publish(msg1)
        self.step1 += 1

        # 🔵 CIRCLE (turtle2)
        msg2.linear.x = 2.0
        msg2.angular.z = 1.0
        self.pub2.publish(msg2)

        # ▱ PARALLELOGRAM (turtle3)
        if self.step3 % 2 == 0:
            msg3.linear.x = 2.0
            msg3.angular.z = 0.0
        else:
            msg3.linear.x = 0.0
            msg3.angular.z = 1.047   # 60 deg

        self.pub3.publish(msg3)
        self.step3 += 1


def main(args=None):
    rclpy.init(args=args)
    node = MultiTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()