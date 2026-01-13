#!/usr/bin/env python3

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Ścieżka do launcha Gazebo z TurtleBotem
    gazebo_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(
                get_package_share_directory('turtlebot3_gazebo'),
                'launch',
                'empty_world.launch.py'
            )
        ])
    )
    
    # Node publikujący czarny obraz
    camera_node = Node(
        package='robot_interface_control',
        executable='camera_publisher',
        name='camera_publisher',
        output='screen'
    )
    
    # Node sterujący robotem przez kliknięcia
    click_controller_node = Node(
        package='robot_interface_control',
        executable='click_controller',
        name='click_controller',
        output='screen'
    )
    
    # Opóźnij start naszych node'ów o 5 sekund (żeby Gazebo zdążyło się załadować)
    delayed_camera = TimerAction(period=5.0, actions=[camera_node])
    delayed_controller = TimerAction(period=5.0, actions=[click_controller_node])
    
    return LaunchDescription([
        gazebo_launch,
        delayed_camera,
        delayed_controller,
    ])

# cd ~/Desktop/projekt/ros2_ws
# colcon build --packages-select robot_interface_control
# source install/setup.bash
# export TURTLEBOT3_MODEL=waffle_pi
# ros2 launch robot_interface_control robot_control.launch.py