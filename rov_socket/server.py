import socket
import json
from StringIO import StringIO

dearclient = { 'data' : { 'one': 1, 'two': 2 }, 'lol': 'meme' }
serversocket = None
clientsocket = None

def post():
  global dearclient
  global serversocket
  encode = serialize(dearclient)
  head = str(len(encode))

  for x in range(10 - len(head)):
    head = '0' + head

  encode = head + encode
  serversocket.send(encode)

# return deserialized json
def get(data):
  global clientsocket
  chunks = []
  count = 0
  length = clientsocket.recv(10)
  length = int(length)

  return deserialize(clientsocket.recv(length))


def serialize(data):
  io = StringIO()
  json.dump(data, io)
  return io.getvalue()

def deserialize(data):
  io = StringIO(data)
  return json.load(io)

def server():
  global serversocket
  global clientsocket

  #create an INET, STREAMing socket
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #bind the socket to a public host, and a well-known port
  serversocket.bind((socket.gethostname(), 80))
  #become a server socket

  serversocket.listen(5)
  (clientsocket, address) = serversocket.accept()

if __name__ == '__main__':
  server()
