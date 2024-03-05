# external imports
import os,config,utils
from pathlib import Path
from time import perf_counter

# Wrapper functions for the implementations with Gui features removed
def Claude_wrapper(filepath):
    try:
        with open(filepath, 'r') as f:
            data = f.read()
        
        records = []
        for line in data.split('\n'):
            if ':' in line:
                name, value = line.split(':')
                records.append({'name': name, 'value': value})
        
        records.sort(key=lambda x: int(x['value']), reverse=True)
        
        test_filepath = os.path.join(os.getcwd(), 'test.txt')        
        with open(test_filepath, 'w') as f:
            for record in records:
                f.write(f"{record['name']}:{record['value']}\n")
        
        return len(records)
    
    except FileNotFoundError:
        print("Error: File not found") 
        return 0
    
    except:
        print("Error: Unable to process file")
        return 0
    
def ChatGPT_wrapper(filepath):
    try:
        # Check if the provided file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError("The provided file does not exist.")
        
        # Read the content of the provided .txt file
        with open(filepath, 'r') as file:
            lines = file.readlines()
        
        # Parse the data into name-value pairs
        data = []
        for line in lines:
            parts = line.strip().split(":")
            if len(parts) == 2:
                data.append({'name': parts[0], 'value': parts[1]})
        
        # Sort the list of dictionaries in descending order based on the 'value' key
        sorted_data = sorted(data, key=lambda x: x['value'], reverse=True)
        
        # Write sorted name-value pairs to a temporary .txt file
        temp_file_path = 'test.txt'
        with open(temp_file_path, 'w') as temp_file:
            for item in sorted_data:
                temp_file.write(f"{item['name']}:{item['value']}\n")
        
        return len(sorted_data)
    
    except FileNotFoundError:
        print("Error: File not found") 
        return 0
    
    except:
        print("Error: Unable to process file")
        return 0

def Bard_wrapper(filepath):
    try:
        with open(filepath, "r") as file:
            content = file.readlines()

        parsed_data = []
        for line in content:
            name, value = line.strip().split(":")
            parsed_data.append({"name": name, "value": value})

        parsed_data.sort(key=lambda item: item["value"], reverse=True)

        temp_file_path = "test.txt"
        with open(temp_file_path, "w") as temp_file:
            for item in parsed_data:
                temp_file.write(f"{item['name']}: {item['value']}\n")

        return len(parsed_data)

    except FileNotFoundError:
        print("Error: The specified file path does not exist.")
        return 0
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return 0

def CodeLLama_wrapper(filepath):
    try:
        # Check if the file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError("The provided file does not exist.")
        
        # Read the content of the file
        with open(filepath, 'r') as f:
            data = f.read()

        # Parse the data into name-value pairs
        name_value_pairs = []
        for line in data.splitlines():
            name, value = line.split(':')
            name_value_pairs.append({'name': name, 'value': value})

        # Sort the list of dictionaries in descending order based on the 'value' key
        sorted_name_value_pairs = sorted(name_value_pairs, key=lambda x: x['value'], reverse=True)

        # Check if a file named 'test.txt' already exists in the working directory
        if os.path.exists('test.txt'):
            # Overwrite the file with the sorted name-value pairs
            with open('test.txt', 'w') as f:
                for pair in sorted_name_value_pairs:
                    f.write(f"{pair['name']}: {pair['value']}\n")
        else:
            # Create a temporary .txt file named 'test.txt' with the sorted name-value pairs
            with open('test.txt', 'w') as f:
                for pair in sorted_name_value_pairs:
                    f.write(f"{pair['name']}: {pair['value']}\n")

        return len(sorted_name_value_pairs)

    except FileNotFoundError:
        print("Error: File not found") 
        return 0
    
    except:
        print("Error: Unable to process file")
        return 0

def Perplexity_wrapper(filepath):
  try:
    # Read the content of the provided .txt file
    with open(filepath, 'r') as file:
      content = file.read()

    # Utilize the delimiter ":" to parse the data within the file into name-value pairs with keys 'name' and 'value', respectively, as a list of dictionary variables
    name_value_pairs = []
    for line in content.split('\n'):
      if line.strip() != '':
        name, value = line.split(':')
        name_value_pairs.append({'name': name.strip(), 'value': int(value.strip())})

    # Sort the list of dictionaries in descending order based on the 'value' key
    sorted_name_value_pairs = sorted(name_value_pairs, key=lambda x: x['value'], reverse=True)
     
    return len(sorted_name_value_pairs)
   
  except FileNotFoundError:
    print("Error: File not found") 
    return 0
   
  except:
    print("Error: Unable to process file")
    return 0

def Copilot_wrapper(filepath):
  try:
    # Read the content of the provided .txt file
    with open(filepath, 'r') as file:
      content = file.read()

    # Utilize the delimiter ":" to parse the data into name-value pairs
    name_value_pairs = []
    lines = content.split('\n')
    for line in lines:
      if ':' in line:
        name, value = line.split(':')
        name_value_pairs.append({'name': name.strip(), 'value': value.strip()})

    # Sort the list of dictionaries in descending order based on the 'value' key
    sorted_pairs = sorted(name_value_pairs, key=lambda x: x['value'], reverse=True)
   
    return len(sorted_pairs)
  
  except FileNotFoundError:
    print("Error: File not found") 
    return 0
  
  except:
    print("Error: Unable to process file")
    return 0

# Define the wrappers for GUI-based implementations
wrappers = {
    "Claude": Claude_wrapper,
    "ChatGPT": ChatGPT_wrapper,
    "Bard": Bard_wrapper,
    "CodeLLama": CodeLLama_wrapper,
    "Perplexity": Perplexity_wrapper,
    "Copilot": Copilot_wrapper
}

# Warm-up phase function
def warm_up(implementation):
    """Run a few iterations to warm up the system."""
    for _ in range(5):  # Run each implementation 5 times as a warm-up
        try:
            implementation(config.get_txt_file_path())
        except Exception:
            pass  # Ignore errors during warm-up

# Timing and avg calculation function
def avg_execution_time(implementation, name, results_file_path):
    filepath = Path(__file__).parent / results_file_path
    implementation_file = implementation.__code__.co_filename
    if not os.path.isfile(implementation_file):
        print(f"Error: The file {implementation_file} does not exist.")
        return
    # Use the wrapper function for GUI-based implementations
    func = wrappers.get(name, implementation)
    times = []  # Store individual run times for each iteration
    warm_up(func)

    # Measure the execution time for different numbers of iterations
    for i in [50000]:
        times = []
        times_executed = 0
        for j in range(i):
            start = perf_counter()
            try:
                func(config.get_txt_file_path())
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
    implementations = config.get_implementations()
    config.setup_txt_file()
    # make text file bigger
    generator = config.txt_file_generator()
    generator(1000)
    for impl, name in implementations:
        avg_execution_time(impl, name, results_file_path)

if __name__ == "__main__":
    main()