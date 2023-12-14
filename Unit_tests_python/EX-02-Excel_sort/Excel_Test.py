import pytest
import pandas as pd
from openpyxl import load_workbook
from ChatGPT import excel_sort as ChatGPT
from CodeLLama import excel_sort as CodeLLama
from Bard import excel_sort as Bard

# Define a list of implementations to test
implementations = [ChatGPT,CodeLLama,Bard]

@pytest.mark.parametrize("excel_sort", implementations)
def test_sort_excel_data(excel_sort):
    # Define the path to the test Excel file
    test_file = "GPUs.xlsx"

    # Sort the data
    sorted_data = excel_sort(test_file, 0)

    # Check if the sorted data is in descending order for each column
    for column in sorted_data.columns:
        assert sorted_data[column].is_monotonic_decreasing

# Run the tests
if __name__ == "__main__":
    pytest.main([__file__])