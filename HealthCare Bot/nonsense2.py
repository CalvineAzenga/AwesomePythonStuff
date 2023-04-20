from tkinter import *
from datetime import datetime
import textwrap
root=Tk()
root.configure(bg='lightblue')
frame=Frame(root)
frame.pack(fill=BOTH,expand=1)
canvas=Canvas(frame,width=200,height=200,bg='white')
canvas.grid(row=0,column=0,columnspan=2)

bubbles=[]

class BotBubble:
    def __init__(self,master,message) -> None:
        self.master=master
        self.frame=Frame(master,bg='lightgrey')
        self.i=self.master.create_window(90,160,window=self.frame)
        Label(self.frame,text=datetime.now(),font=("Raleway",7),bg="light grey").grid(row=0,column=0,sticky="w",padx=5)
        Label(self.frame,text=message,font=("Raleway",13),bg="light grey").grid(row=1,column=0,sticky="w",padx=5,pady=3)
        root.update_idletasks()
        
        def draw_triangle(self, widget):
            x1,x2,y1,y2=self.master.bbox(widget)
            return x1,y2-10,x1-15,y2+10,x1,y2
        self.master.create_polygon(draw_triangle(self,self.i),fill="light grey",outline="light grey")
def update_scrollRegion(event=None):
    canvas.configure(scrollregion=canvas.bbox(ALL))
    canvas.yview_moveto(1)

hei=0
def send_message():
    global hei
    a=BotBubble(canvas,message=textwrap.fill(entry.get(),width=10))
    hei+=a.frame.winfo_height()+10
    if bubbles:
        canvas.move(ALL,0,hei)
    bubbles.append(a)
    update_scrollRegion()
scrollbar=Scrollbar(frame)
scrollbar.configure(command=canvas.yview)
scrollbar.grid(sticky=(NSEW),column=3)
entry=Entry(frame,width=26)
entry.grid(row=1,column=0)
Button(frame,text="Send",command=send_message).grid(row=1,column=1)
frame.bind('<Configure>',update_scrollRegion)
root.mainloop()

