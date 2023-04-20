from sys import winver
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
root=Tk()
style=ttk.Style(root)
style.theme_use('clam')
root.tk_setPalette("#212D3B")

root.title('ChatBot Canvas')
root.eval("tk::PlaceWindow . center")
root.geometry("400x600")
bitmp=Image.open('images/clear.jpg')
root.resizable(0,0)
root.wm_attributes("-toolwindow",True)
canvas=Canvas(root,background='blue')
canvas.place(relx=0,rely=0,relwidth=0.95,relheight=0.9)
root.update()
width=canvas.winfo_width()
height=canvas.winfo_height()
bitmp=bitmp.resize((width,height),Image.ANTIALIAS)
bitmp=ImageTk.PhotoImage(bitmp)
canvas.create_image(0,0,image=bitmp,anchor='nw',tags=("background",))

scrollbar=ttk.Scrollbar(root,orient='vertical')
scrollbar.place(relx=0.95,rely=0,relheight=0.9,relwidth=0.05)

def custom_yview(*args,**kwargs):
    canvas.yview(*args,**kwargs)
    x=canvas.canvasx(0)
    y=canvas.canvasy(0)
    canvas.coords("background",x,y)
root.update()

scrollbar.configure(command=custom_yview)
saiz=0
for x in range(0,200):
    lbl=Label(canvas,text=str(x)*50,background='#2b2b2b',foreground='beige',wraplength=210,font=("Verdana",12))
    canvas.create_window(10,saiz,anchor='nw',window=lbl)
    lbl2=Label(canvas,text=str(x)*60,background='#0E502B',foreground='beige',wraplength=210,font=("Verdana",12))
    root.update_idletasks()
    saiz+=lbl.winfo_reqheight()+20
    canvas.create_window(int(canvas.winfo_width()/2.5),saiz,anchor='nw',window=lbl2)
    saiz+=lbl2.winfo_reqheight()+20
canvas.configure(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox('all'))

root.mainloop()