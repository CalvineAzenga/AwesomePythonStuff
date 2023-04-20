from datetime import datetime
import time
from tkinter import *
from tkinter import ttk
import winsound
from ttkthemes import ThemedStyle
import sys
import cv2
import threading
from PIL import Image, ImageTk
import pickle
from modelTrainer import predict
from faceRecAPI import show_prediction_labels_on_image
from DbConnection import DbConnection, DbRetrieve
import dataCollectionPane
import os
import pyttsx3

pyttsx3.init()
engine = pyttsx3.Engine()

root = Tk()
root.geometry("1200x720")
root.title("")
# root.wm_iconbitmap("./favicon.ico")
root.attributes("-fullscreen", 1)
# style = ttk.Style(root)
style = ThemedStyle(root)

full_canv = Canvas(root, bg='#bd781d', highlightthickness=0)
full_canv.place(rely=0, relx=0, relwidth=1, relheight=1)


def updateWindow():
    try:
        if root.state() == "normal":
            root.wm_overrideredirect(1)
    except:
        pass
    root.after(100, updateWindow)


updateWindow()


def minimizeWindow(event):
    root.overrideredirect(0)
    root.iconify()


def restoreWindow(event):
    if root.attributes('-fullscreen'):
        root.overrideredirect(1)
        root.attributes("-fullscreen", 0)
        rest_label.configure(text="1")
    else:
        root.overrideredirect(0)
        root.attributes("-fullscreen", 1)
        rest_label.configure(text="2")


clos_canv = Canvas(full_canv, bg="#1f1f3a", highlightthickness=0)
clos_canv.place(rely=0, relx=0, relwidth=1, height=30)

title_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="MUT Automated Classroom Attendance System",
                    font=("Cambria", 14), cursor="none")
title_label.pack(side=LEFT, padx=7)

dest_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="X", font=("Arial", 15), cursor="hand2")
dest_label.pack(side=RIGHT, padx=7)
dest_label.bind("<ButtonPress>", lambda event: sys.exit())

rest_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="2", font=("Marlett", 12), cursor="hand2")
rest_label.pack(side=RIGHT, padx=7)
rest_label.bind("<ButtonPress>", restoreWindow)

minimize_label = Label(clos_canv, bg='#1f1f3a', fg="#ffffff", text="-", font=("Arial", 30), cursor="hand2")
minimize_label.pack(side=RIGHT, padx=7)
minimize_label.bind("<ButtonPress>", minimizeWindow)

root.update_idletasks()

bottom_canv = Canvas(root, bg='red', highlightthickness=0)
bottom_canv.place(y=30, relx=0, relheight=(root.winfo_height() - 30) / root.winfo_height(), relwidth=1)

lblAttendeeName = Label(bottom_canv, text="", font=("Lucida Calligraphy", 15, "bold"), background="#183958",
                        foreground="yellow")
lblAttendeeName.place(relx=0.01, rely=0.01)

mainBackImage = Image.open("./assets/t_bg1.jpg")
mainBackImage = mainBackImage.resize((root.winfo_width(), root.winfo_height()), Image.Resampling.LANCZOS)
mainBackImage = ImageTk.PhotoImage(mainBackImage, master=root)
bottom_canv.create_image(0, 0, image=mainBackImage, anchor="nw")

bottom_canv.update_idletasks()
cameraCanvas = Canvas(bottom_canv, bg="#bd781d", highlightthickness=0, border=5, relief=RIDGE)
cameraCanvas.place(x=10, y=50, relwidth=0.7, relheight=0.8)
cameraCanvas.create_image(0, 0, image=mainBackImage, anchor="nw")

buttonCanvas = Canvas(bottom_canv, bg="lightblue", highlightthickness=0)
buttonCanvas.place(x=10, rely=0.9, relwidth=0.7, relheight=0.09)

# Radio Buttons
# Variables
radioBtnVariable = StringVar(root)

