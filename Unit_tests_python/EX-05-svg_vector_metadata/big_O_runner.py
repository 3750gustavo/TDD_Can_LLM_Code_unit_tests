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
        svg_gen = config.svg_generator()
        best, others = big_o.big_o(implementation, data_generator=svg_gen, n_repeats=100)
        with open(results_file_path, 'a') as file:
            print(f'Best class that fits for {name}: {best}')
            file.write(f'Best class that fits for {name}: {best}\n')
            for class_, residuals in others.items():
                print(f'{class_}: {residuals}')
                file.write(f'{class_}: {residuals}\n')
            file.write('-'*80 + "\n")
        config.cleanup_temp_svg()
    except Exception as e:
        config.cleanup_temp_svg()
        print(f"An error occurred while running big_o: {e}")