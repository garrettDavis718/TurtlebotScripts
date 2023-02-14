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
        print(f"Front Distance : {msg.ranges[0]}")
        print(f"Back Distance : {msg.ranges[180]}")
        if msg.ranges[0] > 1.5:
            move_cmd.linear.x = 0.2
            move_cmd.angular.z = 0.0
        else:
            move_cmd.linear.x = 0.1
            move_cmd.angular.z = 0.3
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