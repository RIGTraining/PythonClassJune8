from tkinter import *

window = Tk()
window.geometry('500x500')

ety = Entry(window)
ety.pack()
chk = Checkbutton(window, text='save password ?')
chk.pack()
rdo1 = Radiobutton(window, text='male')
rdo2 = Radiobutton(window, text='female')

rdo1.pack()
rdo2.pack()

sb = Scrollbar(window)
sb.pack(side=RIGHT, fill=Y)

lb = Listbox(window, yscrollcommand=sb.set)
lb.pack()

for i in range(10, 50):
    lb.insert(END, str(i))




window.mainloop()
