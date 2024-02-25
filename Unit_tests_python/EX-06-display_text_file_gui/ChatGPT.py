import os
import tkinter as tk
from tkinter import messagebox

def display_text_file(file_path):
    try:
        # Check if the provided file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError("The provided file does not exist.")
        
        # Read the content of the provided .txt file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Parse the data into name-value pairs
        data = []
        for line in lines:
            parts = line.strip().split(":")
            if len(parts) == 2:
                data.append({'name': parts[0], 'value': parts[1]})
        
        # Sort the list of dictionaries in descending order based on the 'value' key
        sorted_data = sorted(data, key=lambda x: x['value'], reverse=True)
        
        # Write sorted name-value pairs to a temporary .txt file
        temp_file_path = 'test.txt'
        with open(temp_file_path, 'w') as temp_file:
            for item in sorted_data:
                temp_file.write(f"{item['name']}:{item['value']}\n")
        
        # Display the contents of the temporary .txt file in a window GUI
        root = tk.Tk()
        text_area = tk.Text(root)
        text_area.pack()
        with open(temp_file_path, 'r') as temp_file:
            text_area.insert(tk.END, temp_file.read())
        root.mainloop()
        
        return (True, os.path.abspath(temp_file_path))
    
    except FileNotFoundError as e:
        messagebox.showerror("Error", str(e))
        return (False, None)

    except Exception as e:
        messagebox.showerror("Error", str(e))
        return (False, None)