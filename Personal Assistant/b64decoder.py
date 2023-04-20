# Free spreadsheet
from tkinter import *
from tkinter import ttk,filedialog
import threading

root=Tk()
root.geometry("1020x600")
root.wm_attributes("-toolwindow",True)
# style=ttk.Style(root)
# style.theme_use('default')
root.title("Excel Sheet")
vertical_scrollbar=ttk.Scrollbar(root,orient=VERTICAL)
vertical_scrollbar.pack(side=RIGHT,fill=Y)

horizontal_scrollbar=ttk.Scrollbar(root,orient=HORIZONTAL)
horizontal_scrollbar.pack(side=BOTTOM,fill='both')
canvas=Canvas(root,highlightthickness=0)
canvas.pack(side=TOP,anchor=NW,fill=BOTH,expand=TRUE)
canvas1=Frame(canvas)
# canvas1.pack(fill=BOTH)
canvas.create_window(0,0,window=canvas1)
vertical_scrollbar.configure(command=canvas.yview)
horizontal_scrollbar.configure(command=canvas.xview)
root.update()
def createSpreadSheet():
    for row in range(0,101):
        for column in range(0,21):
            root.update_idletasks()
            ass=Entry(canvas1,font=("Verdana",10),justify=CENTER)
            ass.grid(row=row,column=column)
            ass.insert("0",(row,column))
    canvas.configure(scrollregion=canvas.bbox('all'))
    canvas.configure(xscrollcommand=horizontal_scrollbar.set,yscrollcommand=vertical_scrollbar.set)
    root.mainloop()

createSpreadSheet()
