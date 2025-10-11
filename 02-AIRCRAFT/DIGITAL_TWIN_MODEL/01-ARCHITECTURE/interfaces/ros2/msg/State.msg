# Digital Twin State Message (ROS2)

std_msgs/Header header

# Aircraft identification
string aircraft_id
string flight_id

# Position and attitude
geometry_msgs/Pose pose
geometry_msgs/Twist twist

# Propulsion
float64 fc_voltage
float64 fc_current
float64 h2_flow_rate

# Electrical
float64 battery_soc
float64 battery_voltage

# Flight dynamics
float64 altitude_msl_ft
float64 tas_kts
float64 pitch_deg
float64 roll_deg
float64 yaw_deg
