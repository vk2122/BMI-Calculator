from tkinter import *
from tkinter import ttk
import Process.Height_Convertor as hecon
import Process.BMI_Calculator as Bmi
import time
import datetime

root=Tk()
root.geometry("500x300")
root.title("BMI")

localtime=time.asctime(time.localtime(time.time()))
         
lblInfo=Label(root,font=('helvetica',24,'bold'),text="BMI Calculator",fg="Black",bd=10,anchor='w')
lblInfo.pack()

lblInfo=Label(root,font=('arial',12,'bold'),text=localtime,fg="Steel Blue",bd=10,anchor='w')
lblInfo.pack()

m=IntVar()
def con():
    a=m.get()
    if a==1:
          hecon.hcon()
    elif a==2:
          Bmi.bmi()
    else:
        root.destroy()

r_g=Radiobutton(root,font=('arial',12,'bold'),text="Height Converter",variable=m,value=1)
r_a=Radiobutton(root,font=('arial',12,'bold'),text="BMI Calculator",variable=m,value=2)
r_e=Radiobutton(root,font=('arial',12,'bold'),text="Exit.",variable=m,value=3)
btn=Button(root,text='Continue',padx=16,bd=8,fg='black',font=('Arial',12,'bold'),command=con)
r_g.place(x=1,y=110)
r_a.place(x=1,y=150)
r_e.place(x=1,y=190)
btn.place(x=100,y=230)
root.mainloop()
