#! /usr/bin/python
import rospy
import json
from shared_msgs.msg import can_msg, auto_command_msg, thrust_status_msg, thrust_command_msg, esc_single_msg
from sensor_msgs.msg import Imu, Temperature
from std_msgs.msg import Float32

from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect

async_mode = None
app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app, async_mode=async_mode)
thread = Node
thread_lock = Lock()

with open ('../../../../surface/frontend/src/packets.json') as json_data:
  data = json.load(json_data,)

dearflask = data['dearflask']
dearclient = data['dearclient']
fmapper = packet_mapper(dearflask)
cmapper = packet_mapper(dearclient)
thrust_pub = None
auto_pub = None

@socketio.on('dearflask')
def dearflask(json):
<<<<<<< HEAD
  dearFlask = json
  emit('my_response', dearClient)

  for data in dearFlask["thrusters"]:
    setattr(thrust_command_msg(), data, dearFlask["thrusters"][data])
=======
  global dearflask = json
  emit('my_response', dearclient)
>>>>>>> 849dff9890afd5ee191629b4df37a9ea42476478
  thrust_pub.publish(thrust_command_msg())

  for data in dearFlask["auto"]:
    setattr(auto_command_msg(), data, dearFlask["auto"][data])
  auto_pub.publish(auto_command_msg())

def name_received(msg):
  names = clientMapper.get_msg_vars(msg)
  for name in names:
    clientMapper.map(name, getattr(msg, name), dearClient)

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
      esc_single_msg, name_received)

  status_sub = rospy.Subscriber('/rov/thrust_status',thrust_status_msg,
    name_received);

  temp_sub = rospy.Subscriber('/rov/temp', Temperature,
    name_received);

  imu_sub = rospy.Subscriber('/rov/imu', Imu,
    name_received);

  ph_sub = rospy.Subscriber('/rov/ph',Float32,
    name_received);

  depth_sub = rospy.Subscriber('/rov/depth', Float32,
    name_received);

  # Publishers out onto the ROS System
  thrust_pub = rospy.Publisher(ns + 'thrust_command',
    thrust_command_msg, queue_size=10);

  auto_pub= rospy.Publisher(ns +'auto_command',
    auto_command_msg, queue_size=10);

  socketio.run(app, port=5001, debug=True)

  rate = rospy.Rate(10) # 10hz

  rospy.spin()
  #while not rospy.is_shutdown():
  #  thrust_pub.publish(thrust_command_msg())
  #  auto_pub.publish(auto_command_msg())
