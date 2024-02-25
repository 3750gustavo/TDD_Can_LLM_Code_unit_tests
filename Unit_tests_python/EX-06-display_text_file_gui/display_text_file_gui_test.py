import pytest
import os
from CodeLLama import display_text_file as CodeLLama
from ChatGPT import display_text_file as ChatGPT
from Bard import display_text_file as Bard
from Claude import display_text_file as Claude
from Perplexity import display_text_file as Perplexity
from Copilot import display_text_file as Copilot

# Define the implementations with their names
implementations = [
    (CodeLLama, 'CodeLLama'),
    (ChatGPT, 'ChatGPT'),
    (Bard, 'Bard'),
    (Claude, 'Claude'),
    (Perplexity, 'Perplexity'),
    (Copilot, 'Copilot')
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
        file.write("Leo: 10\nJoana: 20\nThomas: 15\n")
    
    # Call the function
    success,file_path = implementation(test_file)
    
    # Assert that the function returns True indicating success
    assert success == True, (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: True, got: {success}"
    )
    # Assert that a valid file_path was returned
    assert os.path.exists(file_path), (
        f"Test failed for {implementation.__name__}. "
        f"Expected file path: {file_path}, got: {file_path}"
    )

def test_display_text_file_failure(implementation, tmp_path):
    """
    Test to verify that the function returns False and None for a non-existent file.
    """
    # Save into a variable an invalid file path leading to no file whatsoever
    non_existent_file_path = tmp_path / "non_existent.txt"
    
    # Call the function
    success,file_path = implementation(non_existent_file_path)
    
    # Assert that the function returns False indicating failure
    assert success == False, (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: False, got: {success}"
    )
    # Assert that the file_path is None
    assert file_path == None, (
        f"Test failed for {implementation.__name__}. "
        f"Expected file path: None, got: {file_path}"
    )

def test_display_text_file_sorting(implementation, tmp_path):
    """
    Test to verify that values are correctly sorted in descending order.
    """
    test_file = tmp_path / "test_sorting.txt"
    with open(test_file, 'w') as file:
        file.write("Last: 10\nFirst: 20\nSecond: 15\n")

    success, file_path = implementation(test_file)
    expected_sorted_data = [('First', 20.0), ('Second', 15.0), ('Last', 10.0)]

    # Assert that the function returns True indicating success
    assert success == True, (
        f"Test failed for {implementation.__name__}. "
        f"Expected success: True, got: {success}"
    )
    # Assert that a valid file_path was returned
    assert os.path.exists(file_path), (
        f"Test failed for {implementation.__name__}. "
        f"Expected file path: {file_path}, got: {file_path}"
    )
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Split the content into lines
    lines = content.split('\n')

    # Remove any empty lines
    lines = [line for line in lines if line]

    # first assert that the total number of lines is 3
    assert len(lines) == 3, (
        f"Test failed for {implementation.__name__}. "
        f"Expected 3 lines, got: {len(lines)}"
    )

    # Parse the data into name-value pairs for the next assertion
    data = [line.split(':') for line in lines]
    name_value_pairs = [(name.strip(), float(value.strip())) for name, value in data]

    # Assert that the name-value pairs are sorted in descending order
    assert name_value_pairs == expected_sorted_data, (
        f"Test failed for {implementation.__name__}. "
        f"Expected: {expected_sorted_data}, got: {name_value_pairs}"
    )

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-06-display_text_file_gui\display_text_file_gui_test.py