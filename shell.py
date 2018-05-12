import subprocess

def run(args):
    return subprocess.run(args, shell=True, check=True)
