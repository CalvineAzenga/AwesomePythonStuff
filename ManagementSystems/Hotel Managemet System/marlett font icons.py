import tkinter as tk
from tkinter import ttk,font
from tkinter.ttk import Scrollbar,Style


class Scrollable(tk.Frame):
    def __init__(self,frame,width=16):
        scrollbar=Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

        self.canvas=tk.Canvas(frame,yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)

        scrollbar.configure(command=self.canvas.yview)

        self.canvas.bind("<Configure>",self.fillcanvas)

        tk.Frame.__init__(self,frame)
        self.windows_item=self.canvas.create_window(0,0,window=self,anchor=tk.NW)
    def fillcanvas(self, event):
        canvas_width=event.width
        self.canvas.itemconfigure(self.windows_item,width=canvas_width)
    def update(self) -> None:
        self.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox(self.windows_item))

root=tk.Tk()
fontList=font.families()
root.geometry("800x600")
style=Style()
style.theme_use('clam')
body=ttk.Frame(root)

body.place(relheight=1,relwidth=1)

scrollable_body=Scrollable(body,width=20)
column=0
row=0
letterlist="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~!@#$%^&*())_+=-`[]\\|}{:\";',.<>/?"
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='lime',font=("Webdings",20))
    lbl2=tk.Label(scrollable_body,text="Webdings- "+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='green',font=("Marlett",20))
    lbl2=tk.Label(scrollable_body,text="Marlett- "+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='orange',font=("wingdings",20))
    lbl2=tk.Label(scrollable_body,text="Webdings- "+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='blue',font=("wingdings 2",20))
    lbl2=tk.Label(scrollable_body,text="Webdings 2- "+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='indigo',font=("wingdings 3",20))
    lbl2=tk.Label(scrollable_body,text="Webdings- 3"+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='yellow',font=("Map Symbols",20))
    lbl2=tk.Label(scrollable_body,text="Map Symbols- "+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass
for letter in letterlist:
    lbl=tk.Label(scrollable_body,text=f"{letter}",fg='beige',font=("Mapinfo Cartographic",20))
    lbl2=tk.Label(scrollable_body,text="Mapinfo Cartographic- "+letter+": ",fg='beige',font=("Raleway",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass

scrollable_body.update()
root.tk_setPalette("#2b2b2b")
root.mainloop()