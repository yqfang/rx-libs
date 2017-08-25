import subprocess
import time

def f():
    p = subprocess.Popen(["/Users/yqfang/.pyenv/versions/2.6.9/bin/python", "10s_process.py"])
    while p.poll() is None:
        # print('Still running')
        time.sleep(1)
    print("end")