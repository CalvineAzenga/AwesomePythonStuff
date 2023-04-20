import sys
import threading
import datetime
from tkinter import Tk,ttk
import tkinter as tk
from PIL import Image,ImageTk
from win32api import GetSystemMetrics
from math import floor
from ttkthemes import ThemedStyle
from CMAScreenRecorder import ScreenRecorder



window=Tk()
window.overrideredirect(1)
window.attributes("-topmost",1)
style=ThemedStyle(window)
# print(style.get_themes())
style.theme_use("radiance")
# Screen Dimensions
width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

# Resized Window according to screen size 
resizedWidth=floor((1/4)*width)+50
resizedHeight=floor((1/4)*height)+20

# (x,y) point to place window in the bottom right corner of the screen
x_root=int(width-(resizedWidth+10))
y_root=int(height-(resizedHeight+10))

window.geometry(f"{resizedWidth}x{resizedHeight}+{x_root}+{y_root}")

back_img=Image.open("./graphics/back2.png")
back_img=back_img.resize((resizedWidth,resizedHeight),Image.ANTIALIAS)
back_img=ImageTk.PhotoImage(image=back_img,master=window)

screenRecorder=ScreenRecorder()
def startRecorder():
    global screenRecorder
    if screenRecorder==None:
        screenRecorder=ScreenRecorder()
    thread=threading.Thread(target=screenRecorder.startRecording)
    thread.daemon=True
    thread.start()
    startBtn.pack_forget()
    stopBtn.pack(side="left",padx=(5,5))

def stopRecorder():
    global screenRecorder
    screenRecorder.stopRecording()
    stopBtn.pack_forget()
    startBtn.pack(side="left",padx=(5,5))
    screenRecorder=None

def closeWindow(event):
    try:
        stopRecorder()
    except:
        sys.exit(0)
    sys.exit(0)

    



mainCanvas=tk.Canvas(window,highlightthickness=0,border=0)
mainCanvas.place(relx=0,rely=0,relwidth=1,relheight=1)
# mainCanvas.create_image(0,0,image=back_img,anchor="nw")

appBar=tk.Canvas(window,highlightthickness=0,border=0,background="#07011B")
appBar.place(relx=0,rely=0,relwidth=1,relheight=0.15)

appNameLbl=tk.Label(appBar,background="#07011B",foreground="#EAEAEA",text="Cally Snip", font=("Cambria",11))
appNameLbl.pack(side="left",anchor="center")

closeLbl=tk.Label(appBar,background="#07011B",foreground="#EAEAEA",text="X", font=("Raleway",12),cursor="hand2")
closeLbl.pack(side="right",anchor="center",padx=(0,5))

minimizeLbl=tk.Label(appBar,background="#07011B",foreground="#EAEAEA",text="__", font=("Raleway",8),cursor="hand2")
minimizeLbl.pack(side="right",anchor="center",padx=(0,6),pady=(0,12))

closeLbl.bind("<ButtonPress>", lambda event:closeWindow(event))


bottomCanvas=tk.Canvas(window,highlightthickness=0,border=0)
bottomCanvas.place(relx=0,rely=0.15,relwidth=1,relheight=1-0.15)
# bottomCanvas.create_image(0,0,image=back_img,anchor="nw")




start_img=Image.open("./graphics/start.png")
start_img=start_img.resize((80,80),Image.ANTIALIAS)
start_img=ImageTk.PhotoImage(image=start_img,master=window)
startBtn=tk.Button(bottomCanvas,relief=tk.FLAT,border=0,cursor="hand2",background="#EAEAEA",text="Start",foreground="#07011B",font=("Cambria",10,"bold"),image=start_img,compound="center")
startBtn.pack(side="left",padx=(5,5))
startBtn.configure(command=startRecorder)


