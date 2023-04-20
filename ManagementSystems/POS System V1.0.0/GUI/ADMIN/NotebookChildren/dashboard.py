from tkinter import Frame, Label


# frame = PhotoImage(data=running_dog, format='gif -index %i' % (frame_cnt))

class Dashboard:
    def __init__(self, master):
        self.master = master
        self.mainFrame = Frame(self.master, background="#DCDAD5")
        self.mainFrame.pack(side="left", fill="both", padx=4, pady=4, expand=True)
        self.welcomeLbl = Label(self.mainFrame, text="Dashboard Admin", background="#DCDAD5", foreground="#2b2b2b",
                                font=("Verdana", 14))
        self.welcomeLbl.pack(side="top", anchor="nw", padx=5, pady=5)

        self.contentPane = Frame(self.mainFrame, background="#DCDAD5")
        self.contentPane.pack(side="bottom", fill="both", anchor="center", expand=True)

        self.leftContentPane = Frame(self.contentPane, background="#DCDAD5")
        self.leftContentPane.place(relx=0, rely=0, relheight=1, relwidth=0.4)

        self.rightContentPane = Frame(self.contentPane, background="beige")
        self.rightContentPane.place(relx=0.4, rely=0, relheight=1, relwidth=0.6)

        self.box_total_sales = Frame(self.leftContentPane, relief="ridge", border=4, background="teal")
        self.box_total_sales.place(relx=0.0, rely=0.01, relwidth=0.9, relheight=0.3)

        self.box_total_sales = Frame(self.leftContentPane, relief="ridge", border=4, background="#5C723D")
        self.box_total_sales.place(relx=0.0, rely=0.32, relwidth=0.9, relheight=0.3)

        self.box_total_sales = Frame(self.leftContentPane, relief="ridge", border=4, background="#9EC862")
        self.box_total_sales.place(relx=0.0, rely=0.63, relwidth=0.9, relheight=0.3)
