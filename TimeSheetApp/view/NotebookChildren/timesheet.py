from tkinter import Frame, Label, Entry


class TimeSheet:
    def __init__(self, master):
        self.master = master
        self.mainFrame = Frame(self.master, background="#DCDAD5")
        self.mainFrame.pack(side="left", fill="both", padx=4, pady=4, expand=True)
        self.welcomeLbl = Label(self.mainFrame, text="Timesheet", background="#DCDAD5", foreground="#2b2b2b",
                                font=("Verdana", 14))
        self.welcomeLbl.pack(side="top", anchor="nw", padx=5, pady=5)

        self.contentPane = Frame(self.mainFrame, background="#DCDAD5")
        self.contentPane.pack(side="bottom", fill="both", anchor="center", expand=True)

        self.contentPane.master.update()
        width = self.contentPane.master.winfo_reqwidth()
        print(self.master['width'])
        rows = 25
        columns = 12
        relx = 0
        rely = 0
        relwidth = 1 / columns
        relheight = 1 / rows

        for row in range(1, rows + 1):
            for column in range(1, columns + 1):

                if (column * 2) /row == 2 or (row * 2) / column == 2:
                    bg = "green"
                if row == column:
                    bg = "#A23D29"
                else:
                    bg = "#282F47"
                e = Entry(self.contentPane, bg=bg, font=("Georgia", 12), justify='center')
                e.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
                relx += relwidth
                e.insert("0", ((row + 1) * (column + 1)))
            rely += relheight
            relx = 0

    def getWindowWidth(self):
        self.master.update_idletasks()
        return self.master.winfo_reqwidth()
