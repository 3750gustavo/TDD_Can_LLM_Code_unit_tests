import os
import time

def compare_directories(dir1, dir2):
    # Initialize the report dictionary
    report = {
        'Passed': True,
        'Failed_Count': 0,
        'Failed_Tests': []
    }

    # Get the list of files in both directories
    files1 = os.listdir(dir1)
    files2 = os.listdir(dir2)

    # Iterate over the files in both directories
    for file1, file2 in zip(files1, files2):
        # Get the modification times for the files
        mod_time1 = os.path.getmtime(os.path.join(dir1, file1))
        mod_time2 = os.path.getmtime(os.path.join(dir2, file2))

        # Check if the files have the same modification time
        if mod_time1 != mod_time2:
            # If the files have different modification times, add a failed test to the report
            report['Failed_Count'] += 1
            report['Failed_Tests'].append({
                'Test': 'Modification Time',
                'Failed_Files': [file1, file2],
                'Failure_Location': 'dir1' if mod_time1 < mod_time2 else 'dir2'
            })

    # Check if any files are missing from one of the directories
    missing_files = set(files1).symmetric_difference(files2)
    if missing_files:
        # If there are missing files, add a failed test to the report
        report['Failed_Count'] += 1
        report['Failed_Tests'].append({
            'Test': 'Missing Files',
            'Failed_Files': list(missing_files),
            'Failure_Location': 'dir1' if len(missing_files) > 0 else 'dir2'
        })

    # Check if any files have different content
    for file1, file2 in zip(files1, files2):
        # Get the contents of the files
        with open(os.path.join(dir1, file1), 'r') as f1, open(os.path.join(dir2, file2), 'r') as f2:
            content1 = f1.read()
            content2 = f2.read()

        # Check if the contents of the files are the same
        if content1 != content2:
            # If the contents of the files are different, add a failed test to the report
            report['Failed_Count'] += 1
            report['Failed_Tests'].append({
                'Test': 'Content',
                'Failed_Files': [file1, file2],
                'Failure_Location': 'dir1' if content1 < content2 else 'dir2'
            })

    # Return the report
    return report