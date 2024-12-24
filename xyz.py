
from tkinter import *
r=Tk()
r.geometry("900x900")

l1=Label(r,text="name of owner")
l1.grid(row=0,column=1)
l2=Label(r,text="name of the company")
l2.grid(row=1,column=1)
l3=Label(r,text="address of the company")
l3.grid(row=2,column=1)
l4=Label(r,text="contract person name")
l4.grid(row=3,column=1)
l5=Label(r,text="telephone no")
l5.grid(row=4,column=1)
l6=Label(r,text="transport amount")
l6.grid(row=5,column=1)
l7=Label(r,text=" delivery charge")
l7.grid(row=6,column=1)
l8=Label(r,text="salary of workers")
l8.grid(row=7,column=1)





e1=Entry(r)
e1.grid(row=0,column=2)
e2=Entry(r)
e2.grid(row=1,column=2)
e3=Entry(r)
e3.grid(row=2,column=2)
e4=Entry(r)
e4.grid(row=3,column=2)
e5=Entry(r)
e5.grid(row=4,column=2)
e6=Entry(r)
e6.grid(row=5,column=2)
e7=Entry(r)
e7.grid(row=6,column=2)
e8=Entry(r)
e8.grid(row=7,column=2)


def submit():
   print(e1.get())
   print(e2.get())
   print(e3.get())
   print(e4.get())
   print(e5.get())

   print(e6.get())
   print(e7.get())
   print(e8.get())
  
 
def sub():
    a=int(e6.get())
    b=int(e7.get())
    c=a-b

   

b=Button(r,text="sub",command=lambda:sub())
b.grid(row=3,column=3) 
   
 
b=Button(r,text="submit",command=lambda:submit())

b.grid(row=15,column=15) 

r.mainloop()  


