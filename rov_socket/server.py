import socket
import json
from StringIO import StringIO

with open ('packet.json') as json_data:
  dearflask = json.load(json_data,)

dearclient = { 'data' : { 'one': 1, 'two': 2 }, 'lol': 'meme' }
serversocket = None
clientsocket = None

# posts dearclient
def post():
  global dearclient
  global serversocket
  encode = serialize(dearclient)
  head = str(len(encode))

  for x in range(10 - len(head)):
    head = '0' + head

  encode = head + encode
  serversocket.send(encode)

# return deserialized dearflask
def get():
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

def init_server():
  global serversocket
  global clientsocket

  #create an INET, STREAMing socket
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  #bind the socket to a public host, and a well-known port
  serversocket.bind((socket.gethostname(), 5001))
  #become a server socket
  print('server started')

#wait
def listen():
  global serversocket
  global clientsocket

  serversocket.listen(5)
  (clientsocket, address) = serversocket.accept()
  print('client connected')
  chunks = []
  count = 0
  length = clientsocket.recv(10)
  length = int(length)

  return deserialize(clientsocket.recv(length))

def ordered(obj):
  if isinstance(obj, dict):
    return sorted((k, ordered(v)) for k, v in obj.items())
  if isinstance(obj, list):
    return sorted(ordered(x) for x in obj)
  else:
    return obj

if __name__ == '__main__':
  global dearflask
  init_server()
  while (1):
    data = listen()
    print(data)
    print(ordered(data) == ordered(dearflask))
