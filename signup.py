from tkinter import*
from tkinter import messagebox
win=Tk()
win.configure(background="teal")
win.geometry("750x600")
win.title("opay")
def reg():
    if ent1.get()=="" or ent2.get() =="":
        messagebox.showerror("dear user", 'fill in your info ')
    else:
        messagebox.showinfo('dear user ','Signup successful;')
def log ():
    win.destroy()
    import login
lab=Label(win,text="Welcome Back",background="teal",font=("times new roman",30,"bold"))
lab.place(x=220,y=150)
lab1=Label(win,text="Username:",background="teal",font=("times new roman",20,"bold"))
lab1.place(x=90,y=200)
ent1=Entry(win,width=30,bd=0,font=("arial",15,"bold"))
ent1.place(x=225,y=210)
lab2=Label(win,text="Password:",background="teal",font=("times new roman",20,"bold"))
lab2.place(x=90,y=290)
ent2=Entry(win,width=30,bd=0,font=("arial",15,"bold"))
ent2.place(x=225,y=290)
lab3=Label(win,text="E-mail:",background="teal",font=("times new roman",20,"bold"))
lab3.place(x=120,y=350)
ent3=Entry(win,width=35,bd=0,font=("arial",15,"bold"))
ent3.place(x=225,y=350)
btn=Button(win,width=25,height=2,bg='black',text='Register',fg='white',font=("times new roman",14,"bold"),cursor='hand2',command=reg)
btn.place(x=250,y=450)
win.mainloop()