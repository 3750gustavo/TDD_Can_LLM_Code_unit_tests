import pandas as pd
import tempfile
import shutil

def excel_sort(file_path, column_index):
    # Read the Excel file into a DataFrame
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        return str(e)  # Handle file read errors
    
    # Sort the DataFrame by the specified column in descending order
    try:
        df = df.sort_values(df.columns[column_index], ascending=False, na_position='last')
    except Exception as e:
        return str(e)  # Handle sorting errors
    
    # Create a temporary directory to store the sorted Excel file
    temp_dir = tempfile.mkdtemp()
    
    # Generate a temporary file name
    temp_file_path = temp_dir + "/sorted_data.xlsx"
    
    # Save the sorted DataFrame to the temporary Excel file
    try:
        df.to_excel(temp_file_path, index=False)
    except Exception as e:
        return str(e)  # Handle file save errors
    
    return temp_file_path