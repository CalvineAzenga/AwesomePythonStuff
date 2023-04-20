from tkinter import Button, Tk, Canvas, Label, PhotoImage, Frame, simpledialog, LabelFrame, Toplevel, Entry, IntVar, Wm
from tkinter import ttk
from win32api import GetSystemMetrics
from PIL import Image, ImageTk
from datetime import datetime
import random
import SimpleDialogCally
import tabulate
from PrintingServices.TEXTPrinter import POSPrinter
import os

window = Tk()
printer = POSPrinter()
style = ttk.Style(window)
style.theme_use("clam")
print(style.theme_names())

width = int(GetSystemMetrics(0))
height = int(GetSystemMetrics(1))

pos_x = int((GetSystemMetrics(0) - width) / 2)
pos_y = int((GetSystemMetrics(1) - height) / 2)
window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.tk_setPalette("#282923")
window.wm_state("zoomed")

deleteImg = Image.open("../../Assets/icons/delete1.png")
deleteImg = deleteImg.resize((16, 16), Image.Resampling.LANCZOS)
deleteImg = ImageTk.PhotoImage(deleteImg, master=window)

editImg = Image.open("../../Assets/icons/edit.png")
editImg = editImg.resize((16, 16), Image.Resampling.LANCZOS)
editImg = ImageTk.PhotoImage(editImg, master=window)

mainCanvas = Canvas(window, bg="#9EC862", bd=0, borderwidth=0, highlightthickness=0)
mainCanvas.place(relx=0, rely=0, relwidth=1, relheight=1)
canvasWidth = width
canvasHeight = height
backgroundImg = Image.open("../../cally.png")
backgroundImg = backgroundImg.resize((canvasWidth, canvasHeight), Image.Resampling.LANCZOS)
backgroundImg = ImageTk.PhotoImage(backgroundImg, master=window)
mainCanvas.create_image(0, 0, image=backgroundImg, anchor="nw")

appBar = Canvas(mainCanvas, bg="#004C4C", highlightthickness=0, bd=0, borderwidth=0)
appBar.place(rely=0, relx=0, relwidth=1, relheight=0.1)

titleLbl = Label(appBar, bg="#004C4C", text="Cally POS V1.0.0", fg="beige", font=("Verdana", 12), anchor="w")
titleLbl.pack(side="left")

operationPane = Canvas(mainCanvas, background="lavender", highlightthickness=0, bd=0, borderwidth=0)
operationPane.place(relx=0, rely=0.1, relwidth=0.7, relheight=0.9)

sidebar = Canvas(mainCanvas, background="#006666", highlightthickness=0, bd=0, borderwidth=0)
sidebar.place(relx=0.7, rely=0.1, relwidth=0.3, relheight=0.9)

topSideBarCanvas = Canvas(sidebar, background="#006666", highlightthickness=0, bd=0, borderwidth=0)
topSideBarCanvas.place(relx=0, rely=0, relwidth=1, relheight=0.3)

paymentsLabelFrame = LabelFrame(topSideBarCanvas, text="Payment Options", background="#006666", font=("Verdana", 12),
                                relief="ridge")
paymentsLabelFrame.pack(side="left", fill="both", expand=True, padx=2, pady=2)

btnCash = Button(paymentsLabelFrame, text="Cash", background="#004C4C", relief="ridge", foreground="cyan", border=3,
                 font=("Verdana", 12))
btnCash.place(relx=0.1 / 4, rely=0.1 / 3, relwidth=0.3, relheight=0.45)

btnVoucher = Button(paymentsLabelFrame, text="Voucher", background="#004C4C", relief="ridge", foreground="orange",
                    border=3, font=("Verdana", 12))
btnVoucher.place(relx=(0.1 / 4) * 2 + 0.3, rely=0.1 / 3, relwidth=0.3, relheight=0.45)

