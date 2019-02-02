import socketio
import time

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('Connected to the server')

if __name__ == '__main__':
  sio.connect('http://localhost:5000', namespaces=['/test'])
  sio.emit('update_data',{ 'data': 'hi' }, namespace='/test')
  time.sleep(5)
  sio.disconnect()
