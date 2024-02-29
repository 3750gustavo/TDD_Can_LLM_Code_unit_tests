# big_O_runner.py
import subprocess, os
from pathlib import Path
import config
# try to import big_o, if it fails, install it
try:
    import big_o
except ImportError:
    subprocess.run(['pip', 'install', 'big_o'])
    import big_o

def run_big_o(implementation, name, results_file_path, list1, list2, list3):
    filepath = Path(__file__).parent / results_file_path
    if not os.path.isfile(filepath):
        print(f"Error: The file {filepath} does not exist.")
        return
    try:
        best,others = big_o.big_o(implementation, min_n=1000, max_n=100000, n_measures=10)
        with open(results_file_path, 'a') as file:
            file.write(f'Big O complexity for {name}:\n')
            file.write(f'Best: {best}\n')
            file.write(f'Others: {others}\n')
            file.write('-'*80 + "\n")
    except Exception:
        text = f'{name} failed to execute'
        with open(results_file_path, 'a') as file:
            file.write(text + "\n")