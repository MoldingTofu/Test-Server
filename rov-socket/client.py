import socketio

sio = socketio.Client()

@sio.on('connect')
def on_connect():
    print('I\'m connected to the server')

if __name__ == '__main__':
  url = 'http://localhost:5000/'
  sio.connect(url, namespaces=['/test'])
  sio.emit('update_data', {'data': 'hi'})
  sio.disconnect()
