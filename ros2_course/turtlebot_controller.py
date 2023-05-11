import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist



class Turtlebot_Controller(Node):
    def __init__(self):
        print("turtlebot controller vagyok")
        super().__init__('turtlebot_controller')

        #node = rclpy.create_node('lidar_subscriber')

        self.subscription = self.create_subscription(LaserScan,'/scan',self.scan_callback,10)
        self.publisher = self.create_publisher(Twist,'/cmd_vel',10)
        self.cmd_vel_msg = Twist()

    def scan_callback(self,scan_data):
        ranges = scan_data.ranges
        for range in ranges:
            if range < 0.2:
                print("fal")
                print(range)
                self.cmd_vel_msg.linear.x = 0.0
                self.cmd_vel_msg.angular.z = 0.0
                self.publisher.publish(self.cmd_vel_msg)
                return
            
        print("nem fal")
        self.cmd_vel_msg.linear.x = 0.2
        self.cmd_vel_msg.angular.z = 0.0
        self.publisher.publish(self.cmd_vel_msg)
    
def main(args=None):
    rclpy.init(args=args)
    tbc = Turtlebot_Controller()
    rclpy.spin(tbc)


    tbc.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()