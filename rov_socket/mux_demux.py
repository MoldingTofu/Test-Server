#! /usr/bin/python
import rospy
from shared_msgs.msg import can_msg, auto_command_msg, thrust_status_msg, thrust_command_msg, esc_single_msg
from sensor_msgs.msg import Imu, Temperature
from std_msgs.msg import Float32

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app, async_mode=async_mode)
thread = Node
thread_lock = Lock()

@socketio.on('dearclient')
def dearclient():
  #build packet
  #emit('my_response', packet)
  pass

@socketio.on('dearflask')
def dearflask(json):
  mapper = packet_mapper(json)
  print mapper.names

def name_received(msg):
  pass

#def thrust_status_received(msg):
#  pass # This runs on a seperate thread
#def esc_single_received(msg):
#  pass # This runs on a seperate thread

#def temp_received(msg):
#  pass # This runs on a seperate thread
#def imu_received(msg):
#  pass # This runs on a seperate thread
#def ph_received(msg):
#  pass # This runs on a seperate thread
#def depth_received(msg):
#  pass # This runs on a seperate thread

if __name__ == "__main__":
  rospy.init_node('mux_demux')
  ns = rospy.get_namespace() # This should return /surface
  

  # Retrieve data from the ROS System
  esc_sub = rospy.Subscriber('/rov/esc_single', 
      esc_single_msg, esc_single_received)

  status_sub = rospy.Subscriber('/rov/thrust_status',thrust_status_msg,
    thrust_status_received);

  temp_sub = rospy.Subscriber('/rov/temp', Temperature,
    temp_received);

  imu_sub = rospy.Subscriber('/rov/imu', Imu,
    imu_received);

  ph_sub = rospy.Subscriber('/rov/ph',Float32,
    ph_received);

  depth_sub = rospy.Subscriber('/rov/depth', Float32,
    depth_received);

  # Publishers out onto the ROS System
  thrust_pub = rospy.Publisher(ns + 'thrust_command',
    thrust_command_msg, queue_size=10);

  auto_pub= rospy.Publisher(ns +'auto_command',
    auto_command_msg, queue_size=10);

  socketio.run(app, port=5001, debug=True)

  rate = rospy.Rate(10) # 10hz
  rospy.spin()
  #thrust_pub.publish(thrust_command_msg())
  #auto_pub.publish(auto_command_msg())
