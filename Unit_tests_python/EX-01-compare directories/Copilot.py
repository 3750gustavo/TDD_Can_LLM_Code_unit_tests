import os
import datetime

def compare_directories(dir1, dir2):
    file_counts = {}
    failed_tests = []
    
    # Iterate over files in dir1
    for root, dirs, files in os.walk(dir1):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            
            # Count occurrences of file names
            if file_name in file_counts:
                file_counts[file_name] += 1
            else:
                file_counts[file_name] = 1
    
    # Iterate over files in dir2
    for root, dirs, files in os.walk(dir2):
        for file in files:
            file_path = os.path.join(root, file)
            file_name = os.path.basename(file_path)
            
            # Count occurrences of file names
            if file_name in file_counts:
                file_counts[file_name] += 1
            else:
                file_counts[file_name] = 1
    
    # Compare modification dates of files found in both directories
    for file_name, count in file_counts.items():
        if count == 2:
            file_path1 = os.path.join(dir1, file_name)
            file_path2 = os.path.join(dir2, file_name)
            
            mod_time1 = os.path.getmtime(file_path1)
            mod_time2 = os.path.getmtime(file_path2)
            
            if mod_time1 != mod_time2:
                failed_tests.append((file_name, file_path1, file_path2))
    
    # Display results
    if len(failed_tests) == 0:
        print("OK - All files passed the tests.")
    else:
        print(f"{len(failed_tests)} files failed the tests:")
        for file_name, file_path1, file_path2 in failed_tests:
            print(f"File: {file_name}, Failed in: {file_path1}, {file_path2}")

# Example usage
compare_directories("/path/to/dir1", "/path/to/dir2")