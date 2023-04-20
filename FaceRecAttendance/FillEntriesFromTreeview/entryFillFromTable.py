from tkinter import Canvas, Entry, Label,Tk,ttk
import tkinter as tk
import sqlite3

window=Tk()
window.geometry("800x600")
window.title("")
window.attributes("-toolwindow",1)
mainCanvas=Canvas(window)
mainCanvas.pack(side="left",fill="both",expand=True)

style=ttk.Style(window)
style.theme_use("clam")

topCanvas=Canvas(mainCanvas,background="silver",highlightthickness=0)
topCanvas.place(relx=0,rely=0,relwidth=1,relheight=0.3)

# Labels for Entries and Entries
lblName=Label(topCanvas,text="Name",background="silver",foreground="maroon",font=("Raleway",12,"bold"))
lblName.grid(row=0,column=0,padx=10,pady=10,sticky="w")

entryName=ttk.Entry(topCanvas,font=("Raleway",12))
entryName.grid(row=0,column=1,padx=10,pady=10,sticky="w")

lblDepartment=Label(topCanvas,text="Department",background="silver",foreground="maroon",font=("Raleway",12,"bold"))
lblDepartment.grid(row=1,column=0,padx=10,pady=10,sticky="w")

entryDepartment=ttk.Entry(topCanvas,font=("Raleway",12))
entryDepartment.grid(row=1,column=1,padx=10,pady=10,sticky="w")

lblCourse=Label(topCanvas,text="Course",background="silver",foreground="maroon",font=("Raleway",12,"bold"))
lblCourse.grid(row=2,column=0,padx=10,pady=10,sticky="w")

entryCourse=ttk.Entry(topCanvas,font=("Raleway",12))
entryCourse.grid(row=2,column=1,padx=10,pady=10,sticky="w")

lblYear=Label(topCanvas,text="Year",background="silver",foreground="maroon",font=("Raleway",12,"bold"))
lblYear.grid(row=0,column=2,padx=10,pady=10,sticky="w")

entryYear=ttk.Entry(topCanvas,font=("Raleway",12))
entryYear.grid(row=0,column=3,padx=10,pady=10,sticky="w")

lblSemester=Label(topCanvas,text="Semester",background="silver",foreground="maroon",font=("Raleway",12,"bold"))
lblSemester.grid(row=1,column=2,padx=10,pady=10,sticky="w")

entrySemester=ttk.Entry(topCanvas,font=("Raleway",12))
entrySemester.grid(row=1,column=3,padx=10,pady=10,sticky="w")

lblGender=Label(topCanvas,text="Gender",background="silver",foreground="maroon",font=("Raleway",12,"bold"))
lblGender.grid(row=2,column=2,padx=10,pady=10,sticky="w")

entryGender=ttk.Entry(topCanvas,font=("Raleway",12))
entryGender.grid(row=2,column=3,padx=10,pady=10,sticky="w")


tableCanvas=Canvas(mainCanvas,background="beige",highlightthickness=0)
tableCanvas.place(relx=0,rely=0.3,relwidth=1,relheight=0.7)

#scroll bar 
scroll_x = ttk.Scrollbar(tableCanvas,orient=tk.HORIZONTAL)
scroll_y = ttk.Scrollbar(tableCanvas,orient=tk.VERTICAL)

table=ttk.Treeview(tableCanvas,column=("Name","Dep","Course","Year","Sem","Gender"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

table.heading("Name",text="Name")
table.heading("Dep",text="Department")
table.heading("Course",text="Course")
table.heading("Year",text="Year")
table.heading("Sem",text="Semester")
table.heading("Gender",text="Gender")

table["show"]="headings"


# Set Width of Colums 
table.column("Name",width=100)
table.column("Dep",width=100)
table.column("Course",width=100)
table.column("Year",width=100)
table.column("Sem",width=100)
table.column("Gender",width=100)


scroll_x.pack(side=tk.BOTTOM,fill=tk.X)
scroll_y.pack(side=tk.RIGHT,fill=tk.Y)
scroll_x.config(command=table.xview)
scroll_y.config(command=table.yview)

def fillEntries(event):
        cursor_focus = table.focus()
        content = table.item(cursor_focus)
        data = content["values"] # List of values of the selected row

        name=data[0]
        department=data[1]
        course=data[2]
        year=data[3]
        semester=data[4]
        gender=data[5]
        
        # Clear all entries First
        entryName.delete(0,tk.END)
        entryDepartment.delete(0,tk.END)
        entryCourse.delete(0,tk.END)
        entryYear.delete(0,tk.END)
        entrySemester.delete(0,tk.END)
        entryGender.delete(0,tk.END)

        # Insert The data into entries
        entryName.insert(0,name)
        entryDepartment.insert(0,department)
        entryCourse.insert(0,course)
        entryYear.insert(0,year)
        entrySemester.insert(0,semester)
        entryGender.insert(0,gender)

        
table.pack(fill=tk.BOTH,expand=1)

table.bind("<<TreeviewSelect>>",fillEntries) # Important, fill entrty boxes on every selection change of the treeview



# Sample Data inserted into table

connection=sqlite3.connect("./faceRecDB.db")
cursor=connection.cursor()
cursor.execute("SELECT fullname,department,course,admYear,semester,gender FROM studentz")
results=cursor.fetchall()
for row in results:
    table.insert("",tk.END,values=row)

window.mainloop()