from tkinter import Button, Canvas, Label, LabelFrame, Menubutton, font, ttk,Tk
from PIL import Image,ImageTk
from win32api import GetSystemMetrics
from recorder import record,releaseVideo
import _thread

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
w_width = 800
w_height = 500
pos_x=int((width-(w_width))/2)
pos_y=int((height-(w_height))/2)
window=Tk()
window.wm_attributes("-topmost",1)
style=ttk.Style(window)

# style.theme_use('clam')
window.tk_setPalette("#1E1E1E")
window.geometry(f"{w_width}x{w_height}+{pos_x}+{pos_y}")
window.wm_overrideredirect(1)

# Images
try:
    img_logo=Image.open("./graphics/wolframalpha.png")
    img_logo=img_logo.resize((30,30),Image.ANTIALIAS)
    img_logo=ImageTk.PhotoImage(img_logo)

    img_restart=Image.open("./graphics/media-seek-backward.png")
    img_restart=img_restart.resize((30,30),Image.ANTIALIAS)
    img_restart=ImageTk.PhotoImage(img_restart)

    img_play=Image.open("./graphics/media-playback-start.png")
    img_play=img_play.resize((30,30),Image.ANTIALIAS)
    img_play=ImageTk.PhotoImage(img_play)

    img_pause=Image.open("./graphics/media-playback-pause.png")
    img_pause=img_pause.resize((30,30),Image.ANTIALIAS)
    img_pause=ImageTk.PhotoImage(img_pause)

    img_end=Image.open("./graphics/media-seek-forward.png")
    img_end=img_end.resize((30,30),Image.ANTIALIAS)
    img_end=ImageTk.PhotoImage(img_end)

    img_stop=Image.open("./graphics/media-playback-stop.png")
    img_stop=img_stop.resize((64,64),Image.ANTIALIAS)
    img_stop=ImageTk.PhotoImage(img_stop)

    img_record=Image.open("./graphics/media-record.png")
    img_record=img_record.resize((64,64),Image.ANTIALIAS)
    img_record=ImageTk.PhotoImage(img_record)

    img_fullscreen=Image.open("./graphics/zoom-fit-best.png")
    img_fullscreen=img_fullscreen.resize((100,100),Image.ANTIALIAS)
    img_fullscreen=ImageTk.PhotoImage(img_fullscreen)

    
except:
    pass

appbar=ttk.Label(window,background="#323233")
appbar.place(relx=0,rely=0,relwidth=1,relheight=0.08)

appbarlower=ttk.Label(window,background="#252526")
appbarlower.place(relx=0,rely=0.08,relwidth=1,relheight=0.05)

file_menu_btn=Menubutton(appbarlower,text='File',font=("Raleway",10),background="#252526")
file_menu_btn.pack(side='left')

preferences_menu_btn=Menubutton(appbarlower,text='Preferences',font=("Raleway",10),background="#252526")
preferences_menu_btn.pack(side='left')

help_menu_btn=Menubutton(appbarlower,text='Help',font=("Raleway",10),background="#252526")
help_menu_btn.pack(side='left')

logo_lbl=ttk.Label(appbar,text="SnipRec V1.0.0",font=("Georgia",15),compound="left",background="#323233",foreground="beige",image=img_logo)
logo_lbl.pack(side='left')

close_lbl=ttk.Label(appbar,text="X",font=("Raleway",18),foreground="beige",background="#323233",cursor="hand2")
close_lbl.pack(side='right',padx=10,pady=6)

minimize_lbl=ttk.Label(appbar,text="__\n",font=("Raleway",13),foreground="beige",background="#323233",cursor="hand2")
minimize_lbl.pack(side='right',padx=10)

content_pane=ttk.Label(window,background="#1b1b1b")
content_pane.place(relx=0,rely=0.13,relwidth=1,relheight=0.87)

video_canvas=Canvas(content_pane)
video_canvas.place(relx=0.25,rely=0.05,relwidth=0.5,relheight=0.5)
img_video=Image.open("./graphics/video-x-generic.png")
# window.update()
img_video=img_video.resize((video_canvas.winfo_width(),video_canvas.winfo_height()),Image.ANTIALIAS)
img_video=ImageTk.PhotoImage(img_video)
video_canvas.create_image(0,0,image=img_video,anchor='nw')

video_canvas_actions=ttk.Label(video_canvas,background='#333')
video_canvas_actions.place(relx=0.3,rely=0.8,relwidth=0.4,relheight=0.18)

video_restart_lbl=ttk.Label(video_canvas_actions,justify='center',image=img_restart,compound='center',foreground='beige',background="#333")
video_restart_lbl.pack(side='left',anchor='center',expand=True)

