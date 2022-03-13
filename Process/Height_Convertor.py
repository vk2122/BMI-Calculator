from tkinter import *
from tkinter import ttk

def hcon():
    root=Tk()
    root.geometry("650x475")
    root.title("Height Converter")
    root.fontsize=20
    lblInfo=Label(root,font=('helvetica',24,'bold'),text="Height Convertor",fg="Black",bd=10,anchor='w')
    lblInfo.pack()

    lblInfo=Label(root,font=('helvetica',22,'bold'),text="Input your height",fg="Black",bd=10,anchor='w')
    lblInfo.place()

    label_f=Label(root,text='Feets:',font=('Arial',22,'bold'))
    label_i=Label(root,text='Inches:',font=('Arial',22,'bold'))
    lblres=Label(root,font=("helvetica",22,"bold"),text=("Your Height:"),fg="Black",bd=10,anchor="w")
    
    lblInfo.place(x=1, y=80)
    label_f.place(x=25,y=150)
    label_i.place(x=25,y=210)
    lblres.place(x=1,y=270)

    f=IntVar()
    i=IntVar()

    F=Entry(root,width=5,bd=8,textvariable=f)
    I=Entry(root,width=5,bd=8,textvariable=i)
    F.place(x=150,y=150)
    I.place(x=150, y=210)

    def heicon(x,y):
        y += x * 12
        z = round(y * 2.54, 1)
        return z

    a=f.get()
    b=i.get()
    H=heicon(a,b)

    def close():
        root.destroy()
    
    btn=Button(root,text='Calculate',padx=16,bd=8,fg='black',font=('Arial',22,'bold'),command=heicon)
    btn.place(x=100,y=350)
    btn1=Button(root,text='Close',padx=16,bd=8,fg='black',font=('Arial',22,'bold'),command=close)
    btn1.place(x=400,y=350)          
    root.mainloop()
