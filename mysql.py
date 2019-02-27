import subprocess
import sys

args = sys.argv
pwd = "--password=" + args[1]
print( pwd )

#p = subprocess.Popen(["mosquitto_sub", "-h localhost", "-t /test"], stdout=subprocess.PIPE)
#for line in iter(p.stdout.readline,b''):
#    print(line.rstrip().decode("utf8"))
#    subprocess.Popen(["mysql", "-u", "kani", "--password=hogehoge", "iot","--execute=show databases"])

subprocess.Popen(["mysql", "-u", "kani", pwd, "iot","--execute=show databases"])