video_play_lbl=ttk.Label(video_canvas_actions,justify='center',image=img_play,compound='center',foreground='beige',background="#333")
video_play_lbl.pack(side='left',anchor='center',expand=True)



video_end_lbl=ttk.Label(video_canvas_actions,justify='center',image=img_end,compound='center',foreground='beige',background="#333")
video_end_lbl.pack(side='left',anchor='center',expand=True)

recorder_frame=Canvas(content_pane,highlightthickness=0)
recorder_frame.place(relx=0.1,rely=0.58,relwidth=0.8,relheight=0.4)

record_area_container=Canvas(recorder_frame,background="#1E1E1E",relief='solid',borderwidth=0,highlightthickness=1,highlightbackground='#333',highlightcolor='#333')
record_area_container.place(relx=0.01,rely=0.01,relwidth=0.3,relheight=0.98)

rec_area_full=Menubutton(record_area_container,image=img_fullscreen,text="Full Screen",foreground="silver",font=("Verdana",10),compound='top',background='#1e1e1e',border=0,relief='flat',cursor="hand2")
rec_area_full.place(relx=0.01,rely=0.1,relwidth=0.6,relheight=0.7)

rec_area_custom=LabelFrame(record_area_container,background='#1e1e1e',borderwidth=0)
rec_area_custom.place(relx=0.61,rely=0.1,relwidth=0.39,relheight=0.7)

custom_x1_txt=ttk.Entry(rec_area_custom,foreground="grey",background="#202634",width=10)
custom_x1_txt.pack(side='top',pady=4)

custom_x1_txt.insert(0,"X1")

custom_x2_txt=ttk.Entry(rec_area_custom,foreground="grey",background="#202634",width=10)
custom_x2_txt.pack(side='top',pady=4)

custom_x2_txt.insert(0,"X2")

custom_width_txt=ttk.Entry(rec_area_custom,foreground="grey",background="#202634",width=10)
custom_width_txt.pack(side='top',pady=4)

custom_width_txt.insert(0,"Width")

custom_height_txt=ttk.Entry(rec_area_custom,foreground="grey",background="#202634",width=10)
custom_height_txt.pack(side='top',pady=4)
custom_height_txt.insert(0,"Height")

record_other_container=Canvas(recorder_frame,background="#1E1E1E",relief='solid',borderwidth=0,highlightthickness=1,highlightbackground='#333',highlightcolor='#333')
record_other_container.place(relx=0.35,rely=0.01,relwidth=0.64,relheight=0.98)

camera_lbl=Menubutton(record_other_container,background="#1E1E1E",text="Toggle camera",font=("Verdana",10),foreground="silver")
camera_lbl.pack(side='left',pady=20)
img_camera=Image.open("./graphics/camera-switch-symbolic.symbolic.png")
window.update()
img_camera=img_camera.resize((int(64),int(64)),Image.ANTIALIAS)
img_camera=ImageTk.PhotoImage(img_camera)
camera_lbl.configure(image=img_camera,compound='top')

audio_lbl=Menubutton(record_other_container,background="#1E1E1E",text="Audio [ON]",font=("Verdana",10),foreground="silver")
audio_lbl.pack(side='left',pady=40)
img_audio=Image.open("./graphics/audio-speakers.png")
window.update()
img_audio=img_audio.resize((64,64),Image.ANTIALIAS)
img_audio=ImageTk.PhotoImage(img_audio)
audio_lbl.configure(image=img_audio,compound='top')

record_button=Button(record_other_container,background="#1E1E1E",font=("Verdana",10),image=img_record,relief='flat',borderwidth=0,text="Record",compound="top",foreground="silver")
record_button.pack(side='left',padx=40)

stop_button=Button(record_other_container,background="#1E1E1E",font=("Verdana",10),image=img_stop,relief='flat',borderwidth=0,text="Stop",compound="top",foreground="silver")
stop_button.pack(side='left',padx=40)

def recordIt():
    record_button.pack_forget()
    stop_button.pack(side='left',padx=40)
    _thread.start_new_thread(record,("Thread-1",window,video_canvas))
record_button.configure(command=recordIt)

def releaseVid():
    stop_button.pack_forget()
    record_button.pack(side='left',padx=40)
    releaseVideo()
stop_button.configure(command=releaseVid)
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

    appbar.bind('<Button-1>', save_last_pos)
    appbar.bind('<B1-Motion>', dragging)
    def minimize_window(event):
        window.overrideredirect(0)
        window.iconify()

    def show_windoww():
        if  window.state() == 'normal':
            window.overrideredirect(1)
        window.after(1, show_windoww)
    show_windoww()
    close_lbl.bind("<ButtonPress>",lambda event:window.destroy())
    minimize_lbl.bind("<ButtonPress>",minimize_window)
except:
    pass
window.mainloop()
