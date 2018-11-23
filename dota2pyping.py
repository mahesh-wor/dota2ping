import sys
import subprocess
import os
import threading

sevip = {'SE Asia-1':'sgp-1.valve.net',
'Europe West':'lux.valve.net',
'Europe East':'vie.valve.net',
'US West':'eat.valve.net',
'US East':'iad.valve.net',
'Australia':'syd.valve.net',
'Russia':'sto.valve.net',
'South America':'gru.valve.net',
'South Africa-1':'196.38.180.1',
'South Africa-2':'197.80.200.1',
'South Africa-3':'197.84.209.1',
'Dubai':'185.25.183.1',
'SE Asia-2':'sgp-2.valve.net',
'India':'116.202.224.146',
}
print('\n')
art="""▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒
▓▓▓▒░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▒░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░▒▓▓▓▓▓▓▓
▓▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░▒▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▒░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▒▒░░░░░░▒▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▒░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░░░▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▒░▒▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓
▓▓▓▓▓▓▓▒░░▒▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░▒▓▓▓▓▓▓▓
▓▓▓▓▓▓▒░░░░░▒▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░▒▓▓▓▓▓
▓▓▓▓▓▒░░░░░░░░▒▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░░▒▓▓▓
▓▓▓▓▒░░░░░░░░░░░▒▓▓▓▓▓▓▓▓▓▒░░░░░░░░░░░░▒▓▓
▓▓▓▓▓▒░░░░░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░░░░░▒▓▓▓
▓▓▓▓▓▓▒░░░░▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒░░░░░▒▓▓▓▓
▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒"""

#print(sevip['same'])
#print(sevip['sea'])

print(art) #for ascii art

art_init = 0

def pingserver(ip,sev,art_init):
    ping_response = subprocess.Popen(["/bin/ping","-c1", ip], stdout=subprocess.PIPE).stdout.read()
    latency = str(ping_response)
    ping_value=latency.split('ms\\n\\n---')[0].split('=')[-1]

    #print(art_init)
    #print(art.split('\n\n')[art_init])

    if len(ping_value) > 10:
        #print('length',len(ping_value))
        ping_value = 'Error / IP_mismatch'
        print(sev,'----------------',ping_value)
    else:
        print(sev,'----------------',ping_value)

threads_list = []
for sev,ip in sevip.items():
    #    art_init = art_init+1;
    #    print(art_init, 'loop')
        t = threading.Thread(target=pingserver,name='thread_{}'.format(sev),args=(ip,sev,art_init))
        threads_list.append(t)
        t.start()


    #print('{} has started'.format(t.name))


#    ping_list_dict['sev']=ping_value
#    print(ping_list_dict)
