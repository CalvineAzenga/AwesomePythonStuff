import tkinter as tk
from tkinter import ttk

root=tk.Tk()

cTableContainer=tk.Canvas(root)
fTable=tk.Label(cTableContainer)
sbHorizontalScrollBar=tk.Scrollbar(root)
sbVerticalScrollBar=tk.Scrollbar(root)

def updateScrollRegion():
    cTableContainer.update_idletasks()
    cTableContainer.configure(scrollregion=fTable.bbox())
def createScrollableContainer():
    cTableContainer.configure(xscrollcommand=sbHorizontalScrollBar.set,yscrollcommand=sbVerticalScrollBar,highlightthickness=0)
    sbHorizontalScrollBar.configure(orient=tk.HORIZONTAL,command=cTableContainer.xview)
    sbVerticalScrollBar.configure(orient=tk.VERTICAL,command=cTableContainer.yview)
    sbHorizontalScrollBar.pack(fill=tk.X,side=tk.BOTTOM)
    sbVerticalScrollBar.pack(fill=tk.Y,side=tk.RIGHT)
    cTableContainer.pack(fill=tk.BOTH,side=tk.LEFT)
    cTableContainer.create_window(0,0,window=fTable,anchor=tk.NW)
i=0
def addNewLabel():
    global i
    while True:
        tk.Label(fTable,text=f"Hello World {i}").grid(row=i,column=0)
        i+=1
        if i>200:
            break

createScrollableContainer()
addNewLabel()
updateScrollRegion()
root.mainloop()