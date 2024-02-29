from pathlib import Path
import os
import config
from utils import reset_file
from big_O_runner import run_big_o

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_file_path = os.path.join(script_dir, 'big_o_results.txt')
    reset_file(results_file_path)

    for impl, name in config.implementations:
        run_big_o(impl, name, results_file_path, config.list1, config.list2, config.list3)

if __name__ == "__main__":
    main()