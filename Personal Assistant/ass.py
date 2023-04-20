import threading
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, LEFT, RIGHT, VERTICAL, X, Y
from tkinter.ttk import Label, Progressbar,Scrollbar,Entry, Style
import tkinter as tk

root = tk.Tk()
style=Style(root)
style.theme_use('default')
root.geometry("1020x600")
ScrollV=Scrollbar(root,orient=VERTICAL)
ScrollV.pack(side=RIGHT,fill=Y)

ScrollH=Scrollbar(root,orient=HORIZONTAL)
ScrollH.pack(side=BOTTOM,fill=X)

canvas=tk.Canvas(root,highlightthickness=0,xscrollcommand=ScrollH.set,yscrollcommand=ScrollV.set)
canvas.pack(side=LEFT,fill=BOTH,expand=True)
# Pack 50 Label on the box
r=10
c=10
r=int(r)
c=int(c)
ScrollV.configure(command=canvas.yview)
ScrollH.configure(command=canvas.xview)
def drawIt():
    global r,c
    for row in range(80):
        for column in range(10):
            txt = Label(canvas,text=(row,column),width=15)
            canvas.create_window(c,r,window=txt,anchor='center')
            c+=txt.winfo_reqwidth()
            
        r+=txt.winfo_reqheight()
        c=10
    canvas.configure(scrollregion=canvas.bbox("all"))
    
threading.Thread(target=drawIt,daemon=True).start()
root.mainloop()