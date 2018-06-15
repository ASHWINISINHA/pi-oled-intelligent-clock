import subprocess
from time import sleep

y=(0.1)
subprocess.Popen(["python", 'rd1.py'])
sleep(y)
subprocess.Popen(["python", 'rs1.py'])
sleep(y)
subprocess.Popen(["python", 'rl1.py'])
