import pandas as pd
from openpyxl import load_workbook

def excel_sort(file_path, column_index):
    # Load the Excel file into a pandas dataframe
    df = pd.read_excel(file_path)

    # Sort the dataframe in descending order based on the specified column
    df = df.sort_values(by=df.columns[column_index], ascending=False)

    # Create a new xlsx file using the openpyxl engine
    writer = pd.ExcelWriter(file_path, engine='openpyxl')

    # Write the sorted dataframe to the new xlsx file
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the writer and return the new xlsx file
    writer.save()
    return writer.book