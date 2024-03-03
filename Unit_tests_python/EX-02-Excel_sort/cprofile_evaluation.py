# external imports
import os,config,utils
from pathlib import Path
from time import perf_counter

# Warm-up phase function
def warm_up(implementation,excel_file):
    """Run a few iterations to warm up the system."""
    for _ in range(5):  # Run each implementation 5 times as a warm-up
        try:
            implementation(excel_file, 0)
        except Exception:
            pass  # Ignore errors during warm-up

# Timing and avg calculation function
def avg_execution_time(implementation, name, results_file_path, excel_file):
    filepath = Path(__file__).parent / results_file_path
    implementation_file = implementation.__code__.co_filename
    if not os.path.isfile(implementation_file):
        print(f"Error: The file {implementation_file} does not exist.")
        return
    times = []  # Store individual run times for each iteration
    # Warm-up phase
    warm_up(implementation,excel_file)
    
    for i in [100]:
        times = []
        times_executed = 0
        for j in range(i):
            start = perf_counter()
            try:
                implementation(excel_file, 0)
                times_executed += 1
            except Exception:
                continue  # Skip to the next iteration on error
            end = perf_counter()
            times.append(end - start)
        if times_executed > 0:
            # Calculate the average execution time for the current number of iterations
            avg_execution_time_ms = sum(times) / times_executed * 1000
            # Round to 6 decimal places
            avg_execution_time_ms = round(avg_execution_time_ms, 6)
            text = f'{name} executed in an average of {avg_execution_time_ms} ms for {i} iterations'
            utils.append_to_file(filepath, text)
        else:
            text = f'{name} failed to execute for {i} iterations'
            utils.append_to_file(filepath, text)

    # Print the results
    utils.print_file(filepath)
def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    results_file_path = os.path.join(script_dir, 'cprofile_results.txt')
    utils.reset_file(results_file_path)
    excel_file= config.generate_random_excel_file()
    implementations = config.get_implementations()
    for impl, name in implementations:
        avg_execution_time(impl, name, results_file_path,excel_file)

if __name__ == "__main__":
    main()