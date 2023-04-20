from tkinter import Frame, Label, font
from tkinter.ttk import Style, Treeview, Scrollbar

# frame = PhotoImage(data=running_dog, format='gif -index %i' % (frame_cnt))
from controller.chats.dashboadCharts import performanceChart, plotCharts


class Dashboard:
    def __init__(self, master):
        self.master = master
        self.style = Style(self.master)
        self.mainFrame = Frame(self.master, background="#DCDAD5")
        self.mainFrame.pack(side="left", fill="both", padx=4, pady=4, expand=True)
        self.welcomeLbl = Label(self.mainFrame, text="Good morning, Monica", background="#DCDAD5", foreground="#2b2b2b",
                                font=("Lucida Calligraphy", 12))
        self.welcomeLbl.pack(side="top", anchor="nw", padx=5, pady=(10, 0))

        self.contentPane = Frame(self.mainFrame, background="#DCDAD5")
        self.contentPane.pack(side="bottom", fill="both", anchor="center", expand=True)

        self.leftContentPane = Frame(self.contentPane, background="#DCDAD5")
        self.leftContentPane.place(relx=0, rely=0, relheight=1, relwidth=0.4)

        self.rightContentPane = Frame(self.contentPane, background="#DCDAD5")
        self.rightContentPane.place(relx=0.4, rely=0.1, relheight=0.9, relwidth=0.6)

        self.box_dashboard_1 = Frame(self.leftContentPane, relief="flat", border=0, background="#DCDAD5")
        self.box_dashboard_1.place(relx=0.0, rely=0.01, relwidth=0.9, relheight=0.3)

        self.lbl_1 = Label(self.box_dashboard_1, font=("Verdana", 10), text='Payable time this week',
                           background="#DCDAD5", foreground="#282F47")
        self.lbl_1.grid(row=0, column=0, sticky='e', padx=4, pady=(15, 5))

        self.lbl_1_ = Label(self.box_dashboard_1, font=("Verdana", 10, 'bold'), text='456.78 Hrs', background="#DCDAD5",
                            foreground="maroon")
        self.lbl_1_.grid(row=0, column=1, sticky='w', padx=4, pady=(15, 5))

        self.lbl_2 = Label(self.box_dashboard_1, font=("Verdana", 10), text='Top workers this week(Hrs)',
                           background="#DCDAD5", foreground="#282F47")
        self.lbl_2.grid(row=1, column=0, sticky='e', padx=4, pady=(0, 5))

        self.lbl_2_ = Label(self.box_dashboard_1, font=("Verdana", 10, 'bold'), text='-> Jane Virginia [38.46]',
                            background="#DCDAD5",
                            foreground="#2b2b2b")
        self.lbl_2_.grid(row=1, column=1, sticky='w', padx=4, pady=(0, 5))

        self.lbl_3_ = Label(self.box_dashboard_1, font=("Verdana", 10, 'bold'), text='-> Mikel Schofield [37.23]',
                            background="#DCDAD5",
                            foreground="#2b2b2b")
        self.lbl_3_.grid(row=2, column=1, sticky='w', padx=4, pady=(0, 5))

        self.lbl_4_ = Label(self.box_dashboard_1, font=("Verdana", 10, 'bold'), text='-> Chandler Bong [37.22]',
                            background="#DCDAD5",
                            foreground="#2b2b2b")
        self.lbl_4_.grid(row=3, column=1, sticky='w', padx=4, pady=(0, 5))

        self.box_dashboard_2 = Frame(self.leftContentPane, relief="ridge", border=2, background="#5C723D")
        self.box_dashboard_2.place(relx=0.0, rely=0.32, relwidth=0.9, relheight=0.6)

        self.box2_title = Label(self.box_dashboard_2, text='Highest Throughput Projection', background="#5C723D",
                                font=("Verdana", 12), foreground='#282923')
        self.box2_title.pack(side='top', fill='x', ipady=8)

        self.box_treeview_frame = Frame(self.box_dashboard_2, relief="ridge", border=2, background="#9EC862")
        self.box_treeview_frame.pack(side='top', fill='both', expand=True)

        self.style.configure("Treeview", font=("Verdana", 8), foreground="#2b2b2b", fieldbackground="#F5F5F5")
        self.style.configure("Treeview.Heading", font=("Verdana", 10), foreground="#2b2b2b", background="#9EC862")
        self.style.map("Treeview", background=[('selected', '#878787')], font=[('selected', ('Verdana', 8, 'bold'))],
                       foreground=[('selected', '#2B2B2B')])

        scrollbar = Scrollbar(self.box_treeview_frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        treeview = Treeview(self.box_treeview_frame,
                            columns=("Department", "ID", "Name", "Score"),
                            show="headings",
                            selectmode="browse")
        treeview.pack(side="left", fill="both", expand=1, padx=0)

        treeview.tag_configure("odd", background="#F5F5F5")
        treeview.tag_configure("even", background="#FFFFFF")

        treeview.heading("#1", text="Department", anchor="center")
        treeview.heading("#2", text="Employee ID", anchor="center")
        treeview.heading("#3", text="Name", anchor="center")
        treeview.heading("#4", text="Score", anchor="center")

        treeview.column("#1", anchor="center", width=10)
        treeview.column("#2", anchor="center", width=10)
        treeview.column("#3", anchor="center", width=10)
        treeview.column("#4", anchor="center", width=10)

        treeview.tag_configure("odd", background="#eee")
        treeview.tag_configure("even", background="#ddd")
        treeview.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=treeview.yview)

        for i in range(1, 201):
            if i % 2 == 0:
                treeview.insert('', 'end', values=(f"Cat {i}", i, f"Spyrogyra {i}", i * i), tags=("even",))
            else:
                treeview.insert('', 'end', values=(f"Cat {i}", i, f"Spyrogyra {i}", i * i), tags=("odd"))
            i += 1
        performanceChart(self.rightContentPane)
        # plotCharts(self.rightContentPane)
        # self.box_total_sales = Frame(self.leftContentPane, relief="ridge", border=4, background="#9EC862")
        # self.box_total_sales.place(relx=0.0, rely=0.63, relwidth=0.9, relheight=0.3)
