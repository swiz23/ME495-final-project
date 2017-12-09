#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from ar_track_alvar.msgs import AvlarMarker
import rospy
import sys
import numpy as np


from geometry_msgs.msg import Twist
    
def callback(data):
    #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    print "hi"
def artransform():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('artransform', anonymous=True)

    #th=AvlarMarker()
    rospy.Subscriber("ar_pose_marker", AvlarMarker, th)
    print th
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':

    try:
        artransform()
    except rospy.ROSInterruptException:
        pass

