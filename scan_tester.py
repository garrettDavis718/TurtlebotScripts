import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class LidarSubscriber(Node):
    def __init__(self):
        super().__init__("laser_subscriber_node")
        self.sub = self.create_subscription(LaserScan, "/scan", self.subscriber_callback, 10)
    def subscriber_callback(self, msg : LaserScan):
        print(f"Front Scan : {msg.ranges[0]}")
        print(f"Back Scan : {msg.ranges[180]}")

def main():
    rclpy.init()
    my_sub = LidarSubscriber()
    
    print("Waiting for data to be published over the topic...")

    try:
        rclpy.spin(my_sub)
    except KeyboardInterrupt:
        my_sub.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()