import subprocess
from time import sleep

y=(0.1)
subprocess.Popen(["python", 'rd1.py'])
sleep(y)
subprocess.Popen(["python", 'rs2.py'])
sleep(y)
subprocess.Popen(["python", 'timeled.py'])

