## display_text_file_gui EX 06 versions

# Original Prompt: Create an Python function called "display_text_file" that takes only one argument which is the path to the .txt file. This function should:
    - Read the contents of the specified .txt file
    - Parse the data from the file using a delimiter like ':'
    - Sort the values in descending order
    - Display the sorted names and corresponding values on a window GUI with line breaks between each name-value pair as they are present in the original text file.
    - Return a boolean value indicating whether the operation was successful or not.
    If an error occurs during any of these steps, the function should return false and display an appropriate error message on the screen.

## Revisions

1. Develop a Python function named "display_text_file" that that accepts a single parameter representing the path to a .txt file. This function must perform the following tasks:
    - Read the content of the provided .txt file.
    - Utilize the delimiter ":" to parse the data within the file into name-value pairs with keys 'name' and 'value', respectively, as a list of dictionary variables.
    - Sort the list of dictionaries in descending order based on the 'value' key.
    - Check if a file named 'test.txt' already exists in the working directly, if not, create a temporary (Do not delete the file upon completion) .txt file named 'test.txt' with the sorted name-value pairs, each pair separated by a line break; if it does, overwrite the file with the sorted name-value pairs.
    - Display the contents of the temporary .txt file in a window GUI.
    - Upon completion, return a tuple containing a boolean value indicating whether the operation was successful and the absolute path to the temporary .txt file.
    - If an error occurs during any of these steps, like the provided file path does not exist, the function should return false, NONE as the absolute path to the temporary .txt file and display an appropriate error message on the screen.
    - The function should be named "display_text_file" and should be able to handle exceptions and errors gracefully.

    - Reason: This revision clarifies the function's requirements and expectations, as well as the handling of edge cases.