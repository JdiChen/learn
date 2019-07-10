import _thread
from time import sleep,ctime
def loop():
    print("start loop at",ctime())
    sleep(4)
    print("loop end at",ctime())
def loop1():
    print("start loop1 at", ctime())
    sleep(2)
    print("loop1 end at", ctime())
if __name__=='__main__':
    print("start thread at ",ctime())
    _thread.start_new_thread(loop,())
    _thread.start_new_thread(loop1,())
    sleep(5)

    print("thread end at ",ctime())