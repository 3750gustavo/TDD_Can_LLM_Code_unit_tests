import os
from datetime import datetime

def compare_directories(dir1, dir2):
  """
  Compares two directories and returns a detailed report as a dictionary.

  Args:
      dir1: Path to the first directory.
      dir2: Path to the second directory.

  Returns:
      A dictionary containing the comparison report.
  """

  report = {
      "Passed": True,
      "Failed_Count": 0,
      "Failed_Tests": [],
  }

  # Get all files in each directory
  dir1_files = {f: os.path.getmtime(os.path.join(dir1, f)) for f in os.listdir(dir1)}
  dir2_files = {f: os.path.getmtime(os.path.join(dir2, f)) for f in os.listdir(dir2)}

  # Check for missing files
  missing_files = set(dir1_files.keys()) ^ set(dir2_files.keys())
  if missing_files:
    report["Passed"] = False
    report["Failed_Count"] += 1
    failure_location = "dir1" if dir1_files else "dir2"
    report["Failed_Tests"].append({
      "Failed_Files": list(missing_files),
      "Failure_Location": failure_location,
    })

  # Compare existing files by modification date
  for filename, mtime1 in dir1_files.items():
    if filename in dir2_files:
      mtime2 = dir2_files[filename]
      if mtime1 != mtime2:
        report["Passed"] = False
        report["Failed_Count"] += 1
        failure_location = "dir1" if mtime1 < mtime2 else "dir2"
        report["Failed_Tests"].append({
          "Failed_Files": [filename],
          "Failure_Location": failure_location,
        })

  return report

# Example usage
report = compare_directories("/path/to/dir1", "/path/to/dir2")
print(report)