import os
from datetime import timedelta
from typing import Dict, List

def compare_directories(dir1: str, dir2: str) -> Dict[str, Union[bool, int, List[Dict]]]:
    result = {
        "Passed": True,
        "Failed_Count": 0,
        "Failed_Tests": []
    }
    
    # Check if both paths exist and are valid directories
    if not os.path.isdir(dir1) or not os.path.isdir(dir2):
        result["Passed"] = False
        return result

    # Get lists of files in each directory
    files_in_dir1 = [f for f in os.listdir(dir1) if os.path.isfile(os.path.join(dir1, f))]
    files_in_dir2 = [f for f in os.listdir(dir2) if os.path.isfile(os.path.join(dir2, f))]

    # Compare file counts
    if len(files_in_dir1) != len(files_in_dir2):
        result["Passed"] = False
        result["Failed_Tests"].append({"Test": "File Count Mismatch", "Failed_Files": sorted([x for x in set(files_in_dir1).union(set(files_in_dir2)) if x not in set(files_in_dir1 & files_in_dir2)]), "Failure_Location": "both"})
        
    else:
        # Compare file contents and last modified times
        for filename in set(files_in_dir1).intersection(set(files_in_dir2)):
            file1_path = os.path.join(dir1, filename)
            file2_path = os.path.join(dir2, filename)
            
            try:
                mtime1 = os.stat(file1_path).st_mtime
                mtime2 = os.stat(file2_path).st_mtime
                
                if os.path.getsize(file1_path) != os.path.getsize(file2_path) or abs((timedelta(seconds=mtime2 - mtime1)).total_seconds()) > 60 * 5:  # 5 minutes difference considered significant
                    result["Passed"] = False
                    result["Failed_Tests"].append({"Test": "Content or Last Modified Time Mismatch", "Failed_Files": [filename], "Failure_Location": ("dir1" if mtime1 < mtime2 else "dir2")})
                    break
            except FileNotFoundError:
                result["Passed"] = False
                result["Failed_Tests"].append({"Test": "Missing File", "Failed_Files": [filename], "Failure_Location": "both"})
                break

    result["Failed_Count"] = len(result["Failed_Tests"])
    return result