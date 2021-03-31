import tkinter
from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("250x400+555+184")
root.resizable(0,0)
root.title("Calculator")

A = 0
dot = 1

val = ""
oprtr = ""

def btneq_isclicked():
    global A
    global oprtr
    global val
    if oprtr == "+":
        B = val.split("+")[1]
        C = float(A)+float(B)
        data.set(round(C,3))
        val=str(C)
    elif oprtr == "-":
        B = val.split("-")[1]
        C = float(A)-float(B)
        data.set(round(C,3))
        val=str(C)
    elif oprtr == "*":
        B = val.split("*")[1]
        C = float(A)*float(B)
        data.set(round(C,3))
        val=str(C)
    elif oprtr == "/":
        B = val.split("/")[1]
        if int(B) == 0:
            messagebox.showerror("Error","Division by 0 is not allowed")
            A = ""
            val = ""
            data.set(val)
        else:
            C = float(A)/float(B)
            data.set(round(C,3))
            val=str(C)
    elif oprtr == "^":
        B = int(val.split("^")[1])
        C = pow(int(A),B)
        data.set(str(C))
        val=str(C)
    elif oprtr == "%":
        B = val.split("%")[1]
        C = float(A)%float(B)
        data.set(round(C,3))
        val=str(C)


def btnclr_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = 0
    oprtr = ""
    val = ""
    data.set(val)
    
def btnpls_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = val
    oprtr = "+"
    val = val + "+"
    data.set(val)
    
def btnmns_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = val
    oprtr = "-"
    val = val + "-"
    data.set(val)
    
def btnx_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = val
    oprtr = "*"
    val = val + "*"
    data.set(val)
    
def btndvd_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = val
    oprtr = "/"
    val = val + "/"
    data.set(val)
    
def btnpwr_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = val
    oprtr = "^"
    val = val + "^"
    data.set(val)
    
def btnmdl_isclicked():
    global A
    global oprtr
    global val
    global dot
    dot = 1
    A = val
    oprtr = "%"
    val = val + "%"
    data.set(val)
    
def btnpm_isclicked():
    global A
    global oprtr
    global val
    A = val
    A=round(0-float(A),3)
    data.set(str(A))
    val = str(A)


def btn0_isclicked():
    global val
    val = val + "0"
    data.set(val)
    
def btn1_isclicked():
    global val
    val = val + "1"
    data.set(val)
    
def btn2_isclicked():
    global val
    val = val + "2"
    data.set(val)
    
def btn3_isclicked():
    global val
    val = val + "3"
    data.set(val)
    
def btn4_isclicked():
    global val
    val = val + "4"
    data.set(val)
    
def btn5_isclicked():
    global val
    val = val + "5"
    data.set(val)
    
def btn6_isclicked():
    global val
    val = val + "6"
    data.set(val)
    
def btn7_isclicked():
    global val
    val = val + "7"
    data.set(val)
    
def btn8_isclicked():
    global val
    val = val + "8"
    data.set(val)
    
def btn9_isclicked():
    global val
    val = val + "9"
    data.set(val)
    
def btndot_isclicked():
    global val
    global dot
    if dot == 1:
        dot+=1
        val = val + "."
        data.set(val)
    

data = StringVar()

lbl = Label(root, text="Label",anchor=SE,font=("Consolas",20), textvariable = data, background="#ffffff", fg = "#000000")
lbl.pack(expand=True,fill="both")

f0 = Frame(root, bg="#011100")
f0.pack(expand=True, fill="both")
btnclr = Button(f0, text="C",font=("Consolas",22),relief=FLAT,command=btnclr_isclicked)
btnclr.pack(side=LEFT,expand=True,fill="both")
btnpwr = Button(f0, text="^",font=("Consolas",22),relief=FLAT,command=btnpwr_isclicked)
btnpwr.pack(side=LEFT,expand=True,fill="both")
btnmdl = Button(f0, text="%",font=("Consolas",22),relief=FLAT,command=btnmdl_isclicked)
btnmdl.pack(side=LEFT,expand=True,fill="both")
btnpls = Button(f0, text="+",font=("Consolas",22),relief=FLAT,command=btnpls_isclicked)
btnpls.pack(side=LEFT,expand=True,fill="both")


f1 = Frame(root, bg="#000000")
f1.pack(expand=True, fill="both")
btn1 = Button(f1, text="1",font=("Consolas",22),relief=FLAT,command=btn1_isclicked)
btn1.pack(side=LEFT,expand=True,fill="both")
btn2 = Button(f1, text="2",font=("Consolas",22),relief=FLAT,command=btn2_isclicked)
btn2.pack(side=LEFT,expand=True,fill="both")
btn3 = Button(f1, text="3",font=("Consolas",22),relief=FLAT,command=btn3_isclicked)
btn3.pack(side=LEFT,expand=True,fill="both")
btnmns = Button(f1, text="-",font=("Consolas",22),relief=FLAT,command=btnmns_isclicked)
btnmns.pack(side=LEFT,expand=True,fill="both")

f2 = Frame(root, bg="#009000")
f2.pack(expand=True, fill="both")
btn4 = Button(f2, text="4",font=("Consolas",22),relief=FLAT,command=btn4_isclicked)
btn4.pack(side=LEFT,expand=True,fill="both")
btn5 = Button(f2, text="5",font=("Consolas",22),relief=FLAT,command=btn5_isclicked)
btn5.pack(side=LEFT,expand=True,fill="both")
btn6 = Button(f2, text="6",font=("Consolas",22),relief=FLAT,command=btn6_isclicked)
btn6.pack(side=LEFT,expand=True,fill="both")
btnx = Button(f2, text="*",font=("Consolas",22),relief=FLAT,command=btnx_isclicked)
btnx.pack(side=LEFT,expand=True,fill="both")

f3 = Frame(root, bg="#099900")
f3.pack(expand=True, fill="both")
btn7 = Button(f3, text="7",font=("Consolas",22),relief=FLAT,command=btn7_isclicked)
btn7.pack(side=LEFT,expand=True,fill="both")
btn8 = Button(f3, text="8",font=("Consolas",22),relief=FLAT,command=btn8_isclicked)
btn8.pack(side=LEFT,expand=True,fill="both")
btn9 = Button(f3, text="9",font=("Consolas",22),relief=FLAT,command=btn9_isclicked)
btn9.pack(side=LEFT,expand=True,fill="both")
btndvd = Button(f3, text="/",font=("Consolas",22),relief=FLAT,command=btndvd_isclicked)
btndvd.pack(side=LEFT,expand=True,fill="both")

f4 = Frame(root, bg="#011100")
f4.pack(expand=True, fill="both")
btnpm = Button(f4, text="±",font=("Consolas",22),relief=FLAT,command=btnpm_isclicked)
btnpm.pack(side=LEFT,expand=True,fill="both")
btn0 = Button(f4, text="0",font=("Consolas",22),relief=FLAT,command=btn0_isclicked)
btn0.pack(side=LEFT,expand=True,fill="both")
btndot = Button(f4, text=".",font=("Consolas",22),relief=FLAT,command=btndot_isclicked)
btndot.pack(side=LEFT,expand=True,fill="both")
btneq = Button(f4, text="=",font=("Consolas",22),relief=FLAT,command=btneq_isclicked)
btneq.pack(side=LEFT,expand=True,fill="both")

root.mainloop()