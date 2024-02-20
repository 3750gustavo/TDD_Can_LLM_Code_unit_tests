import os
from pathlib import Path
from collections import Counter

def compare_directories(dir1, dir2, comparison_type='list'):
    """Compare files between two directories based on given type of comparison.

    Args:
        dir1 (str): First directory path.
        dir2 (str): Second directory path.
        comparison_type ('list', 'dict', 'tuple') : Type of comparison. Defaults to 'list'.
             - 'list': Compare by filename only.
             - 'dict': Compare by full path and filename.
             - 'tuple': Compare by filename and modification time.

    Raises:
        ValueError: If comparison_type not in ['list', 'dict', 'tuple'].
        
    Returns:
        dict: Resulting report containing number of successful comparisons, failures per test, and failing filenames.
    """
    
    # Check validity of comparison_type
    if comparison_type not in {'list', 'dict', 'tuple'}:
        raise ValueError("Invalid comparison_type. Must be either 'list', 'dict', or 'tuple'.")

    # Get lists of files from both directories
    files_in_dir1 = [f.name for f in Path(dir1).iterdir() if f.is_file()]
    files_in_dir2 = [f.name for f in Path(dir2).iterdir() if f.is_file()]

    # Count occurrences of files across directories
    count_map = {}
    if comparison_type == 'list':
        count_map = Counter([x for x in files_in_dir1 if x in files_in_dir2])
    elif comparison_type == 'dict':
        count_map = {os.path.join(Path(dir1).resolve(), f): files_in_dir1.count(f) for f in set(files_in_dir1)} \
                    | {os.path.join(Path(dir2).resolve(), f): files_in_dir2.count(f) for f in set(files_in_dir2)}
    else:
        count_map = {f: len(list(filter(lambda d: f in d, ([Path(dir1).resolve().glob('*'+f+'.*'), Path(dir2).resolve().glob('*'+f+'.*')])))) for f in set(files_in_dir1 & set(files_in_dir2))}

    # Find files occurring twice
    twice_occurring = {k: v for k, v in count_map.items() if v > 1}

    # Compare modification times for those files
    if comparison_type == 'tuple':
        results = {}
        for file_name, occurence_count in twice_occurring.items():
            try:
                mtime1 = min((p.stat().st_mtime for p in Path(dir1).rglob(file_name)), key=lambda t: t)[0].timestamp()
                mtime2 = min((p.stat().st_mtime for p in Path(dir2).rglob(file_name)), key=lambda t: t)[0].timestamp()
                if abs(mtime1 - mtime2) < 5 * 60:  # Allow up to 5 minutes difference
                    results[file_name] = 'OK'
                else:
                    results[file_name] = 'Failed due to different modification times.'
            except FileNotFoundError:
                results[file_name] = 'Failed because file does not exist in at least one directory.'
        return {
            'successful_comparisons': sum(v <= 1 for _, v in count_map.items()),
            'failed_by_duplicate': len(twice_occurring),
            'results': {key: value for key, value in results.items() if value != 'OK'}
        }

    # Return basic statistics without comparing modification times
    else:
        return {
            'successful_comparisons': sum(v <= 1 for _, v in count_map.items()),
            'failed_by_duplicate': len(twice_occurring),
            'results': {key: 'Failed' for key, _ in twice_occurring.items()}
        }