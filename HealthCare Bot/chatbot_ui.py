from tkinter import Label,END,NORMAL,PhotoImage,DISABLED, Text
from tkinter.ttk import Scrollbar,Style
import textwrap
from datetime import datetime
from PIL import Image,ImageTk
def ChatBotUI(self,EntryBox,ChatLog):
    style=Style(ChatLog)
    style.theme_use('clam')
    

    current_time=datetime.now().strftime("%D - %H:%M \n")

    img2=PhotoImage(master=self,file='icons/assistant2.png')
    img3=PhotoImage(master=self,file='icons/emblem-default.png')
    background_img=Image.open('images/clear.jpg')
    background_img=ImageTk.PhotoImage(background_img,master=self)
    # ChatLog.image_create(END,image=background_img)

    def send(event):
        msg = EntryBox.get("1.0", 'end-1c').strip()
        EntryBox.delete("0.0", END)
        current_time=datetime.now().strftime("%D - %H:%M \n")
        

        if msg != '':
            ChatLog.config(state=NORMAL)
            ChatLog.insert(END, current_time+' ',("small", "right", "colour"))
            ChatLog.window_create(END,window=Label(ChatLog, fg="#E6E7E9",text=msg,wraplength=200, font=("Arial", 11),bg="#25313C", bd=4, justify="left"))
            ChatLog.insert(END, '\n ', "right")
            ChatLog.window_create(END,window=Label(ChatLog,image=img3, fg="#E6E7E9", font=("Arial", 11),bg="#151E27", bd=4, justify="left"))
            ChatLog.insert(END,'\n ', "left")
            ChatLog.config(foreground="lime",font=("Helvetica", 9))
            ChatLog.yview(END)
            res = "Bot's response goes into here, elongating this message to test textwrap"
            ChatLog.insert(END, current_time+' ',("small", "colour", "left"))
            ChatLog.window_create(END,window=Label(ChatLog,image=img2, fg="#E6E7E9",text="", font=("Arial", 11), bd=4, justify="left"))
            ChatLog.insert(END, '\n ', "left")
            ChatLog.window_create(END,window=Label(ChatLog, fg="#E6E7E9",text=res,wraplength=200, font=("Arial", 11),bg="#25313C", bd=4, justify="left"))
            ChatLog.insert(END, '\n ', "right")            
            ChatLog.config(state=DISABLED)
            ChatLog.yview(END)

    ChatLog.update_idletasks()
    ChatLog.config(state=NORMAL)
    ChatLog.tag_config("right", justify="right")
    ChatLog.tag_config("small", font=("Helvetica", 8))
    ChatLog.tag_config("colour", foreground="cyan")
    ChatLog.insert(END, current_time, ("small","colour"))
    ChatLog.insert(END,textwrap.fill(f"Hello {'*Name*'}.How can I assist you?",30))
    ChatLog.insert(END,'\n')
    ChatLog.config(foreground="lime", font=("Helvetica", 9))
    
    ChatLog.config(state=DISABLED)
    
    # Bind scrollbar to Chat window
    scrollbar = Scrollbar(self,command=ChatLog.yview, cursor="double_arrow")
    scrollbar.place(relx=0.95,rely=0,relwidth=0.05,relheight=1)
    ChatLog['yscrollcommand'] = scrollbar.set
    ChatLog.tag_config("left", justify="left")
    EntryBox.bind("<Return>",send)
    ChatLog.bind("<ButtonPress>","break")