btnVisa = Button(paymentsLabelFrame, text="Visa", background="#004C4C", relief="ridge", foreground="skyblue", border=3,
                 font=("Verdana", 12))
btnVisa.place(relx=(0.1 / 4) * 3 + 0.6, rely=0.1 / 3, relwidth=0.3, relheight=0.45)

btnMpesa = Button(paymentsLabelFrame, text="M-PESA", background="#004C4C", relief="ridge", foreground="lime", border=3,
                  font=("Verdana", 12))
btnMpesa.place(relx=0.1 / 4, rely=(0.1 / 3) * 2 + 0.45, relwidth=0.3, relheight=0.45)

btnbank = Button(paymentsLabelFrame, text="Bank", background="#004C4C", relief="ridge", foreground="beige", border=3,
                 font=("Verdana", 12))
btnbank.place(relx=(0.1 / 4) * 2 + 0.3, rely=(0.1 / 3) * 2 + 0.45, relwidth=0.3, relheight=0.45)

# btnVisa1 = Button(paymentsLabelFrame, text="Visa", background="#004C4C", relief="ridge", foreground="beige",
# border=3,font=("Verdana",12)) btnVisa1.place(relx=(0.1 / 4)*3+0.6, rely=(0.1 / 3)*2+0.45, relwidth=0.3,
# relheight=0.45)


bottomSideBarCanvas = Canvas(sidebar, background="#006666", highlightthickness=0, bd=0, borderwidth=0)
bottomSideBarCanvas.place(relx=0, rely=0.3, relwidth=1, relheight=0.7)

subtotalLbl = Label(bottomSideBarCanvas, background="#006666", text="Sub Total", font=("Cambria", 15),
                    foreground="#dddddd")
subtotalLbl.grid(row=0, column=0, padx=(25, 0), pady=(30, 0), sticky="e")

subtotalLblValue = Label(bottomSideBarCanvas, background="#006666", text="5,000", font=("Cambria", 15),
                         foreground="orange")
subtotalLblValue.grid(row=0, column=1, padx=20, pady=(30, 0), sticky="w")

VATLbl = Label(bottomSideBarCanvas, background="#006666", text="V.A.T", font=("Cambria", 15),
               foreground="#dddddd")
VATLbl.grid(row=1, column=0, padx=(25, 0), pady=(10, 0), sticky="e")

VATLblValue = Label(bottomSideBarCanvas, background="#006666", text="5,000", font=("Cambria", 15),
                    foreground="orange")
VATLblValue.grid(row=1, column=1, padx=20, pady=(10, 0), sticky="w")

discountLbl = Label(bottomSideBarCanvas, background="#006666", text="Discount", font=("Cambria", 15),
                    foreground="#dddddd")
discountLbl.grid(row=2, column=0, padx=(25, 0), pady=(10, 0), sticky="e")

discountLblValue = Label(bottomSideBarCanvas, background="#006666", text="0.00", font=("Cambria", 15),
                         foreground="yellow")
discountLblValue.grid(row=2, column=1, padx=20, pady=(10, 0), sticky="w")

totalLbl = Label(bottomSideBarCanvas, background="#006666", text="Total", font=("Cambria", 25, "bold"),
                 foreground="#dddddd")
totalLbl.grid(row=4, column=0, padx=(25, 0), pady=(20, 0), sticky="e")

totalLblValue = Label(bottomSideBarCanvas, background="#006666", text="500,000.00 (Ksh.)", font=("Cambria", 25),
                      foreground="maroon")
totalLblValue.grid(row=4, column=1, padx=20, pady=(20, 0), sticky="w")

balanceLbl = Label(bottomSideBarCanvas, background="#006666", text="Balance", font=("Cambria", 18, "bold"),
                   foreground="#dddddd")
balanceLbl.grid(row=6, column=0, padx=(25, 0), pady=(30, 0), sticky="e")

