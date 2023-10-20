#!/usr/bin/env python3

from turt_simu.srv import turtsrv, turtsrvRequest, turtsrvResponse

import rospy

from geometry_msgs.msg import Twist

    
def turtrect():
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

            # #turn
            move.linear.x = 0
            move.angular.z = 1.570796
            pub.publish(move)
            print("turn 90")
            rate.sleep()

def turttri():
    
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


def drw_shps(req):

    if req.a == 1:
        print('Behold! Drawing Rectangle!')
        turtrect()
        resp = "Rectangle"

    elif req.a == 2:
        print('Behold! Drawing Triangle!')
        turttri()
        resp = "Triangle"

    elif req.a == 3:
        print('Behold! Drawing Circle!')
        turtcirc()
        resp = "Circle"
    else:
        rospy.logerr("Invalid shape type requested")
        resp = "error"

    return turtsrvResponse(resp)

    
def drw_shps_server():
    rospy.init_node('drw_shps_server')
    srv = rospy.Service('draw_shape', turtsrv, drw_shps)
    print('Ready to take the commands!')
    rospy.spin()
    

if __name__ == "__main__":

    drw_shps_server()