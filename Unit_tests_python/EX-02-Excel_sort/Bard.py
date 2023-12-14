from io import BytesIO

import pandas as pd
from openpyxl import load_workbook


def excel_sort(file_path, column_index):
    """
    Sorts an Excel file in descending order based on a specified column and returns a new, unsaved xlsl file.

    Args:
        file_path (str): The path to the Excel file.
        column_index (int): The index of the column to sort by (0-based).

    Returns:
        bytes: The contents of the sorted xlsl file in memory.

    Raises:
        ValueError: If the provided file path is invalid.
        IndexError: If the provided column index is out of bounds.
    """

    # Read the Excel file into a pandas DataFrame
    try:
        with open(file_path, "rb") as f:
            data = pd.read_excel(f)
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")

    # Sort the DataFrame by the specified column in descending order
    try:
        sorted_data = data.sort_values(by=column_index, ascending=False)
    except IndexError:
        raise IndexError(f"Invalid column index: {column_index}")

    # Create a new xlsl file in memory
    output_file = BytesIO()
    writer = pd.ExcelWriter(output_file, engine="openpyxl")

    # Write the sorted DataFrame to the new xlsl file
    sorted_data.to_excel(writer, sheet_name="Sorted Data")
    writer.save()

    # Return the contents of the new xlsl file in memory
    return output_file.getvalue()