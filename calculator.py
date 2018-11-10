from tkinter import *
import math 
class calci:
    def __init__(self):
        self.total =0
        self.exprr=""
    def enter(self,num):
        self.exprr=str(self.exprr)
        self.exprr=self.exprr+str(num)
        equation.set(self.exprr)
    def sin(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.sin(math.radians(self.total))
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def cos(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.cos(math.radians(self.total))
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def tan(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.tan(math.radians(self.total))
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def tanh(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.tanh(math.radians(self.total))
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def sinh(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.sinh(math.radians(self.total))
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def cosh(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.cosh(math.radians(self.total))
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def log(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.log(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def exp(self):
        try:
            self.total=int(self.exprr)
            self.exprr=math.exp(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def pi(self):
        try:
            #self.total=int(self.exprr)
            self.exprr=math.pi
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def log2(self):
        try:
            self.total=int(self.exprr)
            self.exprr=math.log2(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def squareroot(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.sqrt(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def square(self):
        try:
            self.total=float(self.exprr)
            self.exprr=(self.total)**2
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def degrees(self):
        try:
            self.total=int(self.exprr)
            self.exprr=math.degrees(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def factorial(self):
        try:
            self.total=int(float(self.exprr))
            self.exprr=math.factorial(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def radians(self):
        try:
            self.total=int(self.exprr)
            self.exprr=math.radians(self.total)
            equation.set(self.exprr)
        except:
            equation.set("Error!")
            self.exprr="" 
    def equat(self):
        try:
            self.exprr=str(eval(self.exprr))
            equation.set(self.exprr)                
        except:
            equation.set("Error!")
            self.exprr=""
    def clear(self):
        #global exprr
        equation.set("")
        self.exprr=""
cal1=Tk()
cal1.configure(background="light blue",border=7)
cal1.title('Calculator')
#cal1.geometry("265x254")
global call
cal = Frame (cal1)
equation=StringVar()
exprr_field=Entry(cal1,textvariable=equation,justify=RIGHT)
exprr_field.grid(columnspan=4,ipadx=60,ipady=10)
equation.set("0")
def scientific():
    global cal
    cal.destroy()
    cal = Frame (cal1)
    mod=Button(cal,text=' % ',fg='black',bg='light grey',command=lambda: obj.enter("%"),height=2,width=7) 
    mod.grid(row=2,column=0,padx=0,pady=1,sticky="nsew") 
    leftbrac=Button(cal,text=' ( ',fg='black',bg='light grey',command=lambda: obj.enter("("),height=2,width=7) 
    leftbrac.grid(row=2,column=1,padx=0,pady=1,sticky="nsew") 
    rightbrac=Button(cal,text=' ) ',fg='black',bg='light grey',command=lambda: obj.enter(")"),height=2,width=7) 
    rightbrac.grid(row=2,column=2,padx=0,pady=1,sticky="nsew")
    divide=Button(cal,text=' / ',fg='black',bg='light grey',command=lambda: obj.enter("/"),height=2,width=7) 
    divide.grid(row=2,column=3,padx=1,pady=1,sticky="nsew")
    b1=Button(cal,text=' 1 ',fg='black',bg='light grey',activebackground='light grey',activeforeground='black',command=lambda: obj.enter(1),height=2,width=7)
    b1.grid(row=3,column=0,padx=1,pady=1,sticky="nsew")  
    b2=Button(cal,text=' 2 ',fg='black',bg='light grey',command=lambda: obj.enter(2),height=2,width=7) 
    b2.grid(row=3,column=1,padx=0,pady=1,sticky="nsew") 
    b3=Button(cal,text=' 3 ',fg='black',bg='light grey',command=lambda: obj.enter(3),height=2,width=7) 
    b3.grid(row=3,column=2,padx=1,pady=1,sticky="nsew") 
    b4=Button(cal,text=' 4 ',fg='black',bg='light grey',command=lambda: obj.enter(4),height=2,width=7) 
    b4.grid(row=4, column=0,padx=1,pady=1,sticky="nsew")
    b5=Button(cal,text=' 5 ',fg='black',bg='light grey',command=lambda: obj.enter(5),height=2,width=7) 
    b5.grid(row=4,column=1,padx=1,pady=1,sticky="nsew")
    b6=Button(cal,text=' 6 ',fg='black',bg='light grey',command=lambda: obj.enter(6),height=2,width=7) 
    b6.grid(row=4,column=2,padx=1,pady=1,sticky="nsew")
    b7=Button(cal,text=' 7 ',fg='black',bg='light grey',command=lambda: obj.enter(7),height=2,width=7) 
    b7.grid(row=5,column=0,padx=1,pady=1,sticky="nsew")
    b8=Button(cal,text=' 8 ',fg='black',bg='light grey',command=lambda: obj.enter(8),height=2,width=7) 
    b8.grid(row=5,column=1,padx=1,pady=1,sticky="nsew")
    b9=Button(cal,text=' 9 ',fg='black',bg='light grey',command=lambda: obj.enter(9),height=2,width=7) 
    b9.grid(row=5,column=2,padx=1,pady=1,sticky="nsew")
    b0=Button(cal,text=' 0 ',fg='black',bg='light grey',command=lambda: obj.enter(0),height=2,width=7) 
    b0.grid(row=6, column=1,padx=1,pady=1,sticky="nsew")
    plus=Button(cal,text=' + ',fg='black',bg='light grey',command=lambda: obj.enter("+"),height=2,width=7) 
    plus.grid(row=3, column=3,padx=1,pady=1,sticky="nsew")
    minus=Button(cal,text=' - ',fg='black',bg='light grey',command=lambda: obj.enter("-"),height=2,width=7) 
    minus.grid(row=4, column=3,padx=1,pady=1,sticky="nsew") 
    multiply=Button(cal,text=' * ',fg='black',bg='light grey',command=lambda: obj.enter("*"),height=2,width=7) 
    multiply.grid(row=5,column=3,padx=1,pady=1,sticky="nsew")
    dot=Button(cal,text=' . ',fg='black',bg='light grey',command=lambda: obj.enter("."),height=2,width=7) 
    dot.grid(row=6,column=2,padx=1,pady=1,sticky="nsew")
    equal=Button(cal,text=' = ',fg='black',bg='light grey',command=lambda: obj.equat(),height=2,width=7) 
    equal.grid(row=6,column=3,padx=1,pady=1,sticky="nsew") 
    clear=Button(cal,text='Clear',fg='black',bg='light grey',command=lambda: obj.clear(),height=2,width=7) 
    clear.grid(row=6,column=0,padx=1,pady=1,sticky="nsew")
    #more=Button(cal,text='More...',fg='red',bg='light grey',command=lambda :obj.scientific(),height=1,width=28)
    #more.grid(row=6,padx=1,pady=5,columnspan=4)
    b11=Button(cal,text=' n! ',fg='black',bg='light grey',command=lambda: obj.factorial(),height=2,width=7)
    b11.grid(row=7,column=0,padx=1,pady=1,sticky="nsew")  
    b12=Button(cal,text=' pi ',fg='black',bg='light grey',command=lambda: obj.pi(),height=2,width=7)
    b12.grid(row=7,column=1,padx=1,pady=1,sticky="nsew")
    b13=Button(cal,text=' sin ',fg='black',bg='light grey',command=lambda: obj.sin(),height=2,width=7)
    b13.grid(row=7,column=2,padx=1,pady=1,sticky="nsew")
    b14=Button(cal,text=' cos ',fg='black',bg='light grey',command=lambda: obj.cos(),height=2,width=7)
    b14.grid(row=7, column=3,padx=1,pady=1,sticky="nsew")
    b15=Button(cal,text=' tan ',fg='black',bg='light grey',command=lambda: obj.tan(),height=2,width=7)
    b15.grid(row=8,column=0,padx=1,pady=1,sticky="nsew")
    b16=Button(cal,text=' log ',fg='black',bg='light grey',command=lambda: obj.log(),height=2,width=7)
    b16.grid(row=8,column=1,padx=1,pady=1,sticky="nsew")
    b17=Button(cal,text=' exp ',fg='black',bg='light grey',command=lambda: obj.exp(),height=2,width=7)
    b17.grid(row=8,column=2,padx=1,pady=1,sticky="nsew")
    b18=Button(cal,text=' sinh ',fg='black',bg='light grey',command=lambda: obj.sinh(),height=2,width=7)
    b18.grid(row=8,column=3,padx=1,pady=1,sticky="nsew")
    b19=Button(cal,text=' cosh ',fg='black',bg='light grey',command=lambda: obj.cosh(),height=2,width=7)
    b19.grid(row=9,column=0,padx=1,pady=1,sticky="nsew")
    b20=Button(cal,text=' tanh ',fg='black',bg='light grey',command=lambda: obj.tanh(),height=2,width=7)
    b20.grid(row=9,column=1,padx=1,pady=1,sticky="nsew")
    b21=Button(cal,text=' degree ',fg='black',bg='light grey',command=lambda: obj.degrees(),height=2,width=7)
    b21.grid(row=9,column=2,padx=1,pady=1,sticky="nsew")
    b22=Button(cal,text=' radian ',fg='black',bg='light grey',command=lambda: obj.radians(),height=2,width=7)
    b22.grid(row=9,column=3,padx=1,pady=1,sticky="nsew")
    b23=Button(cal,text=' log2 ',fg='black',bg='light grey',command=lambda: obj.log2(),height=2,width=7)
    b23.grid(row=10,column=0,padx=1,pady=1,sticky="nsew")
    b23=Button(cal,text=' x^y ',fg='black',bg='light grey',command=lambda: obj.enter("**"),height=2,width=7)
    b23.grid(row=10,column=1,padx=1,pady=1,sticky="nsew")
    sq=Button(cal,text=' sqrt ',fg='black',bg='light grey',command=lambda: obj.squareroot(),height=2,width=7) 
    sq.grid(row=10,column=2,padx=0,pady=1,sticky="nsew") 
    squaree=Button(cal,text=' x^2 ',fg='black',bg='light grey',command=lambda: obj.square(),height=2,width=7) 
    squaree.grid(row=10,column=3,padx=0,pady=1,sticky="nsew")
    cal.grid()

def standard():
    global cal
    cal.destroy()
    cal = Frame (cal1)
    mod=Button(cal,text=' % ',fg='black',bg='light grey',command=lambda: obj.enter("%"),height=2,width=7) 
    mod.grid(row=2,column=0,padx=0,pady=1,sticky="nsew") 
    leftbrac=Button(cal,text=' ( ',fg='black',bg='light grey',command=lambda: obj.enter("("),height=2,width=7) 
    leftbrac.grid(row=2,column=1,padx=0,pady=1,sticky="nsew") 
    rightbrac=Button(cal,text=' ) ',fg='black',bg='light grey',command=lambda: obj.enter(")"),height=2,width=7) 
    rightbrac.grid(row=2,column=2,padx=0,pady=1,sticky="nsew")
    divide=Button(cal,text=' / ',fg='black',bg='light grey',command=lambda: obj.enter("/"),height=2,width=7) 
    divide.grid(row=2,column=3,padx=1,pady=1,sticky="nsew")
    b1=Button(cal,text=' 1 ',fg='black',bg='light grey',activebackground='light grey',activeforeground='black',command=lambda: obj.enter(1),height=2,width=7)
    b1.grid(row=3,column=0,padx=1,pady=1,sticky="nsew")  
    b2=Button(cal,text=' 2 ',fg='black',bg='light grey',command=lambda: obj.enter(2),height=2,width=7) 
    b2.grid(row=3,column=1,padx=0,pady=1,sticky="nsew") 
    b3=Button(cal,text=' 3 ',fg='black',bg='light grey',command=lambda: obj.enter(3),height=2,width=7) 
    b3.grid(row=3,column=2,padx=1,pady=1,sticky="nsew") 
    b4=Button(cal,text=' 4 ',fg='black',bg='light grey',command=lambda: obj.enter(4),height=2,width=7) 
    b4.grid(row=4, column=0,padx=1,pady=1,sticky="nsew")
    b5=Button(cal,text=' 5 ',fg='black',bg='light grey',command=lambda: obj.enter(5),height=2,width=7) 
    b5.grid(row=4,column=1,padx=1,pady=1,sticky="nsew")
    b6=Button(cal,text=' 6 ',fg='black',bg='light grey',command=lambda: obj.enter(6),height=2,width=7) 
    b6.grid(row=4,column=2,padx=1,pady=1,sticky="nsew")
    b7=Button(cal,text=' 7 ',fg='black',bg='light grey',command=lambda: obj.enter(7),height=2,width=7) 
    b7.grid(row=5,column=0,padx=1,pady=1,sticky="nsew")
    b8=Button(cal,text=' 8 ',fg='black',bg='light grey',command=lambda: obj.enter(8),height=2,width=7) 
    b8.grid(row=5,column=1,padx=1,pady=1,sticky="nsew")
    b9=Button(cal,text=' 9 ',fg='black',bg='light grey',command=lambda: obj.enter(9),height=2,width=7) 
    b9.grid(row=5,column=2,padx=1,pady=1,sticky="nsew")
    b0=Button(cal,text=' 0 ',fg='black',bg='light grey',command=lambda: obj.enter(0),height=2,width=7) 
    b0.grid(row=6, column=1,padx=1,pady=1,sticky="nsew")
    plus=Button(cal,text=' + ',fg='black',bg='light grey',command=lambda: obj.enter("+"),height=2,width=7) 
    plus.grid(row=3, column=3,padx=1,pady=1,sticky="nsew")
    minus=Button(cal,text=' - ',fg='black',bg='light grey',command=lambda: obj.enter("-"),height=2,width=7) 
    minus.grid(row=4, column=3,padx=1,pady=1,sticky="nsew") 
    multiply=Button(cal,text=' * ',fg='black',bg='light grey',command=lambda: obj.enter("*"),height=2,width=7) 
    multiply.grid(row=5,column=3,padx=1,pady=1,sticky="nsew")
    dot=Button(cal,text=' . ',fg='black',bg='light grey',command=lambda: obj.enter("."),height=2,width=7) 
    dot.grid(row=6,column=2,padx=1,pady=1,sticky="nsew")
    equal=Button(cal,text=' = ',fg='black',bg='light grey',command=lambda: obj.equat(),height=2,width=7) 
    equal.grid(row=6,column=3,padx=1,pady=1,sticky="nsew") 
    clear=Button(cal,text='Clear',fg='black',bg='light grey',command=lambda: obj.clear(),height=2,width=7) 
    clear.grid(row=6,column=0,padx=1,pady=1,sticky="nsew")
    cal.grid()

obj=calci()
def Exit():
    cal1.destroy()
    return
standard()
menubar = Menu(cal1)
filemenu = Menu(menubar, tearoff =0)
menubar.add_cascade(label ="File",menu=filemenu)
filemenu.add_command(label ="Standard", command =standard)
filemenu.add_command(label ="Scientific", command =scientific)
filemenu.add_command(label ="Exit",command = Exit)
cal1.config(menu=menubar)
cal1.mainloop()
