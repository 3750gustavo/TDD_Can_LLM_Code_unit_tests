import os

def compare_directories(dir1, dir2):
   """Compares two directories and returns a detailed report of the comparison."""

   report = {
       "Passed": True,
       "Failed_Count": 0,
       "Failed_Tests": []
   }

   # Get files from both directories
   dir1_files = set(os.listdir(dir1))
   dir2_files = set(os.listdir(dir2))

   # Check for files existing in one directory but not the other
   missing_files = dir1_files.symmetric_difference(dir2_files)
   if missing_files:
       report["Passed"] = False
       report["Failed_Count"] += 1
       report["Failed_Tests"].append({
           "Failed_Files": list(missing_files),
           "Failure_Location": "Both"  # Files missing in both directories
       })

   # Compare files with the same name in both directories
   common_files = dir1_files.intersection(dir2_files)
   for filename in common_files:
       filepath1 = os.path.join(dir1, filename)
       filepath2 = os.path.join(dir2, filename)

       # Check for content differences
       if not filecmp.cmp(filepath1, filepath2, shallow=False):
           report["Passed"] = False
           report["Failed_Count"] += 1
           report["Failed_Tests"].append({
               "Failed_Files": [filename],
               "Failure_Location": "Both"  # Content difference
           })

       # Check for modification date differences (considering sub-second precision)
       mtime1 = os.path.getmtime(filepath1)
       mtime2 = os.path.getmtime(filepath2)
       if mtime1 != mtime2:
           report["Passed"] = False
           report["Failed_Count"] += 1
           failure_location = "dir1" if mtime1 < mtime2 else "dir2"
           report["Failed_Tests"].append({
               "Failed_Files": [filename],
               "Failure_Location": failure_location
           })

   return report