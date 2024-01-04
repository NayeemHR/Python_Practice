from tkinter import *
# from ttkbootstrap.constants import *
import ttkbootstrap as tb
from datetime import date 
from ttkbootstrap.dialogs import Querybox

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x350")

# function
def datey():
    my_label.config(text=f"You Picked : {my_date.entry.get()}")
    print(my_date.entry.get())

def thing():
    cal = Querybox()
    my_label.config(text=f"You Picked : {cal.get_date()}")


my_date = tb.DateEntry(root, bootstyle="danger", firstweekday=5, startdate=date(2023,2,14), str = r"%x")
my_date.pack(pady=50)


# create button
my_button = tb.Button(root, bootstyle="danger outline", text="Get Data", command=datey )
my_button.pack(pady=20)

my_button2 = tb.Button(root, bootstyle="success outline", text="Get Calender", command=thing )
my_button2.pack(pady=20)

#create label
my_label = tb.Label(root, text="You Picked: ")
my_label.pack(pady=20)


root.mainloop()