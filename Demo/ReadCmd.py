import os

cmd = 'ping 127.0.0.1'
out = os.popen(cmd)
print(out.read().strip())