from tkinter import *
import sqlite3
h_book = Tk()
h_book.title('Book your Hostel')
h_book.geometry('1920x1000')
h_book.configure(bg='#ffffff')
bc = PhotoImage(file='maskm.png')
l = Label(h_book,image = bc,bg='black')
l.pack()

l1 = Label(h_book,text='Enter the room no. for booking',font=('Arial',20),bg='#90ED91')
l1.place(x=220,y=765)
e = Entry(h_book,width=25,font=('Arial',20))
e.place(x=600,y=765)
b = Button(h_book,text='Book',font=('Arial',14),cursor='hand2')
b.place(x=995,y=765)

conn = sqlite3.connect('Hostel.sql')
c = conn.cursor()
c.execute("SELECT *,oid FROM customer_registration")
records = c.fetchall()
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