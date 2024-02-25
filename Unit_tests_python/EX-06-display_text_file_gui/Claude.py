import tkinter as tk
from tkinter import messagebox
import os

def display_text_file(filepath):
    try:
        with open(filepath, 'r') as f:
            data = f.read()
        
        records = []
        for line in data.split('\n'):
            if ':' in line:
                name, value = line.split(':')
                records.append({'name': name, 'value': value})
        
        records.sort(key=lambda x: int(x['value']), reverse=True)
        
        test_filepath = os.path.join(os.getcwd(), 'test.txt')        
        with open(test_filepath, 'w') as f:
            for record in records:
                f.write(f"{record['name']}:{record['value']}\n")
        
        window = tk.Tk()
        frame = tk.Frame(master=window)
        
        text_box = tk.Text(master=frame)
        text_box.insert('1.0', open(test_filepath, 'r').read())
        text_box.config(state='disabled')
        
        frame.pack()        
        text_box.pack()
        
        window.mainloop()
        
        return (True, test_filepath)
    
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="File not found") 
        return (False, None)
    
    except:
        messagebox.showerror(title="Error", message="Unable to process file")
        return (False, None)