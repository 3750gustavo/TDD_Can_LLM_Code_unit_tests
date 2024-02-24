import pandas as pd
import tempfile
import os

def excel_sort(excel_file, column_index):
    df = pd.read_excel(excel_file)
    
    # Sort values by specified column in descending order
    df = df.sort_values(by=df.columns[column_index], ascending=False)
    
    # Create temp file path
    tmp_file = tempfile.NamedTemporaryFile(delete=False)
    tmp_path = tmp_file.name
    
    # Save sorted DataFrame to temp csv file
    df.to_csv(tmp_path, index=False)
    
    return tmp_path