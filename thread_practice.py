import time, threading
balance = 0
lock = threading.Lock()

def change_balance(n):
    global balance
    balance = balance + n
    balance = balance - n

def access_to_account(n):
    for i in range(10):
        lock.acquire()
        try:
            change_balance(i) #给 change_balance()上一把锁，当某个线程开始执行时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_balance，只能等待，直到锁被释放后，获得该锁以后才能改
        except Exception as err:
            print(err)
        finally:
            lock.release()
            pass

t1 = threading.Thread(target=access_to_account,args=(5,))
t2 = threading.Thread(target=access_to_account,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)