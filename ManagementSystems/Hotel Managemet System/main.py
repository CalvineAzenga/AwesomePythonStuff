from tkinter.ttk import Label, Treeview, Button, Scrollbar, Style, Entry, Combobox, Radiobutton, Menubutton, OptionMenu
from tkinter import Canvas, PhotoImage, StringVar, Tk, filedialog
from matplotlib import figure, pyplot
import time
import threading
from PIL import Image, ImageTk, ImageOps, ImageDraw, ImageWin
from win32api import GetSystemMetrics
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame
import os
from pyautogui import grab
import win32print
import win32ui

initCWD = os.getcwd()
my_avatar = os.path.join(os.getcwd(), "./profiles/my_avatar.png")
width = int(GetSystemMetrics(0))
height = int(GetSystemMetrics(1))
# if width > 1366:
#     width = 1366
#     height = 768


# print(width,height)
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

        def load_image():
            initialdirectory = os.getcwd()
            selected_file = filedialog.askopenfilename(
                filetypes=(("Image Files", ".png .jpg .jpeg"), ("All Files", "*.*")), initialdir=initialdirectory)
            thiswidth = int(canvas_checkin_picture.winfo_reqwidth())
            thisheight = int(canvas_checkin_picture.winfo_reqheight())
            if len(selected_file) > 0:
                try:
                    checkin_image2 = str(selected_file)
                    checkin_image2 = circulateImage(checkin_image2, (thiswidth, thisheight))
                    canvas_checkin_picture.create_image(0, 0, image=checkin_image2, anchor='nw')
                    canvas_checkin_picture.image = checkin_image2
                    try:
                        os.chdir("/".join(str(selected_file).split('/')[:-1]))
                    except:
                        pass
                except:
                    try:
                        checkin_image2 = my_avatar
                        checkin_image2 = circulateImage(checkin_image2, (thiswidth, thisheight))
                        canvas_checkin_picture.create_image(0, 0, image=checkin_image2, anchor='nw')
                        canvas_checkin_picture.image = checkin_image2
                    except:
                        pass

        def circulateImage(image, size):
            # size=(70,70)
            mask = Image.new('L', size, 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0) + size, fill=255)
            im = Image.open(image)
            im = im.resize(size, Image.ANTIALIAS)
            output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            # output.save('cally.png')
            output = ImageTk.PhotoImage(output, master=main_window)

            return output

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

        # profile_image=Image.open("cally.png")
        # profile_image=profile_image.resize((100,80),Image.ANTIALIAS)
        # profile_image=ImageTk.PhotoImage(profile_image,master=main_window)

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

        main_window.wm_protocol("WM_DELETE_WINDOW", destroyapp)
        main_window.title("")
        main_window.wm_protocol("WM_DELETE_WINDOW", destroyapp)

        # background_image=Image.open('./icons/cally1.png')
        # background_image=background_image.resize((width,height),Image.ANTIALIAS)
        # background_image=ImageTk.PhotoImage(background_image,master=main_window)

        main_canvas = Canvas(main_window, highlightthickness=0, background='beige')
        main_canvas.place(relx=0, rely=0, relheight=1, relwidth=1)
        # main_canvas.create_image(0,0,image=background_image,anchor='nw')

        appbar = Canvas(main_canvas, highlightthickness=0, background='#001D26')
        appbar.place(relx=0, rely=0, relheight=0.15, relwidth=1)

        welcome_bar = Label(appbar, background='#001D26')
        welcome_bar.place(relx=0.01, rely=0, relwidth=0.5, relheight=1)

        welcome_image_canvas = Canvas(welcome_bar, background='#001D26', highlightthickness=0)
        welcome_image_canvas.place(relx=0, rely=0.20, relheight=0.76, relwidth=0.12)
        welcome_image_canvas.update()

        img_width = welcome_image_canvas.winfo_width()
        img_height = welcome_image_canvas.winfo_height()

        profile_image = "./profiles/my_avatar.png"
        profile_image = circulateImage(profile_image, (img_width, img_height))

        welcome_image_canvas.create_image(0, 0, image=profile_image, anchor='nw')

        welcome_note = Label(welcome_bar, text="Welcome, Calvine " + "[" + f"{PASSEDUSERNAME}" + "]",
                             font=("Bahnschrift Light SemiCondensed", 14), foreground="cyan", background='#001D26')
        welcome_note.place(relx=0.124, rely=0.65)

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

        multi_pane_canvas = Canvas(main_canvas, highlightthickness=0, background='beige')
        multi_pane_canvas.place(relx=0.2025, rely=0.15, relheight=0.85, relwidth=0.7975)

        pane_dashboard = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        pane_check_in = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        pane_check_out = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        pane_settings = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        panedamages = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        panereservations = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        panesuitdata = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')
        panecustomerdetails = Canvas(multi_pane_canvas, highlightthickness=0, background='beige')

        # Begin Dashboard
        dash_welcome_bar = Canvas(pane_dashboard, highlightthickness=0, background='beige')
        dash_welcome_bar.place(relx=0, rely=0, relheight=0.3, relwidth=1)

        box_check_ins = Label(dash_welcome_bar, background="#E86700", text="Check ins[230]",
                              font=("Bahnschrift Light SemiCondensed ", 15), foreground="white", image=checkin_img,
                              compound='top', anchor="center")
        box_check_ins.place(relx=0.01, rely=0.1, relwidth=0.2, relheight=0.8)

        box_check_outs = Label(dash_welcome_bar, background="#55AAF5", text="Check outs[33]",
                               font=("Bahnschrift Light SemiCondensed ", 15), foreground="white", image=checkout_img,
                               compound='top', anchor="center")
        box_check_outs.place(relx=0.22, rely=0.1, relwidth=0.2, relheight=0.8)

        box_room_availability = Label(dash_welcome_bar, background="beige",
                                      font=("Bahnschrift Light SemiCondensed", 15), foreground="#2b2b2b")
        box_room_availability.place(relx=0.44, rely=0.1, relwidth=0.25, relheight=1)

        logout_image = PhotoImage(master=main_window, file="./icons/Exit.png")

        lbl_logout = Label(dash_welcome_bar, text="Logout\t", cursor="hand2",
                           font=("Bahnschrift Light SemiCondensed", 12), image=logout_image, compound='right',
                           background="beige")
        lbl_logout.place(relx=0.85, rely=0.1)

        junior_suite_lbl = Label(box_room_availability, text="Juniour Suites:- ",
                                 font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b", background="beige")
        junior_suite_lbl.grid(row=0, column=0, sticky='w')

        deluxe_suite_lbl = Label(box_room_availability, text="Deluxe Suites:- ",
                                 font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b", background="beige")
        deluxe_suite_lbl.grid(row=1, column=0, sticky='w')

        Executive_suite_lbl = Label(box_room_availability, text="Executive Suites:- ",
                                    font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b",
                                    background="beige")
        Executive_suite_lbl.grid(row=3, column=0, sticky='w')

        Terrace_suite_lbl = Label(box_room_availability, text="Terrace Suites:- ",
                                  font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b",
                                  background="beige")
        Terrace_suite_lbl.grid(row=4, column=0, sticky='w')

        Penthouse_suite_lbl = Label(box_room_availability, text="Penthouse Suites:- ",
                                    font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b",
                                    background="beige")
        Penthouse_suite_lbl.grid(row=5, column=0, sticky='w')

        Villa_suite_lbl = Label(box_room_availability, text="Villa Suites:- ",
                                font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b", background="beige")
        Villa_suite_lbl.grid(row=6, column=0, sticky='w')

        OverwaterBungalow_suite_lbl = Label(box_room_availability, text="Overwater Bungalow:- ",
                                            font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b",
                                            background="beige")
        OverwaterBungalow_suite_lbl.grid(row=7, column=0, sticky='w')

        Presidential_suite_lbl = Label(box_room_availability, text="Presidential Suites:- ",
                                       font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b",
                                       background="beige")
        Presidential_suite_lbl.grid(row=8, column=0, sticky='w')

        Royal_suite_lbl = Label(box_room_availability, text="Royal Suites:- ",
                                font=("Bahnschrift Light SemiCondensed", 10), foreground="#2b2b2b", background="beige")
        Royal_suite_lbl.grid(row=9, column=0, sticky='w')

        # Values

        junior_suite_lbl_amount = Label(box_room_availability, text="23", font=("Bahnschrift Light SemiCondensed", 10),
                                        foreground="darkgreen", background="beige")
        junior_suite_lbl_amount.grid(row=0, column=1, sticky='w')

        deluxe_suite_lbl_amount = Label(box_room_availability, text="5", font=("Bahnschrift Light SemiCondensed", 10),
                                        foreground="darkgreen", background="beige")
        deluxe_suite_lbl_amount.grid(row=1, column=1, sticky='w')

        Executive_suite_lbl_amount = Label(box_room_availability, text="51",
                                           font=("Bahnschrift Light SemiCondensed", 10), foreground="darkgreen",
                                           background="beige")
        Executive_suite_lbl_amount.grid(row=3, column=1, sticky='w')

        Terrace_suite_lbl_amount = Label(box_room_availability, text="47", font=("Bahnschrift Light SemiCondensed", 10),
                                         foreground="darkgreen", background="beige")
        Terrace_suite_lbl_amount.grid(row=4, column=1, sticky='w')

        Penthouse_suite_lbl_amount = Label(box_room_availability, text="6",
                                           font=("Bahnschrift Light SemiCondensed", 10), foreground="darkgreen",
                                           background="beige")
        Penthouse_suite_lbl_amount.grid(row=5, column=1, sticky='w')

        Villa_suite_lbl_amount = Label(box_room_availability, text="33", font=("Bahnschrift Light SemiCondensed", 10),
                                       foreground="darkgreen", background="beige")
        Villa_suite_lbl_amount.grid(row=6, column=1, sticky='w')

        OverwaterBungalow_suite_lbl_amount = Label(box_room_availability, text="8",
                                                   font=("Bahnschrift Light SemiCondensed", 10), foreground="darkgreen",
                                                   background="beige")
        OverwaterBungalow_suite_lbl_amount.grid(row=7, column=1, sticky='w')

        Presidential_suite_lbl_amount = Label(box_room_availability, text="3",
                                              font=("Bahnschrift Light SemiCondensed", 10), foreground="darkgreen",
                                              background="beige")
        Presidential_suite_lbl_amount.grid(row=8, column=1, sticky='w')

        Royal_suite_lbl_amount = Label(box_room_availability, text="2", font=("Bahnschrift Light SemiCondensed", 10),
                                       foreground="darkgreen", background="beige")
        Royal_suite_lbl_amount.grid(row=9, column=1, sticky='w')

        dash_recents = Canvas(pane_dashboard, highlightthickness=0, background='beige')
        dash_recents.place(relx=0, rely=0.3, relheight=0.7, relwidth=0.35)

        lbl_recents = Label(dash_recents, font=("Bahnschrift Light SemiCondensed", 12), text="Recent checkins",
                            background="beige")
        lbl_recents.place(relx=0.01, rely=0.1)

        btn_view_recents = Label(dash_recents, font=("Bahnschrift Light SemiCondensed", 11, "underline"),
                                 text="View all", cursor="hand2", background="beige", foreground="blue")
        btn_view_recents.place(relx=0.8, rely=0.1)

        treeview_recents = Treeview(dash_recents, show="headings", columns=(0, 1, 2, 3, 4, 5, 6),
                                    displaycolumns=(0, 1, 2, 3))
        treeview_recents.place(rely=0.2, relx=0.01, relheight=0.79, relwidth=0.99)

        def fixed_map(option):
            return [elm for elm in s.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

        s.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'),
              fieldbackground=fixed_map('fieldbackground'))

        s.configure("Treeview", foreground="#2b2b2b", font=("Verdana", 8))
        s.configure("Treeview.Heading", foreground="#2b2b2b", borderwidth=1, font=("Verdana", 10, "bold"))
        try:
            treeview_recents.heading('#0')
            treeview_recents.heading(0, text="Name")
            treeview_recents.heading(1, text="H.Count")
            treeview_recents.heading(2, text="Phone")
            treeview_recents.heading(3, text="Gender")
            treeview_recents.column('#0', minwidth=0, width=-200)
            treeview_recents.column(0, width=50)
            treeview_recents.column(1, width=10)
            treeview_recents.column(2, width=30)
            treeview_recents.column(3, width=10)

            for row in range(31):
                treeview_recents.insert('', row, text=row + 1)
                treeview_recents.set(treeview_recents.get_children()[row], column=0, value="Calvine Azenga" + str(row))
                treeview_recents.set(treeview_recents.get_children()[row], column=1, value="33")
                treeview_recents.set(treeview_recents.get_children()[row], column=2, value="0700666848")
                treeview_recents.set(treeview_recents.get_children()[row], column=3, value="Male")
                row += 1

        except:
            pass
        scroll_bar1 = Scrollbar(treeview_recents, orient='vertical')
        scroll_bar1.pack(side='right', fill='y')
        scroll_bar1.config(command=treeview_recents.yview)
        treeview_recents.configure(yscrollcommand=scroll_bar1.set)

        dash_charts = Canvas(pane_dashboard, highlightthickness=0, background='beige')
        dash_charts.place(relx=0.35, rely=0.3, relheight=0.7, relwidth=0.65)

        dash_charts_pie = Canvas(dash_charts, highlightthickness=3, background='beige')
        dash_charts_pie.place(relx=0.01, rely=0.25, relheight=0.75, relwidth=0.4)

        dash_charts_bar = Canvas(dash_charts, highlightthickness=3, background='beige')
        dash_charts_bar.place(relx=0.42, rely=0.1, relheight=0.9, relwidth=0.59)

        stockList = ['Junior', 'Deluxe', 'Presidential', 'Executive', 'Royal', 'Bungalow', 'Villa', 'Penthouse',
                     'Terrace']
        stockSplit = [15, 25, 40, 10, 10, 33, 20, 7, 5]

        fig = Figure(facecolor="beige")
        ax = fig.add_subplot(111)
        ax.pie(stockSplit, radius=1, labels=stockList, autopct='%0.2f%%', shadow=False, textprops={'fontsize': 7})
        # ax.pie(stockSplit,radius=1,labels=stockList,shadow=True)

        chart1 = FigureCanvasTkAgg(fig, dash_charts_pie)
        chart1.get_tk_widget().pack()

        lbl_pie_chart = Label(dash_charts_pie, text="Distribution in Suits",
                              font=("Bahnschrift Light SemiCondensed", 15, "underline"), foreground="#2b2b2b",
                              background="beige")
        lbl_pie_chart.place(rely=0, relx=0.1)

        data1 = {'Month': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
                 'Customers': [450, 85, 65, 12, 78, 123, 458, 156, 78, 123, 325, 42]}
        df1 = DataFrame(data1, columns=['Month', 'Customers'])

        figure1 = Figure(facecolor="beige")
        pyplot.rcParams.update({'font.size': 7})

        # print(pyplot.rcParams.keys())
        ax1 = figure1.add_subplot(111)

        bar1 = FigureCanvasTkAgg(figure1, dash_charts_bar)
        bar1.get_tk_widget().pack(side='left', fill='both')
        df1 = df1[['Month', 'Customers']].groupby('Month').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.tick_params(axis='x', labelrotation=20)

        ax1.set_title('Check Ins Per Month this year')

        # Checkin Pane
        checkin_welcome_lbl = Label(pane_check_in, background='silver', text="Enter the customers Details in this Pane",
                                    font=("Bahnschrift Light SemiCondensed", 15), foreground="#2b2b2b")
        checkin_welcome_lbl.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        checkin_details_canvas = Canvas(pane_check_in, background="beige", highlightthickness=0)
        checkin_details_canvas.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        # Labels

        lbl_checkin_firstname = Label(checkin_details_canvas, background="beige", text="First Name:-",
                                      font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_firstname.grid(row=0, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_secondname = Label(checkin_details_canvas, background="beige", text="Middle Name:-",
                                       font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_secondname.grid(row=1, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_surname = Label(checkin_details_canvas, background="beige", text="Surname:-",
                                    font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_surname.grid(row=2, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_email = Label(checkin_details_canvas, background="beige", text="E-mail:-",
                                  font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_email.grid(row=3, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_phone = Label(checkin_details_canvas, background="beige", text="Phone Number:-",
                                  font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_phone.grid(row=4, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_bday = Label(checkin_details_canvas, background="beige", text="Date of Birth:-",
                                 font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_bday.grid(row=5, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_headcount = Label(checkin_details_canvas, background="beige", text="Head Count:-",
                                      font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_headcount.grid(row=6, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_gender = Label(checkin_details_canvas, background="beige", text="Gender:-",
                                   font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_gender.grid(row=7, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_idnumber = Label(checkin_details_canvas, background="beige", text="ID Number:-",
                                     font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_idnumber.grid(row=8, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_suite = Label(checkin_details_canvas, background="beige", text="Suite Type:-",
                                  font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_suite.grid(row=9, column=0, sticky="w", padx=10, pady=8)

        lbl_checkin_roomnumber = Label(checkin_details_canvas, background="beige", text="Room Number:-",
                                       font=("Bahnschrift Light SemiCondensed", 13))
        lbl_checkin_roomnumber.grid(row=10, column=0, sticky="w", padx=10, pady=8)

        # Text boxes
        txt_checkin_firstname = Entry(checkin_details_canvas, background="beige",
                                      font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_firstname.grid(row=0, column=1, sticky="w", padx=10, pady=8)

        txt_checkin_secondname = Entry(checkin_details_canvas, background="beige",
                                       font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_secondname.grid(row=1, column=1, sticky="w", padx=10, pady=8)

        txt_checkin_surname = Entry(checkin_details_canvas, background="beige",
                                    font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_surname.grid(row=2, column=1, sticky="w", padx=10, pady=8)

        txt_checkin_email = Entry(checkin_details_canvas, background="beige",
                                  font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_email.grid(row=3, column=1, sticky="w", padx=10, pady=8)

        txt_checkin_phone = Entry(checkin_details_canvas, background="beige",
                                  font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_phone.grid(row=4, column=1, sticky="w", padx=10, pady=8)

        txt_checkin_bday = Entry(checkin_details_canvas, background="beige",
                                 font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_bday.grid(row=5, column=1, sticky="w", padx=10, pady=8)

        txt_checkin_headcount = Entry(checkin_details_canvas, background="beige",
                                      font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_headcount.grid(row=6, column=1, sticky="w", padx=10, pady=8)

        def fixed_mapradio(option):
            return [elm for elm in s.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

        # s.map('Wild.TRadiobutton', foreground=fixed_mapradio('foreground'), background=fixed_mapradio('background'),
        #     fieldbackground=fixed_mapradio('fieldbackground'))

        s.configure('TRadiobutton', foreground='#2b2b2b', font=('Bahnschrift Light SemiCondensed', 13),
                    background='beige')

        radio_checkin_gender_male = Radiobutton(checkin_details_canvas, text="Male", value="male", variable=gender)
        radio_checkin_gender_male.grid(row=7, column=1, sticky="w", padx=10, pady=8)

        radio_checkin_gender_female = Radiobutton(checkin_details_canvas, text="Female", value="female",
                                                  variable=gender)
        radio_checkin_gender_female.grid(row=7, column=1, sticky="e", ipadx=20, pady=8)

        txt_checkin_idnumber = Entry(checkin_details_canvas, background="beige",
                                     font=("Bahnschrift Light SemiCondensed", 13))
        txt_checkin_idnumber.grid(row=8, column=1, sticky="w", padx=10, pady=8)

        cmb_checkin_suite = Combobox(checkin_details_canvas, background="beige",
                                     font=("Bahnschrift Light SemiCondensed", 13), state="readonly")
        cmb_checkin_suite.grid(row=9, column=1, sticky="w", padx=10, pady=8)
        cmb_checkin_suite['values'] = ['', 'Junior Suite', 'Executive Suite', 'Presidential Suite', 'Royal Suite',
                                       'Villa', 'Overwater Bungalow', 'Deluxe Suite', 'Penthouse Suite',
                                       'Terrace Suite']

        cmb_checkin_roomnumber = Combobox(checkin_details_canvas, background="beige",
                                          font=("Bahnschrift Light SemiCondensed", 13), state="readonly")
        cmb_checkin_roomnumber.grid(row=10, column=1, sticky="w", padx=10, pady=8)
        cmb_checkin_roomnumber['values'] = ['', 'R1', 'R2', 'R3', 'R4', 'R5']

        # checkin_details_canvas.columnconfigure(index=4,weight=2)

        lbl_checkin_picture = Label(checkin_details_canvas, text="\tPicture:-",
                                    font=("Bahnschrift Light SemiCondensed", 13), background="beige")
        lbl_checkin_picture.grid(row=0, column=3, padx=0, pady=8, sticky='w')

        canvas_checkin_picture = Canvas(checkin_details_canvas, background="beige", highlightthickness=0, width=250,
                                        height=250)
        canvas_checkin_picture.grid(row=0, column=4, rowspan=6, padx=10, pady=8, sticky='e')
        canvas_checkin_picture.update()

        thiswidth = int(canvas_checkin_picture.winfo_reqwidth())
        thisheight = int(canvas_checkin_picture.winfo_reqheight())

        checkin_image2 = "./profiles/a (1).jpg"
        checkin_image2 = circulateImage(checkin_image2, (thiswidth, thisheight))
        canvas_checkin_picture.create_image(0, 0, image=checkin_image2, anchor='nw')

        btn_checkin_browse = Button(checkin_details_canvas, text="Browse Picture", command=load_image)
        btn_checkin_browse.grid(row=7, column=4, padx=10, pady=8, sticky='e')

        btn_checkin_submit = Button(checkin_details_canvas, text="SUBMIT")
        btn_checkin_submit.grid(row=8, column=4, padx=10, pady=8, sticky='e')

        lbl_checkin_stat = Label(checkin_details_canvas, text="Successfully checked in", background="beige",
                                 font=("Bahnschrift Light SemiCondensed", 15), foreground="green")
        lbl_checkin_stat.grid(row=9, column=4, padx=10, pady=20, sticky='w')
        # pane Check out

        checkout_welcome_lbl = Canvas(pane_check_out, highlightthickness=0, background='silver')
        checkout_welcome_lbl.place(relx=0, rely=0, relheight=0.1, relwidth=1)

        checkout_welcome_lbl_text = Label(checkout_welcome_lbl, text="Billing and Checkout", background='silver',
                                          font=("Bahnschrift Light SemiCondensed", 15), foreground="#2b2b2b")
        checkout_welcome_lbl_text.place(relx=0.01, rely=0.3)

        check_out_details_canvas = Canvas(pane_check_out, highlightthickness=0, background='beige')
        check_out_details_canvas.place(relx=0, rely=0.1, relheight=0.9, relwidth=0.6)

        check_out_search_bar = Canvas(check_out_details_canvas, highlightthickness=0, background="beige")
        check_out_search_bar.place(relx=0, rely=0, relheight=0.2, relwidth=1)

        check_out_search_lbl = Label(check_out_search_bar, font=("Bahnschrift Light SemiCondensed", 13),
                                     justify='center', width=30, text="Search Customer by:-", background="beige")
        check_out_search_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        check_out_search_cmb = Combobox(check_out_search_bar, font=("Bahnschrift Light SemiCondensed", 15),
                                        justify='center', state='readonly')
        check_out_search_cmb.grid(row=0, column=1, padx=10, pady=10, sticky='e')
        check_out_search_cmb['values'] = ['ID Number', 'Name', 'Phone Number', 'E-mail']

        check_out_search_entry = Entry(check_out_search_bar, font=("Bahnschrift Light SemiCondensed", 15),
                                       justify='center')
        check_out_search_entry.grid(row=1, column=0, columnspan=1, ipadx=5, pady=10, sticky='e')

        check_out_search_btn = Label(check_out_search_bar, font=("Bahnschrift Light SemiCondensed", 15),
                                     compound='center', image=search_img, background="beige")
        check_out_search_btn.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        check_out_labels_canvas = Canvas(check_out_details_canvas, highlightthickness=0, background='beige')
        check_out_labels_canvas.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

        check_out_name_lbl = Label(check_out_labels_canvas, text="Name:-", background="beige", foreground="#2b2b2b",
                                   font=("Bahnschrift Light SemiCondensed", 13))
        check_out_name_lbl.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        check_out_idnum_lbl = Label(check_out_labels_canvas, text="ID Number:-", background="beige",
                                    foreground="#2b2b2b", font=("Bahnschrift Light SemiCondensed", 13))
        check_out_idnum_lbl.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        check_out_hcount_lbl = Label(check_out_labels_canvas, text="Head Count:-", background="beige",
                                     foreground="#2b2b2b", font=("Bahnschrift Light SemiCondensed", 13))
        check_out_hcount_lbl.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        check_out_gender_lbl = Label(check_out_labels_canvas, text="Gender:-", background="beige", foreground="#2b2b2b",
                                     font=("Bahnschrift Light SemiCondensed", 13))
        check_out_gender_lbl.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        check_out_suite_lbl = Label(check_out_labels_canvas, text="Suite Type:-", background="beige",
                                    foreground="#2b2b2b", font=("Bahnschrift Light SemiCondensed", 13))
        check_out_suite_lbl.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        check_out_roomnum_lbl = Label(check_out_labels_canvas, text="Room Number:-", background="beige",
                                      foreground="#2b2b2b", font=("Bahnschrift Light SemiCondensed", 13))
        check_out_roomnum_lbl.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        check_out_damages_lbl = Label(check_out_labels_canvas, text="Damages Amount:-", background="beige",
                                      foreground="#2b2b2b", font=("Bahnschrift Light SemiCondensed", 13))
        check_out_damages_lbl.grid(row=6, column=0, padx=10, pady=10, sticky='w')

        check_out_name_lbl_value = Label(check_out_labels_canvas, text="Denzel Washington", background="beige",
                                         foreground="maroon", font=("Bahnschrift Light SemiCondensed", 11))
        check_out_name_lbl_value.grid(row=0, column=1, padx=0, pady=10, sticky='w')

        check_out_idnum_lbl_value = Label(check_out_labels_canvas, text="326598", background="beige",
                                          foreground="maroon", font=("Bahnschrift Light SemiCondensed", 11))
        check_out_idnum_lbl_value.grid(row=1, column=1, padx=0, pady=10, sticky='w')

        check_out_hcount_lbl_value = Label(check_out_labels_canvas, text="3", background="beige", foreground="maroon",
                                           font=("Bahnschrift Light SemiCondensed", 11))
        check_out_hcount_lbl_value.grid(row=2, column=1, padx=0, pady=10, sticky='w')

        check_out_gender_lbl_value = Label(check_out_labels_canvas, text="Male", background="beige",
                                           foreground="maroon", font=("Bahnschrift Light SemiCondensed", 11))
        check_out_gender_lbl_value.grid(row=3, column=1, padx=0, pady=10, sticky='w')

        check_out_suite_lbl_value = Label(check_out_labels_canvas, text="Deluxe", background="beige",
                                          foreground="maroon", font=("Bahnschrift Light SemiCondensed", 11))
        check_out_suite_lbl_value.grid(row=4, column=1, padx=0, pady=10, sticky='w')

        check_out_roomnum_lbl_value = Label(check_out_labels_canvas, text="DeluxeRm23", background="beige",
                                            foreground="maroon", font=("Bahnschrift Light SemiCondensed", 11))
        check_out_roomnum_lbl_value.grid(row=5, column=1, padx=0, pady=10, sticky='w')

        check_out_damages_lbl_value = Label(check_out_labels_canvas, text="$ 12.356", background="beige",
                                            foreground="maroon", font=("Bahnschrift Light SemiCondensed", 11))
        check_out_damages_lbl_value.grid(row=6, column=1, padx=0, pady=10, sticky='w')

        check_out_picture_box = Canvas(check_out_labels_canvas, highlightthickness=0, background='beige', width=250,
                                       height=250)
        check_out_picture_box.grid(row=0, column=3, columnspan=3, rowspan=5, sticky='e', padx=50)
        check_out_picture_box.update()

        thiswidth1 = int(check_out_picture_box.winfo_reqwidth())
        thisheight1 = int(check_out_picture_box.winfo_reqheight())

        checkout_image2 = "./profiles/b (4).jpg"
        checkout_image2 = circulateImage(checkout_image2, (thiswidth1, thisheight1))
        check_out_picture_box.create_image(0, 0, image=checkout_image2, anchor='nw')

        check_out_btn_submit = Button(check_out_labels_canvas, text="Check Out")
        check_out_btn_submit.grid(row=7, column=3, pady=30, sticky="e")

        check_out_receipt_canvas = Canvas(pane_check_out, highlightthickness=3, highlightbackground='grey',
                                          background='#C6E3FB')
        check_out_receipt_canvas.place(relx=0.6, rely=0.1, relheight=0.9, relwidth=0.4)

        check_out_receipt_top = Canvas(check_out_receipt_canvas, highlightthickness=0, background='#C6E3FB')
        check_out_receipt_top.place(relx=0.01, rely=0.005, relheight=0.33, relwidth=0.98)

        check_out_receipt_logo_canvas = Canvas(check_out_receipt_top, highlightthickness=0, background='#C6E3FB',
                                               width=120, height=80)
        check_out_receipt_logo_canvas.place(rely=0.01, relx=0.35, relwidth=0.4, relheight=0.47)

        check_out_receipt_logo_canvas.update()

        thiswidth13 = int(check_out_receipt_logo_canvas.winfo_reqwidth())
        thisheight13 = int(check_out_receipt_logo_canvas.winfo_reqheight())

        checkout_image23 = Image.open(initCWD + "/icons/logo.png")
        checkout_image23 = checkout_image23.resize((thiswidth13, thisheight13), Image.ANTIALIAS)
        checkout_image23 = ImageTk.PhotoImage(checkout_image23, master=main_window)
        check_out_receipt_logo_canvas.create_image(0, 0, image=checkout_image23, anchor='nw')

        receipt_details_1 = Label(check_out_receipt_top, text="Platinum Hotel Receipt", anchor='center',
                                  font=("Bahnschrift Light SemiCondensed ", 13), background="#C6E3FB")
        receipt_details_1.place(rely=0.48, relx=0, relwidth=1)

        receipt_details_2 = Label(check_out_receipt_top, text="P.O BOX 165 Kaimosi", anchor='center',
                                  font=("Bahnschrift Light SemiCondensed ", 11), background="#C6E3FB")
        receipt_details_2.place(rely=0.6, relx=0, relwidth=1)

        receipt_details_3 = Label(check_out_receipt_top, text="Tel: +254700666848/+254706231609", anchor='center',
                                  font=("Corbel", 12), background="#C6E3FB")
        receipt_details_3.place(rely=0.72, relx=0, relwidth=1)

        receipt_details_3 = Label(check_out_receipt_top, text="", anchor='center',
                                  font=("Bahnschrift Light SemiCondensed ", 10), background="#C6E3FB")
        receipt_details_3.place(rely=0.84, relx=0, relwidth=1)

        check_out_receipt_center = Canvas(check_out_receipt_canvas, highlightthickness=0, background='#C6E3FB')
        check_out_receipt_center.place(relx=0.01, rely=0.335, relheight=0.55, relwidth=0.98)

        check_out_receipt_separator1 = Canvas(check_out_receipt_center, highlightthickness=0, background='silver')
        check_out_receipt_separator1.place(relx=0.01, rely=0, relheight=0.01, relwidth=0.98)

        check_out_receipt_center_header = Canvas(check_out_receipt_center, highlightthickness=0, background='#C6E3FB')
        check_out_receipt_center_header.place(relx=0.01, rely=0.01, relheight=0.1, relwidth=0.98)

        check_out_receipt_center_header_lbl1 = Label(check_out_receipt_center_header, text="Item Type",
                                                     background='#C6E3FB', font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_header_lbl1.place(relx=0, relwidth=0.3)

        check_out_receipt_center_header_lbl2 = Label(check_out_receipt_center_header, text="Value", background='#C6E3FB',
                                                     font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_header_lbl2.place(relx=0.3, relwidth=0.5)

        check_out_receipt_center_header_lbl3 = Label(check_out_receipt_center_header, text="Cost", background='#C6E3FB',
                                                     font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_header_lbl3.place(relx=0.8, relwidth=0.2)

        check_out_receipt_center_content = Canvas(check_out_receipt_center, highlightthickness=0, background='#C6E3FB')
        check_out_receipt_center_content.place(relx=0.01, rely=0.11, relheight=0.89, relwidth=0.98)

        check_out_receipt_center_suit = Label(check_out_receipt_center_content, text="Suit type", background='#C6E3FB',
                                              font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_center_suit.place(rely=0.02, relx=0.01, relwidth=0.3)

        check_out_receipt_center_suit_type = Label(check_out_receipt_center_content, text="Deluxe", background='#C6E3FB',
                                                   font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_center_suit_type.place(rely=0.02, relx=0.31, relwidth=0.5)

        check_out_receipt_center_suit_amount = Label(check_out_receipt_center_content, text="$342.00",
                                                     background='#C6E3FB', font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_suit_amount.place(rely=0.02, relx=0.81, relwidth=0.2)

        check_out_receipt_center_damages = Label(check_out_receipt_center_content, text="Damage type",
                                                 background='#C6E3FB', font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_center_damages.place(rely=0.13, relx=0.01, relwidth=0.3)

        check_out_receipt_center_damages_type = Label(check_out_receipt_center_content, text="Breakages, Misuse",
                                                      background='#C6E3FB', font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_center_damages_type.place(rely=0.13, relx=0.31, relwidth=0.5)

        check_out_receipt_center_damages_amount = Label(check_out_receipt_center_content, text="$45.36",
                                                        background='#C6E3FB', font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_damages_amount.place(rely=0.13, relx=0.81, relwidth=0.2)

        check_out_receipt_separator3 = Canvas(check_out_receipt_center_content, highlightthickness=0, background='grey')
        check_out_receipt_separator3.place(relx=0.78, rely=0.28, relheight=0.01, relwidth=0.98)

        check_out_receipt_total_bill_lbl = Label(check_out_receipt_center_content, text="Total Bill:",
                                                 background='#C6E3FB', font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_total_bill_lbl.place(rely=0.3, relx=0.31, relwidth=0.5)

        check_out_receipt_center_bill_amount = Label(check_out_receipt_center_content, text="$386.36",
                                                     background='#C6E3FB', font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_bill_amount.place(rely=0.3, relx=0.81, relwidth=0.2)

        check_out_receipt_separator31 = Canvas(check_out_receipt_center_content, highlightthickness=0,
                                               background='grey')
        check_out_receipt_separator31.place(relx=0.78, rely=0.4, relheight=0.01, relwidth=0.98)

        check_out_receipt_total_paid_lbl = Label(check_out_receipt_center_content, text="Total Paid:",
                                                 background='#C6E3FB', font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_total_paid_lbl.place(rely=0.45, relx=0.31, relwidth=0.5)

        check_out_receipt_center_paid_amount = Label(check_out_receipt_center_content, text="$1000.00",
                                                     background='#C6E3FB', font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_center_paid_amount.place(rely=0.45, relx=0.81, relwidth=0.2)

        check_out_receipt_total_balance_lbl = Label(check_out_receipt_center_content, text="Balance:",
                                                    background='#C6E3FB', font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_total_balance_lbl.place(rely=0.55, relx=0.31, relwidth=0.5)

        check_out_receipt_center_balance_amount = Label(check_out_receipt_center_content, text="-$613.64",
                                                        foreground="green", background='#C6E3FB',
                                                        font=("Bahnschrift SemiCondensed", 12))
        check_out_receipt_center_balance_amount.place(rely=0.55, relx=0.81, relwidth=0.2)

        check_out_receipt_total_balance_lbl = Label(check_out_receipt_center_content, anchor='center',
                                                    text="Thank you Denzel for trusting our services\n\twww.platinumhotel.biz",
                                                    background='#C6E3FB', font=("Bahnschrift Light SemiCondensed", 12))
        check_out_receipt_total_balance_lbl.place(rely=0.75, relx=0, relwidth=1, relheight=0.25)

        check_out_receipt_separator2 = Canvas(check_out_receipt_center_header, highlightthickness=0,
                                              background='silver')
        check_out_receipt_separator2.place(relx=0, rely=0.9, relheight=0.1, relwidth=1)

        check_out_receipt_print_btn = Button(check_out_receipt_canvas, text="Print Receipt")
        check_out_receipt_print_btn.place(relx=0.65, rely=0.9)






        # Pane settings
        settings_welcome_lbl = Label(pane_settings, background='silver', text="Tweak some settings",
                                     font=("Bahnschrift Light SemiCondensed", 15), foreground="#2b2b2b")
        settings_welcome_lbl.place(relx=0, rely=0, relwidth=1, relheight=0.1)

        settings_details_canvas = Canvas(pane_settings, background="beige", highlightthickness=0)
        settings_details_canvas.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

        printer_cmb = Combobox(settings_details_canvas, font=("Bahnschrift Light SemiCondensed", 15),state='readonly')
        printer_cmb.grid(row=0, column=0, padx=10, pady=20)

        panes_list = [pane_dashboard, pane_check_in, pane_check_out, pane_settings, panedamages, panereservations,
                      panesuitdata, panecustomerdetails]

        def forgetPanes():
            for pane in panes_list:
                pane.place_forget()

        def loadpaneDashboard(event):
            forgetPanes()
            pane_dashboard.place(relx=0, rely=0, relwidth=1, relheight=1)
            dashboard.configure(foreground='orange', background='grey')

        dashboard.bind("<ButtonPress>", loadpaneDashboard)

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

        def hover2(event):
            box_check_ins.configure(foreground='#2b2b2b', background="orange")

        def leave2(event):
            box_check_ins.configure(foreground='white', background="#FF7F0E")

        def hover31(event):
            box_check_outs.configure(foreground='gold', background="blue")

        def leave31(event):
            box_check_outs.configure(foreground='white', background="#55AAF5")

        box_check_outs.bind("<Enter>", hover31)
        box_check_outs.bind("<Leave>", leave31)
        box_check_ins.bind("<Enter>", hover2)
        box_check_ins.bind("<Leave>", leave2)

        close_lbl.bind("<Motion>", hover)
        close_lbl.bind("<Leave>", leave)
        lbl_minimize.bind("<Motion>", hover1)
        lbl_minimize.bind("<Leave>", leave1)
        close_lbl.bind("<ButtonPress>", destroyapp2)

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
            receipt_details_3.configure(text=now)
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

        def listPrinterNames():
            # data = subprocess.check_output(['wmic', 'printer', 'list', 'brief']).decode('utf-8').split('\r\r\n')
            # data = data[1:]
            # i = 0
            # printerlist = []
            # for line in data:
            #     for printer_name in line.split('  '):
            #         if printer_name != "":
            #             printerlist.append(printer_name)
            #             i += 1
            #             break
            printer_info=win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)
            # print(printer_info)

            printer_names=[name for(flgs, description,name,comment) in printer_info]
            printerlist=[]

            for i, name in enumerate(printer_names):
                printerlist.append(name)
                # print(name)
            printer_cmb['value'] = printerlist
            defaultPrinter=win32print.GetDefaultPrinter()
            if defaultPrinter in printerlist:
                printer_cmb.set(defaultPrinter)
                printer_cmb.select_clear()
            main_window.after(5000,listPrinterNames)
        listPrinterNames()

        def selectDefaultPrinter(event):
            defaultPrinter=printer_cmb.get()
            try:
                win32print.SetDefaultPrinter(defaultPrinter)
            except Exception as msg:
                print(msg)
                pass

        def printrecept():
            def printreceipthred():
                x2 = sidebar_pane.winfo_width() + separator.winfo_width() + check_out_details_canvas.winfo_width() + main_window.winfo_rootx()
                y2 = appbar.winfo_height() + checkout_welcome_lbl.winfo_height() + main_window.winfo_rooty()
                receipt_width = check_out_receipt_canvas.winfo_width()
                receipt_height = check_out_receipt_center.winfo_height() + check_out_receipt_top.winfo_height()

                imagee = grab(region=(x2, y2, receipt_width, receipt_height))
                imagee=imagee.convert("P")
                imagee=imagee.convert("RGB")
                
                imagee = imagee.resize((int(imagee.size[0] / 1.1), int(imagee.size[1] * 1.15)), Image.ANTIALIAS)
                HORZRES = 8
                VERTRES = 10

                LOGPIXELSX = 88
                LOGPIXELSY = 90

                PHYSICALWIDTH = 110
                PHYSICALHEIGHT = 111

                PHYSICALOFFSETX = 112
                PHYSICALOFFSETY = 113

                printer_name = win32print.GetDefaultPrinter()
                # print(printer_name)
                hDC = win32ui.CreateDC()
                hDC.CreatePrinterDC(printer_name)
                printable_area = hDC.GetDeviceCaps(HORZRES), hDC.GetDeviceCaps(VERTRES)
                printer_size = hDC.GetDeviceCaps(PHYSICALWIDTH), hDC.GetDeviceCaps(PHYSICALHEIGHT)
                printer_margins = hDC.GetDeviceCaps(PHYSICALOFFSETX), hDC.GetDeviceCaps(PHYSICALOFFSETY)
                

                bmp = imagee
                

                # if bmp.size[0] > bmp.size[1]:
                #     bmp.rotate(90)

                ratios = [1.0 * printable_area[0] / bmp.size[0], 1.0 * printable_area[1] / bmp.size[1]]
                scale = min(ratios)

                hDC.StartDoc("file_name")
                hDC.StartPage()

                dib = ImageWin.Dib(bmp)
                scaled_width, scaled_height = [int(scale * i) for i in bmp.size]
                x1 = int((printer_size[0] - scaled_width) / 2)
                y1 = int((printer_size[1] - scaled_height) / 2)

                x2 = scaled_width
                y2 = scaled_height
                dib.draw(hDC.GetHandleOutput(), (x1, y1, x2, y2))

                hDC.EndPage()
                hDC.EndDoc()
                hDC.DeleteDC()
                
                pixdata = imagee.load()
                
                #
                # for y in range(imagee.size[1]):
                #     for x in range(imagee.size[0]):
                #         if pixdata[x, y] == (245, 245, 220):
                #             pixdata[x, y] = (255, 250, 250)
                
                imagee.show()

            threading.Thread(target=printreceipthred, daemon=True).start()

        check_out_receipt_print_btn.configure(command=printrecept)

        lbl_minimize.bind("<ButtonPress>", minimize_window)
        printer_cmb.bind("<<ComboboxSelected>>",selectDefaultPrinter)
        forgetPanes()
        pane_dashboard.place(relx=0, rely=0, relwidth=1, relheight=1)
        main_window.mainloop()


MAINAPPLICATION()
