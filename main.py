from tkinter import *
from tkinter import messagebox
import ast
import sqlite3
#create a window for login page
root = Tk()
root.title('RoomFinder(Login)')
root.geometry('925x500+300+200')
root.configure(bg='#ffffff')
root.resizable(0,0)
root.iconbitmap('D:\\project_work\\search.ico')
bc = PhotoImage(file='resized.png')
l = Label(root,image = bc,bg='black')
l.pack()
# sign up button click sends us to another window
d = sqlite3.connect('Hostel.sql')
# conn = d.cursor()
# conn.execute(""" CREATE TABLE customer_registration(
#                          Full_name,
#                          Gender,
#                          Permanent_address,
#                          Contact_no,
#                          Room_no
#             )""")
# d.commit() 
# d.close()
def signin():
    username = user.get()
    password = pas.get()

    file = open('datasheet.txt','r')
    d = file.read()
    r = ast.literal_eval(d)
    file.close()

    if username in r.keys() and password == r[username]:
        root.destroy()
        
        def hostels():
            reg = Toplevel()
            reg.title('Register page')
            reg.geometry('1920x1000')
            reg.configure(bg='#ffffff')
            bc = PhotoImage(file='regi (1).png')
            l = Label(reg,image = bc,bg='black')
            l.pack()
            
            # d = sqlite3.connect('Hostel.sql')
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

            def insert1():
               
                hostel = sqlite3.connect('Hostel.sql')
                b = hostel.cursor()
                b.execute("INSERT INTO customer_registration VALUES(:Full_name, :Gender, :Permanent_address, :Contact_no,:Room_no)",{
                    'Full_name': e.get(),
                    'Gender': d.get(),
                    'Permanent_address': e2.get(),
                    'Contact_no': e3.get(),
                    'Room_no': e4.get()
                })
                hostel.commit()
                hostel.close()
                e.delete(0,END)
                d.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)

            def hostel_book():
                
                h_book = Toplevel()
                h_book.title('Book your Hostel')
                h_book.geometry('1920x1000')
                h_book.configure(bg='#ffffff')
                bc = PhotoImage(file='maskm.png')
                l = Label(h_book,image = bc,bg='black')
                l.pack()
                global e4
                l1 = Label(h_book,text='Enter the room no. for booking',font=('Arial',20),bg='#90ED91')
                l1.place(x=220,y=765)
                e4 = Entry(h_book,width=25,font=('Arial',20))
                e4.place(x=600,y=765)
                b = Button(h_book,text='Book',font=('Arial',14),cursor='hand2',command=insert1)
                b.place(x=995,y=765)

                conn = sqlite3.connect('Hostel.sql')
                c = conn.cursor()
                c.execute("SELECT *,oid FROM customer_registration")
                records = c.fetchall()
                # print(records)
                b = []
                for record in records:
                    b.append(record[4])

                if str(112) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=110)
                    
                elif str(112) not in b :
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=110)
                if str(113) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=200)
                elif str(113) not in b:
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1240,y=200)
                if str(1151) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=290)
                elif str(1151) not in b:
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1240,y=290)
                if str(120) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=390)
                elif str(120) not in b:
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1240,y=390)
                if str(115) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=500)
                elif str(115) not in b:
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1240,y=500)
                if str(1202) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='white',height=1,width=9)
                    l.place(x=1240,y=610)
                elif str(1202) not in b:
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='white',height=1,width=8)
                    l.place(x=1240,y=610)
                if str(125) in b:
                    l = Label(h_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1240,y=700)
                elif str(125) not in b:
                    l = Label(h_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1240,y=700)

                h_book.mainloop()

            

            i = PhotoImage(file='s (1).png')
            b = Button(reg,width=75,height=75,cursor='hand2',image=i,command=hostel_book)
            b.place(x=640,y=765)
            e = Entry(reg,width=25,font=('Arial',40),border=0,bg="#D8D8D8")
            e.place(x=270,y=310)


            d=Entry(reg,width=13,font=('Arial',40),border=0,bg="#D8D8D8")
            d.place(x=255,y=410)


            e2 = Entry(reg,width=20,font=('Arial',40),border=0,bg="#D8D8D8")
            e2.place(x=420,y=510)
            e3 = Entry(reg,width=18,font=('Arial',30),border=0,bg="#D8D8D8")
            e3.place(x=390,y=630)
            

            reg.mainloop()

        def flats():

            flat = Toplevel()
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
                b.execute("INSERT INTO customer_registration VALUES(:Full_name, :Gender, :Permanent_address, :Contact_no, :Room_no)",{
                    'Full_name': e.get(),
                    'Gender': d.get(),
                    'Permanent_address': e2.get(),
                    'Contact_no': e3.get(),
                    'Room_no':e4.get()


                })
                hostel.commit()
                hostel.close()
                e.delete(0,END)
                d.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)

            
            def flat_book():
                f_book = Toplevel()
                f_book.title('Book your Hostel')
                f_book.geometry('1920x1000')
                f_book.configure(bg='#ffffff')
                bc = PhotoImage(file='flat_book.png')
                l = Label(f_book,image = bc,bg='black')
                l.pack()
                global e4
                l1 = Label(f_book,text='Enter the flat no. for booking',font=('Arial',20),bg='#0D98BA')
                l1.place(x=220,y=765)
                e4 = Entry(f_book,width=25,font=('Arial',20))
                e4.place(x=600,y=765)
                b = Button(f_book,text='Book',font=('Arial',14),cursor='hand2',command=insert)
                b.place(x=995,y=765)

                conn = sqlite3.connect('Flat.sql')
                c = conn.cursor()
                c.execute("SELECT *,oid FROM customer_registration")
                records = c.fetchall()
                # print(records)
                b = []
                for record in records:
                    b.append(record[4])

                if str(22) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=110)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1230,y=110)
                if str(20) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=200)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1230,y=200)
                if str(25) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=290)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1230,y=290)
                if str(27) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=390)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1230,y=390)
                if str(30) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=500)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=8)
                    l.place(x=1230,y=500)
                if str(35) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='white',height=1,width=9)
                    l.place(x=1230,y=610)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='white',height=1,width=8)
                    l.place(x=1230,y=610)
                if str(17) in b:
                    l = Label(f_book,text='Unavailable',fg='Red',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=700)
                else:
                    l = Label(f_book,text='Available',fg='Green',font=('Arial',18),bg='#FFFFDF',height=1,width=9)
                    l.place(x=1230,y=700)

                f_book.mainloop()


            i = PhotoImage(file='s (1).png')
            b = Button(flat,width=75,height=75,cursor='hand2',image=i,command=flat_book)
            b.place(x=640,y=765)
            e = Entry(flat,width=25,font=('Arial',40),border=0,bg="#D8D8D8")
            e.place(x=270,y=310)
            
            d=Entry(flat,width=13,font=('Arial',40),border=0,bg="#D8D8D8")
            d.place(x=255,y=410)


            e2 = Entry(flat,width=20,font=('Arial',40),border=0,bg="#D8D8D8")
            e2.place(x=420,y=510)
            e3 = Entry(flat,width=18,font=('Arial',30),border=0,bg="#D8D8D8")
            e3.place(x=390,y=630)
            # b1 = Button(flat,width=10,text='Submit',font=('arial',14),cursor='hand2')
            # b1.place(x=390,y=700)
            flat.mainloop()
          
        root1 = Tk()
        root1.title('Welcome Page')
        root1.geometry('1920x1000')
        root1.configure(bg='#ffffff')
        root1.iconbitmap('D:\\project_work\\search.ico')
        bc = PhotoImage(file='welcome1.png')
        l = Label(root1,image = bc,bg='black')
        l.pack()
        b = Button(root1,bg='red',text='Flat',fg='#ffffff',width=20,height=2,font='arial',cursor='hand2',border=0,command=flats)
        b.place(x=128,y=750)
        b1 = Button(root1,bg='red',text='Hostel',fg='#ffffff',width=20,height=2,font='arial',cursor='hand2',border=0,command=hostels)
        b1.place(x=1210,y=750)

        root.mainloop()
    elif username == "admin" and password == "admin":
        root.destroy()
        def query():
                conn = sqlite3.connect('Hostel.sql')
                c = conn.cursor()
                c.execute("SELECT *,oid FROM customer_registration")

                records = c.fetchall()
        
                print_records = ''
                for record in records:
                    print_records += (record[0]) + ' ' + (record[1]) + ' ' + (record[2]) + ' ' + (record[3]) + ' ' + (record[4]) + ' ' + '\t' + str(record[5]) + '\n'

                query_label = Label(f,text=print_records)
                query_label.place(x=75,y=300)


                conn.commit()
                conn.close()

        def query1():
                conn = sqlite3.connect('Flat.sql')
                c = conn.cursor()
                c.execute("SELECT *,oid FROM customer_registration")

                records = c.fetchall()

                print_records = ''
                for record in records:
                    print_records += (record[0]) + ' ' + (record[1]) + ' ' + (record[2]) + ' ' + (record[3]) + ' '+ (record[4]) + ' ' + '\t' + str(record[5]) + '\n'

                query_label = Label(f,text=print_records)
                query_label.place(x=75,y=300)
        

                conn.commit()
                conn.close()



        def delete():
            conn = sqlite3.connect('Hostel.sql')
            c = conn.cursor()
            c.execute("DELETE from customer_registration WHERE oid = " + e1.get())
            print('Deleted Successfully')

            e1.delete(0,END)
            conn.commit()
            conn.close()

        def delete1():
            conn = sqlite3.connect('Flat.sql')
            c = conn.cursor()
            c.execute("DELETE from customer_registration WHERE oid = " + e.get())
            print('Deleted Successfully')

            e.delete(0,END)
            conn.commit()
            conn.close()

        def update():
            conn = sqlite3.connect('Hostel.sql')
            c = conn.cursor()

            record_id = e1.get()

            c.execute(""" UPDATE customer_registration SET
                Full_name = :name,
                Gender = :gender,
                Permanent_address = :address,
                Contact_no = :num,
                Room_no = :room
                WHERE oid = :oid""",
                {   'name' : E0.get(),
                    'gender' : E1.get(),
                    'address' : E2.get(),
                    'num' : E3.get(),
                    'room': E4.get(),
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

            c.execute(""" UPDATE customer_registration SET
                Full_name = :name,
                Gender = :gender,
                Permanent_address = :address,
                Contact_no = :num,
                Room_no = :room
                WHERE oid = :oid""",
                {'name' : F0.get(),
                    'gender' : F1.get(),
                    'address' : F2.get(),
                    'num' : F3.get(),
                    'room': F4.get(),
                    'oid' : record_id
                }

                )
            conn.commit()
            conn.close()

            w.destroy()

        def new1():
            global w

            w = Tk()
            w.title('Update Window')
            w.geometry('400x500')

            b = sqlite3.connect('Flat.sql')
            conn = b.cursor()
            i = e.get()
            conn.execute(" SELECT * FROM customer_registration WHERE oid = " + i)

            records = conn.fetchall()

            global F0
            global F1
            global F2
            global F3
            global F4


            l = Label(w,text='First Name')
            l.place(x=10,y=10)

            l1 = Label(w,text='Gender')
            l1.place(x=10,y=35)

            l2 = Label(w,text='Permanent Address')
            l2.place(x=10,y=60)

            l3 = Label(w,text='Contact Number')
            l3.place(x=10,y=85)

            l4 = Label(w,text='Room.no')
            l4.place(x=10,y=110)


            F0 = Entry(w,width=30)
            F0.place(x=108,y=10)

            F1 = Entry(w,width=30)
            F1.place(x=108,y=35)

            F2 = Entry(w,width=30)
            F2.place(x=108,y=60)

            F3 = Entry(w,width=30)
            F3.place(x=108,y=85)

            F4 = Entry(w,width=30)
            F4.place(x=108,y=110)

            for i in records:
                F0.insert(0,i[0])
                F1.insert(0,i[1])
                F2.insert(0,i[2])
                F3.insert(0,i[3])
                F4.insert(0,i[4])

            b = Button(w,text='Save',cursor='hand2',width=26,command=update1)
            b.place(x=108,y=215)

        def new():
            global win

            win = Tk()
            win.title('Update Window')
            win.geometry('400x500')

            b = sqlite3.connect('Hostel.sql')
            conn = b.cursor()
            record = e1.get()
            conn.execute(" SELECT * FROM customer_registration WHERE oid = " + record)

            records = conn.fetchall()

            global E0
            global E1
            global E2
            global E3
            global E4


            l = Label(win,text='First Name')
            l.place(x=10,y=10)

            l1 = Label(win,text='Gender')
            l1.place(x=10,y=35)

            l2 = Label(win,text='Permanent Address')
            l2.place(x=10,y=60)

            l3 = Label(win,text='Contact Number')
            l3.place(x=10,y=85)

            l4 = Label(win,text='Room.no')
            l4.place(x=10,y=110)


            E0 = Entry(win,width=30)
            E0.place(x=108,y=10)

            E1 = Entry(win,width=30)
            E1.place(x=108,y=35)

            E2 = Entry(win,width=30)
            E2.place(x=108,y=60)

            E3 = Entry(win,width=30)
            E3.place(x=108,y=85)

            E4 = Entry(win,width=30)
            E4.place(x=108,y=110)

            for i in records:
                E0.insert(0,i[0])
                E1.insert(0,i[1])
                E2.insert(0,i[2])
                E3.insert(0,i[3])
                E4.insert(0,i[4])

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
    else:
        messagebox.showerror('Invalid','Invalid Username or Password!')

################################## SIGN UP ################################### 
def signup():
    window = Toplevel(root)
    window.title('SignUp')
    window.geometry('925x500+300+200')
    window.configure(bg='#fff')
    window.resizable(0,0)
    window.iconbitmap('D:\\project_work\\search.ico')
    bc = PhotoImage(file='signupback.png')
    lab = Label(window,image=bc,bg='#000')
    lab.pack()
    # takes the data in the entry box and makes it into dictionary in a txt file and compares
    def signu():
        username = user.get()
        password = pas.get()
        con_pass = conpas.get()
        if password == con_pass and password != 'Password':
            try:
                file = open('datasheet.txt','r+')
                d = file.read()
                r = ast.literal_eval(d)
                dict2 = {username:password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file =open('datasheet.txt','w')
                file.write(str(r))

                messagebox.showinfo('SignUp','Successfully signed up')
            except:
                file = open('datasheet.txt','w')
                pp = str({'Username':'Password'})
                file.write(pp)
                file.close()
        elif username == '' or username == 'Username':
             messagebox.showerror('Invalid','Enter username')
        elif password == '' or password == 'Password':
            messagebox.showerror('Invalid','Enter username')
        elif con_pass == '' or con_pass == 'password':
            messagebox.showerror('Invalid','Enter username')
        elif password != con_pass:
            messagebox.showerror('Invalid','Passwords do not match')

    def sign():
        window.destroy()


    fram = Frame(window,width=350,height=390,bg='#64A3FF')
    fram.place(x=300,y=45)

    head = Label(fram, text='Sign Up',fg='#D3C300',bg='#64A3FF',font=('Microsoft Tahei UI Light',23))
    head.place(x=120,y=5)

    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        name = user.get()
        if name == '':
            user.insert(0,'Username')

    l1 = Label(fram,text='Username:',fg='black',bg='#64A3FF',font=('Microsoft Tahei UI Light',11))
    l1.place(x=55,y=57)

    user = Entry(fram, width=25,fg='#313027',border = 0,bg='#64A3FF',font=('Microsoft Yahei UI light',11))
    user.place(x=57,y=80)
    user.insert(0,'Username')
    user.bind('<FocusIn>',on_enter)
    user.bind('<FocusOut>',on_leave)

    line = Frame(fram,width=255,height=2,bg='#000')
    line.place(x=55,y=107)

    def pas_enter(r):
        pas.delete(0,'end')
    def pas_leave(r):
        name = pas.get()
        if name == '':
            pas.insert(0,'Password')

    l2 = Label(fram,text='Password:',fg='black',bg='#64A3FF',font=('Microsoft Tahei UI Light',11))
    l2.place(x=55,y=130)

    pas = Entry(fram, width=25,fg='#313027',border = 0,bg='#64A3FF',font=('Microsoft Yahei UI light',11),show='*')
    pas.place(x=57,y=155)
    pas.insert(0,'Password')
    pas.bind('<FocusIn>',pas_enter)
    pas.bind('<FocusOut>',pas_leave)

    line1 = Frame(fram,width=260,height=2,bg='#000')
    line1.place(x=55,y=185)
    
    def c_enter(d):
        conpas.delete(0,'end')
    def c_leave(d):
        name = conpas.get()
        if name == '':
            conpas.insert(0,'Password')
    
    l3 = Label(fram,text='Confirm Password:',fg='black',bg='#64A3FF',font=('Microsoft Tahei UI Light',11))
    l3.place(x=55,y=210)
    
    conpas = Entry(fram, width=25,fg='#313027',border = 0,bg='#64A3FF',font=('Microsoft Yahei UI light',11),show='*')
    conpas.place(x=57,y=235)
    conpas.insert(0,'Password')
    conpas.bind('<FocusIn>',c_enter)
    conpas.bind('<FocusOut>',c_leave)
    
    line2 = Frame(fram,width=255,height=2,bg='#000')
    line2.place(x=55,y=265)
    
    s_u = Button(fram, width=30,pady=7,text='Sign Up',bg='#D3C300',fg='#64A3FF',border = 0,command=signu,cursor='hand2')
    s_u.place(x=75,y=280)
    
    l4 = Label(fram,text='I have an account.', fg='#000',bg='#64A3FF',cursor='hand2')
    l4.place(x=105,y=320)
    
    signin = Button(fram,width=6,text='Sign In',border=0,bg='#64A3FF',cursor='hand2',fg='#D3C300',command=sign)
    signin.place(x=205,y=320)
    
    window.mainloop()
    
    ##########################################################################

    #creating a frame where sign in features will be in
fram = Frame(root,width = 350, height=350, bg='#FCF3CF')
fram.place(x=300,y=75)

#Sign IN label 
heading = Label(fram, text='Sign In',fg='#57A1F8',bg='#FCF3CF',font=('Microsoft Tahei UI Light',23))
heading.place(x=130,y=35)

#username ra password ko entry boxes
def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

user = Entry(fram, width=25,fg='#313027',border=0,bg='#FCF3CF',font=('Microsoft Tahei UI Light',11))
user.place(x=40,y=110)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

line = Frame(fram,width=295,height=2,bg='black')
line.place(x=35,y=137)

def data_enter(d):
    pas.delete(0,'end')
def data_leave(d):
    name = pas.get()
    if name == '':
        pas.insert(0,'Password')

pas = Entry(fram, width=25,fg='#313027',border=0,bg='#FCF3CF',font=('Microsoft Tahei UI Light',11),show='*')
pas.place(x=40,y=170)
pas.insert(0,'Password')
pas.bind('<FocusIn>',data_enter)
pas.bind('<FocusOut>',data_leave)
line = Frame(fram,width=295,height=2,bg='black')
line.place(x=35,y=195)
#sign-in button
sign_in = Button(fram,width=25,pady=7,text='Log In',bg='#57A1F8',fg='white',border = 0,cursor='hand2',command=signin)
sign_in.place(x=85,y=234)
l1 = Label(fram,text="Don't have an account?",fg='black',bg='#FCF3CF',font=('Microsoft YaHei UI Light',9))
l1.place(x=80,y=280)
#sign-up button
sign_up = Button(fram, width=6,text='Sign Up',border=0,bg='#FCF3CF',fg='#57A1F8',cursor='hand2',command=signup)
sign_up.place(x=220,y=280)
root.mainloop()