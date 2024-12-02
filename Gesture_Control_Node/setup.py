from setuptools import find_packages, setup

package_name = 'Gesture_Control_Node'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='divam',
    maintainer_email='divam@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'directions_step1 = Gesture_Control_Node.Step1_Directions:main',
            'gripper_step2 = Gesture_Control_Node.Step2_Grippers:main',
            'robot_control = Gesture_Control_Node.final_S1_s2:main',
        ],
    },
)
