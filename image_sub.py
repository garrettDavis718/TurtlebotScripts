import rclpy # Python library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # Package to convert between ROS and OpenCV Images
import cv2 # OpenCV library

class ImageSubscriber(Node):
    def __init__(self):
    # Initiate the Node class's constructor and give it a name
        super().__init__('image_subscriber')
        self.sub = self.create_subscription(Image, "camera/image_raw", self.subscriber_callback, 10)
        self.br = CvBridge()
    def subscriber_callback(self, data : Image):
        self.get_logger().info('Receiving video frame')
        current_frame = self.br.imgmsg_to_cv2(data)
    
        # Display image
        cv2.imshow("camera", current_frame)
        
        cv2.waitKey(1)

    
def main():
    rclpy.init()
    my_sub = ImageSubscriber()
    print("Waiting for data to be published over the topic...")

    try:
        rclpy.spin(my_sub)
    except KeyboardInterrupt:
        my_sub.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()


