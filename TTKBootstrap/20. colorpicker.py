from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from ttkbootstrap.dialogs.colorchooser import ColorChooserDialog

# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x600")

def cc():
    #create color chooser
    my_color = ColorChooserDialog()

    #show color chooser
    my_color.show()

    #return color chooser
    colors = my_color.result

    #output the label
    my_label.config(text=colors.hex)
    root.configure(background=colors.hex)




my_button = tb.Button(root, text="Click Me!", bootstyle="danger", command=cc)
my_button.pack(pady=40)

my_label = tb.Label(root, text='', font=("Helvetica", 18))
my_label.pack(pady=20)




root.mainloop()


