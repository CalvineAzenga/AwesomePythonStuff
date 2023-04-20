import threading
from tkinter.ttk import Label, Button, Style, Combobox, Entry, Treeview
from tkinter import Label, PhotoImage, Canvas, font
from PIL import Image
import ttkthemes as tk
from tkinter.constants import E
from ttkthemes.themed_tk import ThemedTk
from win32api import GetSystemMetrics
import time
from includes import login_script
from main import MAINAPPLICATION

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)


class LOGINSYSTEM():
    def __init__(self):
        def destroyapp():
            self.root.destroy()

        self.root = tk.ThemedTk()
        self.root.set_theme('clam')
        self.root.geometry(f"{int(width / 1.5)}x{int(height / 1.5)}")
        self.root.resizable(width=0, height=0)
        icon = PhotoImage(master=self.root, height=16, width=16)
        icon.blank()
        icon.transparency_set(0, 0, 0)
        self.root.iconphoto(False, icon)
        # self.root.overrideredirect(1)
        self.root.title("")
        self.root.attributes("-toolwindow", True)
        self.root.attributes("-topmost", True)

        # images
        success_image = PhotoImage(master=self.root, file='./icons/yes2.png')
        failure_image = PhotoImage(master=self.root, file='./icons/critical_icon.png')
        level_image = PhotoImage(master=self.root, file='./icons/btlog.png')
        user_image = PhotoImage(master=self.root, file='./icons/User.png')
        password_image = PhotoImage(master=self.root, file='./icons/login.png')

        # To center the window
        try:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            app_height = self.root.winfo_height()
            app_width = self.root.winfo_width()

            x_loc = int(screen_width / 2) - int(app_width / 2)
            y_loc = int(screen_height / 2) - int(app_height / 2)

            self.root.geometry("+{}+{}".format(x_loc, y_loc))
        except Exception as msg:
            print(msg)
            pass

        self.root.wm_protocol("WM_DELETE_WINDOW", destroyapp)

        main_canvas = Canvas(self.root, bg='beige')
        main_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        app_bar_canvas = Label(main_canvas, bg='#5C723D', text="PLATINUM HOTEL MS", highlightthickness=0,
                               font=("Lucida Calligraphy", 25), fg='lime')
        app_bar_canvas.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        details_canvas = Canvas(main_canvas, bg='beige', highlightthickness=0)
        details_canvas.place(relx=0, rely=0.2, relheight=0.8, relwidth=1)

        lbl_login = Label(details_canvas, text="Login", font=("Pacifico", 20), bg='beige', fg="#202634")
        lbl_login.place(relx=0.35, relwidth=0.3, rely=0.04)

        login_pane = Canvas(details_canvas, background='beige', highlightthickness=0)
        login_pane.place(relx=0.2, relwidth=0.6, rely=0.14, relheight=0.85)

        lbl_stat = Label(login_pane, text="", background='beige', font=("oswald", 13))
        lbl_stat.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="e")

        lbl_cmb = Label(login_pane, text="User Level", font="Verdana 14", bg='beige', fg='green', image=level_image,
                        compound='right')
        lbl_cmb.grid(row=1, column=0, pady=10, padx=10, sticky="e")

        cmb_level = Combobox(login_pane, width=19, font="Verdana 14", state='readonly', foreground='indigo',
                             justify='center')
        cmb_level.grid(row=1, column=1, padx=8, sticky='w')
        cmb_level['values'] = ['', 'Admin', 'Cashier', 'User']

        lbl_username = Label(login_pane, text="Username", font="Verdana 14", bg='beige', fg='green', image=user_image,
                             compound='right')
        lbl_username.grid(row=2, column=0, pady=10, padx=10, sticky="e")

        username_entry = Entry(login_pane, width=20, font="Verdana 14", foreground='indigo', justify='center')
        username_entry.grid(row=2, column=1, padx=8, sticky='w')

        lbl_password = Label(login_pane, text="password", font="Verdana 14", bg='beige', fg='green',
                             image=password_image, compound='right')
        lbl_password.grid(row=3, column=0, pady=10, padx=10, sticky="e")

        password_entry = Entry(login_pane, show='*', width=20, font="Verdana 14", foreground='indigo', justify='center')
        password_entry.grid(row=3, column=1, padx=8, sticky='w')

        def fixed_map2(option):
            return [elm for elm in s.map('TButton', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

        s = Style(self.root)

        s.map('TButton', foreground=fixed_map2('font'))

        s.configure("TButton", font=("Verdana", 13))

        def loginApp():
            level = str(cmb_level.get()).lower()
            username = username_entry.get()
            password = password_entry.get()
            if level == "" or username == "":
                lbl_stat.configure(text="Empty field(s) detected!", foreground='orangered', image=failure_image,
                                   compound='left')
                return
            uname = login_script.try_login(username, level, password)
            if uname[0:7] == 'SUCCESS':
                lbl_stat.configure(text=" " + uname[7:] + " successfully logged in.", foreground='green',
                                   image=success_image, compound='left')

                def loadmainapp():
                    time.sleep(1)
                    self.root.grab_release()
                    self.root.withdraw()
                    MAINAPPLICATION(uname[7:])
                    self.root.grab_set()
                    cmb_level.current(0)
                    lbl_stat.configure(image="", text="")
                    username_entry.delete(0, "end")
                    password_entry.delete(0, "end")
                    self.root.deiconify()

                thread = threading.Thread(target=loadmainapp)
                thread.daemon = True
                thread.start()

            else:
                lbl_stat.configure(text=uname, foreground='orangered', image=failure_image, compound='left')

        btn_submit = Button(login_pane, text="Submit", command=loginApp)
        btn_submit.grid(row=4, column=0, columnspan=2, pady=20, padx=10, sticky="e")

        def save_last_pos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y

        def dragging(event):
            x, y = event.x - lastClickX + self.root.winfo_x(), event.y - lastClickY + self.root.winfo_y()
            self.root.geometry("+{0}+{1}".format(x, y))

        self.root.bind('<B1-Motion>', dragging)
        self.root.bind('<Button-1>', save_last_pos)
        self.root.mainloop()
        pass

LOGINSYSTEM()
