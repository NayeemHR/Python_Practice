from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs import Messagebox

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x600")

def clicker():

    # yesno, ok, okcancel, show_info, show_error, show_question, show_warning, yesnocancel, retrycancel
    mb = Messagebox.yesno("Display Some Message Here", "Here is the Title")

    my_label.config(text=f'You click {mb}')




my_button = tb.Button(root, text="Click Me!", bootstyle="danger", command=clicker)
my_button.pack(pady=40)

my_label = tb.Label(root, text='', font=("Helvetica", 18))
my_label.pack(pady=20)




root.mainloop()


