import os

def compare_directories(dir1, dir2):
    report = {
        'Passed': True,
        'Failed_Count': 0,
        'Failed_Tests': []
    }

    for root, dirs, files in os.walk(dir1):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, dir1)
            file_path2 = os.path.join(dir2, relative_path)

            if not os.path.exists(file_path2):
                report['Passed'] = False
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Test': 'File exists in dir1 but not in dir2',
                    'Failed_Files': [file_path],
                    'Failure_Location': 'dir1'
                })
            else:
                if os.path.getmtime(file_path) != os.path.getmtime(file_path2):
                    report['Passed'] = False
                    report['Failed_Count'] += 1
                    report['Failed_Tests'].append({
                        'Test': 'File modified time differs',
                        'Failed_Files': [file_path, file_path2],
                        'Failure_Location': 'both'
                    })
                if os.path.getsize(file_path) != os.path.getsize(file_path2):
                    report['Passed'] = False
                    report['Failed_Count'] += 1
                    report['Failed_Tests'].append({
                        'Test': 'File size differs',
                        'Failed_Files': [file_path, file_path2],
                        'Failure_Location': 'both'
                    })

    for root, dirs, files in os.walk(dir2):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, dir2)
            file_path1 = os.path.join(dir1, relative_path)

            if not os.path.exists(file_path1):
                report['Passed'] = False
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Test': 'File exists in dir2 but not in dir1',
                    'Failed_Files': [file_path],
                    'Failure_Location': 'dir2'
                })

    return report