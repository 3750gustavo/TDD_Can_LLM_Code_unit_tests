import pandas as pd

def excel_sort(file_path, column_index):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)

        # Check if the column_index is valid
        if column_index < 0 or column_index >= len(df.columns):
            raise ValueError("Invalid column index")

        # Sort the DataFrame by the specified column in descending order
        df_sorted = df.sort_values(by=df.columns[column_index], ascending=False)

        # Create an in-memory Excel writer
        excel_writer = pd.ExcelWriter('in_memory_excel.xlsx', engine='openpyxl')
        df_sorted.to_excel(excel_writer, index=False)

        # Get the in-memory Excel object
        in_memory_excel = excel_writer.save()

        return in_memory_excel
    except Exception as e:
        return str(e)