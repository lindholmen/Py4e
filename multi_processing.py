from multiprocessing import Process
from multiprocessing import Pool
import os
import time
import random

def run_process(name):
    print(f"Run child process {name} {os.getpid()}")

print(f"Parent process {os.getpid()}")
p = Process(target = run_process, args=("test",))
print('Child process will start.')
p.start()
p.join() # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
print('Child process end.')
print('###############################################################################################')

def long_time_task(name):
    print(f"Run child process {name} {os.getpid()}")
    start = time.time()
    time.sleep(random.random() *3)
    end = time.time()
    print(f"Running time for the process {name} is {end-start}")

p = Pool(4) #最多同时执行4个进程
for i in range(5):
    p.apply_async(func=long_time_task,args={"name" +str(i),})

print('Waiting for all subprocesses done...')
p.close() # 调用close()之后就不能继续添加新的Process了。
p.join() # join()方法会等待所有子进程执行完毕
print('All subprocesses done.')
print('###############################################################################################')



# 进程通信
from multiprocessing import Queue
def msg_producer(q):
    print(f"Run child process {os.getpid()}")
    for i in ["alice","bob","carol"]:
        q.put(i)
        time.sleep(random.random() *3)

def msg_consumer(q):
    while True:
        msg_name = q.get()
        print(f'Get {msg_name} from queue.')


q = Queue()
producer = Process(target=msg_producer,args=(q,))
consumer = Process(target=msg_consumer,args=(q,))
producer.start()
consumer.start()
producer.join()
consumer.terminate()

