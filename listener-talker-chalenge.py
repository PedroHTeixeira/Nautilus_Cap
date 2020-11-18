# ROS 18/11/2020 10:00 Part-2-T-L
import rospy
from std_msgs.msg import Int64

def callback(data):
    a = data.data
    if a % 2 != 0:
        print(a)

def talker():
    pub = rospy.Publisher('chatter', Int64, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        i=0
        while i<=10:
            nmbr_str = i 
            pub.publish(nmbr_str)
            rate.sleep()
            i+=1

def listener():
    rospy.init_node('listener-talker', anonymous=True)
    rospy.Subscriber('chatter', Int64, callback)
    

if __name__ == '__main__':
    try:
        listener()
        talker()
    except rospy.ROSInterruptException:
        pass