#!/usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('index.html')

@socketio.on('connect')
def connect(message):
  emit('reponse', {'data': 'data'})
  print('connected')

@socketio.on('disconnect')
def disconnect():
  print('disconnected')

if __name__ == '__main__':
  socketio.run(app)
