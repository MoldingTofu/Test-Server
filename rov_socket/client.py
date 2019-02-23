import socket

#create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 80))

dearflask = { 'data': 1, 'meme': { 'lol': 'hehexd' } }

s.send('12345')

def dearflask(json):
  pass

def dearclient():
  pass
