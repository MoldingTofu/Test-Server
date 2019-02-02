#! /usr/bin/python
import rospy
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
thread = None
thread_lock = Lock()

def status_received(msg):
  mapper = packet_mapper(packet)

@socketio.on('dearclient')
def dearclient():
  pass

@socketio.on('dearflask')
def dearflask(json):
  pass

if __name__ == "__main__":
  rospy.init_node('mux_demux')
  ns = rospy.get_namespace() # This should return /surface

  # Retrieve data from the ROS System
  esc_sub = rospy.Subscriber('/rov/esc_single', 
    esc_single_msg, status_received)

  status_sub = rospy.Subscriber('/rov/thrust_status',
    thrust_status_msg, status_received);

  temp_sub = rospy.Subscriber('/rov/temp', Temperature,
    status_received);

  imu_sub = rospy.Subscriber('/rov/imu', Imu,
    status_received);

  ph_sub = rospy.Subscriber('/rov/ph',Float32,
    status_received);

  depth_sub = rospy.Subscriber('/rov/depth', Float32,
    status_received);

  # Publishers out onto the ROS System
  thrust_pub = rospy.Publisher(ns + 'thrust_command',
    thrust_command_msg, queue_size=10);

  auto_pub= rospy.Publisher(ns +'auto_command',
    auto_command_msg, queue_size=10);

  socketio.run(app, port=5001, debug=True)

  rate = rospy.Rate(10) # 10hz
  # TODO: I2C related activities
  while not rospy.is_shutdown():
    thrust_pub.publish(thrust_command_msg())
    auto_pub.publish(auto_command_msg())
    rate.sleep()
