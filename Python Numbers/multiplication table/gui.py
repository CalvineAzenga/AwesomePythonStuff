from tkinter import ttk,Tk
import tkinter
import pyttsx3

pyttsx3.init()
main_window=Tk()
main_window.title("Multiplication Table in Python")
rows=20
columns=40
lbl_width=1/columns
relx=0
rely=0
rowt=0
columnt=0
lbl_list=[]
for row in range(1,rows+1):
    for column  in range(1,columns+1):
        lbl=ttk.Label(main_window,font=("Raleway",10,'bold'),relief='flat',foreground='green')
        answer=row*column

        lbl.configure(text=answer)
        lbl.grid(row=rowt,column=columnt,sticky='w',padx=5,pady=5)
        columnt+=1

        if column==1 or row==1:
            lbl.configure(foreground='yellow',font=("Corbel",13,"bold"))
        else:
            def press3(text):
                pyttsx3.speak(text.replace("x","times"))
            def hover3(lbl1,text):
                lbl1.configure(foreground='red')
                main_window.title(text)

            def leave3(lbl1):
                lbl1.configure(foreground='green')
            text=f"{row} x {column} = {answer}"
            lbl.bind("<Enter>", lambda event, lbl1=lbl,text=text: hover3(lbl1,text))
            lbl.bind("<Leave>", lambda event, lbl1=lbl: leave3(lbl1))
            lbl.bind("<ButtonPress>", lambda event, text=text: press3(text))

            
        if column%columns==0:
            rowt+=1
            columnt=0
        

main_window.tk_setPalette("#2b2b2b")
main_window.attributes("-toolwindow",True)
main_window.mainloop()