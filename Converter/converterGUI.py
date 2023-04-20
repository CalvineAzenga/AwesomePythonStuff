import os
from tkinter import *
from tkinter import ttk
import sys
from win32api import GetSystemMetrics
from datetime import datetime
import ttkthemes
import winsound
# from ttkbootstrap import Style

# style1=Style(theme='yeti')

width=GetSystemMetrics(0)
height=GetSystemMetrics(1)

window_w=800
window_h=480
center_x=int((width-window_w)/2)
center_y=int((height-window_h)/2)

CURRENCY_LIST=['USD','CAN','KES','POUND','YEN','RUP','ZAZ','TSH']

window=ttkthemes.ThemedTk()
style=ttkthemes.ThemedStyle(window)
print(style.theme_names())
style.theme_use('clam')
window.attributes("-topmost",True)
window.overrideredirect(1)
window.tk_setPalette("#E6E4E5")
window.geometry(f"{window_w}x{window_h}+{center_x}+{center_y}")

app_bar=Label(window,background="#0179D8",text="Unit Converter V1.0.0",foreground="beige",padx=20,justify=LEFT,font=("Georgia",13),anchor=W)
app_bar.place(relx=0,rely=0,relwidth=1,relheight=0.08)

decoration_lbl=Label(app_bar,background="#0179D8")
decoration_lbl.place(relx=0.84,rely=0,relwidth=0.14,relheight=1)

minimize_lbl=Label(decoration_lbl,text="-",font=("Verdana",30,"bold"),foreground='beige',background="#0179D8")
minimize_lbl.pack(side=LEFT,expand=True,pady=13)

maxrestore_lbl=Label(decoration_lbl,text="1",font=("Webdings",15),foreground='beige',background="#0179D8")
maxrestore_lbl.pack(side=LEFT,expand=True)

close_lbl=Label(decoration_lbl,text="X",font=("Verdana",15),foreground='beige',background="#0179D8")
close_lbl.pack(side=LEFT,expand=True)

separator=ttk.Separator(window)
separator.place(relx=0,rely=0.08,relheight=0.004,relwidth=1)

header_lbl=Label(window,background="#245985",text="Welcome to Real Time Unit Converter",justify=CENTER,anchor=CENTER,foreground="beige",font=("Georgia",25))
header_lbl.place(relx=0,rely=0.084,relwidth=1,relheight=0.12)

content_pane=Label(window,background="#E6E4E5")
content_pane.place(relx=0,rely=0.204,relwidth=1,relheight=0.796)

results_pane=Label(content_pane,background="#E6E4E5")
results_pane.place(relx=0,rely=0,relwidth=1,relheight=0.25)

results_lbl=Label(results_pane,background="#E6E4E5",justify=CENTER,text="1 USD = 74.93 Indian Rupee",font=("Cambria",20),pady=10)
results_lbl.pack(side=TOP)

time_lbl=Label(results_pane,background="#E6E4E5",justify=CENTER,text=f"Date: {str(datetime.now()).split('.')[0]}",font=("Verdana",12))
time_lbl.pack(side=TOP)

controls_pane=Label(content_pane,background="#E6E4E5")
controls_pane.place(relx=0,rely=0.25,relwidth=1,relheight=0.75)

cmb_from=ttk.Combobox(controls_pane,font=("Cambria",20),state='readonly')
cmb_from.place(relx=0.15,rely=0.15,relwidth=0.25,relheight=0.18)
cmb_from['values']=CURRENCY_LIST

cmb_to=ttk.Combobox(controls_pane,font=("Cambria",20),state='readonly')
cmb_to.place(relx=0.6,rely=0.15,relwidth=0.25,relheight=0.18)
cmb_to['values']=CURRENCY_LIST

entry_from=ttk.Entry(controls_pane,font=("Cambria",20))
entry_from.place(relx=0.175,rely=0.45,relwidth=0.2,relheight=0.18)

