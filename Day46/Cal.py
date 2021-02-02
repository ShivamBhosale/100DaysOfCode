from tkinter import *
root=Tk()
root.title("Simple Calculator")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_click(number):
    #e.delete(0,END) 
    e.insert(END,number)

def button_clear():
    e.delete(0,END)

def button_add():
    first_num=e.get()
    global f_num
    global math
    math="Addition"
    f_num = int(first_num)
    e.delete(0,END)

def button_sub():
    first_num=e.get()
    global f_num
    global math
    math="Subtraction"
    f_num = int(first_num)
    e.delete(0,END)

def button_mul():
    first_num=e.get()
    global f_num
    global math
    math="Mul"
    f_num = int(first_num)
    e.delete(0,END)
    
def button_div():
    first_num=e.get()
    global f_num
    global math
    math="Div"
    f_num = int(first_num)
    e.delete(0,END)

def button_per():
    first_num=e.get()
    global f_num
    global math
    math="Per"
    f_num = int(first_num)
    e.delete(0,END)

def button_equal():
    second_num=e.get()
    e.delete(0,END)
    if(math=="Addition"):
        e.insert(0,f_num+int(second_num))
    if(math=="Subtraction"):
        e.insert(0,f_num-int(second_num))
    if(math=="Mul"):
        e.insert(0,f_num*int(second_num))
    if(math=="Div"):
        e.insert(0,int(f_num/int(second_num)))
    if(math=="Per"):
        e.insert(0,int((f_num/int(second_num)*100)))


button_1 = Button(root, text="1", padx=40, pady=20,fg='Red', command=lambda: button_click(1))
button_2 = Button(root, text="2", padx=40, pady=20,fg='Red', command=lambda: button_click(2))
button_3 = Button(root, text="3", padx=40, pady=20,fg='Red', command=lambda: button_click(3))
button_4 = Button(root, text="4", padx=40, pady=20,fg='Red', command=lambda: button_click(4))
button_5 = Button(root, text="5", padx=40, pady=20,fg='Red', command=lambda: button_click(5))
button_6 = Button(root, text="6", padx=40, pady=20,fg='Red', command=lambda: button_click(6))
button_7 = Button(root, text="7", padx=40, pady=20,fg='Red', command=lambda: button_click(7))
button_8 = Button(root, text="8", padx=40, pady=20,fg='Red', command=lambda: button_click(8))
button_9 = Button(root, text="9", padx=40, pady=20,fg='Red', command=lambda: button_click(9))
button_0 = Button(root, text="0", padx=40, pady=20,fg='Red', command=lambda: button_click(0))
button_add=Button(root,text="+",padx=40,pady=20,fg='Red', command=button_add)
button_sub=Button(root,text="-",padx=40,pady=20,fg='Red', command=button_sub)
button_mul=Button(root,text="*",padx=40,pady=20,fg='Red', command=button_mul)
button_div=Button(root,text="/",padx=40,pady=20,fg='Red', command=button_div)
button_equal=Button(root,text="=",padx=40,pady=20,fg='Red',command=button_equal)
button_per=Button(root,text="%",padx=40,pady=20,fg='Red',command=button_per)
button_clear=Button(root,text="Clear",padx=79,pady=20,fg='Red', command=button_clear)

# grid the buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_0.grid(row=4,column=0)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_sub.grid(row=6,column=0)
button_mul.grid(row=6,column=1)
button_div.grid(row=6,column=2)
button_equal.grid(row=5,column=1)
button_per.grid(row=5,column=2)





root.mainloop()