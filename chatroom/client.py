import socket
import threading
import time

tLOCK = threading.Lock()
shutdown = False

def receiving(name,sock):
    while not shutdown:
        try:
            tLOCK.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                print str(data)
        except:
            pass
        finally:
            tLOCK.release()
host = '127.0.0.1'
port = 0


server = ('127.0.0.1',5000)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host,port))

s.setblocking(0)
rt =  threading.Thread(target = receiving,args = ("RecvThread",s))
rt.start()

alias = raw_input("name: ")
message = raw_input(alias+"->")

while message != "q":
    if message != '':
        s.sendto(alias + " " + message,server)
    tLOCK.acquire()
    message = raw_input(alias+"->")
    tLOCK.release()
    time.sleep(0.2)
shutdown = True
rt.join()
s.close()