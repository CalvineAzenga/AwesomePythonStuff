from tkinter import Button, Tk, Canvas, Label
from tkinter import ttk
from win32api import GetSystemMetrics
from PIL import Image, ImageTk
from datetime import datetime
import random


window = Tk()
style = ttk.Style(window)
style.theme_use("clam")
print(style.theme_names())
window.title("Cally POS V1.0.0")
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

appBar = Canvas(mainCanvas, bg="#5C723D", highlightthickness=0, bd=0, borderwidth=0)
appBar.place(rely=0, relx=0, relwidth=1, relheight=0.1)

titleLbl = Label(appBar, bg="#5C723D", text="Cally POS V1.0.0", fg="beige", font=("Verdana", 12), anchor="w")
titleLbl.pack(side="left")

btnClose = Label(appBar, text=" X ", cursor="hand2", relief="flat", font=("Verdana", 18), background="#5C723D")
btnClose.pack(side="right", fill="y")

timeDateLbl = Label(appBar, text=str(datetime.now()).split(".")[0], bg="#5C723D", fg="silver", font=("Verdana", 12))
timeDateLbl.place(relx=0.8, rely=0.7)


def updateTimeDate():
    timeDateLbl.configure(text=str(datetime.now()).split(".")[0])
    timeDateLbl.after(100, updateTimeDate)


updateTimeDate()

btnClose.bind("<Enter>", lambda event: btnClose.configure(fg="#2D0007"))
btnClose.bind("<Leave>", lambda event: btnClose.configure(fg="#FFFFFF"))
btnClose.bind("<ButtonPress>", lambda event: window.destroy())

sidebar = Canvas(mainCanvas, background="#A1B955", highlightthickness=0, bd=0, borderwidth=0)
sidebar.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.9)

operationPane = Canvas(mainCanvas, background="lavender", highlightthickness=0, bd=0, borderwidth=0)
operationPane.place(relx=0, rely=0.1, relwidth=0.7, relheight=0.9)

topPane = Canvas(operationPane, background="#dddddd", highlightthickness=0, bd=0, borderwidth=0)
topPane.place(relx=0, rely=0, relwidth=1, relheight=0.8)

topPaneHeader = Canvas(topPane, background="lavender", highlightthickness=0, bd=0, borderwidth=0)
topPaneHeader.place(relx=0, rely=0, relwidth=1, relheight=0.15)

barcodeLbl1 = Label(topPaneHeader, text="Enter Barcode Here", font=("Georgia", 14), fg="gray", bg="lavender")
barcodeLbl1.pack(side="left", anchor="nw", pady=10, padx=10)

barcodeImg = Image.open("./barcode.png")
barcodeImg = barcodeImg.resize((80, 25), Image.Resampling.LANCZOS)
barcodeImg = ImageTk.PhotoImage(barcodeImg, master=window)

barcodePicBox = Label(topPaneHeader, padx=10, text=" ", compound="right", image=barcodeImg, fg="gray", bg="lavender")
barcodePicBox.place(relx=0, rely=0.5)

barcodeTxt = ttk.Entry(topPaneHeader, font=("Verdana", 15), justify="center", width=30)
barcodeTxt.pack(side="bottom", anchor="sw", pady=10)

tableContainer = Canvas(topPane, bg="beige", relief="ridge", bd=5, highlightthickness=0)
tableContainer.place(relx=0.005, rely=0.16, relwidth=0.905, relheight=0.8)

tableHeader = Canvas(tableContainer, background="beige", relief="ridge", height=35, highlightthickness=0, bd=3)
tableHeader.pack(side="top", anchor="nw", fill="x", pady=5, padx=5, expand=0)

tableContentsContainer1 = Canvas(tableContainer, background="beige", relief="flat", highlightthickness=0, bd=3)
tableContentsContainer1.pack(side="top", fill="both", pady=5, padx=7, expand=1)

window.update()
height_h = int(tableContentsContainer1.winfo_height())

scrollable_frame = Canvas(tableContentsContainer1, bg="beige", highlightthickness=0, borderwidth=0)
scrollable_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
width_w = int(tableContentsContainer1.winfo_width())

tableContentsContainer = Canvas(scrollable_frame, background="beige", relief="flat", highlightthickness=0, bd=3)
# tableContentsContainer.pack(side="left",fill="both",pady=8,padx=0,expand=1)


