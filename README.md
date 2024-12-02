# Gestura
A gesture controlled robot simulated in gazebo with ROS2

For Simulation perform colcon build and then 

```
ros2 launch gestura_simulation own_lauch.py
```

For teleop, In another terminal run

```
ros2 run gestura_simulation key_publisher.py
```

For Getsure based control, run

```
ros2 run Gesture_Control_Node robot_control.py
```

Follow the instructions to control the robot
