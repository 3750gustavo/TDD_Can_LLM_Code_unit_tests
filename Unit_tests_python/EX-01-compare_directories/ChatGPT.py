import os
import filecmp

def compare_directories(dir1, dir2):
    report = {
        "Passed": True,
        "Failed_Count": 0,
        "Failed_Tests": []
    }

    def compare_files(file1, file2):
        return os.path.getmtime(file1) > os.path.getmtime(file2)

    def compare_directories_recursive(dir1, dir2):
        nonlocal report
        dir_comparison = filecmp.dircmp(dir1, dir2)

        for file in dir_comparison.diff_files:
            file1 = os.path.join(dir1, file)
            file2 = os.path.join(dir2, file)
            if compare_files(file1, file2):
                report["Passed"] = False
                report["Failed_Count"] += 1
                report["Failed_Tests"].append({
                    "Test": "File Modification Time",
                    "Failed_Files": [file],
                    "Failure_Location": "dir1"
                })
            else:
                report["Passed"] = False
                report["Failed_Count"] += 1
                report["Failed_Tests"].append({
                    "Test": "File Modification Time",
                    "Failed_Files": [file],
                    "Failure_Location": "dir2"
                })

        for subdir in dir_comparison.common_dirs:
            compare_directories_recursive(os.path.join(dir1, subdir), os.path.join(dir2, subdir))

    compare_directories_recursive(dir1, dir2)

    return report