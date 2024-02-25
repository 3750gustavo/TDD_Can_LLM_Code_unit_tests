import pytest
import os
from CodeLLama import display_text_file as CodeLLama
from ChatGPT import display_text_file as ChatGPT

# Define the implementations with their names
implementations = [
    (CodeLLama, 'CodeLLama'),
    (ChatGPT, 'ChatGPT')
]

# Test .txt file path
txt_file_path = os.path.join(os.path.dirname(__file__), "test.txt")

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

def test_display_text_file_success(implementation, tmp_path):
    # Create a temporary test file
    test_file = tmp_path / "test.txt"
    with open(test_file, 'w') as file:
        file.write("Name1: 10\nName2: 20\nName3: 15\n")
    
    # Call the function
    success = implementation(test_file)
    
    # Assert that the function returns True indicating success
    assert success == True, (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: True, got: {success}"
    )

def test_display_text_file_failure(implementation, tmp_path):
    # Create a temporary test file with invalid data
    test_file = tmp_path / "test.txt"
    with open(test_file, 'w') as file:
        file.write("Name1: 10\nInvalidLine\nName3: 15\n")
    
    # Call the function
    success = implementation(test_file)
    
    # Assert that the function returns False indicating failure
    assert success == False, (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: False, got: {success}"
    )

def test_display_text_file_sorting(implementation, tmp_path):
    """
    Test to verify that values are correctly sorted in descending order.
    """
    test_file = tmp_path / "test_sorting.txt"
    with open(test_file, 'w') as file:
        file.write("Name1: 1\nName2: 3\nName3: 2\n")

    success, sorted_data = implementation(test_file)
    expected_sorted_data = "Name2: 3\nName3: 2\nName1: 1\n"

    assert success == (True, "Function should successfully process the file") , (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: True, got: {success}"
    )
    assert sorted_data == (expected_sorted_data, "Values should be sorted in descending order"), (
        f"Test failed for {implementation.__name__}. "
        f"Expected sorted data: {expected_sorted_data}, got: {sorted_data}"
    )

def test_display_text_file_error_handling(implementation, tmp_path):
    """
    Test to verify that the function handles various error conditions appropriately.
    """
    # Test for file not found error
    non_existent_file = tmp_path / "non_existent.txt"
    success = implementation(non_existent_file)
    assert success == (False, "Function should return False for non-existent file"), (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: False, got: {success}"
    )
    # Additional error conditions like permission issues, empty file, etc., can be added here.

@pytest.mark.skip(reason="Requires GUI testing setup")
def test_display_text_file_gui_display(implementation, tmp_path):
    """
    Test to verify that the GUI correctly displays the names and sorted values.
    Note: This test is skipped by default as it requires a GUI testing setup.
    """
    # This is a placeholder for a GUI test. In a real scenario, this would involve
    # using a GUI testing framework or tool to interact with and verify the application's GUI.
    # For example, using the `pywinauto` library to interact with the GUI elements.

# Add more test cases as needed


# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-06-display_text_file_gui\display_text_file_gui_test.py