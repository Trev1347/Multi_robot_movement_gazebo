import os
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution, TextSubstitution
import math


def generate_launch_description():
    Launch_description = [
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare('robot_gazebo'), 'launch', 'start_world.launch.py'
                ])
            )
        )
    ]

    N=10
    A=5

    for i in range(N):
        Launch_description.append(IncludeLaunchDescription(
            PathJoinSubstitution([
                FindPackageShare('robot_gazebo'), 'launch', 'spawn_with_control.launch.xml'
            ]),
            launch_arguments={
                'robot_name': 'robot_'+str(i+1),
                'robot_file': 'robot.xacro',
                'x_spawn': str(round(A*math.sin(2*math.pi*i/N),2)),
                'y_spawn': str(round(A*math.cos(2*math.pi*i/N),2)),
                'z_spawn': '0.16',
                'roll_spawn': '0.0',
                'pitch_spawn': '0.0',
                'yaw_spawn': '0.0',
            }.items()
        )
    )
    
    return LaunchDescription(Launch_description)