import random
from subprocess import call

for x in xrange(1, 100):
    ipAdd = "10."
    ipAdd += ".".join(map(str, (random.randint(128, 255)
                                for _ in range(3))))
call(["ifconfig", "eth0", "%d", "netmask", "255.255.255.0", "broadcast", "192.168.2.255" % ipAdd])
print ipAdd
