from tkinter import*
from tkinter import messagebox
win=Tk()
win.configure(background="dark violet")
win.geometry("750x600")
win.title("opay")
def log():
    if ent1.get()=="" or ent2.get() =="":
        messagebox.showerror("Dear user", 'fill in your info ')
    else:
        messagebox.showinfo('Dear user ','login successful;')
def reg():
    win.destroy()
    import signup
lab=Label(win,text="Welcome Back",background="dark violet",fg='white',font=("times new roman",30,"bold"))
lab.place(x=220,y=50)
def log():
    if ent1.get()=="admin" and ent2.get() =="1234":
        win.destroy()
        import main
    else:
        messagebox.showerror("Dear user","username or password incorrect")
lab1=Label(win,text="Username:",background="dark violet",fg='white',font=("times new roman",20,"bold"))
lab1.place(x=90,y=150)
ent1=Entry(win,width=30,bd=0,font=("arial",15,"bold"))
ent1.place(x=225,y=160)
lab2=Label(win,text="Password:",background="dark violet",fg='white',font=("times new roman",20,"bold"))
lab2.place(x=90,y=230)
ent2=Entry(win,width=30,bd=0,font=("arial",15,"bold"))
ent2.place(x=225,y=230)
btn=Button(win,width=25,height=2,bg='black',text='Login',fg='white',font=("times new roman",14,"bold"),cursor='hand2',command=log)
btn.place(x=250,y=280)
acct=Label(win,text="Dont have an account?",background="dark violet",font=("times new roman",12))
acct.place(x=300,y=370)
btn1=Button(win,text='register',fg='tomato',bg='dark violet',font=("times new roman",12),cursor='hand2',bd=0,activebackground='teal',activeforeground='red',command=reg)
btn1.place(x=450,y=370)
win.mainloop()