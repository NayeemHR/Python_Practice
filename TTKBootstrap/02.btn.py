from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x350")

# Create a function
def checker():
    if var1.get() == 1:
        my_label.config(text="Checked!")
    else:
        my_label.config(text="Unchecked!")

# Create Label
my_label = Label(text="Click the checkbutton below", font=("Helvetica", 14))
my_label.pack(pady=(40,10))

# CheckButton
var1 = IntVar()
my_check = tb.Checkbutton(bootstyle="primary", text="Check me Out!", variable=var1, onvalue=1,offvalue=0, command=checker)
my_check.pack(pady=10)


# TOOLBUTTON
var2 = IntVar()
my_check2 = tb.Checkbutton(bootstyle="danger, toolbutton", text="ToolButton!!", variable=var2, onvalue=1, offvalue=0, command=checker)
my_check2.pack(pady=10)

# Outline TOOLBUTTON
var3 = IntVar()
my_check3 = tb.Checkbutton(bootstyle="danger, toolbutton, outline", text=" Outline ToolButton!!", variable=var3, onvalue=1, offvalue=0, command=checker)
my_check3.pack(pady=10)

# Round Toggle Button
var4 = IntVar()
my_check4 = tb.Checkbutton(bootstyle="success, round-toggle", text=" Round Toggle!!", variable=var4, onvalue=1, offvalue=0, command=checker)
my_check4.pack(pady=10)


# Squre Toggle Button
var5 = IntVar()
my_check5 = tb.Checkbutton(bootstyle="success, square-toggle", text=" Square Toggle!!", variable=var5, onvalue=1, offvalue=0, command=checker)
my_check5.pack(pady=10)

# Button style

my_style = tb.Style()
my_style.configure('success.Outline.TButton', font=("Helvetica", 24))

my_button = tb.Button(text="Hello Button", bootstyle="success", style="success.Outline.TButton", width=20)

my_button.pack(pady= 10)







root.mainloop()