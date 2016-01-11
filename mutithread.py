#coding = utf-8
import time
import threading

loops = [4,2]

def loop(nloop,nsec):
    print 'start loop' , nloop , 'at:' , time.ctime()
    time.sleep(nsec)
    print 'loop' , nloop , 'done at' , time.ctime() 

def main():
    print 'start main at :' + time.ctime()
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()
    
    print 'close main at :' + time.ctime()

if __name__ == '__main__':
    main();