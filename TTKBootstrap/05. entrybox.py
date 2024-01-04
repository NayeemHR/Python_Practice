from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x350")

# function
def speak():
    my_label.config(text=f"You Typed : {my_entry.get()}")

# create a entry box
my_entry = tb.Entry(root,bootstyle="success", font=("Helvetica", 18), foreground="yellow", width=12,show="*")
my_entry.pack(pady=50)

# create button
my_button = tb.Button(root, bootstyle="danger outline", text="Clicke me", command=speak )
my_button.pack(pady=20)


#create label
my_label = tb.Label(root, text="")
my_label.pack(pady=20)


root.mainloop()