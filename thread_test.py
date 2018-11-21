import threading
import time

def sleeper (n, name):
    print ('hi am {}. goint to sleep for 5 sec \n'.format(name))
    time.sleep(n)
    print ('{} has woke up from sleep \n'.format(name))
"""
t = threading.Thread(target = sleeper,name='thread1',
                     args = (5,'thread1'))

t.start()

"""
threads_list = []
start = time.time()
for i in range(5):
    t = threading.Thread(target=sleeper,name='thread{}'.format(i),args=(5,'thread{}'.format(i)))
    threads_list.append(t)
    t.start()
    print('{} has started'.format(t.name))

for t in threads_list:
    t.join()
end = time.time()
print('time tanken:{}'.format(end-start))
print('All Tthreads finished job')
