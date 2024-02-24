import pandas as pd
import tempfile

def excel_sort(file_path, column_index):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Sort the DataFrame based on the specified column in descending order
    df = df.sort_values(by=df.columns[column_index], ascending=False)

    # Create a temporary file to store the sorted data
    temp_file = tempfile.NamedTemporaryFile(delete=False)

    # Write the sorted DataFrame to the temporary file
    df.to_excel(temp_file.name, index=False)

    # Return the path to the temporary file
    return temp_file.name