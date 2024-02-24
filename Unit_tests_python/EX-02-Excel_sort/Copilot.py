import pandas as pd
import tempfile

def excel_sort(file_path, column_index):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)
    
    # Sort the DataFrame based on the specified column in descending order
    df_sorted = df.sort_values(df.columns[column_index], ascending=False)
    
    # Create a temporary file to save the sorted data
    temp_file = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False)
    temp_file.close()
    
    # Save the sorted data to the temporary file
    df_sorted.to_excel(temp_file.name, index=False)
    
    # Return the path of the temporary file
    return temp_file.name