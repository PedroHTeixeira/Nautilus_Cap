# ROS 18/11/2020 10:00 Part-1-L
import rospy
from std_msgs.msg import Int64

def callback(data):
    a = data.data
    if a % 2 != 0:
        print(a)

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('chatter', Int64, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()