stop_img=Image.open("./graphics/stop.png")
stop_img=stop_img.resize((80,80),Image.ANTIALIAS)
stop_img=ImageTk.PhotoImage(image=stop_img,master=window)
stopBtn=tk.Button(bottomCanvas,relief=tk.FLAT,border=0,cursor="hand2",background="#EAEAEA",text="Stop",foreground="beige",font=("Cambria",10,"bold"),image=stop_img,compound="center")
stopBtn.configure(command=stopRecorder)

labelFrame=tk.LabelFrame(bottomCanvas,background="#EAEAEA",text="Preferences",font=("Raleway",8))
labelFrame.place(relx=0.3,rely=0.01,relheight=0.98,relwidth=0.69)


style.configure(ttk.Checkbutton().winfo_class(),font=("Verdana",7),foreground='black',background="#EAEAEA")
style.configure(ttk.Entry().winfo_class(),font=("Verdana",7),foreground='black',background="#EAEAEA")

cameraCheckBox=ttk.Checkbutton(labelFrame,cursor="hand2",text="Include WebCam")
cameraCheckBox.grid(row=0,column=0,sticky="nw")

audioCheckBox=ttk.Checkbutton(labelFrame,cursor="hand2",text="Include Audio")
audioCheckBox.grid(row=1,column=0,sticky="nw")

fullscreenCheckBox=ttk.Checkbutton(labelFrame,cursor="hand2",text="Capture FullScreen")
fullscreenCheckBox.grid(row=2,column=0,sticky="nw")


custom_x_Entry_Lbl=tk.Label(labelFrame,text="X_ROOT",font=("Verdana",7),foreground='black',background="#EAEAEA")
custom_x_Entry_Lbl.grid(row=3,column=0,sticky="nw",padx=(30,0),pady=(10,4))


custom_x_Entry=ttk.Entry(labelFrame,width=4)
custom_x_Entry.grid(row=3,column=0,sticky="nw",padx=(90,0),pady=(10,4))


custom_width_Entry_Lbl=tk.Label(labelFrame,text="WIDTH",font=("Verdana",7),foreground='black',background="#EAEAEA")
custom_width_Entry_Lbl.grid(row=3,column=1,sticky="nw",padx=(5,0),pady=(10,4))


custom_width_Entry=ttk.Entry(labelFrame,width=4)
custom_width_Entry.grid(row=3,column=1,sticky="nw",padx=(60,0),pady=(10,4))



custom_y_Entry_Lbl=tk.Label(labelFrame,text="Y_ROOT",font=("Verdana",7),foreground='black',background="#EAEAEA")
custom_y_Entry_Lbl.grid(row=4,column=0,sticky="nw",padx=(30,0),pady=(10,4))


custom_y_Entry=ttk.Entry(labelFrame,width=4)
custom_y_Entry.grid(row=4,column=0,sticky="nw",padx=(90,0),pady=(10,4))


custom_height_Entry_Lbl=tk.Label(labelFrame,text="HEIGHT",font=("Verdana",7),foreground='black',background="#EAEAEA")
custom_height_Entry_Lbl.grid(row=4,column=1,sticky="nw",padx=(5,0),pady=(10,4))


custom_height_Entry=ttk.Entry(labelFrame,width=4)
custom_height_Entry.grid(row=4,column=1,sticky="nw",padx=(60,0),pady=(10,4))


# Dragging window functionality 
try:
    lastClickX = 0
    lastClickY = 0

    def save_last_pos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def dragging(event):
        x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
        window.geometry("+{0}+{1}".format(x, y))

    appBar.bind('<Button-1>', save_last_pos)
    appBar.bind('<B1-Motion>', dragging)
except:
    pass

def minimize_window(event):
    window.wm_state('withdrawn')
    window.overrideredirect(0)
    window.iconify()

def update_window():
    if  window.state() == 'normal':
        window.overrideredirect(1)
    try:
        secs=screenRecorder.getRecordingSecondsElapsed()
        stopBtn.configure(text=datetime.timedelta(seconds=secs))
    except:
        pass
    window.after(10, update_window)
update_window()
minimizeLbl.bind("<ButtonPress>", lambda event:minimize_window(event))

window.mainloop()