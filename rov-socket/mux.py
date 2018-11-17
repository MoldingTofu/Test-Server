from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
socketio = SocketIO(app)

@socketio.on('message')
def handle_message(message):
  send(message)

@socketio.on('json')
def handle_json(json):
  #send to ros?
  print('received json: ' + str(json))

if __name__ == '__main__':
  socketio.run(app)