cameraRadioBtn = ttk.Radiobutton(buttonCanvas, variable=radioBtnVariable, value="camera", text="Use Camera Live Stream")
cameraRadioBtn.pack(side=LEFT, padx=20)

pictureRadioBtn = ttk.Radiobutton(buttonCanvas, variable=radioBtnVariable, value="picture",
                                  text="Select Picture or Pictures Folder")
pictureRadioBtn.pack(side=LEFT, padx=20)

videoRadioBtn = ttk.Radiobutton(buttonCanvas, variable=radioBtnVariable, value="video", text="Use Video File")
videoRadioBtn.pack(side=LEFT, padx=20)

detailsCanvas = Canvas(bottom_canv, bg="lavender", highlightthickness=0)
detailsCanvas.place(relx=0.72, y=50, relwidth=0.27, relheight=0.5)

detailsCanvasTop = Canvas(detailsCanvas, bg="#bd781d", highlightthickness=0)
detailsCanvasTop.place(relx=0, rely=0, relwidth=1, relheight=0.1)

lbl = Label(detailsCanvasTop, text="Student Details", fg="#1f1f3a", bg="#bd781d", font=("Cambria", 15))
lbl.pack(pady=(5, 0))

detailsCanvasBottom = Canvas(detailsCanvas, bg="lavender", highlightthickness=0)
detailsCanvasBottom.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

lblName = Label(detailsCanvasBottom, text="Name:", fg="#2b2b2b", bg="lavender", font=("Cambria", 15))
lblName.grid(row=0, column=0, sticky=SE, padx=(20, 0), pady=(10, 0))

lblNameA = Label(detailsCanvasBottom, text="", fg="grey", bg="lavender", font=("Cambria", 11))
lblNameA.grid(row=0, column=1, sticky=SW, padx=(10, 0))

lblCourse = Label(detailsCanvasBottom, text="Course:", fg="#2b2b2b", bg="lavender", font=("Cambria", 15))
lblCourse.grid(row=1, column=0, sticky=SE, padx=(20, 0), pady=(10, 0))

lblCourseA = Label(detailsCanvasBottom, text="", fg="grey", bg="lavender", font=("Cambria", 11))
lblCourseA.grid(row=1, column=1, sticky=SW, padx=(10, 0))

lblRegNo = Label(detailsCanvasBottom, text="Reg No:", fg="#2b2b2b", bg="lavender", font=("Cambria", 15))
lblRegNo.grid(row=2, column=0, sticky=SE, padx=(20, 0), pady=(10, 0))

lblRegNoA = Label(detailsCanvasBottom, text="", fg="grey", bg="lavender", font=("Cambria", 11))
lblRegNoA.grid(row=2, column=1, sticky=SW, padx=(10, 0))

lblContact = Label(detailsCanvasBottom, text="Contact:", fg="#2b2b2b", bg="lavender", font=("Cambria", 15))
lblContact.grid(row=3, column=0, sticky=SE, padx=(20, 0), pady=(10, 0))

lblContactA = Label(detailsCanvasBottom, text="", fg="grey", bg="lavender", font=("Cambria", 11))
lblContactA.grid(row=3, column=1, sticky=SW, padx=(10, 0))

lblGender = Label(detailsCanvasBottom, text="Gender:", fg="#2b2b2b", bg="lavender", font=("Cambria", 15))
lblGender.grid(row=4, column=0, sticky=SE, padx=(20, 0), pady=(10, 0))

lblGenderA = Label(detailsCanvasBottom, text="", fg="grey", bg="lavender", font=("Cambria", 11))
lblGenderA.grid(row=4, column=1, sticky=SW, padx=(10, 0))

lblDepatment = Label(detailsCanvasBottom, text="Department:", fg="#2b2b2b", bg="lavender", font=("Cambria", 15))
lblDepatment.grid(row=5, column=0, sticky=SE, padx=(20, 0), pady=(10, 0))

