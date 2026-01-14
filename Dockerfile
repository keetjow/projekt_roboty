FROM osrf/ros:humble-desktop

ENV DEBIAN_FRONTEND=noninteractive
ENV TURTLEBOT3_MODEL=waffle_pi

RUN apt update && apt install -y \
    python3-pip \
    ros-humble-turtlebot3* \
    ros-humble-gazebo-ros \
    ros-humble-cv-bridge \
    python3-opencv \
    x11-apps \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /ros2_ws
COPY ros2_ws /ros2_ws

RUN . /opt/ros/humble/setup.sh && \
    colcon build

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc && \
    echo "source /ros2_ws/install/setup.bash" >> ~/.bashrc

CMD ["bash"]
