import time
import zmq
from datetime import datetime

port=9999
context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

def x():
    tid = socket.type=='pyobj'

    tid=0
    now = datetime.now()
    while True:
        tid+=1
        time.sleep(1)

def f(tid,ts):
    while True:
        tid = socket.recv()
        s = x()
        socket.send_pyobj(s)
        time.sleep(2)


def g(tid,ts):
    time.sleep(3)
    pass

def y(tid,ts):
    #compute throughout
    print"MSG = ",tid+now