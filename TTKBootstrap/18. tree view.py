from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as tb
import time
# root = Tk()
root = tb.Window(themename="superhero")
root.title("TTK Bootstrap!")
# root.iconbitmap('images/logo.png')
root.geometry("1200x600")

# ! Define columns
columns = ("first_name", "last_name", "email")

# ! Create Treeview
my_tree = tb.Treeview(root , bootstyle="success", columns=columns, show="headings" )
my_tree.pack(pady=20)

# ! Define headings 
my_tree.heading('first_name', text="First Name")
my_tree.heading('last_name', text="Last Name")
my_tree.heading('email', text="Email")

# ! Create sample data
contacts = []

for n in range(1,20):
    contacts.append((f"First {n}", f"Last {n}", f"email{n}@address.com"))

# Add Data to Treeview
for contact in contacts:
    my_tree.insert('', END, values=contact)






root.mainloop()


