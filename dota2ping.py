import sys
import subprocess
import os

sevip = {'sea':'103.28.54.1','euw':'146.66.152.1',
'eue':'146.66.155.1','usw':'192.69.96.1',
'use':'208.78.164.1','au':'103.10.125.1',
'ru':'146.66.156.1','same':'209.197.29.1',
'saf':'197.80.200.1','dubai':'185.25.183.1'}

print(sevip['same'])
print(sevip['sea'])

for sev,ip in sevip.items():
    ping_response = subprocess.Popen(["/bin/ping","-c1", ip], stdout=subprocess.PIPE).stdout.read()
    latency = str(ping_response)
    if len(latency) > 5:
        print(len(latency))
        ping_value = 'Error'
    else:
        ping_value=latency.split('ms\\n\\n---')[0].split('=')[-1]
    print(ping_value)



#    ping_list_dict['sev']=ping_value
#    print(ping_list_dict)



input()
