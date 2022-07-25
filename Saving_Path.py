from tkinter import filedialog

def select_path(Button):
    #allows user to select path from the file explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)
