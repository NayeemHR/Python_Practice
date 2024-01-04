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

def stuff(x):
    my_menu.config(bootstyle=x)
    my_label.config(text=f"You selected: {x}")



my_menu = tb.Menubutton(root, bootstyle="warning", text="Things!")
my_menu.pack(pady=50)

inside_menu = tb.Menu(my_menu)

item_var = StringVar()
for x in ['primary', 'secondary', 'danger', 'info']:
    inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x : stuff(x))

my_menu['menu'] = inside_menu


my_label = tb.Label(root, text="")
my_label.pack(pady=40)


root.mainloop()
