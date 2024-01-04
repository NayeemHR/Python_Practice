from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x350")

# Create a function for the button
counter = 0

def changer():
    global counter
    counter+=1
    if counter % 2 == 0:
        my_label.config(text="Hello World!")
    else:
        my_label.config(text="Goodbye World")

# // Create Label

my_label = tb.Label(text="Hello World!", font=("Helvetica", 14), bootstyle="default")
my_label.pack(pady=50)

# Create a button
my_button = tb.Button(text="Click Me!", bootstyle="success, outline", command=changer)
# my_button = tb.Button(text="Click Me!", bootstyle="success, link")
my_button.pack(pady=20)

root.mainloop()