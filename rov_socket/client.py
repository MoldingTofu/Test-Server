import socketio
import time

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to the server')

if __name__ == '__main__':
  sio.connect('http://localhost:5001')
  sio.emit('connect')
  sio.emit('dearclient')
  sio.disconnect()
