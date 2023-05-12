# ros2_course
##About

Turtlebot3 obstackle evasion --robotic vacuum cleaner--

Installing turtlebot3 simulation package:
  $ cd ~/turtlebot3_ws/src/
  $ git clone -b foxy-devel https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git
  $ cd ~/turtlebot3_ws && colcon build --symlink-install
  
Starting the simulation:
  $ export TURTLEBOT3_MODEL=waffle
  $ ros2 launch turtlebot3_gazebo turtlebot3_world.launch.py
  
Starting the turtlebot controller:
  $ ros2 launch ros2_course turtlebot_controller_launch.py
