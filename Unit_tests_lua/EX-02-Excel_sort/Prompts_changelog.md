## EXCEL Prompts EX 02 versions

# Original Prompt: Write a Lua function called "excel_sort" that takes an input Excel file path and column numbers as parameters, then sorts the data in each specified column in descending order. Finally, display the sorted data.

## Revisions

1. Write a Lua function named "excel_sort" that accepts an Excel file path and column numbers as parameters. This function sorts the data in each specified column in descending order and returns a new Excel file containing the sorted data.
   - Reason: This revision clarifies that the function creates a new Excel file with sorted data instead of just displaying it.

2. Write a Lua function called "excel_sort" that accepts an Excel file path and a single column index as a parameter. This function sorts the data based on the specified column in descending order and returns a new Excel file with the sorted data.
    - Reason: This revision specifies that the function works with a single column, making it more focused and understandable.

3. Write a Lua function named "excel_sort" that takes an input Excel file path and a column index number as parameters. This function sorts the data based on the specified column in descending order and returns the sorted data as an Excel file (xlsl format).
    - Reason: This revision adds clarity by specifying the return format of the sorted data and provides a more detailed explanation of the function's behavior.

4. Create a Lua function named 'excel_sort' that accepts an Excel file path and a column index number as arguments. The function should sort the data in descending order based on the specified column and return the sorted data as an in-memory Excel object. Importantly, the original file should not be modified, and the new file should not be saved to disk.
    - Reason: This is a major rewrite to clearly define the requirements, emphasizing that the function should return sorted data as an in-memory object without saving it to disk, and it should not modify the original file.

5. Define a Lua function called `excel_sort` that receives two arguments: an Excel file path and a column index number. This function will sort the data based on the specified column in descending order and return the sorted data as an in-memory Excel object without modifying the original file or saving the new file to disk.
    - Reason: I have revised the prompt several times to better clarify its requirements and improve its readability. The current revision specifies that the function should take an Excel file path and a column index number as arguments, sort the data based on the specified column in descending order, and return the sorted data as an in-memory Excel object without modifying the original file or saving the new file to disk.

6. Write a Lua function called `excel_sort` with two parameters: an Excel file path and a column index number. This function will sort the data based on the specified column in descending order and save the sorted data to a temporary file on disk. The function should return the path to the temporary file. PS: It should handle columns with mixed data types, handle sorting of strings, integers, floats, dates, etc.
    - Reason: This revision clarifies that the function should save the sorted data to a temporary file on disk and return the path to that file. It also specifies that the function should handle columns with mixed data types, such as strings, integers, floats, and dates.