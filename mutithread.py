#coding = utf-8
import time
import threading
tLock = threading.Lock()
def fun(a):
    tLock.acquire()
    print "I am a thread"+a+"\n"
    tLock.release()
def main():
    thread = []
    for i in range(5):   
        t = threading.Thread(target = fun ,args = str(i))
        thread.append(t)
    for i in range(5):
        thread[i].start()
    for i in range(5):
        thread[i].join()

if __name__ == '__main__':
    main()