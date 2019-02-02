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


jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ roscore 
mux_demux.py      packet_mapper.py  server.py         
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ roscore 
mux_demux.py      packet_mapper.py  server.py         
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ roscore packet_mapper.py Usage: roscore [options]

roscore: error: roscore does not take arguments
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ roscore
... logging to /home/jeremy/.ros/log/d458ec50-21a2-11e9-ae82-fcf8ae7a4c66/roslaunch-notmac-17158.log
Checking log directory for disk usage. This may take awhile.
Press Ctrl-C to interrupt
Done checking log file disk usage. Usage is <1GB.

started roslaunch server http://notmac:42669/
ros_comm version 1.14.3


SUMMARY
========

PARAMETERS
 * /rosdistro: melodic
 * /rosversion: 1.14.3

NODES

auto-starting new master
process[master]: started with pid [17168]
ROS_MASTER_URI=http://notmac:11311/

setting /run_id to d458ec50-21a2-11e9-ae82-fcf8ae7a4c66
process[rosout-1]: started with pid [17179]
started core service [/rosout]
python packet_mapper.py
^C[rosout-1] killing on exit
[master] killing on exit
lsshutting down processing monitor...
... shutting down processing monitor complete
done
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ ls
mux_demux.py  packet_mapper.py  server.py
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ clear

jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim ~/.bashrc 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux packet_mapper.py
[rospack] Error: package 'mux_demux' not found
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ source ../../../
.gitignore  launch/     src/        
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ source ../../../devel/setup.bash 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux packet_mapper.py
names:  ['addr', 'data', 'stabilization_dim', 'temperature', 'pressure', 'status', 'thrust_vec', 'dims_locked', 'id', 'data', 'disable_thrusters', 'desired_thrust', 'inverted', 'temperature', 'current', 'hbl', 'vfl', 'hfr', 'vbl', 'vbr', 'hfl', 'vfr', 'hbr']
paths:  {'data': 'in2.data', 'addr': 'addr'}
{'addr': '6581', 'in2': {'data': '0'}}
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim packet_mapper.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim 
mux_demux.py      packet_mapper.py  server.py         
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim mux_demux.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ git branch
  development
  feat-build-frontend
* feat-mux-demux
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ ls
mux_demux.py  packet_mapper.py  server.py
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux packet_mapper.py 
names:  ['addr', 'data', 'stabilization_dim', 'temperature', 'pressure', 'status', 'thrust_vec', 'dims_locked', 'id', 'data', 'disable_thrusters', 'desired_thrust', 'inverted', 'temperature', 'current', 'hbl', 'vfl', 'hfr', 'vbl', 'vbr', 'hfl', 'vfr', 'hbr']
paths:  {'data': 'in2.data', 'addr': 'addr'}
{'addr': '6581', 'in2': {'data': '0'}}
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux 
mux_demux.py      packet_mapper.py  
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux 
mux_demux.py      packet_mapper.py  
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux mux_demux.py 
^Cjeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim mux_demux.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ python server.py
  File "server.py", line 41
    disconnect()
             ^
SyntaxError: invalid syntax
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim server.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ python server.py
  File "server.py", line 43
    if __name__ == '__main__':
                             ^
SyntaxError: invalid syntax
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim packet_mapper.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ cat packet_mapper.py 
#! /usr/bin/python
import shared_msgs.msg


class packet_mapper:

    topic_paths = {}

    def __init__(self, packet):
        names = list()
        msgs = dict([(name, cls) for name, cls in shared_msgs.msg.__dict__.items() if isinstance(cls, type)])
        for msg in msgs.keys():
            #print msg
            for key,value in getattr(shared_msgs.msg, msg).__dict__.iteritems():
                if type(value).__name__ == 'member_descriptor':
                    names.append(key)

        print 'names: ', names

        for name in names:
            path = self._build_path(packet, name)
            if path:
                self.topic_paths[name] = path

        print 'paths: ', self.topic_paths

    def map(self, var, value, packet):
        path = self.topic_paths[var]
        split = path.split('.')
        p = packet
        for e in split[:-1]:
            p = p[e]
        p[split[-1]] = value

    def _build_path(self, d, name):
        for key,value in d.items():
            if type(value) == dict:
                ret = self._build_path(value, name)
                if ret != "":
                    return key + '.' + ret
            if key == name:
                return key
        return ""

if __name__ == "__main__":
    packet = { 'addr' : 'hello', 'in2' : { 'data' : 1    }   }
    mapper = packet_mapper(packet)
    mapper.map('addr', '6581', packet)
    mapper.map('data', '0', packet)
    print packet


jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim server.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ python server.py 
  File "server.py", line 43
    if __name__ == "__main__":
                             ^
SyntaxError: invalid syntax
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim server.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ python server.py 
  File "server.py", line 43
    if __name__ == "__main__":
                             ^
SyntaxError: invalid syntax
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim server.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ python server.py
  File "server.py", line 43
    if __name__ == '__main__':
                             ^
SyntaxError: invalid syntax
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ source ~/Documents/
test-server/ X11-Core/    
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ source ~/Documents/test-server/rov-socket/
client.py  README.md  server.py  templates/ venv/      
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ source ~/Documents/test-server/rov-socket/venv/bin/activate
(venv) jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ python server.py
  File "server.py", line 43
    if __name__ == '__main__':
                             ^
SyntaxError: invalid syntax
(venv) jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ deactivate
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ git pull
remote: Enumerating objects: 121, done.
remote: Counting objects: 100% (121/121), done.
remote: Compressing objects: 100% (31/31), done.
remote: Total 126 (delta 91), reused 116 (delta 89), pack-reused 5
Receiving objects: 100% (126/126), 14.92 KiB | 636.00 KiB/s, done.
Resolving deltas: 100% (91/91), completed with 50 local objects.
From https://github.com/purduerov/X11-Core
   c24e7f9..bb1c483  development     -> origin/development
 * [new branch]      feat-camera     -> origin/feat-camera
   309f295..23d31d8  feat-fix-packet -> origin/feat-fix-packet
   523d850..21a7d1c  feat-keyboard   -> origin/feat-keyboard
   0596672..e5e4958  ros             -> origin/ros
   e6336c9..2fc5e95  ui-redesign     -> origin/ui-redesign
Already up to date.
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ git pull
Already up to date.
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ git pull
Already up to date.
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ ls
mux_demux.py  packet_mapper.py  server.py
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ git pull
Already up to date.
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim server.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ git pull
remote: Enumerating objects: 7, done.
remote: Counting objects: 100% (7/7), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 7 (delta 5), reused 7 (delta 5), pack-reused 0
Unpacking objects: 100% (7/7), done.
From https://github.com/purduerov/X11-Core
   92a1e26..436cfa7  feat-mux-demux -> origin/feat-mux-demux
Updating 92a1e26..436cfa7
Fast-forward
 ros/src/mux_demux/scripts/packet_mapper.py | 18 +++++++++++++++---
 1 file changed, 15 insertions(+), 3 deletions(-)
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ vim packet_mapper.py 
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ rosrun mux_demux packet_mapper.py 
names:  ['addr', 'data', 'stabilization_dim', 'temperature', 'pressure', 'status', 'thrust_vec', 'dims_locked', 'id', 'data', 'disable_thrusters', 'desired_thrust', 'inverted', 'temperature', 'current', 'hbl', 'vfl', 'hfr', 'vbl', 'vbr', 'hfl', 'vfr', 'hbr']
paths:  {'data': 'in2.data', 'addr': 'addr'}
None
jeremy@notmac:~/Documents/X11-Core/ros/src/mux_demux/scripts$ 

