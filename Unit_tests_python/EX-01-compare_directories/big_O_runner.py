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

def run_big_o(implementation, name, results_file_path):
    filepath = Path(__file__).parent / results_file_path
    if not os.path.isfile(filepath):
        print(f"Error: The file {filepath} does not exist.")
        return
    try:
        data_generator = config.generate_big_o_test_folders_n()
        dir1, dir2 = config.get_folders_paths()
        best,others = big_o.big_o(lambda arr:implementation(dir1,dir2), data_generator=data_generator,min_n=100, max_n=10000, n_repeats=20)
        with open(results_file_path, 'a') as file:
            print(f'Best class that fits for {name}: {best}')
            file.write(f'Best class that fits for {name}: {best}\n')
            for class_, residuals in others.items():
                print(f'{class_}: {residuals}')
                file.write(f'{class_}: {residuals}\n')
            file.write('-'*80 + "\n")

    except Exception as e:
        print(f"An error occurred while running big_o: {e}")