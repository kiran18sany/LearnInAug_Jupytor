import threading
import time

def longSquare(num,results):
    time.sleep(1)
    results[num]= num**2

results={}
t1=threading.Thread(target = longSquare, args=(1,results))


t2=threading.Thread(target = longSquare, args=(2,results))

t1.start()
print ('k')
t2.start()

t1.join()
print ('k1')
t2.join()

print(results)