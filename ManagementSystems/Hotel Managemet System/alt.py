from tkinter.ttk import Label,Button,Style,Combobox,Entry
from tkinter import Label, PhotoImage, Canvas, font
import ttkthemes as tk
from tkinter.constants import E
from win32api import GetSystemMetrics
import pyttsx3

# pyttsx3.init()
# engine=pyttsx3.Engine()

# engine.say("Welcome Calvin, hello to you, you've  logged in successfully.")
# engine.runAndWait()
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

def LOGINSYSTEM():
    
    root=tk.ThemedTk()
    
    root.set_theme('clam')
    root.geometry(f"{int(width/1.2)}x{int(height/1.2)}")
    root.resizable(width=1, height=1)
    icon=PhotoImage(master=root,height=16,width=16)
    icon.blank()
    icon.transparency_set(0,0,0)
    root.iconphoto(False,icon)
    root.overrideredirect(1)
    root.attributes("-topmost",True)
    def destroyapp():
        root.destroy()
    

    # To center the window
    try:
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

    root.wm_protocol("WM_DELETE_WINDOW",destroyapp)



    main_canvas=Canvas(root,bg='beige')
    main_canvas.place(relx=0,rely=0,relheight=1,relwidth=1)

    app_bar_canvas=Label(main_canvas,bg='#5C723D',text="PLATINUM HOTEL MS",highlightthickness=0, font=("Pacific0",30),fg='lime')
    app_bar_canvas.place(relx=0,rely=0,relheight=0.2,relwidth=1)

    details_canvas=Canvas(main_canvas,bg='beige',highlightthickness=0)
    details_canvas.place(relx=0,rely=0.2,relheight=0.8,relwidth=1)

    lbl_login=Label(details_canvas,text="Login",font=("Pacifico",20),bg='beige',fg="#202634")
    lbl_login.place(relx=0.35,relwidth=0.3,rely=0.04)

    login_pane=Canvas(details_canvas,background='beige',highlightthickness=0)
    login_pane.place(relx=0.2,relwidth=0.6,rely=0.14,relheight=0.85)

    lbl_stat=Label(login_pane,text="Error or success",background='beige',font=("oswald",13))
    lbl_stat.grid(row=0,column=0,columnspan=2,pady=10,padx=10,sticky="e")

    lbl_cmb=Label(login_pane,text="Privilege Level",font="Verdana 15",bg='beige',fg='grey')
    lbl_cmb.grid(row=1,column=0,pady=10,padx=10,sticky="e")

    cmb_level=Combobox(login_pane,width=19,font="Verdana 15")
    cmb_level.grid(row=1, column=1,padx=8,sticky='w')
    

    lbl_username=Label(login_pane,text="Username",font="Verdana 15",bg='beige',fg='grey')
    lbl_username.grid(row=2,column=0,pady=10,padx=10,sticky="e")

    username_entry=Entry(login_pane,width=20,font="Verdana 15")
    username_entry.grid(row=2, column=1,padx=8,sticky='w')

    lbl_password=Label(login_pane,text="password",font="Verdana 15",bg='beige',fg='grey')
    lbl_password.grid(row=3,column=0,pady=10,padx=10,sticky="e")

    password_entry=Entry(login_pane,show='*',width=20,font="Verdana 15")
    password_entry.grid(row=3, column=1,padx=8,sticky='w')
    def fixed_map2(option):
        return [elm for elm in s.map('TButton', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    s=Style()

    s.map('TButton', foreground=fixed_map2('foreground'), background=fixed_map2('background'),
        fieldbackground=fixed_map2('fieldbackground'))

    s.configure("TButton",font=("Verdana",13))

    btn_submit=Button(login_pane,text="Submit")
    btn_submit.grid(row=4,column=0,columnspan=2,pady=20,padx=10,sticky="e")

    def save_last_pos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def dragging(event):
        x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+{0}+{1}".format(x, y))

    root.bind('<B1-Motion>', dragging)
    root.bind('<Button-1>', save_last_pos)
    root.mainloop()
    pass
        

LOGINSYSTEM()