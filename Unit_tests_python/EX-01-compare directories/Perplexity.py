import os
import filecmp

def compare_directories(dir1, dir2):
    """
    Compare two directories and return a detailed report of the comparison as a dictionary.
    """
    report = {
        'Passed': True,
        'Failed_Count': 0,
        'Failed_Tests': []
    }
    
    # Compare the directories using filecmp
    cmp = filecmp.dircmp(dir1, dir2)
    
    # Compare files in dir1 and dir2
    for file in cmp.diff_files:
        report['Passed'] = False
        report['Failed_Count'] += 1
        report['Failed_Tests'].append({
            'Test': 'File Content',
            'Failed_Files': [file],
            'Failure_Location': 'both'
        })
    
    # Compare files only in dir1
    for file in cmp.left_only:
        report['Passed'] = False
        report['Failed_Count'] += 1
        report['Failed_Tests'].append({
            'Test': 'File Existence',
            'Failed_Files': [file],
            'Failure_Location': 'dir1'
        })
    
    # Compare files only in dir2
    for file in cmp.right_only:
        report['Passed'] = False
        report['Failed_Count'] += 1
        report['Failed_Tests'].append({
            'Test': 'File Existence',
            'Failed_Files': [file],
            'Failure_Location': 'dir2'
        })
    
    # Compare files with different modification times
    for file in cmp.diff_files:
        report['Passed'] = False
        report['Failed_Count'] += 1
        report['Failed_Tests'].append({
            'Test': 'File Modification Time',
            'Failed_Files': [file],
            'Failure_Location': 'both'
        })
    
    return report