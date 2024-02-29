# main.py
from pathlib import Path
import os
from config import implementations
from utils import ensure_pylint_installed, reset_file
from pylint_runner import run_pylint

def main():
    ensure_pylint_installed()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_file_path = os.path.join(script_dir, 'pylint_results.txt')
    reset_file(results_file_path)
    for impl, name in implementations:
        run_pylint(impl, name, results_file_path)

if __name__ == "__main__":
    main()