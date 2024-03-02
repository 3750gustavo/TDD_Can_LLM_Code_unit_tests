# utils.py
import subprocess

def ensure_pylint_installed():
    try:
        subprocess.run(['pylint', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("Pylint is not installed. Installing now...")
        subprocess.run(['pip', 'install', 'pylint'], check=True)

def reset_file(filepath):
    with open(filepath, 'w') as file:
        file.write("")

def append_to_file(filepath, text):
    with open(filepath, 'a') as file:
        file.write(text + "\n")

def print_file(filepath):
    with open(filepath, 'r') as file:
        print(file.read())