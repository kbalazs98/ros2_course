# ros2_course
##About

Turtlebot3 obstackle evasion --robotic vacuum cleaner--

Installing turtlebot3 simulation package: https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
  $ cd ~/turtlebot3_ws/src/
  $ git clone -b foxy-devel 
  $ cd ~/turtlebot3_ws && colcon build --symlink-install
  
Starting the simulation:
  $ export TURTLEBOT3_MODEL=waffle
  $ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
  
Starting the turtlebot controller:
  $ ros2 launch ros2_course turtlebot_controller_launch.py

Documentation:
The code is a ROS 2 node that controls a Turtlebot using laser scan data. It subscribes to the /scan topic for laser scan information and publishes velocity commands on the /cmd_vel topic.

The scan_callback method is the callback function for the laser scan subscription. It receives the laser scan data and calls the go_forward method.

The go_forward method sets the linear velocity and publishes the command. It calculates the turn angle using the calc method and calls the turn method to perform the turn.

The turn method sets the angular velocity and publishes the command. It calculates the turn duration and loops until the desired time is reached. Finally, it stops the angular velocity and publishes the command.

The calc method calculates the turn angle based on the laser scan data. If it doesn't detect obstacle it returns 0 so the turn method won't be called.

Overall, the code controls the Turtlebot by moving it forward and making turns based on the laser scan information.
