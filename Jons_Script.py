#simple detection

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class WallAvoider(Node):
    def __init__(self):
        super().__init__("wall_avoider_node")
        self.sub = self.create_subscription(LaserScan, "/scan",
         self.subscriber_callback, 10)
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def subscriber_callback(self, msg : LaserScan, move_cmd = Twist()):
        print("==========================")
        print('s1 [270]')
        print (msg.ranges[270])
        print('s2 [0]')
        print (msg.ranges[0])
        print('s3 [90]')
        print(msg.ranges[90])
        if msg.ranges[0] > 1 or msg.ranges == 'inf':
            move_cmd.linear.x = 0.2
            move_cmd.angular.z = 0.0
        if msg.ranges[0] < 1:
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.2
        if msg.ranges[270] < 0.3:
            move_cmd.linear.x = 0.1
            move_cmd.angular.z = 0.2
        if msg.ranges[315] < 0.3:
            move_cmd.linear.x = 0.0
            move_cmd.angular.z = 0.2
        self.pub.publish(move_cmd)

def main():
    rclpy.init()
    my_node = WallAvoider()
    print("Waiting for data to be published over the topic...")

    try:
        rclpy.spin(my_node)
    except KeyboardInterrupt:
        stop = Twist()
        my_node.pub.publish(stop)
        my_node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()