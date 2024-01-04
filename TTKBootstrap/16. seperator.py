from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time
# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x350")


label1 = tb.Label(root, bootstyle="light", text="Label 1")
label1.pack(pady=40)

my_sep = tb.Separator(root, bootstyle="danger")
my_sep.pack()

label1 = tb.Label(root, bootstyle="light", text="Label 1")
label1.pack(pady=40)

my_sep2 = tb.Separator(root, bootstyle="danger", orient="vertical")
my_sep2.pack()

label1 = tb.Label(root, bootstyle="light", text="Label 1")
label1.pack(pady=40)


my_sep = tb.Separator(root, bootstyle="danger")
my_sep.pack(fill=X, padx=100)

label1 = tb.Label(root, bootstyle="light", text="Label 1")
label1.pack(pady=40)

# ! size grip
my_sizegrip = tb.Sizegrip(root, bootstyle="info")
my_sizegrip.pack(anchor="se", fill="both", expand=True)


root.mainloop()