import subprocess

p = subprocess.Popen(["mosquitto_sub", "-h localhost", "-t /test"], stdout=subprocess.PIPE)
for line in iter(p.stdout.readline,b''):
    print(line.rstrip().decode("utf8"))
    subprocess.Popen(["mysql", "-u", "kani", "--password=hogehoge", "iot","--execute=show databases"])
