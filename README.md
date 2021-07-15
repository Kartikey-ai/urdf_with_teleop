# URDF Differential drive robot

There are three different types of urdf file present in here hermes, car_description, vehicle_Description. All of them are differential drive robots. Code is defined to work with a teleop. 
 
 
 https://user-images.githubusercontent.com/67441175/125789314-1aa646de-9eaa-492b-86d5-3a20a3e17cfd.mp4


 
 
### WORLD
World file in gazebo is a maze and is developed with a network of walls. So our bot will navigate in this environment with the help od a teleop key.

### NOTE
All the description files here are fully developed but there is a slight need to adjust the inertia values in the car_Description and vehicle_description xacro file. Adjusting it would help in proper navigation of the bot using teleop.

## Test
To test all the urdf file you just need to change the xacro file name in vehicle_description.launch and run teleop launch file simultaneously

### Map
You can also add maps in RVIZ. A different folder is made for such work.

#### Commands
- roslaunch my_vehicle vehicle_description.launch
- roslaunch my_vehicle teleop.launch
