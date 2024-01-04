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

my_notebook = tb.Notebook(root, bootstyle="dark")
my_notebook.pack(pady=20)

tab1  = tb.Frame(my_notebook)
tab2  = tb.Frame(my_notebook)

my_meter = tb.Meter(tab1, bootstyle="success", subtext="Remaining Balance", interactive=True, textright="%", textleft="Only" )
my_meter.pack(pady=10)

my_meter2 = tb.Meter(tab2, bootstyle="success", subtext="Remaining Balance", interactive=True, textright="%", metertype="semi", stripethickness=5, metersize=220, amountused=20)
my_meter2.pack(padx=10)

# add our frame to notebook

my_notebook.add(tab1, text="Tab 1")
my_notebook.add(tab2, text="Tab 2")

root.mainloop()
