import pandas as pd
from io import BytesIO
from openpyxl import Workbook

def excel_sort(file_path, column_index):
    # Load the Excel file using pandas
    df = pd.read_excel(file_path)

    # Sort the DataFrame in descending order based on the specified column
    df = df.sort_values(by=df.columns[column_index], ascending=False)

    # Create a new Excel writer
    output_excel = BytesIO()
    writer = pd.ExcelWriter(output_excel, engine='openpyxl')
    writer.book = Workbook()

    # Convert the DataFrame back to Excel format
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Save the Excel file in memory
    writer.save()
    writer.close()

    # Reset the buffer position and return the sorted Excel file
    output_excel.seek(0)

    return output_excel