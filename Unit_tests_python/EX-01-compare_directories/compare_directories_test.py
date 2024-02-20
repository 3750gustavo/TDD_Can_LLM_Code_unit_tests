import pytest
import os
import datetime

# Import implementations
from Perplexity import compare_directories as Perplexity
from Copilot import compare_directories as Copilot
from ChatGPT import compare_directories as ChatGPT

# Define the implementations with their names
implementations = [
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot'),
    (ChatGPT, 'ChatGPT')
]

# Folders paths
dir1 = os.path.join(os.getcwd(), 'test_folder1')
dir2 = os.path.join(os.getcwd(), 'test_folder2')

# Ensure the folders exist
for directory in [dir1, dir2]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to set the modification date of a file
def set_date(file_path,date=datetime.datetime(2021, 1, 1)):
    os.utime(file_path, (date.timestamp(), date.timestamp()))

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
            set_date(file_path)

# Function to create files in the folders with some differences
def create_files_with_differences():
    # Create two files with the same content and modification date in both folders
    for i in range(2):
        file_content = f'This is file {i} content'
        modification_time = datetime.datetime(2021, 1, 1)
        for directory in [dir1, dir2]:
            file_path = os.path.join(directory, f'file{i}.txt')
            with open(file_path, 'w') as file:
                file.write(file_content)
            # Set modification date to 2021-01-01
            set_date(file_path)
    # Create two files with same content but different modification date in both folders (current date in dir2)
    for i in range(2, 4):
        # same content for both files
        file_content = f'This is file {i} content'
        # base modification date
        modification_time = datetime.datetime(2021, 1, 1)
        # create file in dir1
        file_path = os.path.join(dir1, f'file{i}.txt')
        with open(file_path, 'w') as file:
            file.write(file_content)
        # Set modification date to 2021-01-01
        set_date(file_path)
        # create file in dir2
        file_path = os.path.join(dir2, f'file{i}.txt')
        with open(file_path, 'w') as file:
            file.write(file_content)
        
    # Create one additional file in dir2
    additional_file_content = "This is file 5 content"
    additional_file_path = os.path.join(dir2, 'file5.txt')
    with open(additional_file_path, 'w') as file:
        file.write(additional_file_content)
    # Set modification date to 2021-01-01
    set_date(additional_file_path)

# Function to delete all files from the folders
def delete_files():
    for directory in [dir1, dir2]:
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            os.remove(file_path)

# Expected result for the first test where all files have the same modification date
expected_result_all_same_date = {
    "Passed": True,
    "Failed_count": 0,
    "Failed_tests": []
}

# Expected result for the test where three files differ, but only two of them are in both folders
expected_result_with_differences = {
    "Passed": False,
    "Failed_count": 2,
    "Failed_tests": [
        {
            "Test": "File Existence",
            "Failed_Files": ["file0.txt", "file1.txt"],
            "Failure_Location": "both"
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