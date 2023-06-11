# RPLIDAR ROS package

=====================================================================

ROS node and test application for RPLIDAR

Visit following Website for more details about RPLIDAR:

rplidar HomePage:   http://www.slamtec.com/en/Lidar

rplidar SDK: https://github.com/Slamtec/rplidar_sdk

How to build rplidar ros package
=====================================================================
    1) Clone this project to your workspace src folder
    2) Running `colcon build` to build `rplidarNode` and `rplidarNodeClient`


Node parameters:


- `serial_port` - (`string`, default: `/dev/ttyUSB0`) serial port name used in your system. 
- `serial_baudrate` - (`int`, default: `115200`) serial port baud rate. 
- `frame_id` - (`string`, default: `laser_frame`) frame ID for the device. 
- `inverted` - (`bool`, default: `false`) indicated whether the LIDAR is mounted inverted. 
- `angle_compensate` - (`bool`, default: `false`) indicated whether the driver needs do angle compensation. 
- `scan_mode` - (`string`, default: empty) the scan mode of lidar. 

Node services:

- `stop_motor` (`std_srvs/Empty`) Call the serive to stop the motor of rplidar. 
- `start_motor` (`std_srvs/Empty`) Call the service to start the motor of rplidar. 

# How to run rplidar ros package
=====================================================================

There are launch files for RpLidar models:

- for RPLIDAR A1/A2
    ```
    ros2 launch rplidar_ros rplidar.launch.py
    ```
- for RPLIDAR A3
    ```
    ros2 launch rplidar_ros rplidar_a3.launch.py
    ```
- for RPLIDAR S1
    ```
    ros2 launch rplidar_ros rplidar_s1.launch.py
    ```

For every launch file, the output scans are available on `/scan` topic.

Notice: the difference is `serial_baudrate` between A1/A2 and A3/S1

RPLidar frame
=====================================================================
RPLidar frame must be broadcasted according to picture shown below

For RpLidar A1:

![RpLidar A1 coordinate frame](rplidar_A1.png "RpLidar A1 coordinate frame")

For RpLidar A2:

![RpLidar A2 coordinate frame](rplidar_A2.png "RpLidar A2 coordinate frame")
