#!/usr/bin/python
# ROS 18/11/2020 17:00 Part-1
import rospy
import tf2_ros
import tf2_msgs
import geometry_msgs.msg
import math

rospy.init_node("solar_system", anonymous="True")
rate = rospy.Rate(10)
broadcaster = tf2_ros.TransformBroadcaster()

class Planets():
    def __init__(self,label,radius,header="Sun"):
        self.radius = radius
        
        self.trans=geometry_msgs.msg.TransformStamped()
        self.trans.header.frame_id = header
        self.trans.child_frame_id = label
        
        self.trans.transform.translation.x = 1
        self.trans.transform.translation.y = 2
        self.trans.transform.translation.z = 0
        
        self.trans.transform.rotation.x = 0
        self.trans.transform.rotation.y = 0
        self.trans.transform.rotation.z = 0
        self.trans.transform.rotation.w = 1

    def translate(self):
        x = 2* rospy.Time.now().to_sec() * math.pi / (self.radius**(3/2) * 60)
        self.trans.transform.translation.x = self.radius * math.sin(x)
        self.trans.transform.translation.y = self.radius * math.cos(x)
        self.trans.transform.translation.z = 0.0
        return self.trans

Earth_Radius = rospy.get_param("Earth_Radius")
Titan_Radius = rospy.get_param("Titan_Radius")
Venus_Radius = rospy.get_param("Venus_Radius")
Mercury_Radius = rospy.get_param("Mercury_Radius")
Mars_Radius = rospy.get_param("Mars_Radius")
Jupiter_Radius = rospy.get_param("Jupiter_Radius")
Saturn_Radius = rospy.get_param("Saturn_Radius")
Uranus_Radius = rospy.get_param("Uranus_Radius")
Neptune_Radius = rospy.get_param("Neptune_Radius")
Europa_Radius = rospy.get_param("Europa_Radius")

planets=[ Planets("Earth",Earth_Radius),Planets("Titan",Titan_Radius,"Saturn"), Planets("Venus",Venus_Radius), Planets("Mercury",Mercury_Radius), Planets("Mars",Mars_Radius),Planets("Jupiter",Jupiter_Radius), Planets("Saturn",Saturn_Radius), Planets("Uranus",Uranus_Radius), Planets("Neptune",Neptune_Radius),Planets("Europa",Europa_Radius,"Jupiter")]

while not rospy.is_shutdown():
    for i in planets:
        broadcaster.sendTransform(i.translate())
    rate.sleep()

