from tkinter import *
import sqlite3
def admin():
    def query():
            conn = sqlite3.connect('Hostel.sql')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM Customer_registration")

            records = c.fetchall()
    
            print_records = ''
            for record in records:
                print_records += (record[0]) + ' ' + (record[1]) + ' ' + (record[2]) + ' ' + (record[3]) + ' ' + '\t' + str(record[4]) + '\n'

            query_label = Label(f,text=print_records)
            query_label.place(x=75,y=300)


            conn.commit()
            conn.close()

    def query1():
            conn = sqlite3.connect('Flat.sql')
            c = conn.cursor()
            c.execute("SELECT *,oid FROM Customer_registration")

            records = c.fetchall()

            print_records = ''
            for record in records:
                print_records += (record[0]) + ' ' + (record[1]) + ' ' + (record[2]) + ' ' + (record[3]) + ' ' + '\t' + str(record[4]) + '\n'

            query_label = Label(f,text=print_records)
            query_label.place(x=75,y=300)
    

            conn.commit()
            conn.close()



    def delete():
        conn = sqlite3.connect('Hostel.sql')
        c = conn.cursor()
        c.execute("DELETE from Customer_registration WHERE oid = " + e1.get())
        print('Deleted Successfully')

        e1.delete(0,END)
        conn.commit()
        conn.close()

    def delete1():
        conn = sqlite3.connect('Flat.sql')
        c = conn.cursor()
        c.execute("DELETE from Customer_registration WHERE oid = " + e.get())
        print('Deleted Successfully')

        e.delete(0,END)
        conn.commit()
        conn.close()

    def update():
        conn = sqlite3.connect('Hostel.sql')
        c = conn.cursor()

        record_id = e1.get()

        c.execute(""" UPDATE Customer_registration SET
            Full_name = :name,
            Gender = :gender,
            Permanent_address = :address,
            Contact_no = :num
            WHERE oid = :oid""",
            {'name' : E0.get(),
                'gender' : E1.get(),
                'address' : E2.get(),
                'num' : E3.get(),
                'oid' : record_id
            }

            )
        conn.commit()
        conn.close()

        win.destroy()

    def update1():
        conn = sqlite3.connect('Flat.sql')
        c = conn.cursor()

        record_id = e.get()

        c.execute(""" UPDATE Customer_registration SET
            Full_name = :name,
            Gender = :gender,
            Permanent_address = :address,
            Contact_no = :num
            WHERE oid = :oid""",
            {'name' : E0.get(),
                'gender' : E1.get(),
                'address' : E2.get(),
                'num' : E3.get(),
                'oid' : record_id
            }

            )
        conn.commit()
        conn.close()

        win.destroy()

    def new1():
        global win

        win = Tk()
        win.title('Update Window')
        win.geometry('400x500')

        b = sqlite3.connect('Flat.sql')
        conn = b.cursor()
        record = e1.get()
        conn.execute(" SELECT * FROM Customer_registration WHERE oid = " + record)

        records = conn.fetchall()

        global E0
        global E1
        global E2
        global E3


        l = Label(win,text='First Name')
        l.place(x=10,y=10)

        l1 = Label(win,text='Gender')
        l1.place(x=10,y=35)

        l2 = Label(win,text='Permanent Address')
        l2.place(x=10,y=60)

        l3 = Label(win,text='Contact Number')
        l3.place(x=10,y=85)


        E0 = Entry(win,width=30)
        E0.place(x=108,y=10)

        E1 = Entry(win,width=30)
        E1.place(x=108,y=35)

        E2 = Entry(win,width=30)
        E2.place(x=108,y=60)

        E3 = Entry(win,width=30)
        E3.place(x=108,y=85)

        for i in records:
            E0.insert(0,i[0])
            E1.insert(0,i[1])
            E2.insert(0,i[2])
            E3.insert(0,i[3])

        b = Button(win,text='Save',cursor='hand2',width=26,command=update1)
        b.place(x=108,y=215)

    def new():
        global win

        win = Tk()
        win.title('Update Window')
        win.geometry('400x500')

        b = sqlite3.connect('Hostel.sql')
        conn = b.cursor()
        record = e1.get()
        conn.execute(" SELECT * FROM Customer_registration WHERE oid = " + record)

        records = conn.fetchall()

        global E0
        global E1
        global E2
        global E3


        l = Label(win,text='First Name')
        l.place(x=10,y=10)

        l1 = Label(win,text='Gender')
        l1.place(x=10,y=35)

        l2 = Label(win,text='Permanent Address')
        l2.place(x=10,y=60)

        l3 = Label(win,text='Contact Number')
        l3.place(x=10,y=85)


        E0 = Entry(win,width=30)
        E0.place(x=108,y=10)

        E1 = Entry(win,width=30)
        E1.place(x=108,y=35)

        E2 = Entry(win,width=30)
        E2.place(x=108,y=60)

        E3 = Entry(win,width=30)
        E3.place(x=108,y=85)

        for i in records:
            E0.insert(0,i[0])
            E1.insert(0,i[1])
            E2.insert(0,i[2])
            E3.insert(0,i[3])

        b = Button(win,text='Save',cursor='hand2',width=26,command=update)
        b.place(x=108,y=215)




    f = Tk()
    f.title('Admin')
    f.geometry('400x500')
    ########################################### HOSTEL #################################################
    b = Button(f,text='Show Records',cursor='hand2',command=query)
    b.pack()
    l = Label(f,text='Enter ID')
    l.place(x=100,y=40)
    e1 = Entry(f,width=19)
    e1.place(x=150,y=40)
    b2 = Button(f,text='Delete',cursor='hand2',width=15,command=delete)
    b2.place(x=150,y=65)
    b3 = Button(f,text='Update',cursor='hand2',width=15,command=new)
    b3.place(x=150,y=95)
    #_______________________________________________________________________________________________________
    ########################################### Flats ###################################################
    B = Button(f,text='Show Records(Flats)',cursor='hand2',command=query1)
    B.place(x=150,y=130)
    l1 = Label(f,text='Enter ID(flats)')
    l1.place(x=75,y=170)
    e = Entry(f,width=19)
    e.place(x=150,y=170)
    b2 = Button(f,text='Delete',cursor='hand2',width=15,command=delete1)
    b2.place(x=150,y=195)
    b3 = Button(f,text='Update',cursor='hand2',width=15,command=new1)
    b3.place(x=150,y=225)
    #_________________________________________________________________________________________________________
    f.mainloop()