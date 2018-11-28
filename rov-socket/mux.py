#!/usr/bin/env python
from threading import Lock
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('index.html', async_mode=socketio.async_mode)

@socketio.on('connect', namespace='/test')
def connect():
  emit('my_response', {'data': 'Connected', 'count':0})
  print('connected')

@socketio.on('disconnect', namespace='/test')
def disconnect():
  print('disconnected', request.sid)

if __name__ == '__main__':
  socketio.run(app)
