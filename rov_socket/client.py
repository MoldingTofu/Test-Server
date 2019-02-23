import socket
import json
from StringIO import StringIO

dearflask = { 'data': 1, 'meme': { 'lol': 'hehexd' } }
#dearflask = {'youngsik': 'meme', 'tobi': 'peen', 'jeremy': {'sheen': 'leen', 'dean': 'fiend'} }

s = None

# posts dearflask as a client
def post():
  global dearflask
  global s
  encode = serialize(dearflask)
  head = str(len(encode))

  for x in range(10 - len(head)):
    head = '0' + head

  encode = head + encode
  s.send(encode)

def serialize(data):
  io = StringIO()
  json.dump(data, io)
  return io.getvalue()

def deserialize(data):
  io = StringIO(data)
  return json.load(io)

def client():
  #create an INET, STREAMing socket
  global s
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((socket.gethostname(), 80))
 
if __name__ == '__main__':
  client()
  post()
