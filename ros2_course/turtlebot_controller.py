from rclpy.node import Node
import rclpy
from sensor_msgs.msg import LaserScan



class Turtlebot_Controller(Node):
    def __init__(self):
        print("turtlebot controller vagyok")
        super().__init__('turtlebot_controller')

        node = rclpy.create_node('lidar_subscriber')

        subscriber = node.create_subscription(LaserScan,'/scan',scan_callback,10)
        subscriber

        try:
            rclpy.spin(node)
        except KeyboardInterrupt:
            pass

def scan_callback(scan_data):
    ranges = scan_data.ranges
    if len(ranges)>0:
        print("Distance to the nearest obstacle: ", ranges[0])

def main(args=None):
    rclpy.init(args=args)
    tbc = Turtlebot_Controller()



    tbc.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()