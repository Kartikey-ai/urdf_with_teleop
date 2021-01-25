#! /usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def callback(data):
    print("Data recieved")

def listener():
    rospy.init_node('listener')
    rospy.Subscriber('/cmd_vel', Twist, callback )

if __name__ =='__main__':
    listener()
