from setuptools import setup
import os
from glob import glob

package_name = 'robot_interface_control'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='WojtekKacper',
    maintainer_email='wojciech.gandziarowski@student.put.poznan.pl',
    description='Projekt zaliczeniowy',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'camera_publisher = robot_interface_control.camera_display:main',
            'click_controller = robot_interface_control.click_controller:main',
        ],
    },
)