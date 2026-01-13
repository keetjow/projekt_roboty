# Projekt zaliczeniowy
# Wojciech Gandziarowski, Kacper Gadomski


cd ~/Desktop/projekt/ros2_ws
colcon build --packages-select robot_interface_control
source install/setup.bash
export TURTLEBOT3_MODEL=waffle_pi
ros2 launch robot_interface_control robot_control launch.py