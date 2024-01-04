from tkinter import *
from ttkbootstrap.constants import *
from PIL import Image
Image.CUBIC = Image.BICUBIC
import ttkbootstrap as tb

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("500x1000")

global counter
counter = 5

def up():
    my_meter.step(10)
    

def down():
    my_meter.step(-10)


def clicker():
    global counter
    if counter <= 100:
        my_meter.configure(amountused=counter)
        counter +=5
        my_btn.configure(text=f"Click Me {my_meter.amountusedvar.get()}")


my_meter = tb.Meter(root, bootstyle="success", subtext="Remaining Balance", interactive=True, textright="%", textleft="Only" )
my_meter.pack(pady=10)

my_meter2 = tb.Meter(root, bootstyle="success", subtext="Remaining Balance", interactive=True, textright="%", metertype="semi", stripethickness=5, metersize=220, amountused=20)
my_meter2.pack(padx=10)

my_meter3 = tb.Meter(root, bootstyle="success", subtext="Remaining Balance", interactive=True, textright="%", stripethickness=5, metersize=200, padding=10, amountused=20, amounttotal=200 )
my_meter3.pack(pady=10)

my_btn = tb.Button(root, text="click me 5", command=clicker)
my_btn.pack(pady=10)

my_btn1 = tb.Button(root, text="UP", command=up)
my_btn1.pack(pady=10)

my_btn2 = tb.Button(root, text="Down", command=down)
my_btn2.pack(pady=10)

# def stuff(x):
#     my_menu.config(bootstyle=x)
#     my_label.config(text=f"You selected: {x}")



# my_menu = tb.Menubutton(root, bootstyle="warning", text="Things!")
# my_menu.pack(pady=50)

# inside_menu = tb.Menu(my_menu)

# item_var = StringVar()
# for x in ['primary', 'secondary', 'danger', 'info']:
#     inside_menu.add_radiobutton(label=x, variable=item_var, command=lambda x=x : stuff(x))

# my_menu['menu'] = inside_menu


# my_label = tb.Label(root, text="")
# my_label.pack(pady=40)


root.mainloop()