lblDepatmentA = Label(detailsCanvasBottom, text="", fg="grey", bg="lavender", font=("Cambria", 11))
lblDepatmentA.grid(row=5, column=1, sticky=SW, padx=(10, 0))

startRecognitionImage = Image.open("./assets/t_btn1.png")
startRecognitionImage = startRecognitionImage.resize((150, 150), Image.Resampling.LANCZOS)
startRecognitionImage = ImageTk.PhotoImage(startRecognitionImage, master=root)

startRecognitionBtn = Button(bottom_canv, image=startRecognitionImage, compound=CENTER, border=0, relief="flat",
                             background="#29AAE3", cursor="hand2")
startRecognitionBtn.place(relx=0.72, rely=0.6)

attendanceImage = Image.open("./assets/att.jpg")
attendanceImage = attendanceImage.resize((150, 150), Image.Resampling.LANCZOS)
attendanceImage = ImageTk.PhotoImage(attendanceImage, master=root)

attendanceBtn = Button(bottom_canv, image=attendanceImage, compound=CENTER, border=0, relief="flat",
                       background="lightblue", cursor="hand2")
attendanceBtn.place(relx=0.86, rely=0.6)

signupImage = Image.open("./assets/Blue-Button-PNG-Picture.png")
signupImage = signupImage.resize((100, 50), Image.Resampling.LANCZOS)
signupImage = ImageTk.PhotoImage(signupImage, master=root)

signupBtn = Button(bottom_canv, image=signupImage, compound=CENTER, border=0, relief="flat", background="#25507A",
                   cursor="hand2", command=lambda:dataCollectionPane.show())
signupBtn.place(relx=0.8, rely=0.9)


def loadFilesFromFolder():
    startRecognitionBtn.configure(state='disabled')
    for file in os.listdir("./available"):
        try:
            cap = cv2.VideoCapture(os.path.join("./available", file))
            conn = DbRetrieve()
            ret, frame = cap.read()
            if ret:
                # Different resizing options can be chosen based on desired program runtime.
                # Image resizing for more stable streaming
                img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                # img=frame
                # process_this_frame = process_this_frame + 1
                # if process_this_frame % 30 == 0:
                predictions = predict(img, model_path="MUTFaceRecognitionModel.clf")
                frame, regNo = show_prediction_labels_on_image(frame, predictions)

                try:
                    outcomes = conn.fillRecognitionData(regNo=str(regNo).upper())[0]
                    fillCard(outcomes[0], outcomes[1], outcomes[2], outcomes[3], outcomes[4], outcomes[5])
                    lblAttendeeName.configure(text=str(outcomes[0]))
                except Exception as msg:
                    lblAttendeeName.configure(text="")
                    pass
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                # img=img.resize((cameraCanvas.winfo_width(),cameraCanvas.winfo_height()),Image.Resampling.LANCZOS)
                fxh = cameraCanvas.winfo_height()
                # fxw=cameraCanvas.winfo_width()
                hpercnt = (fxh / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercnt)))
                img = img.resize((wsize, fxh), Image.Resampling.NEAREST)
                originX = int((cameraCanvas.winfo_width() - wsize) / 2)
                img = ImageTk.PhotoImage(img, master=root)
                cameraCanvas.create_image(originX, 0, anchor="nw", image=img)
                cameraCanvas.image = img
                # fillTreeview()
                # time.sleep(1)
        except:
            pass
    startRecognitionBtn.configure(state='normal')
    # engine.say("Done Looping through all the Images")
    # engine.runAndWait()
    winsoundBeep()


def winsoundBeep():
    winsound.Beep(600, 300)
    winsound.Beep(700, 300)
    winsound.Beep(500, 300)
    winsound.Beep(600, 300)
    winsound.Beep(700, 300)


def fromFolderThread():
    thread = threading.Thread(target=loadFilesFromFolder)
    thread.daemon = True
    thread.start()


