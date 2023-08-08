from tkinter import *
root = Tk()
root.title('Welcome Page')
root.geometry('1920x1000')
root.configure(bg='#ffffff')
root.iconbitmap('D:\\project_work\\search.ico')
bc = PhotoImage(file='welcome1.png')
l = Label(root,image = bc,bg='black')
l.pack()
b = Button(root,bg='red',text='Hotels',fg='#ffffff',width=20,height=2,font='arial')
b.place(x=128,y=750)

b1 = Button(root,bg='red',text='Hostels',fg='#ffffff',width=20,height=2,font='arial')
b1.place(x=1200,y=750)

root.mainloop()