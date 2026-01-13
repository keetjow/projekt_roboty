#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch',
                'empty_world.launch.py'
            )
        ])
    )
    
    camera_node = Node(
        package='robot_interface_control',
        executable='camera_publisher',
        name='camera_publisher',
        output='screen'
    )
    
    click_controller_node = Node(
        package='robot_interface_control',
        executable='click_controller',
        name='click_controller',
        output='screen'
    )
    
    return LaunchDescription([
        gazebo_launch,
        camera_node,
        click_controller_node,
    ])

# cd ~/Desktop/projekt/ros2_ws
# colcon build --packages-select robot_interface_control
# source install/setup.bash
# export TURTLEBOT3_MODEL=waffle_pi
# ros2 launch robot_interface_control robot_control.launch.py