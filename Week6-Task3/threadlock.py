import threading
def one(name,lock):
    lock.acquire()
    new()
    print(name,token)
    lock.release()
token = 0
def new():
    global token
    token = token+1

l1 = threading.Lock()
t1 = threading.Thread(target = one,args = ["dhoni",l1])    
t2 = threading.Thread(target = one,args = ["virat",l1])
##t3 = threading.Thread(target=one,args=["bharani",l1])

t1.start()
t2.start()
##t3.start()

t1.join()
t2.join()
##t3.join()
