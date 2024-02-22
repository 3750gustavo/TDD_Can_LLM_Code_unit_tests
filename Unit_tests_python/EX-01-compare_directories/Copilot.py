import os
import filecmp

def compare_directories(dir1, dir2):
    report = {
        'Passed': True,
        'Failed_Count': 0,
        'Failed_Tests': []
    }

    for root, dirs, files in os.walk(dir1):
        for file in files:
            file_path1 = os.path.join(root, file)
            file_path2 = os.path.join(dir2, os.path.relpath(file_path1, dir1))

            if not os.path.exists(file_path2):
                report['Passed'] = False
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Test': 'File Missing',
                    'Failed_Files': [file],
                    'Failure_Location': 'dir2'
                })
            elif not filecmp.cmp(file_path1, file_path2):
                report['Passed'] = False
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Test': 'File Content Mismatch',
                    'Failed_Files': [file],
                    'Failure_Location': 'dir1' if os.path.getmtime(file_path1) < os.path.getmtime(file_path2) else 'dir2'
                })

    return report