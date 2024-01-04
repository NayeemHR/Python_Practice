from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time
# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x350")

#frame
my_frame = tb.Frame(root)
my_frame.pack(pady=20)

#create a scrollbar
my_scroll = tb.Scrollbar(my_frame, orient="vertical", bootstyle="dark round")
my_scroll.pack(side="right", fill='y')

# create a Text Widget
my_text = Text(my_frame,width=30, height=25, yscrollcommand=my_scroll.set, wrap="none", font=("Helvetica", 18))
my_text.pack()

# ? Config the scrollbar
my_scroll.config(command=my_text.yview)









root.mainloop()