
import subprocess
ping_response = subprocess.Popen(["/bin/ping","-c1", "8.8.8.8"], stdout=subprocess.PIPE).stdout.read()
latency = str(ping_response)
ping_list=latency.split('ms\\n\\n---')[0].split('=')[-1]
print(ping_list)
