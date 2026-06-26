from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, TimerAction

def generate_launch_description():
    return LaunchDescription([

        # 🐢 Start turtlesim
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='sim',
            output='screen'
        ),

        # 🐢 Spawn turtle2 using service (CORRECT WAY)
        TimerAction(
            period=2.0,
            actions=[
                ExecuteProcess(
                    cmd=[
                        'ros2', 'service', 'call',
                        '/spawn',
                        'turtlesim/srv/Spawn',
                        '{x: 5.0, y: 5.0, theta: 0.0, name: "turtle2"}'
                    ],
                    output='screen'
                )
            ]
        ),

        # 🎮 Teleop for turtle1
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop',
            prefix='xterm -e',
            output='screen'
        ),

        # 🤖 Start follower AFTER spawn
        TimerAction(
            period=3.0,
            actions=[
                Node(
                    package='my_launch_pkg',
                    executable='follow_turtle',
                    name='follower',
                    output='screen'
                )
            ]
        ),
    ])