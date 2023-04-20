import threading
from tkinter.ttk import *
import time
from tkinter import Canvas,Tk,Listbox,Entry,PhotoImage,Menubutton as mnb
import json
import difflib
import ttkthemes as tk
from tkhtmlview import HTMLLabel
from tkhtmlview import HTMLScrolledText
import pyttsx3
import re

key=''
data = json.load(open('data2.json'))
mylist=[]
i=0
for word in data:
    mylist.append(str(word))
print(i)
mylist=sorted(mylist)
current_word=''
load_allow=0
window=tk.ThemedTk()
engine=pyttsx3.init()
window.set_theme('clam')
window.geometry("1000x600")
# window.attributes("-toolwindow",True)
window.attributes("-topmost",True)
window.title("Calvo Advanced Dictionary")
# window.attributes("-alpha",0.95)


def fixed_map(option):
    return [elm for elm in s.map('TMenubutton', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

def fixed_map2(option):
    return [elm for elm in s.map('TButton', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

s=Style()

s.map('TMenubutton', foreground=fixed_map('foreground'), background=fixed_map('background'),
      fieldbackground=fixed_map('fieldbackground'))

s.configure("TMenubutton", foreground="lime", background="darkgreen", fieldbackground="green", bordercolor="gold",
            darkcolor="#2b2b2b", lightcolor="green", borderwidth=2, font=("Verdana",10))

# s.map('TButton', foreground=fixed_map2('foreground'), background=fixed_map2('background'),
#       fieldbackground=fixed_map2('fieldbackground'))
#
# s.configure("TButton", foreground="lime", background="darkgreen", fieldbackground="green", bordercolor="gold",
#             darkcolor="#2b2b2b", lightcolor="green", borderwidth=2, font=("Verdana",10))


app_bar=Label(window, background="#5C723D")
app_bar.place(relx=0,rely=0,relheight=0.15,relwidth=1)

btn_history=Menubutton(app_bar,text="History",cursor="hand2")
btn_history.place(relx=0.9,rely=0.5,relwidth=0.08)

btn_settings=Button(app_bar,text="Settings",cursor="hand2")
btn_settings.place(relx=0.8,rely=0.5,relwidth=0.08)





# read_icon=PhotoImage(file="icons/read.gif")

words_pane=Label(window, background="beige")
words_pane.place(relx=0,rely=0.15,relwidth=0.3,relheight=0.85)

entry_field=Entry(words_pane,bg='white',highlightbackground='#9EC862',highlightcolor='green',relief='flat',highlightthickness=1,justify='left',font="Verdana 13")
entry_field.place(relx=0,rely=0,relheight=0.08,relwidth=0.999)

words_list=Listbox(words_pane,bg='beige',activestyle='none',relief='flat',highlightbackground='beige',highlightcolor='beige',highlightthickness=2,font="Verdana 11")
words_list.place(relx=0,rely=0.085,relheight=0.91,relwidth=1)

words_list2=Listbox(words_pane,bg='beige',activestyle='none',relief='flat',highlightbackground='beige',highlightcolor='beige',highlightthickness=2,font="Verdana 11")

meaning_pane=Label(window, background="lavender")
meaning_pane.place(relx=0.3,rely=0.15,relwidth=0.7,relheight=0.85)


lbl = HTMLScrolledText(meaning_pane,bd=0,state="disabled")
lbl.place(relx=0,rely=0,relheight=1,relwidth=1)

lbl.set_html("<div><div/><div style='color:grey;font-size:30px;'>Search words<div>")
lbl.fit_height()

btn_sound=Button(lbl,compound='left',cursor='hand2')
btn_sound.place(relx=0.93,rely=0.01,relwidth=0.06)

pane_close_words=Listbox(words_list2,bg='#045B62',fg='lavender',activestyle='none',relief='flat',highlightbackground='beige',highlightcolor='beige',highlightthickness=2,font="Verdana 11 italic")

def read_word(arg):
    global current_word
    current_word=arg
    engine.say(current_word)
    engine.runAndWait()

def read_word_thread(event):
    global current_word
    thread=threading.Thread(target=read_word,args=(current_word,))
    thread.daemon = True
    thread.start()

def load_word():
    global key
    global current_word
    if key=='':
        key=entry_field.get().lower()
    else:
        pass
    key=str(key).lower()
    if key in data:
        current_word=key[0].upper()+key[1:]
        return data[key]
    elif key.title() in data:
        return data[key.title()]
    elif len(difflib.get_close_matches(key, data.keys())) > 0:
        close_key = difflib.get_close_matches(key, data.keys(),n=50)
        pane_close_words.delete(0,'end')
        for i in range(len(close_key)):
            pane_close_words.insert(i,close_key[i])
        pane_close_words.place(relx=0,rely=0,relwidth=0.9,relheight=0.4)
    else:
        return "Not found"
    pass

def ask():
    HTMLTEXT=''
    # result = list(load_word().split(";"))
    result = load_word()
    if type(result) == list:
        pane_close_words.place_forget()
        num = list(range(1, len(result)+1))
        for item, number in zip(result, num):
            HTMLTEXT+=f"<br /><li style='color:#2b2b2b;font-size:12px;'><span style='color:violet;font-size:12px;'>{number}.) <span/><span style='color:#323233;font-size:12px;'>{item}<span/><br /><li/>"
            # print(f'{number}. {item}')
            pass
        lbl.set_html(str("<div><div/><h1 style='color:darkgreen;font-size:20px;font-weight:bold;font-family:Verdana;'>"+current_word+"<h1/>"+"<div><div/><div><hr><br /><hr><br />"+HTMLTEXT+"<div/>").replace("\\n","<br />").replace("source:","<span style='color:purple;'>source:<span/>"))
    else:
        pass
def ask_thread(event):
    global key
    key=entry_field.get()
    thread=threading.Thread(target=ask)
    thread.daemon=True
    thread.start()

def fill_list_box_initial():
    global mylist
    global load_allow
    load_allow=1
    index=0
    words_list.delete(0,"end")
    words_list.insert('end',*mylist)
    # for word in mylist:
    #     if load_allow:
    #         time.sleep(0.009)
    #         words_list.insert(index,word)
    #         index+=1
    #     else:
    #         break

def updatekey(event):
    global key
    key=words_list.get(words_list.curselection())
    entry_field.delete(0,"end")
    entry_field.insert(0,key)
    ask()

def updatekey2(event):
    global key
    key=pane_close_words.get(pane_close_words.curselection())
    entry_field.delete(0,"end")
    entry_field.insert(0,key)
    ask()

def updatekey3(event):
    global key
    key=words_list2.get(words_list2.curselection())
    entry_field.delete(0,"end")
    entry_field.insert(0,key)
    ask()
def fill_list_on_entry():
    global load_allow, mylist
    if str(entry_field.get())=="":
        words_list2.place_forget()

    else:
        load_allow=0
        words_list2.delete(0,"end")
        i=0
        subword=str(entry_field.get().lower())
        regex=re.compile(f".*{subword}.*")
        compiled_list=list(filter(regex.match,mylist))
        for word in compiled_list:
            words_list2.place(relx=0,rely=0.085,relheight=0.91,relwidth=1)
            words_list2.insert(i,word)
            i+=1
            time.sleep(0.001)


def fill_list_on_entry_thread(event):
    thread5=threading.Thread(target=fill_list_on_entry)
    thread5.daemon=False
    thread5.start()

btn_sound.bind("<ButtonPress>",read_word_thread)
voices=engine.getProperty('voices')
# for voice in voices:
#     print(voice.name)

rate=engine.setProperty('rate',160)
engine.setProperty('voice',voices[0].id)
entry_field.bind("<Return>", ask_thread)
entry_field.bind("<Key>", fill_list_on_entry_thread)
words_list.bind("<<ListboxSelect>>",updatekey)
words_list2.bind("<<ListboxSelect>>",updatekey3)
pane_close_words.bind("<<ListboxSelect>>",updatekey2)

thread1=threading.Thread(target=fill_list_box_initial)
thread1.daemon=True
thread1.start()

scroll_bar=Scrollbar(words_list)
scroll_bar.pack(side='right',fill='y')
scroll_bar.configure(command=words_list.yview)
words_list.configure(yscrollcommand=scroll_bar.set)

scroll_bar2=Scrollbar(words_list2)
scroll_bar2.pack(side='right',fill='y')
scroll_bar2.configure(command=words_list2.yview)
words_list2.configure(yscrollcommand=scroll_bar2.set)

scroll_bar1=Scrollbar(pane_close_words)
scroll_bar1.pack(side='right',fill='y')
scroll_bar1.configure(command=pane_close_words.yview)
pane_close_words.configure(yscrollcommand=scroll_bar1.set)

window.mainloop()
