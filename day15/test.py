from tkinter import *
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


cal = tk.Tk()
cal.title('my Calculator App')
cal.geometry('300x400')

m = ''
def press(n):
    global m
    m += str(n)
    resa.set('hello')


def equal():
    global m
    ans = str(eval(m))
    print(ans)
    resa.set(ans)

    



# eql = ttk.Button(cal,text='=', bootstyle='PRIMARY')

resa = StringVar()
displ = ttk.Entry(cal, textvariable=resa)
displ.grid(row=0, column=0, columnspan=4)

no1 = ttk.Button(cal, text='1', bootstyle='SUCCESS', command=lambda:press(1))
no2 = ttk.Button(cal, text='2', bootstyle='SUCCESS', command=lambda:press(2))
no3 = ttk.Button(cal, text='3', bootstyle='SUCCESS', command=lambda:press(3))
no4 = ttk.Button(cal, text='4', bootstyle='SUCCESS', command=lambda:press(4))

no5 = ttk.Button(cal, text='5', bootstyle='SUCCESS')
no6 = ttk.Button(cal, text='6', bootstyle='SUCCESS')
no7 = ttk.Button(cal, text='7', bootstyle='SUCCESS')
no8 = ttk.Button(cal, text='8', bootstyle='SUCCESS')

# Row 3: 9 0 ans del
no9  = ttk.Button(cal, text='9',   bootstyle='SUCCESS')
no0  = ttk.Button(cal, text='0',   bootstyle='SUCCESS')
ans  = ttk.Button(cal, text='ans', bootstyle='SUCCESS', command=lambda:equal())
dele = ttk.Button(cal, text='del', bootstyle='SUCCESS')

add = ttk.Button(cal, text='+', bootstyle='SUCCESS', command=lambda:press('+'))
sub = ttk.Button(cal, text='-', bootstyle='SUCCESS')
mul = ttk.Button(cal, text='*', bootstyle='SUCCESS')
div = ttk.Button(cal, text='%', bootstyle='SUCCESS')

# display = ttk.Entry(cal)
# display.grid(row=0, column=0, columnspan=4)

no1.grid(row=1, column=1,padx=4, pady=4)
no2.grid(row=1, column=2,padx=4, pady=4)
no3.grid(row=1, column=3,padx=4, pady=4)
no4.grid(row=1, column=4,padx=4, pady=4)

no5.grid(row=2, column=1,padx=4, pady=4) 
no6.grid(row=2, column=2,padx=4, pady=4)
no7.grid(row=2, column=3,padx=4, pady=4) 
no8.grid(row=2, column=4,padx=4, pady=4) 

no9.grid(row=3, column=1,padx=4, pady=4) 
no0.grid(row=3, column=2,padx=4, pady=4) 
ans.grid(row=3, column=3, padx=4, pady=4) 
dele.grid(row=3, column=4, padx=4,pady=4)

add.grid (row=4, column=1, padx=4, pady=4)
sub.grid(row = 4, column=2, padx = 4, pady=4)
mul.grid (row=4, column=3, padx=4, pady=4)
div.grid(row =4, column=4, padx=4, pady=4)



cal.mainloop()