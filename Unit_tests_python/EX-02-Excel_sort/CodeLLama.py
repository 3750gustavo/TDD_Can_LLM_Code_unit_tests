import pandas as pd
import tempfile

def excel_sort(file_path, column_index):
    # Read the data from the specified Excel file
    df = pd.read_excel(file_path)

    # Sort the data in descending order based on the values in the specified column
    df = df.sort_values(by=df.columns[column_index], ascending=False)

    # Handle sorting of columns with mixed data types
    df = df.apply(lambda x: x.astype(str) if x.dtype == 'object' else x)

    # Save the sorted data to a temporary Excel file on disk
    with tempfile.NamedTemporaryFile(suffix='.xlsx') as tmp:
        df.to_excel(tmp.name, index=False)
        return tmp.name