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
for FONT in fontList:

    lbl=tk.Label(scrollable_body,text="+254700666848 My very educated mother just",font=(FONT,13))
    lbl2=tk.Label(scrollable_body,text=FONT+": ",font=("Bahnschrift Light",15))
    lbl2.grid(row=row,column=column,padx=10,pady=10,sticky='w')
    lbl.grid(row=row,column=1,padx=0,pady=5,sticky='w')
    row+=1
    pass

scrollable_body.update()
root.mainloop()
