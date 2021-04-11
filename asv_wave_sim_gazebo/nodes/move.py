#!/usr/bin/env python
# license removed for brevity

import sys
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

rospy.init_node('vel_pub')
pub = rospy.Publisher("/cmd_vel", Twist, queue_size = 10)
rate = rospy.Rate(2)
cmd_vel = Twist()
cmd_vel.linear.x = 2.0
cmd_vel.linear.y = 0.0
cmd_vel.angular.z = 0.0


while not rospy.is_shutdown():
    pub.publish(cmd_vel)
    rate.sleep()