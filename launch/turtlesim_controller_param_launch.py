from launch_ros.actions import Node
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess, TimerAction
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():
    speed_value = LaunchConfiguration('speed')
    omega_value = LaunchConfiguration('omega')
    background_r_value = LaunchConfiguration('background_r')

    speed_launch_arg = DeclareLaunchArgument(
        'speed',
        default_value='1.0',
        description='Turtle speed'
    )

    
    
    omega_launch_arg = DeclareLaunchArgument(
        'omega',
        default_value='20.0',
        description='Turtle speed'
    )
    background_r_launch_arg = DeclareLaunchArgument(
        'background_r',
        default_value='200.0',
        description='Background red component'
    )

    turtlesimnode_1 = Node(
            package='turtlesim',
            namespace='turtlesim1',
            executable='turtlesim_node',
            name='sim'
        )
    
    turtlesimnode_2 = Node(
            package='turtlesim',
            namespace='turtlesim2',
            executable='turtlesim_node',
        )
    
    mimic_node = Node(
            package='turtlesim',
            executable='mimic',
            name='mimic',
            remappings=[
                ('/input/pose', '/turtlesim1/turtle1/pose'),
                ('/output/cmd_vel', '/turtlesim2/turtle1/cmd_vel'),
            ]
        )
    
    controller_node = Node(
            package='ros2_course',
            executable='turtlesim_controller',
            name='controller',
            remappings=[
                ('/turtle1/pose', '/turtlesim1/turtle1/pose'),
                ('/turtle1/cmd_vel', '/turtlesim1/turtle1/cmd_vel'),
            ]
        )
    
    change_background_r = ExecuteProcess(
        cmd=[[
            'ros2 param set ',
            'turtlesimnode_1',
            '/sim background_r ',
            '120'
        ]],
        shell=True
    )
    

    return LaunchDescription([
        turtlesimnode_1,
        turtlesimnode_2,
        mimic_node,
        controller_node,
        change_background_r
    ])
