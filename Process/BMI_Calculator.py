from tkinter import *
from tkinter import ttk
    
def bmi():
    root=Tk()
    root.geometry("625x500")
    root.title("BMI")
    root.fontsize=20
    lblInfo=Label(root,font=('helvetica',24,'bold'),text="BMI Calculator",fg="Black",bd=10,anchor='w')
    lblInfo.pack()

    label_h=Label(root,text='Enter your Height:',font=('Arial',22,'bold'))
    label_w=Label(root,text='Enter your Weight:',font=('Arial',22,'bold'))
    label_b=Label(root,text='Your BMI:',font=('arial',22,'bold'))
    
    label_h.place(x=25,y=90)
    label_w.place(x=25,y=150)
    label_b.place(x=25,y=210)

    h=IntVar()
    w=IntVar()

    H=Entry(root,width=10,bd=8,textvariable=h)
    W=Entry(root,width=10,bd=8,textvariable=w)
    H.place(x=300,y=93)
    W.place(x=300, y=153)

    height=h.get()
    weight=w.get()

    def bmicalc(h,w):
        h2=h*h
        index=(w/h2)*10000
        BMI=round(index,2)
        return BMI

    def close():
        root.destroy()
        
    btn=Button(root,text='Calculate',padx=16,bd=8,fg='black',font=('Arial',22,'bold'),command=bmicalc)
    btn.place(x=100,y=310)
    btn1=Button(root,text='Exit',padx=16,bd=8,fg='black',font=('Arial',22,'bold'),command=close)
    btn1.place(x=400,y=310)          
    root.mainloop()
