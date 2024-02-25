import tkinter as tk
from tkinter import messagebox

def display_text_file(file_path):
    try:
        # Read the contents of the specified .txt file
        with open(file_path, 'r') as file:
            lines = file.readlines()
        
        # Parse the data from the file using a delimiter like ':'
        data = {}
        for line in lines:
            parts = line.strip().split(':')
            if len(parts) == 2:
                name, value = parts
                data[name.strip()] = float(value.strip())  # Assuming values are numeric
        
        # Sort the values in descending order
        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        
        # Display the sorted names and corresponding values on a window GUI
        root = tk.Tk()
        root.title("Sorted Data")
        text_widget = tk.Text(root)
        text_widget.pack()
        
        for name, value in sorted_data:
            text_widget.insert(tk.END, f"{name}: {value}\n")
        
        root.mainloop()
        
        # Return True indicating success
        return True
    
    except Exception as e:
        # Display an appropriate error message on the screen
        messagebox.showerror("Error", str(e))
        return False