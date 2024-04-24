import launch
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return launch.LaunchDescription([
        DeclareLaunchArgument(
            'world',
            default_value='path/to/your/model_1.world',
            description='Path to custom Gazebo world file'
        ),

        Node(
            package='gazebo_ros',
            executable='gazebo',
            name='gazebo',
            output='screen',
            arguments=['-s', 'libgazebo_ros_factory.so', '-r', '--verbose', '-o', LaunchConfiguration('world')]
        )
    ])
