import socketio # for socket

sio = socketio.Client()

@sio.on('connect')
def on_connect():
  print('connected')

if __name__ == '__main__':
  sio.connect('http://localhost:5000/')
  sio.wait()
