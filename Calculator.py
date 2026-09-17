import tkinter as tk
window=tk.Tk()
window.title("GUI CALCULATOR")
window.geometry("350x500")
display=tk.Entry(window,width=30,font=("arial",24),justify="right",bg="black",fg="white")
display.insert(0,"")
display.pack()
window.configure(bg="black")

def press_number(number):
    display.insert(tk.END,number)

#Frame
frame=tk.Frame(window)
frame.pack()

#Button
button_1=tk.Button(frame,text="1",command=lambda:press_number("1"),width=5,height=2,font=("arial",14))
button_1.grid(row=3,column=0)

button_2=tk.Button(frame,text="2",command=lambda:press_number("2"),width=5,height=2,font=("arial",14))
button_2.grid(row=3,column=1)

button_3=tk.Button(frame,text="3",command=lambda:press_number("3"),width=5,height=2,font=("arial",14))
button_3.grid(row=3,column=2)

button_4=tk.Button(frame,text="4",command=lambda:press_number("4"),width=5,height=2,font=("arial",14))
button_4.grid(row=2,column=0)

button_5=tk.Button(frame,text="5",command=lambda:press_number("5"),width=5,height=2,font=("arial",14))
button_5.grid(row=2,column=1)

button_6=tk.Button(frame,text="6",command=lambda:press_number("6"),width=5,height=2,font=("arial",14))
button_6.grid(row=2,column=2)

button_7=tk.Button(frame,text="7",command=lambda:press_number("7"),width=5,height=2,font=("arial",14))
button_7.grid(row=1,column=0)

button_8=tk.Button(frame,text="8",command=lambda:press_number("8"),width=5,height=2,font=("arial",14))
button_8.grid(row=1,column=1)

button_9=tk.Button(frame,text="9",command=lambda:press_number("9"),width=5,height=2,font=("arial",14))
button_9.grid(row=1,column=2)

button_0=tk.Button(frame,text="0",command=lambda:press_number("0"),width=5,height=2,font=("arial",14))
button_0.grid(row=4,column=0)

button_Decimal=tk.Button(frame,text=".",command=lambda:press_number("."),width=5,height=2,font=("arial",14))
button_Decimal.grid(row=4,column=1)

#OPERATORS

def press_operator(operator):
    display.insert(tk.END ,operator)

button_plus=tk.Button(frame,text="+",command=lambda:press_operator("+"),width=5,height=2,font=("arial",14))
button_plus.grid(row=3,column=3)

button_minus=tk.Button(frame,text="-",command=lambda:press_operator("-"),width=5,height=2,font=("arial",14))
button_minus.grid(row=2,column=3)

button_multiplication=tk.Button(frame,text="*",command=lambda:press_operator("*"),width=5,height=2,font=("arial",14))
button_multiplication.grid(row=1,column=3)

button_division=tk.Button(frame,text="÷",command=lambda:press_operator("/"),width=5,height=2,font=("arial",14))
button_division.grid(row=0,column=3)

#BACKSPACE
def backspace():
    current=display.get()
    display.delete(0,tk.END)
    display.insert(0,current[:-1])

button_backspace=tk.Button(frame,text="x",command=backspace,width=5,height=2,font=("arial",14))
button_backspace.grid(row=0,column=1)

#PERCENTAGE
def percentage():
    current=display.get()
    if current:
       value=float(current)
       value=value/100
       display.delete(0,tk.END)
       display.insert(0,value)

button_percentage=tk.Button(frame,text="%",command=percentage,width=5,height=2,font=("arial",14))
button_percentage.grid(row=0,column=2)


#CLEAR BUTTON

def clear_display():
    display.delete(0,tk.END)

button_clear=tk.Button(frame,text="C",command=clear_display,width=5,height=2,font=("arial",14))
button_clear.grid(row=0,column=0)

#PLUS_MINUS

def plus_minus():
      current=display.get()
      if current:
        if current.startswith("-"):
           display.delete(0,tk.END)
           display.insert(0,current[1:])
        else:
           display.delete(0,tk.END)
           display.insert(0,"-"+ current)

button_plus_minus=tk.Button (frame,text="+/-",command=plus_minus,width=5,height=2,font=("arial",14))
button_plus_minus.grid(row=4,column=2)  

#CALCULATE
def calculate():
    expression = display.get()
    try:
     result=eval(expression)
     display.delete(0,tk.END)
     display.insert(0,result)
    except:
     display.delete(0,tk.END)
     display.insert(0,"Error") 
    

button_equal=tk.Button(frame,text="=",command=calculate,width=5,height=2,font=("arial",14))
button_equal.grid(row=4,column=3)

window.mainloop()             