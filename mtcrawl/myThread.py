#coding = utf-8
import threading
import time
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func
        self.args = args
    def run(self):
        print 'starting', self.name , 'at:', time.ctime()
        self.res = apply(self.func,self.args)
        print 'finishing', self.name , 'at:', time.ctime()
    def getResult(self):
        return self.res
