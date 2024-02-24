import tempfile
import pandas as pd
import os
import pytest
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

# Helper function to read a DataFrame from a file path
def read_dataframe_from_file(file_path):
    assert Path(file_path).suffix == '.xlsx', "Invalid file extension"
    return pd.read_excel(file_path)

@pytest.fixture(params=implementations, ids=[impl[1] for impl in implementations])
def implementation(request):
    impl, _ = request.param
    return impl

@pytest.fixture
def file_path():
    return os.path.join(os.path.dirname(__file__), 'GPUs.xlsx')

@pytest.mark.parametrize("column_index", [0, 1, 2])  # Add more column indexes as needed
def test_excel_sort(implementation, file_path, column_index):
    try:
        sorted_file_path = implementation(file_path, column_index)

        if not sorted_file_path:
            pytest.fail(f"Failed to get a valid file path from {implementation.__name__}")

        # Read the sorted data from the temporary file
        sorted_data = read_dataframe_from_file(sorted_file_path)

        # Delete the temporary file
        os.remove(sorted_file_path)

        # Check if the data is sorted correctly
        assert sorted_data.iloc[0, column_index] == max(sorted_data.iloc[:, column_index]), "Data is not sorted correctly"

    except Exception as e:
        pytest.fail(f"An error occurred during testing: {str(e)}")