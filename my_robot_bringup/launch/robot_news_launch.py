from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld =  LaunchDescription()
    
    remap_robot_news_topic = ("robot_news","minna_robot_news")
    
    #robots = ["Chapi", "Atlas", "Swiss Mile", "Mentee", "Zadok"]
    # for robot in robots:
        
    robot_news_station_node = Node(
        package="my_py_pkg",
        executable="robot_news_station",
        name="my_robot_news_station",
        remappings=[
            remap_robot_news_topic
        ],
        parameters=[
            {"robot_name", "tinker"}
        ]
    )
        
        
    smartphone_node = Node(
        package="my_py_pkg",
        executable="smartphone",
        name="smartphone",
        remappings=[
            remap_robot_news_topic
        ]
    )
    
    ld.add_action(robot_news_station_node)
    ld.add_action(smartphone_node)
    
    return ld 

