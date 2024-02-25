import tkinter as tk

def display_text_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = f.read()
        data = data.split(':')
        data.sort(reverse=True)
        root = tk.Tk()
        root.title("Text File Viewer")
        text_widget = tk.Text(root, width=80, height=20, font=("Arial", 12))
        text_widget.pack()
        for name, value in data:
            text_widget.insert(tk.END, f"{name}: {value}\n")
        root.mainloop()
        return True
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False