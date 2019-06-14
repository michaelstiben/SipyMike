import pycom
import time

pycom.heartbeat(False)
output=0x000000

for x in range(0, 10):
    output += 0x000077
    time.sleep(2)
    if (x == 10):
        output = 0x000000
