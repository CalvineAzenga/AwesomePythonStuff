from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from datetime import datetime
import time
import threading
import pyttsx3
import chatFunctions


engine=pyttsx3.Engine()
voices=engine.getProperty("voices")
# for voice in voices:
#     print(voice.name)
# engine.setProperty("rate",95)
engine.setProperty("voice",voices[1].id)

root=Tk()
style=ttk.Style(root)
style.theme_use('clam')
root.tk_setPalette("#212D3B")

root.title('Personal Assistant AI')

root.geometry("400x620")
# To center the window
try:
    icon = PhotoImage(master=root, height=16, width=16)
    icon.blank()
    icon.transparency_set(0, 0, 0)
    root.iconphoto(False, icon)
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    app_height = root.winfo_height()
    app_width = root.winfo_width()

    x_loc = int(screen_width / 2) - int(app_width / 2)
    y_loc = int(screen_height / 2) - int(app_height / 2)

    root.geometry("+{}+{}".format(x_loc, y_loc))
except Exception as msg:
    print(msg)
    pass
bitmp=Image.open('images/clear.jpg')
root.resizable(0,0)
root.wm_attributes("-toolwindow",True)

prof_img1=Image.open('./images/avatars/a13.png')
prof_img1=prof_img1.resize((48,48),Image.ANTIALIAS)
prof_img1=ImageTk.PhotoImage(prof_img1,master=root)

settings_img1=Image.open('./images/setting.png')
settings_img1=settings_img1.resize((36,36),Image.ANTIALIAS)
settings_img1=ImageTk.PhotoImage(settings_img1,master=root)

mic_img1=Image.open('./images/mic1.png')
mic_img1=mic_img1.resize((36,36),Image.ANTIALIAS)
mic_img1=ImageTk.PhotoImage(mic_img1,master=root)

keyboard_img1=Image.open('./images/keyboard.png')
keyboard_img1=keyboard_img1.resize((48,48),Image.ANTIALIAS)
keyboard_img1=ImageTk.PhotoImage(keyboard_img1,master=root)

send_img1=Image.open('./images/send.png')
send_img1=send_img1.resize((44,48),Image.ANTIALIAS)
send_img1=ImageTk.PhotoImage(send_img1,master=root)

top_bar=Label(root,background='#202634')
top_bar.place(relx=0,rely=0,relwidth=1,relheight=0.12)

profile_img_lbl=Label(top_bar,image=prof_img1,background='#202634',compound='left')
profile_img_lbl.pack(side=LEFT,fill=Y)

profile_details_lbl=Label(top_bar,background='#202634',compound='left')
profile_details_lbl.pack(side=LEFT,pady=10)

profile_details_lbl_name=Label(profile_details_lbl,text="Soberano",foreground='beige',font=("Verdana",13),background='#202634',compound='left')
profile_details_lbl_name.pack(side=TOP,anchor=N,fill=X)

profile_details_lbl_status=Label(profile_details_lbl,text="online",foreground='cyan',font=("Verdana",10),background='#202634',compound='left')
profile_details_lbl_status.pack(side=TOP,anchor=S,fill=X)

settings_btn=Button(top_bar,activebackground='#202634',background='#202634',image=settings_img1,compound='center',relief=FLAT,bd=0)
settings_btn.pack(side=RIGHT,pady=8)

canvas_pane=LabelFrame(root,background='#212D3B',relief=GROOVE,bd=5)
canvas_pane.place(relx=0,rely=0.1,relwidth=0.95,relheight=0.8)

canvas=Canvas(canvas_pane,background='#212D3B',bd=0,highlightthickness=0)
canvas.pack(fill=BOTH,expand=True)
root.update()
width=canvas.winfo_width()
height=canvas.winfo_height()
bitmp=bitmp.resize((width,height),Image.ANTIALIAS)
bitmp=ImageTk.PhotoImage(bitmp)
canvas.create_image(0,0,image=bitmp,anchor='nw',tags=("background",))

scrollbar=ttk.Scrollbar(root,orient='vertical')
scrollbar.place(relx=0.95,rely=0.1,relheight=0.8,relwidth=0.05)

