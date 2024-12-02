import cv2 as cv
import subprocess
from geometry_msgs.msg import Twist

def main(args=None):
    Directions_file = "/home/divam/ws2_ros2/src/media_pipe_ros2/src/media_pipe_ros2/media_pipe_ros2/Step_1.py"
    Grippers_file = "/home/divam/ws2_ros2/src/media_pipe_ros2/src/media_pipe_ros2/media_pipe_ros2/Step_2.py"

    while(1):
        print("Enter Command")
        print("\t 'd' to start control of the robot")
        print("\t 'g' to start control of the gripper")
        print("\t 'x' to exit the control")
        inp = input()
        if inp == 'd':
            print("Now Controlling Robot Directions")
            subprocess.run(["python3", Directions_file])
            # with open(Directions_file) as file:
            #     exec(file.read())
        if inp == 'g':
            print("Now Controlling Robot Gripper")
            with open(Grippers_file) as file:
                exec(file.read())
        
        if inp == 'x':
            print("Exiting Robot Control")
            exit()


if __name__ == '__main__':
    main()