import subprocess
import sys

args = sys.argv
pwd = "--password=" + args[1]
print( pwd )

p = subprocess.Popen(["mosquitto_sub", "-h", "localhost", "-t", "/test"], stdout=subprocess.PIPE)
for line in iter(p.stdout.readline,b''):
#    subprocess.Popen(["mysql", "-u", "kani", pwd, "iot","--execute=show databases"])

    cmd = "--execute=" + "INSERT INTO iot.sensor_data (time, temp) VALUES (now(), %f);" % line.rstrip()
    print( cmd )
#    subprocess.Popen(["mysql", "-u", "kani", pwd, "iot", cmd])

# subprocess.Popen(["mysql", "-u", "kani", pwd, "iot","--execute=show databases"])
