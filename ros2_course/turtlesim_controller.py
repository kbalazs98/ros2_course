import math
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose


class TurtlesimController(Node):

    def __init__(self):
        super().__init__('turtlesim_controller')

        self.declare_parameter('speed',0.1)
        self.declare_parameter('omega',20.0)

        self.pose = None
        self.subscription = self.create_subscription(
            Pose,
            '/turtle1/pose',
            self.cb_pose,
            10)

        self.twist_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def cb_pose(self, msg):
        self.pose = msg

    def go_straight(self,distance):
        # Implement straght motion here
        # Create and publish msg

        speed = self.get_parameter('speed').get_parameter_value().double_value
        vel_msg = Twist()
        if distance > 0:
            vel_msg.linear.x = speed
        else:
            vel_msg.linear.x = -speed

        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0

        # Set loop rate
        loop_rate = self.create_rate(100, self.get_clock()) # Hz

        # Calculate time
        T = abs(distance / speed)

        # Publish first msg and note time when to stop
        self.twist_pub.publish(vel_msg)
        # self.get_logger().info('Turtle started.')
        when = self.get_clock().now() + rclpy.time.Duration(seconds=T)

        # Publish msg while the calculated time is up
        while(self.get_clock().now()<when) and rclpy.ok():
            self.twist_pub.publish(vel_msg)
            # self.get_logger().info('On its way...')
            rclpy.spin_once(self)   # loop rate

        # turtle arrived, set velocity to 0
        vel_msg.linear.x = 0.0
        self.twist_pub.publish(vel_msg)
        # self.get_logger().info('Arrived to destination.')

    def turn(self, omega, angle):
        vel_msg = Twist()

        vel_msg.linear.y = 0.0
        vel_msg.linear.z = 0.0
        vel_msg.angular.x = 0.0
        vel_msg.angular.y = 0.0
        vel_msg.angular.z = 0.0

        if angle > 0:
            vel_msg.angular.z = math.radians(omega)
        else:
            vel_msg.angular.z = math.radians(-omega)

        loop_rate = self.create_rate(100, self.get_clock())

        T= abs(angle/omega)

        self.twist_pub.publish(vel_msg)
        when = self.get_clock().now() + rclpy.time.Duration(seconds = T)

        while(self.get_clock().now()<when) and rclpy.ok():
            self.twist_pub.publish(vel_msg)
            # self.get_logger().info('On its way...'
            rclpy.spin_once(self)

        vel_msg.linear.z = 0.0
        self.twist_pub.publish(vel_msg)
        

    def draw_square(self, omega, a):
        for i in range(4):
            self.go_straight(a)
            self.turn(omega,90)

def main(args=None):
    rclpy.init(args=args)
    tc = TurtlesimController()
    #tc.turn(90,90)
    #tc.go_straight(1.0,2.0)

    tc.draw_square(90.0,5.0)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)

 
    tc.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
