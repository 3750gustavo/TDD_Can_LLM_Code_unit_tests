import pytest
import os
import datetime

# Import implementations
from Perplexity import compare_directories as Perplexity
from Copilot import compare_directories as Copilot

# Define the implementations with their names
implementations = [
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot')
]

# Folders paths
dir1 = os.path.join(os.getcwd(), 'test_folder1')
dir2 = os.path.join(os.getcwd(), 'test_folder2')

# Ensure the folders exist
for directory in [dir1, dir2]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to create files in the folders, all with the same modification dates of 2021-01-01
def create_files_all_same_date():
    for i in range(5):
        file_content = f'This is file {i} content'
        modification_time = datetime.datetime(2021, 1, 1)
        for directory in [dir1, dir2]:
            file_path = os.path.join(directory, f'file{i}.txt')
            with open(file_path, 'w') as file:
                file.write(file_content)
            # Set modification date to 2021-01-01
            os.utime(file_path, (modification_time.timestamp(), modification_time.timestamp()))

# Function to create files in the folders with some differences
def create_files_with_differences():
    for i in range(3):
        file_content = f'This is file {i} content'
        modification_time = datetime.datetime(2021, 1, 1)
        for directory in [dir1, dir2]:
            file_path = os.path.join(directory, f'file{i}.txt')
            with open(file_path, 'w') as file:
                file.write(file_content)
            # Set modification date to 2021-01-01
            os.utime(file_path, (modification_time.timestamp(), modification_time.timestamp()))
    
    # Create one additional file in dir2
    additional_file_content = "This is an additional file content"
    additional_file_path = os.path.join(dir2, 'file3.txt')
    with open(additional_file_path, 'w') as file:
        file.write(additional_file_content)
    # Set modification date to 2021-01-01
    os.utime(additional_file_path, (modification_time.timestamp(), modification_time.timestamp()))

# Function to delete all files from the folders
def delete_files():
    for directory in [dir1, dir2]:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)

# Expected result for the first test where all files have the same modification date
expected_result_all_same_date = {
    "passed": True,
    "failed_count": 0,
    "failed_tests": []
}

# Expected result for the test where three files differ, but only two of them are in both folders
expected_result_with_differences = {
    "passed": False,
    "failed_count": 2,
    "failed_tests": [
        {
            "test": "File Existence",
            "failed_files": ["file0.txt", "file1.txt"],
            "failure_location": "both"
        }
    ]
}

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

@pytest.fixture
def setup_files(request):
    create_files_all_same_date()
    request.addfinalizer(delete_files)

@pytest.fixture
def setup_files_with_differences(request):
    create_files_with_differences()
    request.addfinalizer(delete_files)

# Tests
def test_all_same_date(implementation, setup_files):
    result = implementation(dir1, dir2)
    assert result == expected_result_all_same_date

def test_with_differences(implementation, setup_files_with_differences):
    result = implementation(dir1, dir2)
    assert result == expected_result_with_differences

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-01-compare_directories\compare_directories_test.py