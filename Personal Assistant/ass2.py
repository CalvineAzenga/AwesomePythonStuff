import threading
from tkinter.constants import BOTH, BOTTOM, GROOVE, HORIZONTAL, LEFT, RAISED, RIGHT, TOP, VERTICAL, W, X, Y
from tkinter.font import BOLD
from tkinter.ttk import Label, Progressbar,Scrollbar,Entry, Separator, Style
import tkinter as tk

root = tk.Tk()
style=Style(root)
style.theme_use('default')
root.geometry("1020x600")


canvas=tk.Canvas(root,highlightthickness=0)
canvas.pack(side=LEFT,fill=BOTH,expand=True)
class TkTable():
    def __init__(self,master,columns=2):
        TableFrame=tk.Canvas(master=master)
        TableFrame.pack(side=LEFT,expand=True)

        ScrollV=Scrollbar(TableFrame,orient=VERTICAL)
        ScrollV.pack(side=RIGHT,fill=Y)

        ScrollH=Scrollbar(TableFrame,orient=HORIZONTAL)
        ScrollH.pack(side=BOTTOM,fill=X)

        TableCanvas=tk.Frame(TableFrame)
        TableCanvas.pack(side=LEFT,expand=True)
        TableFrame.configure(xscrollcommand=ScrollH.set,yscrollcommand=ScrollV.set)

        for col in range(columns):
            listboxHeader=tk.Label(TableCanvas,cursor='hand2',font=("Verdana",10),text=f"Column {col}",relief=RAISED,bd=0)
            listboxHeader.grid(row=0,column=col,sticky=W,padx=0)

            listbox=tk.Listbox(TableCanvas,width=10,border=0,highlightthickness=1,bd=0,highlightcolor='silver')
            listbox.grid(row=2,column=col,sticky=W,padx=0)
            # listbox.insert("0",col)
    def selectRow():
        pass
    def selectColumn():
        pass
    def addRow():
        pass
    def addColumn():
        pass
    def deleteRow():
        pass
    def deleteColumn():
        pass

table=TkTable(canvas,columns=10)
print(root['cursor'])

root.mainloop()