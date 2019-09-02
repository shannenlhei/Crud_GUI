from tkinter import *
from tkinter import messagebox

list =[]



def name ():
    name = "Welcome, new employee "+"\n" + t1.get() + " " + t2.get() + " :)"
    messagebox.showinfo("Welcome" , name)
    

master = Tk()
Label (master, text= "First Name").grid(row= 0, padx=20, pady=10)
Label (master, text= "Last Name").grid(row=1, padx=20, pady=10)
Label (master, text= "Position").grid(row=2, padx=20, pady= 10)
Label (master, text= "Employees Name").grid(row= 5, padx=20, pady=10)
Label (master, text= "Position").grid(row=5, column= 2,padx=20, pady=10)
t1= Entry(master)
list.append(t1)
t2= Entry(master)
list.append(t2)
t3= Entry(master)
list.append(t3)

t1.grid(row= 0, column= 1, padx= 20, pady=10)
t2.grid(row=1, column= 1, padx= 20, pady= 10)
t3.grid(row=2, column=1, padx=20, pady=10)

b1 = Button(master, text="Add", command=name)
b1.grid(row=3 , column= 1, padx=20, pady= 10)
mainloop()
