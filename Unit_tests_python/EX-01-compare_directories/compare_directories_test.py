import pytest
import os
import datetime

# Import implementations
from Copilot import compare_directories as Copilot
from ChatGPT import compare_directories as ChatGPT
from CodeLLama import compare_directories as CodeLLama

# Define the implementations with their names
implementations = [
    (Copilot, 'Copilot'),
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama')
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
    "Failed_Count": 0,
    "Failed_Tests": []
}

# Expected result for the test where three files differ, but only two of them are in both folders
expected_result_with_differences = {
    "Passed": False,
    "Failed_Count": 2,
    "Failed_Tests": [
        {
            "Failed_Files": ["file2.txt", "file3.txt"],
            "Failure_Location": "dir2"
        }
    ]
}

def assert_test_results(result, expected_result, implementation_name):
    # First two keys are simple and can be checked directly
    assert result["Passed"] == expected_result["Passed"], (
        f"Test failed for {implementation_name}. "
        f"Expected Passed: {expected_result['Passed']}, got: {result['Passed']}"
    )
    assert result["Failed_Count"] == expected_result["Failed_Count"], (
        f"Test failed for {implementation_name}. "
        f"Expected Failed_Count: {expected_result['Failed_Count']}, got: {result['Failed_Count']}"
    )
    # If expected_result has a empty list [] for Failed_Tests, just do a normal assertion
    if expected_result["Failed_Tests"] == []:
        assert result["Failed_Tests"] == expected_result["Failed_Tests"], (
            f"Test failed for {implementation_name}. "
            f"Expected Failed_Tests: {expected_result['Failed_Tests']}, got: {result['Failed_Tests']}"
        )
    # If there is a list, check each entry for the expected keys
    else:
        for i, failed_test in enumerate(expected_result["Failed_Tests"]):
            assert result["Failed_Tests"][i]["Failed_Files"] == failed_test["Failed_Files"], (
                f"Test failed for {implementation_name}. "
                f"Expected Failed_Files: {failed_test['Failed_Files']}, got: {result['Failed_Tests'][i]['Failed_Files']}"
            )
            assert result["Failed_Tests"][i]["Failure_Location"] == failed_test["Failure_Location"], (
                f"Test failed for {implementation_name}. "
                f"Expected Failure_Location: {failed_test['Failure_Location']}, got: {result['Failed_Tests'][i]['Failure_Location']}"
            )

# Define the fixture for the implementations
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

def test_all_same_date(implementation, setup_files):
    try:
        result = implementation(dir1, dir2)
        assert_test_results(result, expected_result_all_same_date, implementation.__name__)
    except AssertionError as ae:
        print(f"Test failed for {implementation.__name__}. Output result: {result}")
        raise ae
    except Exception as e:
        pytest.fail(f"An error occurred during testing: {str(e)}")

def test_with_differences(implementation, setup_files_with_differences):
    try:
        result = implementation(dir1, dir2)
        assert_test_results(result, expected_result_with_differences, implementation.__name__)
    except AssertionError as ae:
        print(f"Test failed for {implementation.__name__}. Output result: {result}")
        raise ae
    except Exception as e:
        pytest.fail(f"An error occurred during testing: {str(e)}")

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-01-compare_directories\compare_directories_test.py