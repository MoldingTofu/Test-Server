to use virtual environment
```
source venv/bin/activate
```

to install flask and flask-io
```
pip install flask --user
```
```
pip install flask-socketio --user
```

python socketio: https://python-socketio.readthedocs.io/en/latest/server.html


TODO:
config file that will connect topics with keys from packet
asynchronous socket
integrate with mux_demux.py and dearflask, dearclient methods
(X11-Core/ros/src/mux_demux/scripts/mux_demux.py)

to test:
```
run roscore
```
new terminal
```
source devel/setup.bash
cd folder/script.py
rosrun folder script.py
```
