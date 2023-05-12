from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros2_course',
            namespace='turtlebot',
            executable='turtlebot_controller',
            name='TBC'
        )
    ])