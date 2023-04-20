from tkinter import Label, Tk,ttk,PhotoImage,Listbox
from pyglet import font
import math
import time
is_running=0
is_paused=0
totalmilliseconds=0

def fill_laps():
    listbox.insert('end',lbl['text'])
    i=listbox.index('end')
    if int(i)%2==0:
        listbox.itemconfigure(i-1,foreground='orange',background='silver')
    else:
        listbox.itemconfigure(i-1,foreground='green',background='grey')
    listbox.see('end')
def pause():
    global is_running
    global is_paused
    pass
def start():
    global is_running
    global is_paused
    global totalmilliseconds
    starttime=time.time_ns()
    def update_timer():
        if not is_paused:
            now=time.time_ns()
            totalmilliseconds=(now-starttime)/1000000
            hours=math.floor(totalmilliseconds/1000/60/60)
            minutes=math.floor((totalmilliseconds/(60000))%60)
            seconds=math.floor((totalmilliseconds/1000)%60)
            milliseconds=math.floor(totalmilliseconds%1000)
            if len(str(milliseconds))==1:
                milliseconds=f"00{milliseconds}"
            if len(str(milliseconds))==2:
                milliseconds=f"0{milliseconds}"
            if len(str(hours))==1:
                hours=f"0{hours}"
            if len(str(seconds))==1:
                seconds=f"0{seconds}"
            if len(str(minutes))==1:
                minutes=f"0{minutes}"
            timetodisplay=f"{hours}:{minutes}:{seconds}:{milliseconds}"
            lbl.configure(text=timetodisplay)
            window.after(1,update_timer)
    update_timer()
        
def startd():
    global is_running
    global is_paused
    global totalmilliseconds
    if not is_paused:
        hours=math.floor(totalmilliseconds/3600000)
        minutes=math.floor((totalmilliseconds/(60000))%60)
        seconds=math.floor((totalmilliseconds/1000)%60)
        milliseconds=math.floor(totalmilliseconds%1000)
        if len(str(milliseconds))==1:
            milliseconds=f"00{milliseconds}"
        if len(str(milliseconds))==2:
            milliseconds=f"0{milliseconds}"
        if len(str(hours))==1:
            hours=f"0{hours}"
        if len(str(seconds))==1:
            seconds=f"0{seconds}"
        if len(str(minutes))==1:
            minutes=f"0{minutes}"
        timetodisplay=f"{hours}:{minutes}:{seconds}:{milliseconds}"
        lbl.configure(text=timetodisplay)
        
        window.after(1,start)
        totalmilliseconds+=1
    

def stop():
    global is_running
    global is_paused
    pass

width=700
height=400
font.add_file("fonts/digital-7/digital-7.ttf")

window=Tk()
style=ttk.Style(window)
style.theme_use('clam')
window.geometry(f"{width}x{height}+{int((width*1.5)/2-width/2)}+{int((height*2)/2-height/2)}")
window.attributes("-toolwindow",True)
window.title("Timer")

main_canvas=ttk.Label(window,background='#2b2b2b').place(relx=0,rely=0,relwidth=1,relheight=1)

style.configure("TLabelframe",background='#2b2b2b')

lbl=ttk.Label(main_canvas,text='00:00:00:000',background="#2b2b2b",font=("Digital-7",45),foreground="orange")
lbl.pack(side='top',anchor='w',padx=200,pady=20)


btn_pane=ttk.Label(main_canvas,background='#2b2b2b')
btn_pane.pack(side='top')

btn_start=ttk.Button(btn_pane,text="Start",command=start)
btn_start.pack(side='left',anchor='center',padx=10)

btn_lap=ttk.Button(btn_pane,text="Lap",command=fill_laps)
btn_lap.pack(side='left',anchor='center',padx=10)

btn_stop=ttk.Button(btn_pane,text="Stop")
btn_stop.pack(side='left',anchor='center',padx=10)
lbl2=ttk.Label(main_canvas,text="Laps Record",font=("Verdana",12),background="#2b2b2b",foreground="cyan")
frame=ttk.LabelFrame(main_canvas,labelwidget=lbl2,cursor="hand2",width=300,height=200)
frame.pack(side="top",pady=20)

listbox=Listbox(frame,borderwidth=1,activestyle='none',font=("Verdana",13),selectborderwidth=0,width=50)
listbox.place(relx=0,rely=0,relheight=1,relwidth=1)
scroll_bar1 = ttk.Scrollbar(listbox)
scroll_bar1.pack(side="right", fill="y")
scroll_bar1.configure(command=listbox.yview)
listbox.configure(yscrollcommand=scroll_bar1.set)



window.mainloop()