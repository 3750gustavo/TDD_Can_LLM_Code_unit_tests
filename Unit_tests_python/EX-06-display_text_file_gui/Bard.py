import tkinter as tk
import os

def display_text_file(file_path):
   """Reads, parses, sorts, and displays contents of a .txt file."""

   try:
       with open(file_path, "r") as file:
           content = file.readlines()

       parsed_data = []
       for line in content:
           name, value = line.strip().split(":")
           parsed_data.append({"name": name, "value": value})

       parsed_data.sort(key=lambda item: item["value"], reverse=True)

       temp_file_path = "test.txt"
       with open(temp_file_path, "w") as temp_file:
           for item in parsed_data:
               temp_file.write(f"{item['name']}: {item['value']}\n")

       # Display contents in GUI window
       root = tk.Tk()
       text_box = tk.Text(root)
       text_box.pack()
       with open(temp_file_path, "r") as temp_file:
           text_box.insert("end", temp_file.read())
       root.mainloop()

       return True, os.path.abspath(temp_file_path)

   except FileNotFoundError:
       print("Error: The specified file path does not exist.")
       return False, None
   except Exception as e:
       print(f"An unexpected error occurred: {e}")
       return False, None