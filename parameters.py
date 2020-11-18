import rospy

rospy.init_node("aula", anonymous="True")
var = rospy.get_param("a")
print(var)