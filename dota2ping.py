import sys
import subprocess
import os
import re
import statistics

sevip = {'sea':'103.28.54.1','euw':'146.66.152.1',
'eue':'146.66.155.1','usw':'192.69.96.1',
'use':'208.78.164.1','au':'103.10.125.1',
'ru':'146.66.156.1','same':'209.197.29.1',
'saf':'197.80.200.1','dubai':'185.25.183.1'}

print(sevip['same'])
print(sevip['sea'])




def ping_list(ip):
    #cmd = "ping" "-n 1 " + ip
    #val = os.system(cmd)
    val = subprocess.Popen(["ping",ip , "-n", '4'], stdout=subprocess.PIPE).stdout.read()
    val=val[-6:-4]
    print(val)
    len(val)

ping_list('8.8.8.8')


input()
