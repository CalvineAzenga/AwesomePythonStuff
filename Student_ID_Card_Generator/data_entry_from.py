from tkinter import Canvas, Tk, ttk,Label,Button,LabelFrame,messagebox,filedialog
import os
import time
from PIL import Image,ImageTk

app=Tk()
style=ttk.Style(app)
style.theme_use("clam")
app.wm_attributes("-toolwindow",True)
app.wm_attributes("-topmost",True)
image=None
app.geometry("600x400+400+50")
# app.resizable(0,0)
app.wm_title("Data Entry Form")

main_canvas=LabelFrame(app)
main_canvas.place(relx=0,rely=0,relwidth=1,relheight=1)

lbl_name=Label(main_canvas,text="Name:",font=("Verdana",12))
lbl_name.grid(row=0,column=0,padx=10,pady=5,sticky='e')

txt_name=ttk.Entry(main_canvas,font=("Verdana",12))
txt_name.grid(row=0,column=1,padx=10,pady=5,sticky='e')

lbl_reg=Label(main_canvas,text="Reg No:",font=("Verdana",12))
lbl_reg.grid(row=1,column=0,padx=10,pady=5,sticky='e')

txt_reg=ttk.Entry(main_canvas,font=("Verdana",12))
txt_reg.grid(row=1,column=1,padx=10,pady=5,sticky='e')

lbl_phone=Label(main_canvas,text="Phone No:",font=("Verdana",12))
lbl_phone.grid(row=2,column=0,padx=10,pady=5,sticky='e')

txt_phone=ttk.Entry(main_canvas,font=("Verdana",12))
txt_phone.grid(row=2,column=1,padx=10,pady=5,sticky='e')

lbl_course=Label(main_canvas,text="Course:",font=("Verdana",12))
lbl_course.grid(row=3,column=0,padx=10,pady=5,sticky='e')

txt_course=ttk.Entry(main_canvas,font=("Verdana",12))
txt_course.grid(row=3,column=1,padx=10,pady=5,sticky='e')

lbl_school=Label(main_canvas,text="School:",font=("Verdana",12))
lbl_school.grid(row=4,column=0,padx=10,pady=5,sticky='e')

txt_school=ttk.Entry(main_canvas,font=("Verdana",12))
txt_school.grid(row=4,column=1,padx=10,pady=5,sticky='e')

lbl_validity=Label(main_canvas,text="Validity:",font=("Verdana",12))
lbl_validity.grid(row=5,column=0,padx=10,pady=5,sticky='e')

txt_validity=ttk.Entry(main_canvas,font=("Verdana",12))
txt_validity.grid(row=5,column=1,padx=10,pady=5,sticky='e')

lbl_picture=Label(main_canvas,text="Picture:",font=("Verdana",12))
lbl_picture.grid(row=6,column=0,padx=10,pady=5,sticky='ne')

lbl_status=Label(main_canvas,text="Successfully Submitted",font=("Verdana",14),foreground="green")
lbl_status.grid(row=6,column=2,padx=10,pady=5)

picture_profile=Canvas(main_canvas,width=150,height=120,background='#EFE4B0')
picture_profile.grid(row=6,column=1,padx=10,pady=5,sticky='w')

btn_picture=Button(main_canvas,text="Select Picture",relief='flat',cursor="hand2",background='#2B2B2B',activebackground="#2B2B2B",activeforeground="orange",foreground="beige",font=("Verdana",12))
btn_picture.grid(row=7,column=1,padx=10,pady=5,sticky='w')

btn_submit=Button(main_canvas,text="SUBMIT",relief='flat',cursor="hand2",background='#551A8B',activebackground="#551A8B",activeforeground="orange",foreground="beige",font=("Verdana",12))
btn_submit.grid(row=7,column=2,padx=20,pady=5,sticky='w')

def submitData():
    fullname=txt_name.get()
    reg=txt_reg.get()
    phone=txt_phone.get()
    course=txt_course.get()
    school=txt_school.get()
    validity=txt_validity.get()
    if(fullname=='' or reg=='' or phone=='' or course=='' or school=='' or validity==''):
        messagebox.showwarning("+ EMPTY FIELD(S)!","Please fill all fields.")
        return
    if(image==None):
        messagebox.showwarning("+ EMPTY IMAGE PATH!","Please select a valid Image File First.")
        return
    file=open("./studentdata.csv",'a',encoding='utf-8',errors='ignore')
    file.write(f"\n{fullname},{reg},{phone},{course},{school},{validity},{image}")
    lbl_status.configure(text="Successfully Submitted!")
    file.close()
    # clearFields()
def clearFields():
    txt_name.delete(0,"end")
    txt_reg.delete(0,"end")
    txt_phone.delete(0,"end")
    txt_course.delete(0,"end")
    txt_school.delete(0,"end")
    txt_validity.delete(0,"end")
    picture_profile.image=None
    image=None
def loadImage():
    global image
    picture=filedialog.askopenfilename(title="Select an Image",filetypes=[("Image Files",(".png",".jpg",".jpeg",".ico",".bmp",".gif"))])
    try:
        img=Image.open(picture)
        img_name=f"{time.time_ns()}.png"
        img.save(f"./profile_images/{img_name}")
        img=img.resize((150,120),Image.ANTIALIAS)
        img=ImageTk.PhotoImage(img, master=app)
        picture_profile.create_image(0,0,anchor="nw",image=img)
        picture_profile.image=img
        image=img_name
    except Exception as msg:
        image=None
        messagebox.showerror("+ FATAL ERROR",str(msg))
btn_picture.configure(command=loadImage)
btn_submit.configure(command=submitData)

def lblUpdater():

    lbl_status.configure(text='')
    app.after(1500,lblUpdater)
lblUpdater()

app.mainloop()