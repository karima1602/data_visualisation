import tkinter as tk
from tkinter import filedialog
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import pandas as pd

def upload():
    global filepath
    filepath = filedialog.askopenfilename(filetypes=(('Text files','*.txt'),('Spreadsheet files','*.csv')))
    file = open(filepath,'r')
    print(filepath)
    return filepath

def visualize():
    selected_tool = selected_tool_var.get()
    global filepath 
    if filepath: 
        data = pd.read_csv(filepath)
        if selected_tool == "Histogram":
            data.plot.hist()
            plt.title("Histogram")
            plt.xlabel("Values")
            plt.ylabel("Frequency")
            plt.tight_layout()
            plt.savefig("temp_plot.png")
            image = Image.open("temp_plot.png")
            photo = ImageTk.PhotoImage(image)
            label_image.config(image=photo)
            label_image.image = photo
        elif selected_tool == "Box plot":  
            data.plot.box()
            plt.title("Box Plot")
            plt.tight_layout()
            plt.savefig("temp_plot_box.png")
            image = Image.open("temp_plot_box.png")
            photo = ImageTk.PhotoImage(image)
            label_image_.config(image=photo)
            label_image_.image = photo
    else:
        print('File not found !!')

def manipulate():
    global filepath, min_label, max_label, mean_label
    selected_fct = selected_fct_var.get()
    if filepath:
        data = pd.read_csv(filepath)
        data_np = data.values  
        numeric_columns = data.select_dtypes(include=['number'])
        if selected_fct == "Min":
            min_value = np.min(numeric_columns) 
            min_label.config(text=f"Minimum value: {min_value}")
        elif selected_fct == "Max":
            max_value = np.max(numeric_columns) 
            max_label.config(text=f"Maximum value: {max_value}") 
        elif selected_fct == "Mean":
            mean_value = np.mean(numeric_columns) 
            mean_label.config(text=f"Mean value: {mean_value}")
    else:
        print('File not found !')



window = tk.Tk()
window.title("Interactive Data Visualization")
window.geometry("1200x600")
window.configure(bg="#F0F0F0")
#window.resizable(False,False)

f1 = tk.Frame(window).grid(padx = 50, pady = 50)
f2 = tk.Frame(window).grid( padx = 50, pady = 50)


selected_tool_var = tk.StringVar(window)
selected_tool_var.set("Select Tool")
selected_fct_var = tk.StringVar(window)
selected_fct_var.set("Select Function")
filepath_var = tk.StringVar(window)

btn_upload = tk.Button(window, text='Open File', command=upload, bg="#793690", fg="white", font=("Arial", 12))
btn_upload.grid(row=0, column=0, padx=10, pady=10)

menu_fcts = tk.OptionMenu(window, selected_fct_var, 'Min', 'Max', 'Mean')
menu_fcts.grid(row=1, column=0, padx=1, pady=10)

btn_manipulation = tk.Button(window, text='Manipulate Data', command=manipulate, bg="#793690", fg="white", font=("Arial", 12))
btn_manipulation.grid(row=1, column=1, padx=250, pady=10)

min_label = tk.Label(f1, text="", bg="#F0F0F0", font=("Arial", 12))
min_label.grid(row=2, column=0, padx=10, pady=10)

max_label = tk.Label(f1, text="", bg="#F0F0F0", font=("Arial", 12))
max_label.grid(row=2, column=1, padx=10, pady=10)

mean_label = tk.Label(f2, text="", bg="#F0F0F0", font=("Arial", 12))
mean_label.grid(row=2, column=2, padx=10, pady=10)


menu_tools = tk.OptionMenu(window, selected_tool_var, 'Histogram', 'Box plot')
menu_tools.grid(row=3, column=0, padx=20, pady=10)

btn_visualize = tk.Button(window, text='Visualize Data', command=visualize, bg="#793690", fg="white", font=("Arial", 12))
btn_visualize.grid(row=3, column=1, padx=250, pady=10)

label_image = tk.Label(f2)
label_image.grid(row=4, column=0,  padx=10, pady=10)


label_image_ = tk.Label(f2)
label_image_.grid(row=4, column=1, padx=150, pady=10)

window.mainloop()