def yieldImageFromURL(url="https://192.168.43.1:8080/video"):
    # url=0
    startRecognitionBtn.configure(state='disabled')
    process_this_frame = 29
    # print('Setting cameras up...')
    cap = cv2.VideoCapture(url)
    conn = DbRetrieve()
    while True:
        ret, frame = cap.read()
        if ret:
            try:
                # Different resizing options can be chosen based on desired program runtime.
                # Image resizing for more stable streaming
                img = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
                # img=frame
                process_this_frame = process_this_frame + 1
                Frame = None
                if process_this_frame % 30 == 0:
                    predictions = predict(img, model_path="MUTFaceRecognitionModel.clf")
                    frame, regNo = show_prediction_labels_on_image(frame, predictions)

                try:
                    outcomes = conn.fillRecognitionData(regNo=str(regNo).upper())[0]
                    fillCard(outcomes[0], outcomes[1], outcomes[2], outcomes[3], outcomes[4], outcomes[5])
                    lblAttendeeName.configure(text=str(outcomes[0]))
                except Exception as msg:
                    lblAttendeeName.configure(text="")
                    pass
                img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(img)
                fxh = cameraCanvas.winfo_height()
                # fxw=cameraCanvas.winfo_width()
                hpercnt = (fxh / float(img.size[1]))
                wsize = int((float(img.size[0]) * float(hpercnt)))
                img = img.resize((wsize, fxh), Image.Resampling.NEAREST)
                originX = int((cameraCanvas.winfo_width() - wsize) / 2)
                img = ImageTk.PhotoImage(img, master=root)
                cameraCanvas.create_image(originX, 0, anchor="nw", image=img)
                cameraCanvas.image = img
                # fillTreeview()
                # time.sleep(1)
            except:
                winsoundBeep()
                pass
    startRecognitionBtn.configure(state='normal')


def fillCard(fullname, course, regNo, phoneNum, gender, department):
    lblNameA.configure(text=fullname)
    lblCourseA.configure(text=course)
    lblRegNoA.configure(text=regNo)
    lblContactA.configure(text=phoneNum)
    lblGenderA.configure(text=gender)
    lblDepatmentA.configure(text=department)


def showFramesThread():
    thread = threading.Thread(target=yieldImageFromURL)
    thread.daemon = True
    thread.start()


startRecognitionBtn.configure(command=showFramesThread)

sliding_list_canvas = Canvas(bottom_canv, bg='#1f1f3a', highlightthickness=1)

sliding_canvas_top_canvas = Canvas(sliding_list_canvas, bg='#1f1f3a', highlightthickness=0)
sliding_canvas_top_canvas.place(y=1, x=1, relheight=0.2, relwidth=0.99)

close_btn_slider = Label(sliding_canvas_top_canvas, text="X", bg='#1f1f3a', fg="lavender", cursor="hand2",
                         font=("Courier", 20))
close_btn_slider.pack(side=RIGHT, anchor=NE, pady=2, padx=2)


def closeSlider(event):
    sliding_list_canvas.place_forget()


close_btn_slider.bind("<ButtonPress>", lambda event: closeSlider(event))

# Sliding Pane
sliding_canvas_top_label = Label(sliding_canvas_top_canvas, bg='#1f1f3a', fg="#bd781d", text="Today's Attendance",
                                 font=("Georgia", 20))
sliding_canvas_top_label.pack(side=LEFT, padx=5)

sliding_canvas_top_label_count = Label(sliding_canvas_top_canvas, bg='#1f1f3a', fg="cyan", text="",
                                       font=("Georgia", 40))
sliding_canvas_top_label_count.pack(side=LEFT, padx=5)

sliding_canvas_bottom_canvas = Canvas(sliding_list_canvas, bg='#1f1f3a', highlightthickness=0)
sliding_canvas_bottom_canvas.place(rely=0.21, x=1, relheight=0.75, relwidth=0.99)

root.update()

def slidePane():
    for x in range(1, 101, 99):
        # relx = 100 / x * 0.52
        relwidth = 0.48
        relx = 1 - 0.0048 * x
        sliding_list_canvas.place(y=0, relx=relx, relheight=1, relwidth=relwidth)


