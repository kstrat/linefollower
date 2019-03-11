import subprocess

def moskau_pi.mp3 (path):
    subprocess.Popen(['mpg123', '-q', path]).wait()
