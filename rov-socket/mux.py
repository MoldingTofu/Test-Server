#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, disconnect

async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None
thread_lock = Lock()

def background_thread():
  count = 0
  while True:
    socketio.sleep(10)
    count += 1
    socketio.emit('my_response', {'data': 'Server generated event', 'count': count}, namespace='/test')

@app.route('/')
def index():
  return render_template('index.html', async_mode=socketio.async_mode)

#@socketio.on('my_event', namespace='/test')
#def text_message(message):
#  session['receive_count'] = session.get('receive_count', 0) + 1
#  emit('my_response',
#    {'data': message['data'], 'count':session['receive_count']})

@socketio.on('connect', namespace='/test')
def test_connect():
  global thread
  with thread_lock:
    if thread is None:
      thread = socketio.start_background_task(target=background_thread)
  emit('my_response', {'data': 'Connected', 'count':0})

@socketio.on('send_data', namespace='/test')
def send_data(json):
  session['receive_count'] = session.get('receive_count', 0) + 1
  emit('my_response',
    {'data': json['data'], 'count': session['receive_count']})
  print('received json: ' + str(json))

@socketio.on('disconnect_request', namespace='/test')
def disconnect_request():
  session['receive_count'] = session.get('receive_count', 0) + 1
  emit('my_response',
    {'data': 'disconnected', 'count': session['receive_count']})
  disconnect()

if __name__ == '__main__':
  socketio.run(app)
