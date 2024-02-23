import os
from datetime import datetime

def compare_directories(dir1, dir2):
    
    report = {
        'Passed': True,
        'Failed_Count': 0,
        'Failed_Tests': []
    }
    
    for root, dirs, files in os.walk(dir1):
        for file in files:
            file1 = os.path.join(root, file)
            file2 = os.path.join(dir2, file)
            
            if not os.path.exists(file2):
                report['Passed'] = False
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Failed_Files': [file],
                    'Failure_Location': 'dir2' 
                })
                
            else:
                stat1 = os.stat(file1)
                stat2 = os.stat(file2)
                
                if stat1.st_mtime < stat2.st_mtime:
                    failure_location = 'dir1'
                else:
                    failure_location = 'dir2'
                    
                if stat1.st_size != stat2.st_size:
                    report['Passed'] = False
                    report['Failed_Count'] += 1
                    report['Failed_Tests'].append({
                        'Failed_Files': [file],
                        'Failure_Location': failure_location
                    })
                
    return report