bottom_pane_keyboard_mic=LabelFrame(root,bd=0)
bottom_pane_keyboard_mic.place(relx=0,rely=0.9,relheight=0.1,relwidth=1)

keyboard_btn=Button(bottom_pane_keyboard_mic,activebackground='#212D3B',image=keyboard_img1,compound='center',relief=FLAT,bd=0)
keyboard_btn.pack(side=LEFT,padx=5,ipadx=10)


text_entry=ttk.Entry(bottom_pane_keyboard_mic,font=("Verdana",15),width=16)
text_entry.pack(side=LEFT,ipady=5)

send_btn=Button(bottom_pane_keyboard_mic,activebackground='#212D3B',image=send_img1,compound='center',relief=FLAT,bd=0)
send_btn.pack(side=LEFT)

mic_btn=Button(bottom_pane_keyboard_mic,activebackground='#212D3B',image=mic_img1,compound='center',relief=FLAT,bd=0)
mic_btn.pack(side=LEFT)

settings_pane=LabelFrame(root)
relwidth=0
ind=1
def animateSettingsPane():
    global relwidth,ind
    relwidth=0
    ind=1
    def realAnimation():
        global relx,relwidth,ind
        ind=int(ind)        
        relwidth+=0.009
        relx=1-relwidth
        settings_pane.place(relx=relx,rely=0,relwidth=relwidth,relheight=1)
        if ind<100:
            ind+=1
            root.after(1,realAnimation)
    realAnimation()
    canvas.bind("<ButtonPress>",lambda event: settings_pane.place_forget())

def custom_yview(*args,**kwargs):
    canvas.yview(*args,**kwargs)
    x=canvas.canvasx(0)
    y=canvas.canvasy(0)
    canvas.coords("background",x,y)
root.update()
scrollbar.configure(command=custom_yview)
saiz=0
welcome_text="Hello there, I'm your smart AI assistant.\nHow can I help you?"
lbl=Label(canvas,text=welcome_text,justify=LEFT,background='#2b2b2b',foreground='beige',wraplength=210,font=("Verdana",12))
canvas.create_window(3,saiz,anchor='nw',window=lbl)
root.update_idletasks()
saiz+=lbl.winfo_reqheight()+20
saiz+=20
canvas.configure(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox('all'))
def replyMsg(quiz):
    global saiz
    lbl=Label(canvas,text=quiz[::-1],justify=LEFT,background='#2b2b2b',foreground='beige',wraplength=210,font=("Verdana",12))
    canvas.create_window(3,saiz,anchor='nw',window=lbl)
    root.update_idletasks()
    saiz+=lbl.winfo_reqheight()+20
    saiz+=20
    canvas.configure(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox('all'))
    canvas.yview_moveto(1)
    custom_yview()
    # def speakReply():
    #     engine.say(quiz)
    #     engine.runAndWait()
    # threading.Thread(target=speakReply,daemon=True).start()
    

    pass
def sendMsg(event=None):
    global saiz
    quiz=text_entry.get().strip()
    lbl2=Label(canvas,text=quiz,justify=LEFT,background='#0E502B',foreground='beige',wraplength=210,font=("Oswald",12))
    root.update_idletasks()
    start_pos=canvas.winfo_reqwidth()-lbl2.winfo_reqwidth()-10
    time_now=str(datetime.now()).split('.')[0]
    lbl_time=Label(canvas,text=time_now,background='#2b2b2b',foreground='beige',font=("Verdana",7))
    canvas.create_window(start_pos,saiz,anchor='nw',window=lbl2)
    saiz+=lbl2.winfo_reqheight()+20
    canvas.create_window(canvas.winfo_reqwidth()-lbl_time.winfo_reqwidth()-10,saiz-20,anchor='nw',window=lbl_time)
    saiz+=20
    canvas.configure(yscrollcommand=scrollbar.set,scrollregion=canvas.bbox('all'))
    replyMsg(quiz)
    canvas.yview_moveto(1)
    custom_yview()

send_btn.configure(command=sendMsg)
text_entry.bind("<Return>",sendMsg)
settings_btn.configure(command=animateSettingsPane)
root.mainloop()