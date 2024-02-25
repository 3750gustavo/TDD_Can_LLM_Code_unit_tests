import os
import tkinter as tk

def display_text_file(file_path):
    # Check if the file exists
    if not os.path.exists(file_path):
        return False, None

    # Read the content of the file
    with open(file_path, 'r') as f:
        data = f.read()

    # Parse the data into name-value pairs
    name_value_pairs = []
    for line in data.splitlines():
        name, value = line.split(':')
        name_value_pairs.append({'name': name, 'value': value})

    # Sort the list of dictionaries in descending order based on the 'value' key
    sorted_name_value_pairs = sorted(name_value_pairs, key=lambda x: x['value'], reverse=True)

    # Check if a file named 'test.txt' already exists in the working directory
    if os.path.exists('test.txt'):
        # Overwrite the file with the sorted name-value pairs
        with open('test.txt', 'w') as f:
            for pair in sorted_name_value_pairs:
                f.write(f"{pair['name']}: {pair['value']}\n")
    else:
        # Create a temporary .txt file named 'test.txt' with the sorted name-value pairs
        with open('test.txt', 'w') as f:
            for pair in sorted_name_value_pairs:
                f.write(f"{pair['name']}: {pair['value']}\n")

    # Display the contents of the temporary .txt file in a window GUI
    root = tk.Tk()
    root.title("Text File Viewer")
    text_widget = tk.Text(root, width=80, height=20)
    text_widget.pack()
    text_widget.insert(tk.END, "\n".join(sorted_name_value_pairs))
    root.mainloop()

    # Return a tuple containing a boolean value indicating whether the operation was successful and the absolute path to the temporary .txt file
    return True, os.path.abspath('test.txt')