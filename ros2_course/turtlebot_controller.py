import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import random
import math

class Turtlebot_Controller(Node):
    def __init__(self):

        super().__init__('turtlebot_controller')

        self.subscription = self.create_subscription(LaserScan,'/scan',self.scan_callback,10)
        self.publisher = self.create_publisher(Twist,'/cmd_vel',10)
        self.ranges = []
        self.cmd_vel_msg = Twist()

    def scan_callback(self,scan_data):
        self.ranges = scan_data.ranges
        #print("tavolsag: ",self.ranges[0])
        self.go_forward()

    def go_forward(self):
        self.cmd_vel_msg.linear.x = 0.25
        self.publisher.publish(self.cmd_vel_msg)
        try:
            angle = self.calc()
            if(angle != 0):
                self.turn(35,angle)
        except Exception as ex:
            print(ex)
            
    def turn(self,omega,angle):
        self.cmd_vel_msg.linear.x = 0.0
        self.cmd_vel_msg.angular.z = -math.radians(omega)
        self.publisher.publish(self.cmd_vel_msg)

        self.create_rate(100)

        T = abs(angle / omega)
        when = self.get_clock().now() + rclpy.time.Duration(seconds = T)

        print(self.cmd_vel_msg.angular.z )
        print(T)

        while (self.get_clock().now() < when) and rclpy.ok():
            self.publisher.publish(self.cmd_vel_msg)
            
        print("vege")
        self.cmd_vel_msg.angular.z = 0.0
        self.publisher.publish(self.cmd_vel_msg)

    def calc(self):
        for i in range(360):
            if((0<=i and i<=25) or (334<=i and i<=359)):   
                if(self.ranges[i]<0.42):
                    print("akadaly iranya: ",i)
                    print("tavolsaga: ",self.ranges[i])
                    angle = i+180
                    if(angle>360):
                        angle = angle-360+random.uniform(-30,30) 
                    else:
                        angle = angle+random.uniform(-30,30)
                    return angle
        return 0     

def main(args=None):
    rclpy.init(args=args)
    tbc = Turtlebot_Controller()

    rclpy.spin(tbc)
    
    
    tbc.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()