def startSlider():
    sliderThread = threading.Thread(target=slidePane)
    sliderThread.daemon = True
    sliderThread.start()


# slidePane()

style.set_theme("clam")
# print(style.get_themes())
style.configure(str(cameraRadioBtn.winfo_class()), font=("Verdana", 10), background="lightblue", foreground="#2b2b2b",
                cellpadding=19)

style.configure("Treeview", font=("Verdana", 10), foreground="#2b2b2b", cellpadding=19)
style.configure("Treeview.Heading", font=("Verdana", 10, "bold"), foreground="#bd781d", background="#1f1f3a")
style.map("Treeview", background=[('selected', 'darkgreen')], font=[('selected', ('Verdana', 10))],
          foreground=[('selected', 'orange')])

scrollbar = ttk.Scrollbar(sliding_canvas_bottom_canvas, orient="vertical")
scrollbar.pack(side="right", fill="y")

treeview = ttk.Treeview(sliding_canvas_bottom_canvas, columns=("Name", "RegNo", "Course", "Department", "Gender"),
                        show="headings",
                        selectmode="browse")
treeview.pack(side="left", fill="both", expand=1, padx=4)

treeview.heading("#1", text="Name", anchor="center")
treeview.heading("#2", text="RegNo", anchor="center")
treeview.heading("#3", text="Course", anchor="center")
treeview.heading("#4", text="Department", anchor="center")
treeview.heading("#5", text="Gender", anchor="center")

treeview.column("#1", anchor="w", width=10)
treeview.column("#2", anchor="w", width=10)
treeview.column("#3", anchor="w", width=10)
treeview.column("#4", anchor="w", width=10)
treeview.column("#5", anchor="w", width=10)

treeview.tag_configure("odd", background="#eee")
treeview.tag_configure("even", background="#ddd")
treeview.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=treeview.yview)


def postPopUpMenu(event):
    conn = DbRetrieve()

    row_id = treeview.identify_row(event.y)
    treeview.selection_set(row_id)
    row_values = treeview.item(row_id)['values']
    print(row_values)
    popUpMenu = Menu(treeview, tearoff=0, font=("Verdana", 10))
    popUpMenu.add_command(label="Edit/Update", accelerator="Ctrl+E")
    popUpMenu.add_command(label="Delete", accelerator="Delete", command=lambda: treeview.delete(row_id))
    popUpMenu.add_command(label="View", accelerator="Ctrl+P")
    popUpMenu.add_separator()
    popUpMenu.add_command(label="Send Email", accelerator="Alt+L")
    popUpMenu.add_command(label="Export All to csv", accelerator="Alt+Q", command=lambda: conn.send2Csv())
    popUpMenu.post(event.x_root, event.y_root)


treeview.tag_bind("row", "<Button-3>", lambda event: postPopUpMenu(event))


def fillTreeview():
    try:
        conn = DbRetrieve()
        result_list = conn.getTreeviewData()
        count = conn.getCountAttendanceToday()
        sliding_canvas_top_label_count.configure(text=count)
        i = 0
        if len(result_list) != 0:
            treeview.delete(*treeview.get_children())
            for result in result_list:
                if i % 2 == 0:
                    treeview.insert('', 'end', values=result, tags=("even", "row"))
                else:
                    treeview.insert('', 'end', values=result, tags=("odd", "row"))
                i += 1
    except:
        pass

    root.after(5000, fillTreeview)


fillTreeview()

# To enable Drag Functionality
lastClickX = 0
lastClickY = 0


def SaveLastClickPos(event):
    global lastClickX, lastClickY
    lastClickX = event.x
    lastClickY = event.y


def dragging(event):
    x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
    root.geometry("+%s+%s" % (x, y))


attendanceBtn.configure(command=startSlider)
clos_canv.bind("<ButtonPress>", SaveLastClickPos)
clos_canv.bind("<B1-Motion>", dragging)
root.mainloop()
