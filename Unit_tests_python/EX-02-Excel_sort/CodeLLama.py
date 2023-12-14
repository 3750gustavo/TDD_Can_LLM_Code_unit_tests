import pandas as pd

def excel_sort(file_path, column_index):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

    # Sort the DataFrame based on the specified column in descending order
    df = df.sort_values(by=df.columns[column_index], ascending=False)

    # Return the sorted DataFrame as an in-memory Excel object
    return df.to_excel()