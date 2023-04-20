from tkinter.ttk import Label, Button, Scrollbar, Style
from tkinter import Canvas, PhotoImage, StringVar, Tk
import time
from win32api import GetSystemMetrics
import os
from pyautogui import grab


initCWD = os.getcwd()
my_avatar = os.path.join(os.getcwd(), "./profiles/my_avatar.png")
width = int(GetSystemMetrics(0))
height = int(GetSystemMetrics(1))
if width > 1366:
    width = 1366
    height = 768


print(width,height)
class MAINAPPLICATION():
    def __init__(self, PASSEDUSERNAME="Calvin") -> None:
        def destroyapp():
            main_window.destroy()

        def destroyapp2(event):
            main_window.destroy()

        main_window = Tk()
        s = Style(main_window)
        s.theme_use('clam')

        main_window.geometry(f"{int(width)}x{int(height)}+0+0")
        main_window.resizable(width=0, height=0)

        icon = PhotoImage(master=main_window, height=16, width=16)
        icon.blank()
        icon.transparency_set(0, 0, 0)
        main_window.iconphoto(False, icon)
        main_window.title("")
        gender = StringVar(main_window)
        # main_window.attributes("-topmost", True)
        main_window.overrideredirect(1)

        # Images
        dashboard_img = PhotoImage(master=main_window, file="./images/4panes/dashboard.png")
        checkin_img = PhotoImage(master=main_window, file="./images/4panes/login.png")
        checkout_img = PhotoImage(master=main_window, file="./images/4panes/logout.png")
        settings_img = PhotoImage(master=main_window, file="./images/4panes/settings.png")
        damages_img = PhotoImage(master=main_window, file="./images/4panes/delete1.png")
        reservations_img = PhotoImage(master=main_window, file="./images/4panes/edit.png")
        customerdetails_img = PhotoImage(master=main_window, file="./images/4panes/add_list.png")
        suitsdata_img = PhotoImage(master=main_window, file="./images/4panes/opera_glasses.png")
        search_img = PhotoImage(master=main_window, file="./images/4panes/search.png")
        view_img = PhotoImage(master=main_window, file="./images/4panes/view2.png")

        def fixed_map2(option):
            return [elm for elm in s.map('TButton', query_opt=option) if elm[:2] != ('!disabled', '!selected')]
        s.map('TButton', foreground=fixed_map2('font'))
        s.configure("TButton", font=("Bahnschrift Light SemiCondensed", 13))

        # To center the window
        try:
            screen_width = main_window.winfo_screenwidth()
            screen_height = main_window.winfo_screenheight()
            app_height = main_window.winfo_height()
            app_width = main_window.winfo_width()

            x_loc = int(screen_width / 2) - int(app_width / 2)
            y_loc = int(screen_height / 2) - int(app_height / 2)

            main_window.geometry("+{}+{}".format(x_loc, y_loc))
        except Exception as msg:
            print(msg)
            pass

        main_canvas = Canvas(main_window, highlightthickness=0, background='beige')
        main_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)

        appbar = Canvas(main_canvas, highlightthickness=0, background='#001D26')
        appbar.place(relx=0, rely=0, relheight=0.15, relwidth=1)

        welcome_bar = Label(appbar, background='#001D26')
        welcome_bar.place(relx=0.01, rely=0, relwidth=0.5, relheight=1)

        welcome_image_canvas = Canvas(welcome_bar, background='#001D26', highlightthickness=0)
        welcome_image_canvas.place(relx=0, rely=0.20, relheight=0.76, relwidth=0.12)
        welcome_image_canvas.update()

        bragging_lbl = Label(appbar, text="Built with love by Calvo Softwares", font=("Bahnschrift Light SemiCondensed ", 12,"italic"), background='#001D26',
                         foreground="lime")
        bragging_lbl.place(relx=0.01, rely=0.8 )


        time_lbl = Label(appbar, text="", font=("Bahnschrift Light SemiCondensed ", 15), background='#001D26',
                         foreground="gold")
        time_lbl.place(relx=0.8, rely=0.6, )

        close_lbl = Label(appbar, text="X", font="Monospace 20", background='#001D26', foreground='white')
        close_lbl.place(relx=0.97, rely=0)

        lbl_minimize = Label(appbar, text="─", font="Monospace 20", background='#001D26', foreground='white')
        lbl_minimize.place(relx=0.94, rely=0)

        sidebar_pane = Canvas(main_canvas, highlightthickness=0, background='#001D26')
        sidebar_pane.place(relx=0, rely=0.15, relwidth=0.2, relheight=0.85)

        separator = Canvas(main_canvas, background='silver', highlightthickness=0)
        separator.place(relx=0.2, rely=0.15, relwidth=0.0025, relheight=0.85)

        # Side Bar Buttons (I used Labels to represent buttons) 

        dashboard = Label(sidebar_pane, text="Dashboard", font=("Bahnschrift Light SemiCondensed", 12),
                          background='beige', image=dashboard_img, compound='left')
        dashboard.place(rely=0, relx=0, relwidth=1, relheight=0.1)

        check_in = Label(sidebar_pane, text="Check In", font=("Bahnschrift Light SemiCondensed", 12),
                         background='beige', image=checkin_img, compound='left')
        check_in.place(rely=0.101, relx=0, relwidth=1, relheight=0.1)

        check_out = Label(sidebar_pane, text="Check Out", font=("Bahnschrift Light SemiCondensed", 12),
                          background='beige', image=checkout_img, compound='left')
        check_out.place(rely=0.203, relx=0, relwidth=1, relheight=0.1)

        customer_details = Label(sidebar_pane, text="Customer Details", font=("Bahnschrift Light SemiCondensed", 12),
                                 background='beige', image=customerdetails_img, compound='left')
        customer_details.place(rely=0.305, relx=0, relwidth=1, relheight=0.1)

        reservations = Label(sidebar_pane, text="Reservations", font=("Bahnschrift Light SemiCondensed", 12),
                             background='beige', image=reservations_img, compound='left')
        reservations.place(rely=0.407, relx=0, relwidth=1, relheight=0.1)

        suitesdata = Label(sidebar_pane, text="Suites Data", font=("Bahnschrift Light SemiCondensed", 12),
                           background='beige', image=suitsdata_img, compound='left')
        suitesdata.place(rely=0.509, relx=0, relwidth=1, relheight=0.1)

        damages = Label(sidebar_pane, text="Damages", font=("Bahnschrift Light SemiCondensed", 12), background='beige',
                        image=damages_img, compound='left')
        damages.place(rely=0.611, relx=0, relwidth=1, relheight=0.1)

        settings = Label(sidebar_pane, text="Settings", font=("Bahnschrift Light SemiCondensed", 12),
                         background='beige', image=settings_img, compound='left')
        settings.place(rely=0.713, relx=0, relwidth=1, relheight=0.1)

        btn_logs = Button(sidebar_pane, text="View Logs", image=view_img, compound='left')
        btn_logs.place(relx=0.2, relwidth=0.6, relheight=0.08, rely=0.84)

        # End of Side Bar Buttons 

        multi_pane_canvas = Canvas(main_canvas, highlightthickness=0, background='beige') # Where the canvases to be produced by sidebar will pack
        multi_pane_canvas.place(relx=0.2025, rely=0.15, relheight=0.85, relwidth=0.7975)

        # The Canvases. Keep their backgrounds as beige for better feel

        pane_dashboard = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        pane_check_in = Canvas(multi_pane_canvas, highlightthickness=0, background='orange')
        pane_check_out = Canvas(multi_pane_canvas, highlightthickness=0, background='yellow')
        pane_settings = Canvas(multi_pane_canvas, highlightthickness=0, background='indigo')
        panedamages = Canvas(multi_pane_canvas, highlightthickness=0, background='violet')
        panereservations = Canvas(multi_pane_canvas, highlightthickness=0, background='blue')
        panesuitdata = Canvas(multi_pane_canvas, highlightthickness=0, background='orangered')
        panecustomerdetails = Canvas(multi_pane_canvas, highlightthickness=0, background='green')

        # Begin Dashboard
        dash_welcome_bar = Canvas(pane_dashboard, highlightthickness=0, background='beige')
        dash_welcome_bar.place(relx=0, rely=0, relheight=0.3, relwidth=1)

        logout_image = PhotoImage(master=main_window, file="./icons/Exit.png")

        lbl_logout = Label(dash_welcome_bar, text="Logout\t", cursor="hand2",
                           font=("Bahnschrift Light SemiCondensed", 12), image=logout_image, compound='right',
                           background="beige")
        lbl_logout.place(relx=0.85, rely=0.1)

        dash_recents = Canvas(pane_dashboard, highlightthickness=0, background='beige')
        dash_recents.place(relx=0, rely=0.3, relheight=0.7, relwidth=0.35)

        panes_list = [pane_dashboard, pane_check_in, pane_check_out, pane_settings, panedamages, panereservations,
                      panesuitdata, panecustomerdetails]

        # Functions To load the various Canvases 

        def forgetPanes():
            for pane in panes_list:
                pane.place_forget()

        def loadpaneDashboard(event):
            forgetPanes()
            pane_dashboard.place(relx=0, rely=0, relwidth=1, relheight=1)
            dashboard.configure(foreground='orange', background='grey')

        dashboard.bind("<ButtonPress>", loadpaneDashboard) # Side Bar Button ++Dashboard++ when pressed to load the above function

        def loadpaneCheckIn(event):
            forgetPanes()
            pane_check_in.place(relx=0, rely=0, relwidth=1, relheight=1)
            check_in.configure(foreground='orange', background='grey')

        check_in.bind("<ButtonPress>", loadpaneCheckIn)

        def loadpaneCheckOut(event):
            forgetPanes()
            pane_check_out.place(relx=0, rely=0, relwidth=1, relheight=1)
            check_out.configure(foreground='orange', background='grey')

        check_out.bind("<ButtonPress>", loadpaneCheckOut)

        def loadpaneCustomerDetails(event):
            forgetPanes()
            panecustomerdetails.place(relx=0, rely=0, relwidth=1, relheight=1)
            customer_details.configure(foreground='orange', background='grey')

        customer_details.bind("<ButtonPress>", loadpaneCustomerDetails)

        def loadpaneSuiteData(event):
            forgetPanes()
            panesuitdata.place(relx=0, rely=0, relwidth=1, relheight=1)
            suitesdata.configure(foreground='orange', background='grey')

        suitesdata.bind("<ButtonPress>", loadpaneSuiteData)

        def loadpaneSettings(event):
            forgetPanes()
            pane_settings.place(relx=0, rely=0, relwidth=1, relheight=1)
            settings.configure(foreground='orange', background='grey')

        settings.bind("<ButtonPress>", loadpaneSettings)

        def loadpaneDamages(event):
            forgetPanes()
            panedamages.place(relx=0, rely=0, relwidth=1, relheight=1)
            damages.configure(foreground='orange', background='grey')

        damages.bind("<ButtonPress>", loadpaneDamages)

        def loadpaneReservations(event):
            forgetPanes()
            panereservations.place(relx=0, rely=0, relwidth=1, relheight=1)
            reservations.configure(foreground='orange', background='grey')

        reservations.bind("<ButtonPress>", loadpaneReservations)

        # Various effects like changing colors on hover or mouse leave 

        sidebar_list = [dashboard, check_in, check_out, customer_details, suitesdata, settings, damages, reservations]
        def hover3(lbl):
            lbl.configure(foreground='purple', background='silver', font=("Bahnschrift Light SemiCondensed", 11))

        def leave3(lbl):
            lbl.configure(foreground='#2b2b2b', background='beige', font=("Bahnschrift Light SemiCondensed", 12))

        for labl in sidebar_list:
            labl.bind("<Enter>", lambda event, lbl=labl: hover3(lbl))
            labl.bind("<Leave>", lambda event, lbl=labl: leave3(lbl))

        def hover(event):
            close_lbl.configure(foreground='red')

        def leave(event):
            close_lbl.configure(foreground='white')

        def hover1(event):
            lbl_minimize.configure(foreground='cyan')

        def leave1(event):
            lbl_minimize.configure(foreground='white')


        close_lbl.bind("<Motion>", hover)
        close_lbl.bind("<Leave>", leave)
        lbl_minimize.bind("<Motion>", hover1)
        lbl_minimize.bind("<Leave>", leave1)
        close_lbl.bind("<ButtonPress>", destroyapp2)

        # Functionality to enable dragging the window

        def save_last_pos(event):
            global lastClickX, lastClickY
            lastClickX = event.x
            lastClickY = event.y
        
        def dragging(event):
            x, y = event.x - lastClickX + main_window.winfo_x(), event.y - lastClickY + main_window.winfo_y()
            main_window.geometry("+{0}+{1}".format(x, y))

        welcome_bar.bind('<B1-Motion>', dragging)
        welcome_bar.bind('<Button-1>', save_last_pos)
        appbar.bind('<B1-Motion>', dragging)
        appbar.bind('<Button-1>', save_last_pos)

        def updatetime():
            now = time.asctime()
            time_lbl.configure(text=now)
            main_window.after(1, updatetime)

        updatetime()

        def minimize_window(event):
            main_window.overrideredirect(0)
            main_window.iconify()

        def winfocuse():
            if main_window.state() == 'normal':
                main_window.overrideredirect(1)
            main_window.after(1, winfocuse)

        winfocuse()

       
        lbl_minimize.bind("<ButtonPress>", minimize_window)
        forgetPanes()
        pane_dashboard.place(relx=0, rely=0, relwidth=1, relheight=1)
        main_window.mainloop()


MAINAPPLICATION()
