import pandas as pd
import tempfile

def excel_sort(file_path, column_index):
   """
   Sorts an Excel file based on a specified column in descending order using pandas.

   Args:
       file_path (str): The path to the Excel file.
       column_index (int): The index of the column to sort by (0-based).

   Returns:
       str: The path to the temporary file with the sorted data.
   """

   try:
       # Read Excel file into a pandas DataFrame
       df = pd.read_excel(file_path)

       # Sort DataFrame in descending order by specified column
       df = df.sort_values(by=df.columns[column_index], ascending=False)

       # Create a temporary file with a unique filename
       with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_file:

           # Save sorted DataFrame to the temporary file
           df.to_excel(temp_file.name, index=False)

       # Return the path to the temporary file
       return temp_file.name

   except FileNotFoundError:
       print(f"Error: File not found at path: {file_path}")
       return None

   except Exception as e:
       print(f"Error: An unexpected error occurred: {e}")
       return None