import pandas as pd

def excel_sort(file_path, col_index):
  """
  Sorts an Excel file's data based on a specified column in descending order.

  Args:
    file_path: The path to the Excel file.
    col_index: The index of the column to sort by (0-based indexing).

  Returns:
    An in-memory Excel object containing the sorted data.
  """

  # Read the Excel file into a Pandas DataFrame
  data_frame = pd.read_excel(file_path)

  # Sort the data by the specified column in descending order
  sorted_data = data_frame.sort_values(by=col_index, ascending=False)

  # Convert the sorted DataFrame back into an Excel object
  excel_obj = pd.ExcelWriter('in_memory_file.xlsx', engine='openpyxl')
  sorted_data.to_excel(excel_obj)
  excel_obj.save()
  excel_obj.close()

  # Load the in-memory Excel object
  with pd.ExcelFile('in_memory_file.xlsx') as xlsx:
    return xlsx.parse(xlsx.sheet_names[0])

  # (Optional) Delete the temporary in-memory file
  os.remove('in_memory_file.xlsx')