import rclpy
import cv2
import mediapipe as mp
from rclpy.node import Node
from media_pipe_ros2_msg.msg import HandPoint,MediaPipeHumanHand,MediaPipeHumanHandList
                            

mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
cap = cv2.VideoCapture(0)

class HandsPublisher(Node):

    def __init__(self):
        super().__init__('mediapipe_publisher')
        self.publisher_ = self.create_publisher(MediaPipeHumanHandList, '/mediapipe/human_hand_list', 10)
        

    def getimage_callback(self):
        mediapipehumanlist = MediaPipeHumanHandList() 
        mediapipehuman = MediaPipeHumanHand()
        points = HandPoint()

        with mp_hands.Hands(
                static_image_mode=False,
                min_detection_confidence=0.7, 
                min_tracking_confidence=0.7, 
                max_num_hands=2) as hands:
            mphands = mp.solutions.hands
            Hands = mphands.Hands(max_num_hands= 2, min_detection_confidence= 0.7, min_tracking_confidence= 0.6 )
            mpdraw = mp.solutions.drawing_utils
            dots = []
            while cap.isOpened():

                success, frame = cap.read()
                if not success:
                    print("Sem camera.")
                            
                RGBframe = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                result = Hands.process(RGBframe)
                if result.multi_hand_landmarks:
                    #print("hand found")
                    for handLm in result.multi_hand_landmarks :
                        #print(handLm)
                        mpdraw.draw_landmarks(frame, handLm, mphands.HAND_CONNECTIONS,
                                              mpdraw.DrawingSpec(color=(0, 0, 0), circle_radius=7,
                                                                thickness=cv2.FILLED),
                                              mpdraw.DrawingSpec(color=(0, 0, 0), thickness=7)
                                              )
                        for id, lm in enumerate(handLm.landmark):
                            h, w, _ = frame.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            # print(id, cx, cy)

                          # cv2.circle(frame, (cx, cy), 5, (0, 255, 0), cv2.FILLED)
                            if id == 4 :
                                # pass
                                Tx, Ty = cx, cy
                                cv2.circle(frame, (Tx, Ty), 6, (255, 0, 0), cv2.FILLED)
                            if id == 8 :
                                # pass
                                cv2.circle(frame, (cx, cy), 6, (255, 0, 0), cv2.FILLED)
                                cv2.line(frame, (cx, cy), (Tx, Ty), (255, 0, 0), 5 )
                                length = ((cx - Tx) ** 2 + (cy - Ty) ** 2) ** 0.5
                                print(length)

                                dots.append(length)

                cv2.imshow('MediaPipe Hands', frame)
                if cv2.waitKey(5) & 0xFF == 27:
                    break        

def main(args=None):
    rclpy.init(args=args)

    hands_publisher = HandsPublisher()
    hands_publisher.getimage_callback()
    
    cap.release()
    
    rclpy.spin(hands_publisher)

    hands_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()