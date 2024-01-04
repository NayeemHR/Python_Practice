from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time
# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x600")

def spinny():
    my_label.config(text=my_spin2.get())

my_spin = tb.Spinbox(root, bootstyle="success", font=("Helvetica", 18), from_=0, to=10)
my_spin.pack(pady=20)

#spinbox list 

stuff = ["Jhon", "April", "Bod"]
my_spin1 = tb.Spinbox(root, bootstyle="success", font=("Helvetica", 18), from_=0, to=10, values=stuff)
my_spin1.pack(pady=20)

my_spin2 = tb.Spinbox(root, bootstyle="success", font=("Helvetica", 18), from_=0, to=10, values=stuff, state="readonly", command=spinny)
my_spin2.pack(pady=20)

#set default
my_spin.set('Jhon')

# Button
my_button = tb.Button(root, text="Click Me!", bootstyle="success", command=spinny)
my_button.pack(pady=10)

my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)






root.mainloop()