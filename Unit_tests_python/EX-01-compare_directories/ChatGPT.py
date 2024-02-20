import os
import filecmp

def compare_directories(dir1, dir2):
    """
    Compare two directories and generate a detailed report of the comparison.

    Args:
        dir1 (str): Path to the first directory.
        dir2 (str): Path to the second directory.

    Returns:
        dict: A dictionary containing the detailed comparison report.
    """

    def compare_files(file1, file2):
        """
        Compare two files and return True if they are identical, False otherwise.
        """
        return filecmp.cmp(file1, file2)

    def list_files(directory):
        """
        List all files in a directory.
        """
        return [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    def compare_directories_recursively(dir1, dir2, report):
        """
        Recursively compare two directories and update the report.
        """
        for item in os.listdir(dir1):
            full_path1 = os.path.join(dir1, item)
            full_path2 = os.path.join(dir2, item)

            if os.path.isfile(full_path1) and os.path.isfile(full_path2):
                if not compare_files(full_path1, full_path2):
                    report['Failed_Count'] += 1
                    report['Failed_Tests'].append({
                        'Test': 'Content',
                        'Failed_Files': [item],
                        'Failure_Location': 'both'
                    })
            elif os.path.isfile(full_path1) and not os.path.isfile(full_path2):
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Test': 'Existence',
                    'Failed_Files': [item],
                    'Failure_Location': 'dir2'
                })
            elif not os.path.isfile(full_path1) and os.path.isfile(full_path2):
                report['Failed_Count'] += 1
                report['Failed_Tests'].append({
                    'Test': 'Existence',
                    'Failed_Files': [item],
                    'Failure_Location': 'dir1'
                })
            elif os.path.isdir(full_path1) and os.path.isdir(full_path2):
                compare_directories_recursively(full_path1, full_path2, report)

    report = {
        'Passed': True,
        'Failed_Count': 0,
        'Failed_Tests': []
    }

    compare_directories_recursively(dir1, dir2, report)

    report['Passed'] = report['Failed_Count'] == 0

    return report