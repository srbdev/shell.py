import subprocess

def run(s):
    return subprocess.run(s, check=True, shell=True)
