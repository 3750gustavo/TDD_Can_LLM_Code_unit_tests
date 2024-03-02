# pylint_runner.py
import subprocess, os
from pathlib import Path

def run_pylint(implementation, name, results_file_path):
    implementation_file = implementation.__code__.co_filename
    if not os.path.isfile(implementation_file):
        print(f"Error: The file {implementation_file} does not exist.")
        return
    try:
        pylint_output = subprocess.run(['pylint', implementation_file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if pylint_output.stderr:
            print(f"Error running pylint on {name}:")
            print(pylint_output.stderr)
        else:
            print(f'PEP8 compliance score for {name}:')
            lines = pylint_output.stdout.split('\n')
            score_line = next((line for line in lines if 'Your code has been rated at' in line), None)
            if score_line:
                print(score_line)
            with open(results_file_path, 'a') as file:
                file.write(f'PEP8 compliance score and details for {name}:\n')
                file.write(pylint_output.stdout + "\n")
                file.write('-'*80 + "\n")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running pylint: {e}")