from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.scrolled import ScrolledFrame

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x600")


my_frame = ScrolledFrame(root, autohide=False)
my_frame.pack(pady=15, padx=15, fill=BOTH, expand=YES)

for x in range(21):
    tb.Button(my_frame, bootstyle="info", text=f"Click Me! {x}").pack(pady=20)
    


root.mainloop()


