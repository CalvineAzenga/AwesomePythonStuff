import tkinter as tk
from tkinter import Label, ttk
from win32api import GetSystemMetrics
from PIL import Image, ImageTk
import pyttsx3
import winsound

pyttsx3.init()
engine = pyttsx3.Engine()
window = tk.Tk()
style = ttk.Style(window)
style.theme_use("clam")
window.title("Cally POS V1.0.0")
window.overrideredirect(1)
width = 400
height = 600
pos_x = int((GetSystemMetrics(0) - width) / 2)
pos_y = int((GetSystemMetrics(1) - height) / 2)
window.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
window.tk_setPalette("gray17")
window.resizable(0, 0)

mainCanvas = tk.Canvas(window, bg="#9EC862", bd=0, borderwidth=0, highlightthickness=0)
mainCanvas.place(relx=0, rely=0, relwidth=1, relheight=1)

appBar = tk.Label(mainCanvas, bg="#5C723D", text="Cally POS V1.0.0", font=("Verdana", 12), anchor="w")
appBar.place(rely=0, relx=0, relwidth=1, relheight=0.1)

btnClose = tk.Label(appBar, text=" X ", cursor="hand2", relief="flat", font=("Verdana", 18), background="#5C723D")
btnClose.pack(side="right", fill="y")

btnClose.bind("<Enter>", lambda event: btnClose.configure(fg="#2D0007"))
btnClose.bind("<Leave>", lambda event: btnClose.configure(fg="#FFFFFF"))
btnClose.bind("<ButtonPress>", lambda event: window.destroy())

loginPane = tk.Canvas(mainCanvas, bg="#9EC862", highlightthickness=0, bd=0, borderwidth=0)
loginPane.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

levelImg = tk.PhotoImage(file="./btlog.png", master=window)
userImg = tk.PhotoImage(file="./User.png", master=window)
passwdImg = tk.PhotoImage(file="./login.png", master=window)

logo = Image.open("./logo.png")
logo = logo.resize((120, 120), Image.ANTIALIAS)
logo = ImageTk.PhotoImage(logo, master=window)

logoLbl = Label(loginPane, bg="#9EC862", image=logo)
logoLbl.pack(side="top", pady=50, fill="both")

loginPane2 = tk.Canvas(loginPane, bg="#9EC862", highlightthickness=0, bd=0, borderwidth=0)
loginPane2.pack(side="left", padx=20, anchor="center")

lblLevel = tk.Label(loginPane2, bg="#9EC862", text="Level", fg="gray17", font=("Verdana", 12))
lblLevel.grid(row=0, column=0, pady=10, sticky="e", padx=10)
levelCmb = ttk.Combobox(loginPane2, font=("Verdana", 14), width=19, justify="center")
levelCmb.grid(row=0, column=1, pady=10, sticky="e")

lblUsername = tk.Label(loginPane2, bg="#9EC862", image=userImg)
lblUsername.grid(row=1, column=0, pady=10, sticky="e", padx=10)
usernameTxt = ttk.Entry(loginPane2, font=("Verdana", 14), justify="center", width=20)
usernameTxt.grid(row=1, column=1, pady=10, sticky="e")

lblPassword = tk.Label(loginPane2, bg="#9EC862", image=passwdImg)
lblPassword.grid(row=2, column=0, pady=10, sticky="e", padx=10)
passwordTxt = ttk.Entry(loginPane2, show=".", font=("Verdana", 14), justify="center", width=20)
passwordTxt.grid(row=2, column=1, pady=10, sticky="e")

forgotPassLbl = tk.Label(loginPane2, text="Forgot password?", anchor="center", cursor="hand2", fg="beige",
                         font=("Verdana", 10))
forgotPassLbl.grid(row=3, column=1, pady=10, sticky="n")

btnLogin = tk.Button(loginPane2, text="LOGIN", bg="#202634", cursor="hand2", fg="#ffffff", relief="ridge", bd=3,
                     font=("Verdana", 16), width=18)
btnLogin.grid(row=4, column=1, pady=10, sticky="w")

statusLbl = tk.Label(loginPane2, text="[-] Incomplete details!", background="maroon", font=("Verdana", 10))
statusLbl.grid(row=5, column=1, pady=10, sticky="n")


def checkFields():
    if len(usernameTxt.get()) < 1 or len(levelCmb.get()) < 1 or len(passwordTxt.get()) < 1:
        statusLbl.configure(text="[-] Empty Field(s) deteted!", background="maroon")
        for a in range(2):
            winsound.Beep(700, 100)
        return False
    else:
        statusLbl.configure(text="[+] Login Successful", background="darkgreen")
        engine.say("Login Successful")
        engine.runAndWait()
        return True


btnLogin.configure(command=checkFields)

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
