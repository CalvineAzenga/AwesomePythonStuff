import time
import numpy as np
from PIL import Image,ImageTk
from tkinter import PhotoImage,Canvas
import ttkthemes as tk
import threading
import login


allow_load=True
text="Initializing."
i=0
SPLASHSCREEN=tk.ThemedTk()
SPLASHSCREEN.set_theme('clam')
SPLASHSCREEN.geometry("900x550")
SPLASHSCREEN.attributes("-topmost",True)
SPLASHSCREEN.overrideredirect(1)
icon=PhotoImage(master=SPLASHSCREEN,height=16,width=16)
icon.blank()
icon.transparency_set(0,0,0)
SPLASHSCREEN.wm_iconphoto(False,icon)


SPLASHSCREEN.resizable(width=0, height=0)

# To center the window
try:
    screen_width = SPLASHSCREEN.winfo_screenwidth()
    screen_height = SPLASHSCREEN.winfo_screenheight()
    app_height = SPLASHSCREEN.winfo_height()
    app_width = SPLASHSCREEN.winfo_width()

    x_loc = int(screen_width / 2) - int(app_width / 2)
    y_loc = int(screen_height / 2) - int(app_height / 2)

    SPLASHSCREEN.geometry("+{}+{}".format(x_loc, y_loc))
except:
    pass

bacground_image=Image.open("./images/gg.jpg")
bacground_image=bacground_image.resize((900,550),Image.ANTIALIAS)
bacground_image=ImageTk.PhotoImage(bacground_image,master=SPLASHSCREEN)

main_canvas=Canvas(SPLASHSCREEN)
main_canvas.place(relx=0,rely=0,relheight=1,relwidth=1)
main_canvas.create_image(0,0,image=bacground_image,anchor='nw')

main_canvas.create_text(450,500,text=text,fill='red',font=("Verdana",20),tag="initializing")


def animate_loader():
    try:
        frame_cnt = 0
        # frames = [PhotoImage(file='Anieyes.gif', format='gif -index %i' % (i)) for i in range(frame_cnt)]
        frames = []
        while 1:
            try:
                frame = PhotoImage(master=SPLASHSCREEN,file="./loaders/loading.gif", format='gif -index %i' % (frame_cnt))
                frames.append(frame)
                frame_cnt += 1
                pass
            except Exception as msg:
                # print(msg)
                # print("Number of frames: " + str(frame_cnt))
                break
        def updateinitializingtext():
            global i
            global text
            global allow_load
            main_canvas.delete("initializing")
            if i>3:
                i=0
            text="Initializing"+"."*i
            main_canvas.create_text(450,500,text=text,fill='lime',font="Verdana 16",tag="initializing")
            i+=1
            if allow_load:
                SPLASHSCREEN.after(200,updateinitializingtext)
        updateinitializingtext()

            


        def updet(ind):
            global allow_load
            frame = frames[ind]
            ind += 1
            if ind == frame_cnt:
                ind = 0
                
            main_canvas.create_image(242,450,image=frame,anchor='nw')
            if allow_load:
                SPLASHSCREEN.after(100, updet, ind)
        updet(0)
    except Exception as msg:
        print(msg)
        pass

def launch_login():
    global allow_load
    time.sleep(3)
    allow_load=False
    SPLASHSCREEN.grab_release()
    SPLASHSCREEN.withdraw()
    login.LOGINSYSTEM()
    SPLASHSCREEN.destroy()
    pass

def save_last_pos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y

def dragging(event):
    x, y = event.x - lastClickX + SPLASHSCREEN.winfo_x(), event.y - lastClickY + SPLASHSCREEN.winfo_y()
    SPLASHSCREEN.geometry("+{0}+{1}".format(x, y))

SPLASHSCREEN.bind('<B1-Motion>', dragging)
SPLASHSCREEN.bind('<Button-1>', save_last_pos)
animate_loader()
threadlogin=threading.Thread(target=launch_login)
threadlogin.daemon=True
threadlogin.start()
SPLASHSCREEN.mainloop()