balanceLblValue = Label(bottomSideBarCanvas, background="#202634", text="5,000.00 (Ksh.)", font=("Cambria", 18),
                        foreground="lime")
balanceLblValue.grid(row=6, column=1, padx=20, pady=(30, 0), sticky="w")

receiptBtn = Button(bottomSideBarCanvas, text="Print Receipt", font=("Verdana", 15))
receiptBtn.grid(row=7, column=1, padx=20, pady=(50, 0), sticky="w")

topPane = Canvas(operationPane, background="#dddddd", highlightthickness=0, bd=0, borderwidth=0)
topPane.place(relx=0, rely=0, relwidth=1, relheight=0.8)

topPaneHeader = Canvas(topPane, background="lavender", highlightthickness=0, bd=0, borderwidth=0)
topPaneHeader.place(relx=0, rely=0, relwidth=1, relheight=0.15)

barcodeLbl1 = Label(topPaneHeader, text="Enter Barcode Here", font=("Georgia", 14), fg="gray", bg="lavender")
barcodeLbl1.pack(side="left", anchor="nw", pady=10, padx=10)

barcodeImg = Image.open("../../barcode.png")
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


HLbl1 = Label(tableHeader, text="Barcode", font=("Verdana", 11), fg="gray", background="beige", bd=3, relief="ridge")
HLbl1.place(relx=0, rely=0, relheight=1, relwidth=0.1)

HLbl2 = Label(tableHeader, text="Product Name", font=("Verdana", 11), fg="gray", background="beige", bd=3,
              relief="ridge")
HLbl2.place(relx=0.1, rely=0, relheight=1, relwidth=0.5)

HLbl3 = Label(tableHeader, text="Qty", font=("Verdana", 11), fg="gray", background="beige", bd=3, relief="ridge")
HLbl3.place(relx=0.6, rely=0, relheight=1, relwidth=0.1)

HLbl4 = Label(tableHeader, text="Action", font=("Verdana", 11), fg="gray", background="beige", bd=3, relief="ridge")
HLbl4.place(relx=0.7, rely=0, relheight=1, relwidth=0.3)


def printReceipt(event):
    printer.print2(tkTable.generateReceipt())


receiptBtn.bind("<ButtonPress>", printReceipt)


