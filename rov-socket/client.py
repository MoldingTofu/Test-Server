import websocket
from websocket import create_connection

ws = create_connection("127.0.0.1:12345")
ws.send('hello')
ws.close()