HLbl1 = Label(tableHeader, text="PID", font=("Verdana", 11), fg="gray", background="beige", bd=3, relief="ridge")
HLbl1.place(relx=0, rely=0, relheight=1, relwidth=0.1)

HLbl2 = Label(tableHeader, text="Product Name", font=("Verdana", 11), fg="gray", background="beige", bd=3,
              relief="ridge")
HLbl2.place(relx=0.1, rely=0, relheight=1, relwidth=0.5)

HLbl3 = Label(tableHeader, text="Qty", font=("Verdana", 11), fg="gray", background="beige", bd=3, relief="ridge")
HLbl3.place(relx=0.6, rely=0, relheight=1, relwidth=0.1)

HLbl4 = Label(tableHeader, text="Action", font=("Verdana", 11), fg="gray", background="beige", bd=3, relief="ridge")
HLbl4.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)


class tableRow():
    def __init__(self, master, index, name=None, qty=1):
        hey = Canvas(master, bd=0, bg="silver", height=15, width=width_w)
        hey.pack(side="top", anchor="nw", fill="x", pady=1, padx=0, expand=0, ipady=5)

        def delete():
            window.update_idletasks()
            scrollable_frame.configure(yscrollcommand=scrollbar.set, scrollregion=scrollable_frame.bbox('all'))
            hey.destroy()

        col1 = Label(master=hey, text=index, background="gray", foreground="beige", padx=10, font=("Raleway", 11))
        col1.place(relx=0, relwidth=0.1, relheight=1)

        col2 = Label(master=hey, text=name, background="silver", foreground="black",
                     font=("Raleway", 11))
        col2.place(relx=0.1, relwidth=0.5, relheight=1)

        col3 = Label(master=hey, text=qty, background="#214665", foreground="orange", cursor="hand2",
                     font=("Raleway", 11))
        col3.place(relx=0.6, relwidth=0.1, relheight=1)

        col4 = Canvas(master=hey, background="#A9C259", highlightthickness=0, borderwidth=0)
        col4.place(relx=0.7, relwidth=0.3, relheight=1)

        btnEdit = Button(col4, text="Edit", bg="green", cursor="hand2", fg="beige", font=("Raleway", 10))
        btnEdit.pack(side="left", padx=10)

        btnDelete = Button(col4, text="Remove", bg="orangered", cursor="hand2", fg="#2b2b2b", font=("Raleway", 10),
                           command=delete)
        btnDelete.pack(side="left", padx=10)


scrollbar = ttk.Scrollbar(topPane, orient='vertical')
scrollbar.configure(command=scrollable_frame.yview)
scrollbar.place(relx=0.91, rely=0.16, relheight=0.8)

# for x in range(40):
#     tableRow(tableContentsContainer, index=x)
#     window.update_idletasks()
scrollable_frame.create_window(0, 0, anchor="nw", window=tableContentsContainer)
scrollable_frame.configure(yscrollcommand=scrollbar.set, scrollregion=scrollable_frame.bbox('all'))

bottomPane = Canvas(operationPane, background="#6B8F45", highlightthickness=0, bd=0, borderwidth=0)
bottomPane.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

bottomPaneUpper = Canvas(bottomPane, background="#81B955", highlightthickness=0, bd=0, borderwidth=0)
bottomPaneUpper.place(relx=0, rely=0, relwidth=1, relheight=0.45)

bottomPaneLower = Canvas(bottomPane, background="#6B8F45", highlightthickness=0, bd=0, borderwidth=0)
bottomPaneLower.place(relx=0, rely=0.45, relwidth=1, relheight=0.55)

index = 0

products = ['Mumias Sugar 1kg', 'Blue Band', 'A4 Book 200P', 'Tissue A', 'Tissue B', 'A1 32GB', 'Kiwi Black 40g',
            'Broadways Sandwich 400g']


def add_row():
    global index
    index += 1
    tableRow(tableContentsContainer, index=index, name=products[random.randint(0, len(products) - 1)])
    window.update_idletasks()
    scrollable_frame.configure(yscrollcommand=scrollbar.set, scrollregion=scrollable_frame.bbox('all'))


btnAdd = Button(bottomPaneLower, text="Add", command=add_row)
btnAdd.pack()

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

window.mainloop()
