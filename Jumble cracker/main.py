from tkinter import ttk, Tk, Text
from word_finder import jumbleSolve
import time
import winsound
import threading
window=Tk()
window.wm_attributes("-topmost",True)
window.geometry("1020x600+100+100")
window.overrideredirect(1)
window.tk_strictMotif(1)
window.tk_setPalette("#DDDDDD")
style=ttk.Style(window)
style.theme_use('clam')
style.configure("TButton",font=("Georgia",16),foreground="#2b2b2b")
app_bar=ttk.Label(window,background="#214665")
app_bar.place(relx=0,rely=0,relheight=0.1,relwidth=1)

app_name_lbl=ttk.Label(app_bar,text="Jumble Cracker",font=("Georgia",20),background="#214665",foreground="beige")
app_name_lbl.pack(side='left',padx=10)

close_lbl=ttk.Label(app_bar,text="X",font=("Verdana",17),foreground="beige",background="#214665")
close_lbl.pack(side="right",padx=10)

minimize_lbl=ttk.Label(app_bar,text="__\n",font=("Verdana",12),justify='center',foreground="beige",background="#214665")
minimize_lbl.pack(side="right",padx=10,pady=12)

content_bar=ttk.Label(window,background="#DDDDDD")
content_bar.place(relx=0,rely=0.1,relheight=0.9,relwidth=1)

top_bar=ttk.Label(content_bar,background="#DDDDDD")
top_bar.place(relx=0,rely=0,relheight=0.15,relwidth=1)

top_bar_lbl=ttk.Label(top_bar,text="Enter your jumbled word",font=("Georgia",16),background="#DDDDDD",foreground="#333")
top_bar_lbl.pack(side='left',padx=10)

top_bar_txt=ttk.Entry(top_bar,font=("Georgia",20),justify='center',background="#DDDDDD",foreground="#551A8B")
top_bar_txt.pack(side='left',padx=10)

left_bar=ttk.Label(content_bar,background="#DDDDDD",borderwidth=3)
left_bar.place(relx=0,rely=0.15,relheight=0.85,relwidth=0.3)

lbl_amount=ttk.Label(left_bar,text="Length of word",font=("Georgia",12),background="#DDDDDD",foreground="#333")
lbl_amount.pack(side='left',padx=10,pady=10,anchor='nw')

txt_amount=ttk.Entry(left_bar,width=10,font=("Georgia",12),background="#DDDDDD",foreground="#333")
txt_amount.pack(side='left',padx=10,pady=10,anchor='ne')

btn_solve=ttk.Button(left_bar,text="Solve")
btn_solve.place(relx=0.01,relwidth=0.4,relheight=0.1,rely=0.3)

right_bar=ttk.Label(content_bar,background="#DDDDDD")
right_bar.place(relx=0.3,rely=0.15,relheight=0.845,relwidth=0.695)

title_lbl=ttk.Label(right_bar,text="",background="#DDDDDD",font=("Georgia",20),foreground="#333")
title_lbl.pack(side='left',anchor='nw')

status_lbl=ttk.Label(left_bar,wraplength=300,text="",background="#DDDDDD",font=("Georgia",12),foreground="#0A4220")
status_lbl.place(relx=0,rely=0.5,relwidth=1)

status_duration_lbl=ttk.Label(left_bar,wraplength=300,text="",background="#DDDDDD",font=("Georgia",12),foreground="#2b2b2b")
status_duration_lbl.place(relx=0,rely=0.6,relwidth=1)

right_bar1=ttk.Label(right_bar)
right_bar1.place(relx=0,rely=0.15,relheight=0.85,relwidth=1)

scrollbar1=ttk.Scrollbar(right_bar1)
scrollbar1.pack(side='right',fill='y',expand=True)

txt_result=Text(right_bar1,background="#DDDDDD",font=("Bahnschrift Light Condensed",17),foreground="#001D26",border=0,state='disabled')
txt_result.pack(side='left',expand=True)
scrollbar1.config(command=txt_result.yview)
txt_result.configure(yscrollcommand=scrollbar1.set)

txt_result.bind("<Key>","break;")
txt_result.bind("<ButtonPress>","break;")
wordlength=''
def threadSolvePuzzle():
    threading.Thread(target=solvePuzzle,daemon=True).start()
def solvePuzzle():
    global wordlength
    status_duration_lbl.configure(text="")
    btn_solve.configure(state='disabled')
    txt_result.configure(state='normal')
    title_lbl.configure(text=f"Possible anagrams of \"{top_bar_txt.get().strip()}\"")
    txt_result.delete("0.0","end")
    status_lbl.configure(text="Iterating through possiblities")
    wordlength=txt_amount.get()
    if wordlength=='':
        wordlength=len(top_bar_txt.get().strip())
    starttime=time.time_ns()
    answer=jumbleSolve(top_bar_txt,txt_result,wordlength)
    stoptime=time.time_ns()
    durattion=str(round(((stoptime-starttime)/1000000000),2))
    worldlist,textt=answer
    txt_result.delete("0.0","end")
    txt_result.insert("0.0",'\t'.join([word for word in worldlist]))
    txt_result.configure(state='disabled')
    status_lbl.configure(text=textt)
    btn_solve.configure(state='normal')
    status_duration_lbl.configure(text=f"Completed after {durattion} seconds")

btn_solve.configure(command=threadSolvePuzzle)
def printOnlyNumbers(event,entry):
    if str(event.keysym) not in ['1','2','3','4','5','6','7','8','9','0','BackSpace']:
        winsound.Beep(600,100)
        return "break"


txt_amount.bind("<Key>",lambda event,entry=txt_amount:printOnlyNumbers(event,entry))
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
    close_lbl.bind("<ButtonPress>",lambda event:window.destroy())
    minimize_lbl.bind("<ButtonPress>",minimize_window)

except:
    pass
window.mainloop()