from tkinter import *
from tkinter import messagebox
import ast

window = Tk()
window.title('SignUp')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(0,0)

def signup():
    username = user.get()
    password = pas.get()
    con_pass = conpas.get()
    if password == con_pass:
        try:
            file = open('datasheet.txt','r+')
            d = file.read()
            r = ast.literal_eval(d)
            dict2 = {username:password}
            r.update(dict2)
            file.truncate(0)
            file.close()

            file =open('datasheet.txt','w')
            w = file.write(str(r))

            messagebox.showinfo('SignUp','Successfully signed up')
        except:
            file = open('datasheet.txt','w')
            pp = str({'Username':'Password'})
            file.write(pp)
            file.close
    
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


fram = Frame(window,width=350,height=390,bg='#FCF3CF')
fram.place(x=300,y=45)

head = Label(fram, text='Sign Up',fg='#57A1F8',bg='#FCF3CF',font=('Microsoft Tahei UI Light',23))
head.place(x=120,y=5)

def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0,'Username')

l1 = Label(fram,text='Username:',fg='black',bg='#FCF3CF',font=('Microsoft Tahei UI Light',11))
l1.place(x=55,y=57)

user = Entry(fram, width=25,fg='#BDBDBD',border = 0,bg='#FCF3CF',font=('Microsoft Yahei UI light',11))
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

l2 = Label(fram,text='Password:',fg='black',bg='#FCF3CF',font=('Microsoft Tahei UI Light',11))
l2.place(x=55,y=130)

pas = Entry(fram, width=25,fg='#BDBDBD',border = 0,bg='#FCF3CF',font=('Microsoft Yahei UI light',11),show='*')
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

l3 = Label(fram,text='Confirm Password:',fg='black',bg='#FCF3CF',font=('Microsoft Tahei UI Light',11))
l3.place(x=55,y=210)

conpas = Entry(fram, width=25,fg='#BDBDBD',border = 0,bg='#FCF3CF',font=('Microsoft Yahei UI light',11),show='*')
conpas.place(x=57,y=235)
conpas.insert(0,'password')
conpas.bind('<FocusIn>',c_enter)
conpas.bind('<FocusOut>',c_leave)

line2 = Frame(fram,width=255,height=2,bg='#000')
line2.place(x=55,y=265)

s_u = Button(fram, width=30,pady=7,text='Sign Up',bg='#57A1F8',fg='#fcf3cf',border = 0,command=signup)
s_u.place(x=75,y=280)

l4 = Label(fram,text='I have an account.', fg='#000',bg='#fcf3cf',cursor='hand2')
l4.place(x=105,y=320)

signin = Button(fram,width=6,text='Sign In',border=0,bg='#fcf3cf',cursor='hand2',fg='#57a1f8',command=sign)
signin.place(x=205,y=320)


window.mainloop()