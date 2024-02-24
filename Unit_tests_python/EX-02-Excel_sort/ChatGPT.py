import pandas as pd
import tempfile

def excel_sort(file_path, column_index):
    # Read Excel file
    df = pd.read_excel(file_path)
    
    # Sort DataFrame based on specified column index
    sorted_df = df.sort_values(df.columns[column_index], ascending=False, na_position='last')
    
    # Create a temporary file to save the sorted data
    with tempfile.NamedTemporaryFile(suffix=".xlsx", delete=False) as temp_file:
        temp_file_path = temp_file.name
        sorted_df.to_excel(temp_file_path, index=False)
    
    return temp_file_path