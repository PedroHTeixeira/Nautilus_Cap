# ROS 18/11/2020 10:00 Part-1-T
import rospy
from std_msgs.msg import Int64

def talker():
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        i=0
        while i<=10:
            nmbr_str = i 
            rospy.loginfo(nmbr_str)
            pub.publish(nmbr_str)
            rate.sleep()
            i+=1

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
