from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
            name='sim'
        ),
        Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        ),
        Node(
            package='ros2_course',
            executable='turtlesim_controller',
            name='controller',
            remappings=[
                ('/turtle1/pose', '/turtlesim1/turtle1/pose'),
                ('/turtle1/cmd_vel', '/turtlesim1/turtle1/cmd_vel'),
            ]
        )
    ])