import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import mysql.connector


class DataEntryForm(ttk.Frame):

    def __init__(self, master):
        super().__init__(master, padding=(20, 10))
        self.pack(fill=BOTH, expand=YES)

        # form variables
        self.name = ttk.StringVar(value="")
        self.address = ttk.StringVar(value="")
        self.phone = ttk.StringVar(value="")

        def fetch_data(self):
            conn = mysql.connector.connect(host="localhost", username="root", password="", database="face_recognition")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from employee")

            data=my_cursor.fetchall()

            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                    self.student_table.insert("", END, values=i)
                conn.commit()
            conn.close()
        def datalist():    
            list = self.fetch_data()    
            print(list)

        btn = ttk.Button( text="Fetch data", command=datalist).pack(pady=10)



if __name__ == "__main__":

    app = ttk.Window("Data Entry", "superhero", resizable=(False, False))
    DataEntryForm(app)
    app.mainloop()
