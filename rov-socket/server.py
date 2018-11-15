import socket

s = socket.socket()
print "socket created"

port = 8000

s.bind(('', port))
print "socket binded to %s" %(port)

s.listen(5)
print "socket is listening"

while True:
  c, addr = s.accept()
  print "got connection from ", addr

  c.send("sent")

  c.close()
