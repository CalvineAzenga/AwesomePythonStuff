from tkinter import Button, Tk, Canvas, Label, PhotoImage, Frame, font
from tkinter import ttk
from win32api import GetSystemMetrics
from PIL import Image, ImageTk
from datetime import datetime

# importing tab Panes
from view.NotebookChildren.dashboard import Dashboard
from view.NotebookChildren.timesheet import TimeSheet

window = Tk()
style = ttk.Style(window)
style.theme_use("clam")
# print(style.theme_names())
window.title("CallyTimeSheet V1.0.0")
window.wm_attributes("-topmost", 1)
window.overrideredirect(1)
width = int(GetSystemMetrics(0))
height = GetSystemMetrics(1)

# width=1200
# height=720
pos_x = int((GetSystemMetrics(0) - width) / 2)
pos_y = int((GetSystemMetrics(1) - height) / 2)
window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.tk_setPalette("gray17")
window.resizable(0, 0)

mainCanvas = Canvas(window, bg="#9EC862", bd=0, borderwidth=0, highlightthickness=0)
mainCanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
canvasWidth = width
canvasHeight = height
backgroundImg = Image.open("./cally.png")
backgroundImg = backgroundImg.resize((canvasWidth, canvasHeight), Image.Resampling.LANCZOS)
backgroundImg = ImageTk.PhotoImage(backgroundImg, master=window)
mainCanvas.create_image(0, 0, image=backgroundImg, anchor="nw")

appBar = Canvas(mainCanvas, bg="#004C4C", highlightthickness=0, bd=0, borderwidth=0)
appBar.place(rely=0, relx=0, relwidth=1, relheight=0.1)

titleLbl = Label(appBar, bg="#004C4C", text="Cali~TS", fg="beige", font=("Verdana", 12), anchor="w")
titleLbl.pack(side="top", anchor="w", padx=10, ipady=12)

titleLbl = Label(appBar, bg="#004C4C", text="Management by Admin [Cally]", fg="cyan", font=("Verdana", 10),
                 anchor="w")
titleLbl.pack(side="bottom", anchor="w", padx=10, ipady=12)

btnClose = Label(appBar, text=" X ", cursor="hand2", relief="flat", font=("Verdana", 18), background="#004C4C")
btnClose.place(relheight=1, x=width - 50)

timeDateLbl = Label(appBar, text=str(datetime.now()).split(".")[0], bg="#004C4C",
                    fg="silver", font=("Verdana", 12))
timeDateLbl.place(relx=0.8, rely=0.6)

menuBarContainer = Canvas(mainCanvas, bg="#005C4C", highlightthickness=0, bd=0, borderwidth=0)
menuBarHeight = 25
menuBarContainer.place(rely=0.1, relx=0, relwidth=1, height=menuBarHeight)

mainContentCanvas = Canvas(mainCanvas, bg="#9EC862", bd=0, borderwidth=0, highlightthickness=0)
mainContentCanvas.place(relx=0, rely=0.1 + (menuBarHeight / height), relwidth=1,
                        relheight=1 - (0.1 + (menuBarHeight / height)))

mainNotebook = ttk.Notebook(master=mainContentCanvas)

style.configure("TNotebook.Tab", font=("Verdana", 9), foreground="#1F1F3A", justify="left")
style.configure(mainNotebook.winfo_class())
# style.configure(mainNotebook.winfo_class(), background="#1F1F3A")

# style.map(TREEVIEWCLASS, background=[('selected', 'darkgreen')], font=[('selected', ('Verdana', 13))],
#           foreground=[('selected', 'orange')])

# Creating various tabs
dashboardNtk = ttk.Notebook(mainNotebook)
timeSheetNtk = ttk.Notebook(mainNotebook)
taxNtk = ttk.Notebook(mainNotebook)
settingsNtk = ttk.Notebook(mainNotebook)
accountsNtk = ttk.Notebook(mainNotebook)
printersNtk = ttk.Notebook(mainNotebook)
reportsNtk = ttk.Notebook(mainNotebook)
workersNtk = ttk.Notebook(mainNotebook)

# Adding Panes to the
Dashboard(dashboardNtk)
TimeSheet(timeSheetNtk)

mainNotebook.add(dashboardNtk, text="Dashboard")
mainNotebook.add(timeSheetNtk, text="Time Sheet")
mainNotebook.add(taxNtk, text="View Data")
mainNotebook.add(workersNtk, text="Employees")
mainNotebook.add(reportsNtk, text="Reports")
mainNotebook.add(printersNtk, text="Printers")
mainNotebook.add(accountsNtk, text="Accounts")
mainNotebook.add(settingsNtk, text="Settings")

mainNotebook.pack(side="right", anchor="center", fill="both", expand=True)


def updateTimeDate():
    timeDateLbl.configure(text=str(datetime.now()).split(".")[0])
    timeDateLbl.after(100, updateTimeDate)


updateTimeDate()

btnClose.bind("<Enter>", lambda event: btnClose.configure(fg="#2D0007"))
btnClose.bind("<Leave>", lambda event: btnClose.configure(fg="#FFFFFF"))
btnClose.bind("<ButtonPress>", lambda event: window.destroy())

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


    appBar.bind('<Button-1>', save_last_pos)
    appBar.bind('<B1-Motion>', dragging)
except:
    pass
# print(font.families(window))
style.configure("TNotebook.Tab", font=("Lato", 10), foreground="#490537")


def start():
    window.mainloop()
