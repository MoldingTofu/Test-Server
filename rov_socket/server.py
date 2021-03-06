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
  length = clientsocket.recv(10)
  try:
    length = int(length)
  except:
    return

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
  serversocket.bind((socket.gethostname(), 80))
  #become a server socket
  print('server started')
  serversocket.listen(5)

def listen():
  global serversocket
  global clientsocket

  print('listening')
  (clientsocket, address) = serversocket.accept()
  print('client connected')

#wait
def accept():
  global serversocket
  global clientsocket

  length = clientsocket.recv(10)
  try:
    length = int(length)
  except:
    raise Exception()

  get = deserialize(clientsocket.recv(length))

  post = {'lol': '1'}
  encode = serialize(post)
  head = str(len(encode))
  for x in range(10 - len(head)):
    head = '0' + head
  encode = head + encode
  clientsocket.send(encode)

  print('update values')

  return get

def ordered(obj):
  if isinstance(obj, dict):
    return sorted((k, ordered(v)) for k, v in obj.items())
  if isinstance(obj, list):
    return sorted(ordered(x) for x in obj)
  else:
    return obj

if __name__ == '__main__':

  init_server()
  listen()
  while (1):
    try:
      data = accept()
      print(data)
      print(ordered(data) == ordered(dearflask))
    except:
      #clientsocket.shutdown(2)
      #clientsocket.close()
      listen()
