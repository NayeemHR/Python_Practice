from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from datetime import date 
from ttkbootstrap.dialogs import Querybox

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x350")

def thing():
    pass

my_frame = tb.Frame(root, bootstyle="light")
my_frame.pack(pady=40)

my_entry = tb.Entry(my_frame, font=("Helvetica", 18))
my_entry.pack(pady=20, padx=20)

my_button = tb.Button(my_frame, text="Click Me!", bootstyle="dark", command=thing)
my_button.pack(pady=20, padx=20)

my_label = tb.Label(root, text="Hello There!", font=("Helvetica", 18), bootstyle="inverse light")
my_label.pack(pady=20)


root.mainloop()