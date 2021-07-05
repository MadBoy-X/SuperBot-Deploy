import os 
import subprocess
os.system("git clone https://github.com/MadBoy-X/SuperBot superbot")
os.chdir("superbot")
os.system("pip install aria2p")
os.system("/usr/local/bin/python -m pip install --upgrade pip")
process = subprocess.Popen(
        ["python3", "-m", "SuperBot"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,)
out, er = process.communicate()
if er:
    print(er.decode())
print("::::::::::::::")
if out:
    print(out.decode())
