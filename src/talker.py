#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from movement import color_detect

def talker():
	pub = rospy.Publisher('move', String, queue_size = 10)
	rospy.init_node('talker', anonymous = True)
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		msg = String()
		msg.data = "%s" %(color_detect.left_right())
		#rospy.loginfo(msg)
		pub.publish(msg)
		rate.sleep()
		
if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass	