entry_to=ttk.Entry(controls_pane,font=("Cambria",20))
entry_to.place(relx=0.625,rely=0.45,relwidth=0.2,relheight=0.18)

menu_variable=StringVar()
menu_units=ttk.OptionMenu(controls_pane,variable=menu_variable)
menu_units.place(relx=0.4,rely=0.6,relwidth=0.2,relheight=0.18)
MENU_VALUES=Menu(menu_units,tearoff=0,background="#E6E4E5",font=("Cambria",15),selectcolor="#245985")

MENU_VALUES.add_radiobutton(label='Currency',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Weight',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Length',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Angles',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Area',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Capacity',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Volume',variable=menu_variable)
MENU_VALUES.add_radiobutton(label='Electricity',variable=menu_variable)

menu_units['menu']=MENU_VALUES

lbl_units=Label(controls_pane,text="Units",font=("Cambria",16),foreground="grey",background='#E6E4E5')
lbl_units.place(relx=0.4,rely=0.8,relwidth=0.2)

def updateTime():
    time_lbl.configure(text=f"Date: {str(datetime.now()).split('.')[0]}")
    window.after(100,updateTime)
updateTime()
def preventKeys(event):
    pass
def maximizeRestore(event):
    if window.attributes("-fullscreen"):
        window.attributes("-fullscreen",False)
        maxrestore_lbl.configure(text='1')
        # window.geometry(f"{window_w}x{window_h}+{center_x}+{center_y}")
    else:
        window.overrideredirect(0)
        maxrestore_lbl.configure(text='2')
        window.attributes('-fullscreen',True)
maxrestore_lbl.bind("<ButtonPress>",maximizeRestore)
def printOnlyNumbers(event,entry):
    if str(event.keysym) not in ['1','2','3','4','5','6','7','8','9','0','BackSpace','period']:
        winsound.Beep(600,100)
        return "break"
    else:
        if '.' in str(entry.get()) and str(event.keysym) == 'period':# To avoid more than one periods in an entry box
            winsound.Beep(600,100)
            return "break"


cmb_to.bind("<Key>",preventKeys)
cmb_from.bind("<Key>",preventKeys)
entry_from.bind("<Key>",lambda event, entry_f=entry_from: printOnlyNumbers(event,entry_f))
entry_to.bind("<Key>",lambda event, entry_t=entry_to: printOnlyNumbers(event,entry_t))
try:
    def save_last_pos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def dragging(event):
        x, y = event.x - lastClickX + window.winfo_x(), event.y - lastClickY + window.winfo_y()
        window.geometry("+{0}+{1}".format(x, y))

    app_bar.bind('<Button-1>', save_last_pos)
    app_bar.bind('<B1-Motion>', dragging)


    def minimize_window(event):
        window.overrideredirect(0)
        window.iconify()


    def show_windoww():
        if  window.state() == 'normal':
            window.overrideredirect(1)
        window.after(1, show_windoww)
    show_windoww()
    def close_window(event):
        sys.exit(0)
        pass
    def mouse_enter1(event):
        minimize_lbl.configure(foreground='maroon')


    def mouse_leave1(event):
        minimize_lbl.configure(foreground='beige')

    def mouse_enter2(event):
        maxrestore_lbl.configure(foreground='maroon')


    def mouse_leave2(event):
        maxrestore_lbl.configure(foreground='beige')


    def mouse_enter(event):
        close_lbl.configure(foreground='red')


    def mouse_leave(event):
        close_lbl.configure(foreground='beige')

    minimize_lbl.bind('<ButtonPress>', minimize_window)
    close_lbl.bind('<ButtonPress>', close_window)

    close_lbl.bind("<Enter>",mouse_enter)
    close_lbl.bind("<Leave>",mouse_leave)
    minimize_lbl.bind("<Enter>",mouse_enter1)
    minimize_lbl.bind("<Leave>",mouse_leave1)
    maxrestore_lbl.bind("<Enter>",mouse_enter2)
    maxrestore_lbl.bind("<Leave>",mouse_leave2)
except:
    pass

window.mainloop()