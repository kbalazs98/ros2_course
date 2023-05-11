import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import random
import math


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
        #for range in enumerate(ranges):
        print(ranges[0])
        for i in range(360):
            if((0<=i and i<=20) or (339<=i and i<=359)):   
                if(ranges[i]<0.55):

                #obstacle_angle = scan_data.angle_min + range_idx * scan_data.angle_increment
                #opposite_angle = math.atan2(math.sin(obstacle_angle),math.cos(obstacle_angle)+math.pi)
                #self.cmd_vel_msg.linear.x = -1.0
                #self.cmd_vel_msg.angular.z = opposite_angle
                #self.publisher.publish(self.cmd_vel_msg)
                    print("szog",i)
                    print("tavolsaga",ranges[i])
                    print("FORDULKEZDODES")
                    angle = i+180
                    print(angle)
                    if(angle>360):
                        self.turn(omega = 30.0, angle = angle-360+random.uniform(-15,15))
                    else:
                        self.turn(omega = 30.0, angle = angle+random.uniform(-15,15))
                    return
        #print("nem fal")
        self.cmd_vel_msg.linear.x = 0.4
        self.cmd_vel_msg.angular.z = 0.0
        self.publisher.publish(self.cmd_vel_msg)

    def turn(self, omega, angle):
        self.cmd_vel_msg.linear.x = 0.0
        self.cmd_vel_msg.angular.z = math.radians(omega)
        self.publisher.publish(self.cmd_vel_msg)

        #rate = self.create_rate(100)  # Adjust the publishing frequency as needed

        T = abs(angle / omega)
        when = self.get_clock().now() + rclpy.time.Duration(seconds = T)

        while (self.get_clock().now() < when) and rclpy.ok():
            self.publisher.publish(self.cmd_vel_msg)
            #print(when-self.get_clock().now())
            #rate.sleep()

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