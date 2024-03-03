import tempfile
import pandas as pd
import os
import pytest
import string
import random
from pathlib import Path
from ChatGPT import excel_sort as ChatGPT
from CodeLLama import excel_sort as CodeLLama
from Bard import excel_sort as Bard
from Copilot import excel_sort as Copilot
from Claude import excel_sort as Claude
from Perplexity import excel_sort as Perplexity

# Define the implementations with their names
implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Bard, 'Bard'),
    (Copilot, 'Copilot'),
    (Claude, 'Claude'),
    (Perplexity, 'Perplexity')
]

def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_dataframe(rows=100, columns=5):
    data = {'col_{}'.format(i): [random_string() for _ in range(rows)] for i in range(columns)}
    df = pd.DataFrame(data)
    return df

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

@pytest.fixture
def file_path():
    # Generate a random DataFrame
    df = generate_random_dataframe()

    # Save the DataFrame as an Excel file
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as temp_file:
        temp_file_path = temp_file.name
        df.to_excel(temp_file_path, index=False)

    return temp_file_path

@pytest.mark.parametrize("column_index", [0, 1, 2])  # Add more column indexes as needed
def test_excel_sort(implementation, file_path, column_index):
    try:
        sorted_file_path = implementation(file_path, column_index)

        if not sorted_file_path:
            pytest.fail(f"Failed to get a valid file path from {implementation[1]}")

        # Read the sorted data from the temporary file
        sorted_data = pd.read_excel(sorted_file_path)

        # Delete the temporary file
        os.remove(sorted_file_path)

        # Check if the data is sorted correctly
        assert sorted_data.iloc[0, column_index] == max(sorted_data.iloc[:, column_index]), f"Data is not sorted correctly in {implementation[1]}"

    except Exception as e:
        pytest.fail(f"An error occurred during testing in {implementation[1]}: {str(e)}")

# To execute this test, run the following command:
# pytest -v -s F:\TFG\TDD_Can_LLM_Code_unit_tests\Unit_tests_python\EX-02-Excel_sort\Excel_Test.py