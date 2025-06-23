from tkinter import *

window = Tk()
window.geometry('500x500')

mainmenu = Menu(window)
window.config(menu=mainmenu)

filelist = Menu(mainmenu)
mainmenu.add_cascade(label="File", menu=filelist)
filelist.add_command(label="New")
filelist.add_command(label="Open")

edit_menu = Menu(mainmenu)
mainmenu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Undo")
edit_menu.add_command(label="Copy")


window.mainloop()