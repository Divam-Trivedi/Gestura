from setuptools import find_packages, setup
from glob import glob as glob

package_name = 'gestura_simulation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Install launch files
        ('share/' + package_name + '/launch', glob('launch/*.launch.*')),
        # Install scripts
        ('lib/' + package_name + '/scripts', glob('scripts/*.py')),
        # Install RViz configuration files
        ('share/' + package_name + '/rviz', glob('rviz/*.rviz')),
        # Install model files
        ('share/' + package_name + '/models', glob('models/vehicle/*', recursive=True)),
        # Install world files
        ('share/' + package_name + '/worlds', glob('worlds/*.world')),
        # Install environment hooks
        ('share/' + package_name + '/hooks', glob('hooks/*.dsv.in')),
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
            'key_publisher = gestura_simulation.key_publisher:main',
        ],
    },


    
)