class tkTableCally:
    def __init__(self):
        self.rows = []
        self.productsList = [{"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '5', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '5', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '1645', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '5', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '5', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '5', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '5', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '1', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'},
                             {"id": '4', "name": 'Sugar 1kg', "qty": '3', "unitPrice": '165', "tax": 'A'}
                             ]

    def generateReceipt(self) -> str:
        receipt = ""
        receipt_top = tabulate.tabulate([["Cally Mart 67\nP.O BOX 46546 Nairobi\nPin A0J2E3I299G\nInvoice Number "
                                          "000000123" + "\n"]], tablefmt="plain")
        total_price = 0
        receipt_middle = []
        receipt_tax_part = ''
        VAT = 456.90
        for row in self.productsList:
            name = str(row['name'])
            qty = int(row['qty'])
            unit_price = float(row['unitPrice'])
            tax_type = str(row['tax'])
            total_row_price = unit_price * qty
            total_price += total_row_price
            receipt_middle.append([name + " @" + str(unit_price) + tax_type, str(qty), str(total_row_price)])

        receipt_middle = tabulate.tabulate(headers=("Title", "Qty", "Price"), tabular_data=receipt_middle,
                                           tablefmt="simple")

        receipt_totals_part = tabulate.tabulate([[f"Subtotal {total_price}\n"], [f"V.A.T {VAT}\n"],
                                                 [f"CashIn {45000.91}\n"],
                                                 [f"Balance {4556.78}\n"]], tablefmt="plain", stralign="right")

        receipt_tax_part += "\n*********************\n"
        receipt_tax_part_middle = tabulate.tabulate(headers=("Tax", "Value(%)"),
                                                    tabular_data=[['A', '16'], ['B', '8'], ['C', '0'], ['D', '0']],
                                                    tablefmt="simple")
        receipt_tax_part += receipt_tax_part_middle

        receipt_tax_part = tabulate.tabulate([[receipt_tax_part]], tablefmt="plain")

        receipt_bottom = tabulate.tabulate([[
            f"You were served by Cate Millan.\n{str(datetime.now()).split('.')[0]}.\nDeveloped by Calvoo Systems "
            f"+254700666848"]],
            tablefmt="plain")
        receipt += receipt_top + "\n"
        receipt += receipt_middle + "\n"
        receipt += receipt_totals_part + "\n"
        receipt += receipt_tax_part + "\n"
        receipt += "\n" + receipt_bottom + "\n"

        receipt = tabulate.tabulate([[receipt]], tablefmt="plain", stralign="center")

        return receipt

    def clearRows(self):
        self.rows.clear()

    def deleteRow(self, id_):
        self.rows.remove(id_)

    def RowExists(self, id_) -> bool:
        for row in self.rows:
            if row.id == id_:
                return True
            else:
                return False

    class tableRow:
        def __init__(self, master, index_, name=None, qty=0):
            self.hey = Frame(master, bd=0, bg="silver", width=width_w)
            self.hey.pack(side="top", anchor="nw", fill="x", pady=1, padx=0, expand=1, ipady=15)
            self.id = index_
            self.name = name

            self.qty = qty
            self.int_var_quantity = IntVar(master=master)

            self.autoAddQty()

            self.col1 = Label(master=self.hey, text=self.id, background="gray", foreground="#202634", padx=10,
                              font=("Verdana", 9))
            self.col1.place(relx=0, relwidth=0.1, relheight=1)

            self.col2 = Label(master=self.hey, text=self.name, background="silver", foreground="black",
                              font=("Raleway", 11))
            self.col2.place(relx=0.1, relwidth=0.5, relheight=1)

            self.col3 = Label(master=self.hey, text=self.qty, textvariable=self.int_var_quantity, background="#214665",
                              foreground="orange", cursor="hand2",
                              font=("Raleway", 11))
            self.col3.place(relx=0.6, relwidth=0.1, relheight=1)

            self.col4 = Canvas(master=self.hey, background="#66B2B2", highlightthickness=0, borderwidth=0)
            self.col4.place(relx=0.7, relwidth=0.3, relheight=1)

            self.btnEdit = ttk.Button(self.col4, text="", image=editImg, compound='center', cursor="hand2",
                                      command=self.edit)
            self.btnEdit.pack(side="left", ipadx=5, padx=5)

            self.btnDelete = ttk.Button(self.col4, text="", image=deleteImg, compound='center', cursor="hand2",
                                        command=self.deleteRow)
            self.btnDelete.pack(side="left")

        def deleteRow(self):
            self.hey.destroy()
            window.update_idletasks()
            scrollable_frame.configure(yscrollcommand=scrollbar.set, scrollregion=scrollable_frame.bbox('all'))
            window.update()

        def edit(self):
            try:
                # This code snippet somehow solves the problem of widgets disappearing ->
                # suddenly when many rows are in the custom table.
                # This code then scrolls back to where the user had scrolled to
                init_scroll_bar_fraction = scrollbar.get()[0]  # get the initial scrolled fraction
                scrollable_frame.yview_moveto(0)
                scrollable_frame.after(0, lambda: scrollable_frame.yview_moveto(init_scroll_bar_fraction))
            except:
                pass
            d = QuantityDialogue(window, qty=self.qty)
            self.qty = int(d.result)
            self.int_var_quantity.set(self.qty)

        def autoAddQty(self):
            self.qty += 1
            self.int_var_quantity.set(self.qty)

        def getId(self):
            return self.id

        def setQuantity(self, qty):
            self.qty = qty
            self.col3.configure(text=self.qty)

    def add_row(self):
        global index
        index += 1
        row = self.tableRow(tableContentsContainer, index_=index, name=products[random.randint(0, len(products) - 1)])
        self.rows.append(row)
        window.update_idletasks()
        scrollable_frame.configure(yscrollcommand=scrollbar.set, scrollregion=scrollable_frame.bbox('all'))
        scrollable_frame.yview_moveto(1)
        print(tabulate.tabulate_formats)
        # print(self.generateReceipt())


scrollbar = ttk.Scrollbar(topPane, orient='vertical')
scrollbar.configure(command=scrollable_frame.yview)
scrollbar.place(relx=0.91, rely=0.16, relheight=0.8)

scrollable_frame.create_window(0, 0, anchor="nw", window=tableContentsContainer)
scrollable_frame.configure(yscrollcommand=scrollbar.set, scrollregion=scrollable_frame.bbox('all'))

bottomPane = Canvas(operationPane, background="#008080", highlightthickness=0, bd=0, borderwidth=0)
bottomPane.place(relx=0, rely=0.8, relwidth=1, relheight=0.2)

bottomPaneUpper = Canvas(bottomPane, background="#004C4C", highlightthickness=0, bd=0, borderwidth=0)
bottomPaneUpper.place(relx=0, rely=0, relwidth=1, relheight=0.3)

bottomPaneLower = Canvas(bottomPane, background="#008080", highlightthickness=0, bd=0, borderwidth=0)
bottomPaneLower.place(relx=0, rely=0.45, relwidth=1, relheight=0.7)

index = 7896514412

products = ['Mumias Sugar 1kg', 'Blue Band', 'A4 Book 200P', 'Tissue A', 'Tissue B', 'A1 32GB', 'Kiwi Black 40g',
            'Broadways Sandwich 400g']

# for x in range(10):
#     add_row()
tkTable = tkTableCally()

btnAdd = Button(bottomPaneLower, text="Add", command=tkTable.add_row)
btnAdd.pack()


def is_full_screen() -> bool:
    value = window.wm_attributes("-fullscreen")
    if value == 0:
        return False
    else:
        return True


def toggle_full_screen():
    if is_full_screen():
        window.wm_attributes("-fullscreen", 0)

    else:
        window.wm_attributes("-fullscreen", 1)


btnFullScreen = Button(bottomPaneLower, text="ToggleFullScreen", command=toggle_full_screen)
btnFullScreen.pack()
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

# Make scrollable_frame respond to mousewheel

try:
    def _bound_to_mousewheel(event):
        scrollable_frame.bind_all("<MouseWheel>", _on_mousewheel)
        scrollable_frame.bind_all("<Up>", _on_up)
        scrollable_frame.bind_all("<Down>", _on_down)


    def _unbound_to_mousewheel(event):
        scrollable_frame.unbind_all("<MouseWheel>")
        scrollable_frame.unbind_all("<Up>")
        scrollable_frame.unbind_all("<Down>")


    def _on_mousewheel(event):
        scrollable_frame.yview_scroll(int(-1 * (event.delta / 120)), "units")


    def _on_up(event):
        scrollable_frame.yview_scroll(int(-1), "units")


    def _on_down(event):
        scrollable_frame.yview_scroll(int(1), "units")


    tableContentsContainer1.bind("<Enter>", _bound_to_mousewheel)
    tableContentsContainer1.bind("<Leave>", _unbound_to_mousewheel)
except:
    pass


class QuantityDialogue(SimpleDialogCally.Dialog):

    def body(self, master):

        self.overrideredirect(1)
        # self.wm_attributes("-toolwindow", 1)
        self.configure(background="#006666", border=5, relief="ridge", padx=5, pady=5)
        self.tk_setPalette("#004C4C")

        self.lblTitle = Label(master, text="Enter Quantity", font=("Verdana", 12), foreground="cyan", relief="ridge",
                              border=1)
        self.lblTitle.grid(row=0, column=0, columnspan=3, ipady=10, ipadx=20, padx=0, sticky="nwse")

        self.btn1 = Button(master, text=1, font=("Verdana", 12), relief="ridge", border=1)
        self.btn1.grid(row=1, column=0, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn2 = Button(master, text=2, font=("Verdana", 12), relief="ridge", border=1)
        self.btn2.grid(row=1, column=1, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn3 = Button(master, text=3, font=("Verdana", 12), relief="ridge", border=1)
        self.btn3.grid(row=1, column=2, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn4 = Button(master, text=4, font=("Verdana", 12), relief="ridge", border=1)
        self.btn4.grid(row=2, column=0, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn5 = Button(master, text=5, font=("Verdana", 12), relief="ridge", border=1)
        self.btn5.grid(row=2, column=1, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn6 = Button(master, text=6, font=("Verdana", 12), relief="ridge", border=1)
        self.btn6.grid(row=2, column=2, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn7 = Button(master, text=7, font=("Verdana", 12), relief="ridge", border=1)
        self.btn7.grid(row=3, column=0, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn8 = Button(master, text=8, font=("Verdana", 12), relief="ridge", border=1)
        self.btn8.grid(row=3, column=1, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn9 = Button(master, text=9, font=("Verdana", 12), relief="ridge", border=1)
        self.btn9.grid(row=3, column=2, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btn0 = Button(master, text=0, font=("Verdana", 12), relief="ridge", border=1)
        self.btn0.grid(row=4, column=1, ipady=10, ipadx=20, padx=0, sticky="nwse")

        self.btnClear = Button(master, text="C", font=("Verdana", 12, "bold"), foreground="orangered", relief="ridge",
                               border=1)
        self.btnClear.grid(row=4, column=2, ipady=10, ipadx=20, padx=0, sticky="nwse")
        self.btnClear.bind("<ButtonPress>", self.clearEntry)

        self.e1 = Entry(master, background="#004C4C", font=("Verdana", 12), justify="center", state="normal")
        self.e1.bind("<Key>", self.validateEntry)

        self.e1.insert("0", self.qty)

        self.e1.grid(row=5, column=0, columnspan=3, ipady=10, ipadx=10, padx=0, pady=(10, 0))

        self.btn0.bind("<ButtonPress>", self.btnAppendText)
        self.btn1.bind("<ButtonPress>", self.btnAppendText)
        self.btn2.bind("<ButtonPress>", self.btnAppendText)
        self.btn3.bind("<ButtonPress>", self.btnAppendText)
        self.btn4.bind("<ButtonPress>", self.btnAppendText)
        self.btn5.bind("<ButtonPress>", self.btnAppendText)
        self.btn6.bind("<ButtonPress>", self.btnAppendText)
        self.btn7.bind("<ButtonPress>", self.btnAppendText)
        self.btn8.bind("<ButtonPress>", self.btnAppendText)
        self.btn9.bind("<ButtonPress>", self.btnAppendText)
        return self.e1

    def btnAppendText(self, event):
        num = event.widget['text']
        self.e1.insert("insert", num)

    def clearEntry(self, event):
        self.e1.delete("0", "end")
        pass

    def validateEntry(self, event):
        acceptedKeys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'BackSpace', 'Delete', 'Left', 'Right',
                        'Return']
        if event.keysym in acceptedKeys:
            pass
        else:
            print(event.keysym)
            return "break"

    def buttonbox(self):
        box = Frame(self)

        w = Button(box, text="OK", width=10, command=self.ok, default="active")
        w.pack(side="left", padx=5, pady=5)

        self.bind("<Return>", self.ok)
        box.pack()
        self.wm_attributes("-topmost", 1)

    def apply(self):
        first = self.e1.get()
        if int(first) < 1:
            first = 1
        self.result = first


window.mainloop()
