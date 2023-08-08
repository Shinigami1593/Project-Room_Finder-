from tkinter import *
import sqlite3
def a():
    flat = Tk()
    flat.title('Register page')
    flat.geometry('1920x1000')
    flat.configure(bg='#ffffff')
    bc = PhotoImage(file='flat.png')
    l = Label(flat,image = bc,bg='black')
    l.pack()
    # d = sqlite3.connect('Flat.sql')
    # conn = d.cursor()
    # conn.execute(""" CREATE TABLE customer_registration(
    #              Full_name,
    #              Gender,
    #              Permanent_address,
    #              Contact_no,
    #              Room_no
    # )""")
    # d.commit()
    # d.close()

    def insert():
        hostel = sqlite3.connect('Flat.sql')
        b = hostel.cursor()
        b.execute("INSERT INTO Customer_registration VALUES(:Full_name, :Gender, :Permanent_address, :Contact_no)",{
            'Full_name': e.get(),
            'Gender': d.get(),
            'Permanent_address': e2.get(),
            'Contact_no': e3.get(),


        })
        hostel.commit()
        hostel.close()
        e.delete(0,END)
        d.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)



    i = PhotoImage(file='s (1).png')
    b = Button(flat,width=75,height=75,cursor='hand2',image=i)
    b.place(x=640,y=765)
    e = Entry(flat,width=25,font=('Arial',40),border=0,bg="#D8D8D8")
    e.place(x=270,y=310)


    d=Entry(flat,width=13,font=('Arial',40),border=0,bg="#D8D8D8")
    d.place(x=255,y=410)


    e2 = Entry(flat,width=20,font=('Arial',40),border=0,bg="#D8D8D8")
    e2.place(x=420,y=510)
    e3 = Entry(flat,width=18,font=('Arial',30),border=0,bg="#D8D8D8")
    e3.place(x=390,y=630)
    flat.mainloop()
a()