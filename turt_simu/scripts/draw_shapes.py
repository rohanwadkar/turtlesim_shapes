#!/usr/bin/env python3

import rospy

from geometry_msgs.msg import Twist

import sys

class Shape:

    def __init__(self):
          pass
    
    def turtrect():
            rospy.init_node('turtshape', anonymous=True)
            pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
            move = Twist()
            rate = rospy.Rate(1) # no. of times the message will publish in 1 second
            rate.sleep()

            for x in range(2):
                #positive-x
                move.linear.x = 2 # eg; if lin_vel is being inputted as 2 then 2 is 2m/s of linear velocity
                move.angular.z = 0
                pub.publish(move)
                print("straight")
                rate.sleep()

                #stop
                # move.angular.z = 0
                # pub.publish(move)
                # print("stop")
                # rate.sleep()

                #turn
                move.linear.x = 0
                move.angular.z = 1.570796
                pub.publish(move)
                print("turn 90")
                rate.sleep()

                # #positive-y
                move.linear.x = 1
                move.angular.z = 0
                pub.publish(move)
                print("straight-y")
                rate.sleep()

                # # #stop
                # move.linear.x = 0
                # move.angular.z = 0
                # pub.publish(move)
                # print("stop")
                # rate.sleep()

                # #turn
                move.linear.x = 0
                move.angular.z = 1.570796
                pub.publish(move)
                print("turn 90")
                rate.sleep()

    def turttri():
        
        rospy.init_node('turtshape',anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        move = Twist()
        rate = rospy.Rate(1) # no. of times the message will publish in 1 second
        rate.sleep()

        for x in range(3):
                #positive-x and stop
                move.linear.x = 2 # eg; if lin_vel is being inputted as 2 then 2 is 2m/s of linear velocity
                move.angular.z = 0
                pub.publish(move)
                print("straight")
                rate.sleep()

                #turn
                move.linear.x = 0
                move.angular.z = 2.0944
                pub.publish(move)
                print("turn 60")
                rate.sleep()


    def turtcirc():
        
        rospy.init_node('turtshape',anonymous=True)
        pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        move = Twist()
        rate = rospy.Rate(1) # no. of times the message will publish in 1 second
        rate.sleep()

        for x in range(3):
                #positive-x and stop
                move.linear.x = 2 # eg; if lin_vel is being inputted as 2 then 2 is 2m/s of linear velocity
                move.angular.z = 2
                pub.publish(move)
                print("drawing circle")
                rate.sleep()

if __name__ == '__main__':
      pass
#     try:
#         turtrect()
#         turttri()
#         turtcirc()
#     except rospy.ROSInterruptException:
#         pass


