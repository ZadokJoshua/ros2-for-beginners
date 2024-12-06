from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld =  LaunchDescription()
    
    remap_robot_news_topic = ("robot_news","minna_robot_news")
    robot_names = ["Chapi", "Atlas", "Swiss_Mile", "Mentee", "Zadok"]
    robot_nodes = []
    
    for robot in robot_names:
        robot_nodes.append(
            Node(
                package="my_py_pkg",
                executable="robot_news_station",
                name=f"{robot}_robot_news_station",
                remappings=[
                    remap_robot_news_topic
                ],
                parameters=[
                    {"robot_name": robot}
                ]
            ))
        
        
    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="smartphone",
        remappings=[
            remap_robot_news_topic
        ]
    )
    
    for node in robot_nodes:
        ld.add_action(node)
    ld.add_action(smartphone_node)
    
    return ld 