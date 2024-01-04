from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time
# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x350")

def clicker():
    my_label.config(text=f'You Selected: {my_topping.get()}')


# radio buttons
toppings = ["Milk", "Egg", "Vegetables"]

my_topping = StringVar()

for topping in toppings:
    tb.Radiobutton(root, bootstyle="danger", variable=my_topping, text=topping, value=topping, command=clicker).pack(pady=10)

#Create button
my_button = tb.Button(root, text="click me", command=clicker)
my_button.pack(pady=20)

my_label = tb.Label(root, text="You Selected: ")
my_label.pack(pady=20)


rb1 = tb.Radiobutton(root, bootstyle="info toolbutton", variable=my_topping, text="Radio Button 1", value="Radio", command=clicker)
rb1.pack(pady=20)
rb2 = tb.Radiobutton(root, bootstyle="info outline toolbutton", variable=my_topping, text="Radio Button 1", value="Radio", command=clicker)
rb2.pack(pady=20)

root.mainloop()