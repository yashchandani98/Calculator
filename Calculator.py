from tkinter import *
window=Tk()
window.title("Calculator")
window.geometry("305x305")
window.resizable(0,0)
expression=''
def cls():
    global expression
    expression=''
    entry.delete(0,END)
    entry.insert(0,expression)
def enter(text):
    global expression
    expression=entry.get()
    expression+=text
    entry.delete(0,END)
    entry.insert(0,expression)
def last_remove():
    global expression
    expression=entry.get()
    expression = expression[:-1]
    entry.delete(0,END)
    entry.insert(0,expression)
def result(event):
    global expression
    expression=entry.get()
    result =eval(expression)
    entry.delete(0,END)
    entry.insert(0,result)
window.bind('<Return>', result)
f1=Frame(window,width=312,height=5).pack(side= TOP)
entry=Entry(f1,textvariable="input_number",bg="white",width=50,font=("Arial Bold",20),justify="right")
#entry.grid(row=0,column=0)
entry.pack(ipady=10)
entry.pack(fill="y")
f2=Frame(window,width=312,height=319)
f2.pack()
b1 = Button(f2,text="C",width=10,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",10),command=cls)
b1.pack(side= LEFT)
b1 = Button(f2,text="←",width=10,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",10),command=last_remove)
b1.pack(side= LEFT)
b1 = Button(f2,text="Close",width=10,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",10),command=window.destroy)
b1.pack(side= LEFT)
f3=Frame(window,width=312,height=319)
f3.pack()
bt1 = Button(f3,text="7",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("7"))
bt1.pack(side= LEFT)
bt1 = Button(f3,text="8",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("8"))
bt1.pack(side= LEFT)
bt1 = Button(f3,text="9",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("9"))
bt1.pack(side= LEFT)
bt1 = Button(f3,text="/",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("/"))
bt1.pack(side= LEFT)
bt1 = Button(f3,text="%",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("%"))
bt1.pack(side= LEFT)
f4=Frame(window,width=312,height=319)
f4.pack()
bt1 = Button(f4,text="4",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("4"))
bt1.pack(side= LEFT)
bt1 = Button(f4,text="5",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("5"))
bt1.pack(side= LEFT)
bt1 = Button(f4,text="6",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("6"))
bt1.pack(side= LEFT)
bt1 = Button(f4,text="-",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("-"))
bt1.pack(side= LEFT)
bt1 = Button(f4,text="*",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("*"))
bt1.pack(side= LEFT)
f5=Frame(window,width=312,height=319)
f5.pack()
bt1 = Button(f5,text="1",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("1"))
bt1.pack(side= LEFT)
bt1 = Button(f5,text="2",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("2"))
bt1.pack(side= LEFT)
bt1 = Button(f5,text="3",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("3"))
bt1.pack(side= LEFT)
bt1 = Button(f5,text="+",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("+"))
bt1.pack(side= LEFT)
bt1 = Button(f5,text="=",width=6,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command=lambda: result("+"))
bt1.pack(side= LEFT)
f6=Frame(window,width=312,height=319)
f6.pack()
bt1 = Button(f6,text="0",width=18,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("0"))
bt1.pack(side= LEFT)
bt1 = Button(f6,text=".",width=18,height=2,bd=3,bg="#eee",cursor="hand2",font=("Arial Bold",8),command= lambda: enter("."))
bt1.pack(side= LEFT)
window.mainloop()