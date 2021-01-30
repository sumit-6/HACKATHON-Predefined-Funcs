import os
from tkinter import*
root=Tk()
root.geometry('900x200')
root.title("Graphing Calculator")
l=Label(root, text="      A Newtonian Graphing Calculator", font=("Arial Bold", 25))
l.grid(row=0,column=0)
def g1():
    os.system('graph_1.py')
def g2():
    os.system('graph_2.py')
def g3():
    os.system('graph_3.py')
def g4():
    os.system('graph_4.py')
def g5():
    os.system('graph_5.py')
def g6():
    os.system('graph_6.py')
    
b1=Button(root,text="e**(sin(x))**2",bg="yellow", fg="black",font=("Arial Bold", 15),command=g1)
b1.grid(row=2,column=0)
b2=Button(root,text="1+(1/cos(x))**2",bg="orange", fg="black",font=("Arial Bold", 15),command=g2)
b2.grid(row=2,column=1)
b3=Button(root,text="(cos(e**(x/4))",bg="green", fg="black",font=("Arial Bold", 15),command=g3)
b3.grid(row=4,column=0)
b4=Button(root,text="3*(sin(x))/x",bg="cyan", fg="black",font=("Arial Bold", 15),command=g4)
b4.grid(row=4,column=1)
b5=Button(root,text="1/x",bg="red", fg="black",font=("Arial Bold", 15),command=g5)
b5.grid(row=6,column=0)
b5=Button(root,text="2**(sin(x)",bg="blue", fg="black",font=("Arial Bold", 15),command=g6)
b5.grid(row=6,column=1)
root.mainloop()
