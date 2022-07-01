from asyncio import base_subprocess
from email.mime import base

from sqlalchemy import true
from launch import LaunchDescription
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory
import launch_ros
from pathlib import Path
import launch
import launch_ros


def generate_launch_description():
    base_path = os.path.realpath(get_package_share_directory("pid_controller"))
    pid_config = (Path(base_path) / "config" / "pid_config.json").as_posix()
    return LaunchDescription(
        [
            launch.actions.DeclareLaunchArgument(
                name="target_frame", default_value="ego_vehicle"
            ),
            launch.actions.DeclareLaunchArgument(
                name="pid_config_path", default_value=pid_config
            ),
            launch.actions.DeclareLaunchArgument(
                name="source_frame", default_value="map"
            ),
            launch.actions.DeclareLaunchArgument(
                name="odom_topic", default_value="/carla/ego_vehicle/odometry"
            ),
            launch.actions.DeclareLaunchArgument(
                name="next_waypoint_topic", default_value="/next_waypoint"
            ),
            launch.actions.DeclareLaunchArgument(
                name="target_speed", default_value="25.0"
            ),
            Node(
                package="pid_controller",
                executable="pid_controller_node",
                name="waypoint_publisher_node",
                output="screen",
                emulate_tty=True,
                parameters=[
                    {
                        "target_frame": launch.substitutions.LaunchConfiguration(
                            "target_frame"
                        ),
                        "pid_config_path": launch.substitutions.LaunchConfiguration(
                            "pid_config_path"
                        ),
                        "source_frame": launch.substitutions.LaunchConfiguration(
                            "source_frame"
                        ),
                        "odom_topic": launch.substitutions.LaunchConfiguration(
                            "odom_topic"
                        ),
                        "next_waypoint_topic": launch.substitutions.LaunchConfiguration(
                            "next_waypoint_topic"
                        ),
                        "target_speed": launch.substitutions.LaunchConfiguration(
                            "target_speed"
                        ),
                    }
                ],
            ),
        ]
    )
