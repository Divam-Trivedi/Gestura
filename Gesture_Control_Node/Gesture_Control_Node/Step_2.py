import cv2 as cv
import mediapipe as mp
import matplotlib.pyplot as plt
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from pynput import keyboard

camera_control = 0


class KeyPublisher(Node):
    def __init__(self):
        super().__init__('key_publisher')
        self.robot_publisher = self.create_publisher(Twist, '/model/vehicle/cmd_vel2', 10)
        self.gripper_publisher = self.create_publisher(Twist, '/model/vehicle/cmd_vel', 10)
        self.get_logger().info('KeyPublisher node started. Press "a" to publish.')

    def publish_message_robot(self, params):
        msg = Twist()
        msg.linear.x = params[0]
        msg.linear.y = params[1]
        msg.linear.z = params[2]
        msg.angular.x = params[3]
        msg.angular.y = params[4]
        msg.angular.z = params[5]
        self.robot_publisher.publish(msg)
        self.get_logger().info(f'Message published: {msg}')
    
    def publish_message_gripper(self, params):
        msg = Twist()
        msg.linear.x = params[0]
        msg.linear.y = params[1]
        msg.linear.z = params[2]
        msg.angular.x = params[3]
        msg.angular.y = params[4]
        msg.angular.z = params[5]
        self.gripper_publisher.publish(msg)
        self.get_logger().info(f'Message published: {msg}')


vid = cv.VideoCapture(camera_control)
vid.set(3, 1280)
mphands = mp.solutions.hands
Hands = mphands.Hands(max_num_hands= 2, min_detection_confidence= 0.7, min_tracking_confidence= 0.6 )
mpdraw = mp.solutions.drawing_utils

dots = []
rclpy.init(args=None)
node = KeyPublisher()
while True :
    _, frame = vid.read()
    # convert from bgr to rgb
    RGBframe = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    result = Hands.process(RGBframe)
    if result.multi_hand_landmarks:
        #print("hand found")
        for handLm in result.multi_hand_landmarks :
            #print(handLm)
            mpdraw.draw_landmarks(frame, handLm, mphands.HAND_CONNECTIONS,
                                  mpdraw.DrawingSpec(color=(0, 0, 0), circle_radius=7,
                                                     thickness=cv.FILLED),
                                  mpdraw.DrawingSpec(color=(0, 0, 0), thickness=7)
                                  )
            for id, lm in enumerate(handLm.landmark):
                h, w, _ = frame.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                # print(id, cx, cy)

               # cv.circle(frame, (cx, cy), 5, (0, 255, 0), cv.FILLED)
                if id == 4 :
                    # pass
                    Tx, Ty = cx, cy
                    cv.circle(frame, (Tx, Ty), 6, (255, 0, 0), cv.FILLED)
                if id == 8 :
                    # pass
                    cv.circle(frame, (cx, cy), 6, (255, 0, 0), cv.FILLED)
                    cv.line(frame, (cx, cy), (Tx, Ty), (255, 0, 0), 5 )
                    length = ((cx - Tx) ** 2 + (cy - Ty) ** 2) ** 0.5
                    print(length)
                    cv.putText(frame, "Open" if int(length) > 50 else "Close", (20, 50), cv.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2, cv.LINE_AA)
                    if int(length) > 50:
                        node.publish_message_gripper([0.05, 0.0, 0.0, 0.0, 0.0, 0.0])
                    else:
                        node.publish_message_gripper([-0.05, 0.0, 0.0, 0.0, 0.0, 0.0])
                        



                    dots.append(length)
    
    cv.imshow("video", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        rclpy.shutdown()
        break
        rclpy.shutdown()

vid.release()
cv.destroyAllWindows()
# rclpy.shutdown()
    #cv.imshow("rgbvideo", RGBframe)
    # cv.imshow("video", frame)
    # cv.waitKey(1)

# plt.scatter(range(len(dots)), dots)
# plt.draw()
# plt.show()
# plt.pause(0.01)
# plt.clf()