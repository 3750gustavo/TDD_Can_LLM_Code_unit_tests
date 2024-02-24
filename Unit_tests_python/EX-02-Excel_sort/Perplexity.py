import pandas as pd
import tempfile

def excel_sort(file_path, column_index):
    # Read the Excel file
    df = pd.read_excel(file_path)
    
    # Sort the data based on the specified column index in descending order
    df_sorted = df.iloc[df.iloc[:, column_index].astype(str).str.lower().argsort()[::-1]]
    
    # Create a temporary file to save the sorted data
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.xlsx')
    
    # Save the sorted data to the temporary file
    df_sorted.to_excel(temp_file.name, index=False)
    
    return temp_file.name