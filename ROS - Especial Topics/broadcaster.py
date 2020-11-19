# ROS 18/11/2020 17:00 Part-1
import rospy
import tf2_ros
import tf2_msgs
import geometry_msgs.msg


rospy.init_node("example", anonymous="True")
rate = rospy.Rate(10)
broadcaster = tf2_ros.TransformBroadcaster()

trans=geometry_msgs.msg.TransformStamped()

trans.header.frame_id = "map"
trans.child_frame_id = "place"

trans.header.stamp = rospy.Time.now()

trans.transform.translation.x = 1
trans.transform.translation.y = 2
trans.transform.translation.z = 0
trans.transform.rotation.x = 0
trans.transform.rotation.y = 0
trans.transform.rotation.z = 0
trans.transform.rotation.w = 1

while not rospy.is_shutdown():
    broadcaster.sendTransform(trans)
    rate.sleep()

rospy.spin()
