from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

#create a function
def clicker():
    my_label.config(text=f"You clicked on {my_combo.get()}!")

def click_bind(e):
    my_label.config(text=f"You clicked on {my_combo.get()}!")


# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x350")


# Create Label
my_label = Label(text="Hello, Combo Box", font=("Helvetica", 14))
my_label.pack(pady=40)


#Create Dropdown Options
days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday"]


# create combobox
my_combo = tb.Combobox(root, bootstyle="success", values=days)
my_combo.pack(pady=20)

# set combo default
my_combo.current(0)

#create a button
my_button = tb.Button(root, text="Click Me!", command=clicker, bootstyle="danger")
my_button.pack(pady=20)

# Bind the combobox
my_combo.bind("<<ComboboxSelected>>", click_bind)





root.mainloop()