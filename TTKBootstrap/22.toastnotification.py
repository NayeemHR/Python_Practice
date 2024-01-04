from tkinter import *
import ttkbootstrap as tb
from ttkbootstrap.toast import ToastNotification


# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x600")

def clicker():
    toast.show_toast()


toast = ToastNotification(title="My toast title", message="this is a toast message !! whahoo!", duration=3000, alert=True, 
                        #   position=(-1900,300,'sw'),
                          )
my_btn = tb.Button(root, text="click me!", command=clicker)
my_btn.pack(pady=30)

root.mainloop()


