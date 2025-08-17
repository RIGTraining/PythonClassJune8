import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = tk.Tk()
window.geometry('400x400') #width=400, height=400

def test_function():
    print('helo')
#widget
lbl = ttk.Label(window, text='username', bootstyle="warning")
lbl.pack()

ety = ttk.Entry(window,  bootstyle='success')
ety.pack()

pasw = ttk.Label(window, text='password')
pasw.pack()

ety1 = ttk.Entry(window,  bootstyle='success')
ety1.pack()

btn = ttk.Button(window, text='Submit', bootstyle='success', command=test_function)
btn.pack()





window.mainloop()