from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time
# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x350")

def scaler(e):
    my_label.config(text=f'{int(my_scale.get())}')
# create a scale/slider
my_scale = tb.Scale(root, bootstyle="warning", length=500, orient="horizontal", from_=0, to=100,command=scaler)
my_scale.pack(pady=50)

# my_scale1 = tb.Scale(root, bootstyle="warning", length=400, orient="vertical")
# my_scale1.pack(pady=50)


my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack(pady=20)








root.mainloop()