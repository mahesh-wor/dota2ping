import threading

import time


def sleeper (n, name):
    print ('hi am {}. goint to sleep for 5 sec \n'.format(name))
    time.sleep(n)
    print ('{} has woke up from sleep \n'.format(name))


t = threading.Thread(target = sleeper,name='thread1',
                     args = (2,'thread1'))

t.start()
