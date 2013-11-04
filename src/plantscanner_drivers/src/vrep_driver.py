import rospy
from plantscanner_drivers.srv import *

def turn360():
    print 'turning!'
    return True

def handle_turn360(req):
    return turn360()

def turn360_server():
    service = rospy.Service('turn360', Turn360, handle_turn360)
    print 'Ready to turn 360!'

if __name__ == '__main__':
    try:
        rospy.init_node('vrep_driver')
        turn360_server()
        rospy.spin()
    except rospy.ROSInterrupException:
        pass

