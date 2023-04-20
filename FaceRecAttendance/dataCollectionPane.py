import os
from tkinter import *  # GUI INTERFACE
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import sys
from DbConnection import DbConnection, DbRetrieve


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x720")
        self.root.title("")
        # self.root.wm_iconbitmap("./favicon.ico")
        self.root.attributes("-fullscreen", 1)
        self.style = ttk.Style(self.root)
        self.style.theme_use("clam")

        self.full_canv = Canvas(self.root, bg='#bd781d', highlightthickness=0)
        self.full_canv.place(rely=0, relx=0, relwidth=1, relheight=1)

        self.clos_canv = Canvas(self.full_canv, bg="#1f1f3a", highlightthickness=0)
        self.clos_canv.place(rely=0, relx=0, relwidth=1, height=30)

        self.title_label = Label(self.clos_canv, bg='#1f1f3a', fg="#ffffff",
                                 text="MUT Automated Classroom Attendance System", font=("Cambria", 14), cursor="none")
        self.title_label.pack(side=LEFT, padx=7)

        self.dest_label = Label(self.clos_canv, bg='#1f1f3a', fg="#ffffff", text="X", font=("Arial", 15),
                                cursor="hand2")
        self.dest_label.pack(side=RIGHT, padx=7)
        self.dest_label.bind("<ButtonPress>", lambda event: self.root.destroy())

        self.rest_label = Label(self.clos_canv, bg='#1f1f3a', fg="#ffffff", text="2", font=("Marlett", 12),
                                cursor="hand2")
        self.rest_label.pack(side=RIGHT, padx=7)
        self.rest_label.bind("<ButtonPress>", self.restoreWindow)

        self.minimize_label = Label(self.clos_canv, bg='#1f1f3a', fg="#ffffff", text="-", font=("Arial", 30),
                                    cursor="hand2")
        self.minimize_label.pack(side=RIGHT, padx=7)
        self.minimize_label.bind("<ButtonPress>", self.minimizeWindow)

        # -----------Variables-------------------
        self.var_dep = StringVar(self.root)
        self.var_course = StringVar(self.root)
        self.var_year = StringVar(self.root)
        self.var_semester = StringVar(self.root)
        self.var_std_id = StringVar(self.root)
        self.var_std_name = StringVar(self.root)
        self.var_div = StringVar(self.root)
        self.var_roll = StringVar(self.root)
        self.var_gender = StringVar(self.root)
        self.var_email = StringVar(self.root)
        self.var_mob = StringVar(self.root)
        self.var_address = StringVar(self.root)
        self.var_teacher = StringVar(self.root)

        self.lastClickX = 0
        self.lastClickY = 0

        # This part is image labels setting start
        # first header image  
        img = Image.open(r"./assets\banner.jpg")
        img = img.resize((1366, 100), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img, master=self.root)

        # set image as lable
        f_lb1 = Canvas(self.full_canv, highlightthickness=0, border=0)
        f_lb1.place(x=0, y=30, relwidth=1, relheight=1)
        f_lb1.create_image(0, 0, anchor="nw", image=self.photoimg)

        # backgorund image
        bg1 = Image.open(r"./assets\bg3.jpg")
        bg1 = bg1.resize((1366, 768), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1, master=self.root)

        # set image as lable
        bg_img = Canvas(self.full_canv, highlightthickness=0, border=0)
        bg_img.place(relx=0, y=130, relwidth=1, relheight=1)
        bg_img.create_image(0, 0, anchor="nw", image=self.photobg1)

        # title section
        title_lb1 = Label(bg_img, text="Data Collection Panel", font=("Cambria", 30, "bold"), bg="lavender",
                          fg="#1f1f3a")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Creating Frame 
        main_frame = Frame(bg_img, bd=2, bg="lavender")  # bd mean border
        main_frame.place(x=5, y=55, width=1355, height=510)

        # Left Label Frame 
        left_frame = LabelFrame(main_frame, bd=2, bg="lavender", relief=RIDGE, text="Student Details",
                                font=("verdana", 12, "bold"), fg="navyblue")
        left_frame.place(x=10, y=10, width=660, height=480)

        left_frame = Canvas(left_frame, bd=2, bg="lavender", relief=RIDGE, highlightthickness=0)
        left_frame.place(relx=0, rely=0, relheight=1, relwidth=1)

        # Current Course 
        current_course_frame = LabelFrame(left_frame, bd=2, bg="lavender", relief=RIDGE, text="Current Course",
                                          font=("verdana", 12, "bold"), fg="navyblue")
        current_course_frame.place(x=10, y=5, width=635, height=150)

        # label Department
        dep_label = Label(current_course_frame, text="Department", font=("verdana", 12, "bold"), bg="lavender",
                          fg="navyblue")
        dep_label.grid(row=0, column=0, padx=5, pady=15)

        # combo box
        dep_combo = ttk.Combobox(current_course_frame, textvariable=self.var_dep, width=15,
                                 font=("verdana", 12, "bold"), state="readonly")
        dep_combo["values"] = ("Select Department", "BSCS", "BSIT", "BSENG", "BSPHY", "BSMATH")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        # -----------------------------------------------------

        # label Course
        cou_label = Label(current_course_frame, text="Course", font=("verdana", 12, "bold"), bg="lavender",
                          fg="navyblue")
        cou_label.grid(row=0, column=2, padx=5, pady=15)

        # combo box
        cou_combo = ttk.Combobox(current_course_frame, textvariable=self.var_course, width=15,
                                 font=("verdana", 12, "bold"), state="readonly")
        cou_combo["values"] = (
        "Select Course", "Bsc Software Engineering", "Bsc Computer Technology", "Bsc Information Technology")
        cou_combo.current(1)
        cou_combo.grid(row=0, column=3, padx=5, pady=15, sticky=W)

        # -------------------------------------------------------------

        # label Year
        year_label = Label(current_course_frame, text="Year", font=("verdana", 12, "bold"), bg="lavender",
                           fg="navyblue")
        year_label.grid(row=1, column=0, padx=5, sticky=W)

        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_year, width=15,
                                  font=("verdana", 12, "bold"), state="readonly")
        year_combo["values"] = ("Select Year", "2017-21", "2018-22", "2019-23", "2020-24", "2021-25")
        year_combo.current(2)
        year_combo.grid(row=1, column=1, padx=5, pady=15, sticky=W)

        # -----------------------------------------------------------------

        # label Semester
        year_label = Label(current_course_frame, text="Semester", font=("verdana", 12, "bold"), bg="lavender",
                           fg="navyblue")
        year_label.grid(row=1, column=2, padx=5, sticky=W)

        # combo box
        year_combo = ttk.Combobox(current_course_frame, textvariable=self.var_semester, width=15,
                                  font=("verdana", 12, "bold"), state="readonly")
        year_combo["values"] = (
        "Select Semester", "Semester-1", "Semester-2", "Semester-3", "Semester-4", "Semester-5", "Semester-6",
        "Semester-7", "Semester-8")
        year_combo.current(7)
        year_combo.grid(row=1, column=3, padx=5, pady=15, sticky=W)

        # Class Student Information
        class_Student_frame = LabelFrame(left_frame, bd=2, bg="lavender", relief=RIDGE,
                                         text="Class Student Information", font=("verdana", 12, "bold"), fg="navyblue")
        class_Student_frame.place(x=10, y=160, width=635, height=230)

        # Student id
        studentId_label = Label(class_Student_frame, text="Std-ID:", font=("verdana", 12, "bold"), fg="navyblue",
                                bg="lavender")
        studentId_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        studentId_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_id, width=15,
                                    font=("verdana", 12, "bold"))
        studentId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # Student name
        student_name_label = Label(class_Student_frame, text="Std-Name:", font=("verdana", 12, "bold"), fg="navyblue",
                                   bg="lavender")
        student_name_label.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        student_name_entry = ttk.Entry(class_Student_frame, textvariable=self.var_std_name, width=15,
                                       font=("verdana", 12, "bold"))
        student_name_entry.grid(row=0, column=3, padx=5, pady=5, sticky=W)

        # Class Didvision
        student_div_label = Label(class_Student_frame, text="Class Division:", font=("verdana", 12, "bold"),
                                  fg="navyblue", bg="lavender")
        student_div_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)

        div_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_div, width=13, font=("verdana", 12, "bold"),
                                 state="readonly")
        div_combo["values"] = ("Morning", "Evening")
        div_combo.current(0)
        div_combo.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Roll No
        student_roll_label = Label(class_Student_frame, text="Roll-No:", font=("verdana", 12, "bold"), fg="navyblue",
                                   bg="lavender")
        student_roll_label.grid(row=1, column=2, padx=5, pady=5, sticky=W)

        student_roll_entry = ttk.Entry(class_Student_frame, textvariable=self.var_roll, width=15,
                                       font=("verdana", 12, "bold"))
        student_roll_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # Gender
        student_gender_label = Label(class_Student_frame, text="Gender:", font=("verdana", 12, "bold"), fg="navyblue",
                                     bg="lavender")
        student_gender_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)

        # combo box
        gender_combo = ttk.Combobox(class_Student_frame, textvariable=self.var_gender, width=13,
                                    font=("verdana", 12, "bold"), state="readonly")
        gender_combo["values"] = ("Male", "Female", "Others")
        gender_combo.current(0)
        gender_combo.grid(row=2, column=1, padx=5, pady=5, sticky=W)

        # Email
        student_email_label = Label(class_Student_frame, text="Email:", font=("verdana", 12, "bold"), fg="navyblue",
                                    bg="lavender")
        student_email_label.grid(row=3, column=0, padx=5, pady=5, sticky=W)

        student_email_entry = ttk.Entry(class_Student_frame, textvariable=self.var_email, width=15,
                                        font=("verdana", 12, "bold"))
        student_email_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)

        # Phone Number
        student_mob_label = Label(class_Student_frame, text="Mob-No:", font=("verdana", 12, "bold"), fg="navyblue",
                                  bg="lavender")
        student_mob_label.grid(row=3, column=2, padx=5, pady=5, sticky=W)

        student_mob_entry = ttk.Entry(class_Student_frame, textvariable=self.var_mob, width=15,
                                      font=("verdana", 12, "bold"))
        student_mob_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

        # Address
        student_address_label = Label(class_Student_frame, text="Address:", font=("verdana", 12, "bold"), fg="navyblue",
                                      bg="lavender")
        student_address_label.grid(row=4, column=0, padx=5, pady=5, sticky=W)

        student_address_entry = ttk.Entry(class_Student_frame, textvariable=self.var_address, width=15,
                                          font=("verdana", 12, "bold"))
        student_address_entry.grid(row=4, column=1, padx=5, pady=5, sticky=W)

        # Teacher Name
        student_tutor_label = Label(class_Student_frame, text="Tutor Name:", font=("verdana", 12, "bold"),
                                    fg="navyblue", bg="lavender")
        student_tutor_label.grid(row=4, column=2, padx=5, pady=5, sticky=W)

        student_tutor_entry = ttk.Entry(class_Student_frame, textvariable=self.var_teacher, width=15,
                                        font=("verdana", 12, "bold"))
        student_tutor_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # Button Frame
        btn_frame = Frame(left_frame, bd=2, bg="lavender", relief=RIDGE)
        btn_frame.place(x=10, y=390, width=635, height=60)

        # save button
        save_btn = Button(btn_frame, command=self.add_data, text="Save", width=7, font=("verdana", 12, "bold"),
                          fg="lavender", bg="navyblue")
        save_btn.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        # delete button
        del_btn = Button(btn_frame, command=self.delete_data, text="Delete", width=7, font=("verdana", 12, "bold"),
                         fg="lavender", bg="navyblue")
        del_btn.grid(row=0, column=2, padx=5, pady=10, sticky=W)

        # reset button
        reset_btn = Button(btn_frame, command=self.reset_data, text="Reset", width=7, font=("verdana", 12, "bold"),
                           fg="lavender", bg="navyblue")
        reset_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        take_photo_btn = Button(btn_frame, command=self.generate_dataset, text="Take Pic", width=9,
                                font=("verdana", 12, "bold"), fg="white", bg="navyblue")
        take_photo_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # ----------------------------------------------------------------------
        # Right Label Frame 
        right_frame = LabelFrame(main_frame, bd=2, bg="lavender", relief=RIDGE, text="Student Details",
                                 font=("verdana", 12, "bold"), fg="navyblue")
        right_frame.place(x=680, y=10, width=660, height=480)

        # Searching System in Right Label Frame
        search_frame = LabelFrame(right_frame, bd=2, bg="lavender", relief=RIDGE, text="Search System",
                                  font=("verdana", 12, "bold"), fg="navyblue")
        search_frame.place(x=10, y=5, width=635, height=80)

        # Phone Number
        search_label = Label(search_frame, text="Search:", font=("verdana", 12, "bold"), fg="navyblue", bg="lavender")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        self.var_searchTX = StringVar(self.root)
        # combo box
        search_combo = ttk.Combobox(search_frame, textvariable=self.var_searchTX, width=12,
                                    font=("verdana", 12, "bold"), state="readonly")
        search_combo["values"] = ("Select", "Reg No")
        search_combo.current(1)
        search_combo.grid(row=0, column=1, padx=5, pady=15, sticky=W)

        self.var_search = StringVar(self.root)
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width=12, font=("verdana", 12, "bold"))
        search_entry.grid(row=0, column=2, padx=5, pady=5, sticky=W)

        search_btn = Button(search_frame, command=self.search_data, text="Search", width=9,
                            font=("verdana", 12, "bold"), fg="lavender", bg="navyblue")
        search_btn.grid(row=0, column=3, padx=5, pady=10, sticky=W)

        showAll_btn = Button(search_frame, command=self.fetch_data, text="Show All", width=8,
                             font=("verdana", 12, "bold"), fg="lavender", bg="navyblue")
        showAll_btn.grid(row=0, column=4, padx=5, pady=10, sticky=W)

        # -----------------------------Table Frame-------------------------------------------------
        # Table Frame
        # Searching System in Right Label Frame
        table_frame = Frame(right_frame, bd=2, bg="lavender", relief=RIDGE)
        table_frame.place(x=10, y=90, width=635, height=360)

        # scroll bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        # create table
        self.student_table = ttk.Treeview(table_frame, column=(
        "ID", "Name", "Dep", "Course", "Year", "Sem", "Gender", "Mob-No", "Address", "Roll-No", "Email", "Guardian"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        self.style.configure('Treeview', rowheight=40)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("ID", text="StudentID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Dep", text="Department")
        self.student_table.heading("Course", text="Course")
        self.student_table.heading("Year", text="Year")
        self.student_table.heading("Sem", text="Semester")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Mob-No", text="Mob-No")
        self.student_table.heading("Address", text="Address")
        self.student_table.heading("Roll-No", text="Roll-No")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Guardian", text="Guardian")
        self.student_table["show"] = "headings"

        # Set Width of Colums
        self.student_table.column("ID", width=100)
        self.student_table.column("Name", width=100)
        self.student_table.column("Dep", width=100)
        self.student_table.column("Course", width=100)
        self.student_table.column("Year", width=100)
        self.student_table.column("Sem", width=100)
        self.student_table.column("Gender", width=100)
        self.student_table.column("Mob-No", width=100)
        self.student_table.column("Address", width=100)
        self.student_table.column("Roll-No", width=100)
        self.student_table.column("Email", width=100)
        self.student_table.column("Guardian", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<<TreeviewSelect>>", self.get_cursor)
        # self.student_table.bind("<KeyRelea>",self.get_cursor)
        # self.student_table.bind("<Key-Up>",self.get_cursor)
        self.fetch_data()
        self.clos_canv.bind("<ButtonPress>", self.SaveLastClickPos)
        self.clos_canv.bind("<B1-Motion>", self.dragging)
        self.updateWindow()

    def generate_dataset(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_div.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_croped(img):
                    # conver gary sacle
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # Scaling factor 1.3
                    # Minimum naber 5
                    for (x, y, w, h) in faces:
                        face_croped = img[y:y + h, x:x + w]
                        return face_croped

                cap = cv2.VideoCapture("https://192.168.43.1:8080/video")
                img_id = 0
                imgFoldeName = "_".join(self.var_std_id.get().split("/"))
                print(imgFoldeName, "Ndo hii")
                try:
                    if os.path.exists("facesDataset/" + imgFoldeName):
                        pass
                    else:
                        os.mkdir("facesDataset/" + imgFoldeName)
                except:
                    pass

                while True:
                    ret, my_frame = cap.read()
                    if face_croped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_croped(my_frame), (200, 200))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_path = "facesDataset/" + imgFoldeName + "/" + str(img_id) + ".jpg"
                        cv2.imwrite(file_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Capture Images", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

            except:
                pass

    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_std_id.set(data[0]),
        self.var_std_name.set(data[1]),
        self.var_dep.set(data[2]),
        self.var_course.set(data[3]),
        self.var_year.set(data[4]),
        self.var_semester.set(data[5]),
        self.var_gender.set(data[6]),
        self.var_mob.set(data[7]),
        self.var_address.set(data[8]),
        self.var_roll.set(str(data[9])),
        self.var_email.set(data[10]),
        self.var_teacher.set(data[11]),

    # ==================Function Decleration==============================
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_course.get == "Select Course" or self.var_year.get() == "Select Year" or self.var_semester.get() == "Select Semester" or self.var_std_id.get() == "" or self.var_std_name.get() == "" or self.var_roll.get() == "" or self.var_gender.get() == "" or self.var_email.get() == "" or self.var_mob.get() == "" or self.var_address.get() == "" or self.var_teacher.get() == "":
            messagebox.showerror("Error", "Please Fill All Fields are Required!", parent=self.root)
        else:
            try:
                conn = DbConnection()
                conn.addStudent(self.var_std_id.get(),
                                self.var_std_name.get(),
                                self.var_dep.get(),
                                self.var_course.get(),
                                self.var_year.get(),
                                self.var_semester.get(),
                                self.var_gender.get(),
                                self.var_mob.get(),
                                self.var_address.get(),
                                self.var_roll.get(),
                                self.var_email.get(),
                                self.var_teacher.get())
                self.fetch_data()
                messagebox.showinfo("Success", "All Records are Saved!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

    # ===========================Fetch data form database to table ================================

    def fetch_data(self):
        conn = DbRetrieve()
        data = conn.getAllStudents()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)

    # ==============================Delete Function=========================================
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "Student Id Must be Required!", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to Delete?", parent=self.root)
                if delete > 0:
                    conn = DbConnection()
                    conn.delete(self.var_std_id.get())
                else:
                    if not delete:
                        return
                self.fetch_data()
                messagebox.showinfo("Delete", "Successfully Deleted!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)

                # Reset Function

    def reset_data(self):
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.var_div.set("Morning"),
        self.var_gender.set("Male"),
        self.var_mob.set(""),
        self.var_address.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),
        self.var_teacher.set(""),

    # ===========================Search Data===================
    def search_data(self):
        if self.var_search.get() == "" or self.var_searchTX.get() == "Select":
            messagebox.showerror("Error", "Select Combo option and enter entry box", parent=self.root)
        else:
            try:
                conn = DbRetrieve()
                rows = conn.searchStudenWithRegNo(self.var_search.get())
                print(rows)
                if len(rows) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in rows:
                        self.student_table.insert("", END, values=i)
                    if rows == None:
                        messagebox.showerror("Error", "Data Not Found", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    def updateWindow(self):
        try:
            if self.root.state() == "normal":
                self.root.wm_overrideredirect(1)
        except:
            pass
        self.root.after(100, self.updateWindow)

    def minimizeWindow(self, event):
        self.root.overrideredirect(0)
        self.root.iconify()

    def restoreWindow(self, event):
        if self.root.attributes('-fullscreen'):
            self.root.overrideredirect(1)
            self.root.attributes("-fullscreen", 0)
            self.rest_label.configure(text="1")
        else:
            self.root.overrideredirect(0)
            self.root.attributes("-fullscreen", 1)
            self.rest_label.configure(text="2")

    # To enable Drag Functionality

    def SaveLastClickPos(self, event):
        self.lastClickX = event.x
        self.lastClickY = event.y

    def dragging(self, event):
        x, y = event.x - self.lastClickX + self.root.winfo_x(), event.y - self.lastClickY + self.root.winfo_y()
        self.root.geometry("+%s+%s" % (x, y))


# main class object
def show():
    root = Tk()
    obj = Student(root)

    root.mainloop()


#show()
