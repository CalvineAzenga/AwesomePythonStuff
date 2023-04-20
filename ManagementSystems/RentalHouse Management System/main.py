from tkinter import Label, Menubutton, Tk, Canvas, ttk, PhotoImage
from win32api import GetSystemMetrics
from PIL import Image, ImageTk
from matplotlib import figure, pyplot
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandas import DataFrame
import random
# from tkinter import font


root=Tk()
style=ttk.Style(root)

# style.theme_use('clam')
# print(font.families())
width=int(GetSystemMetrics(0)/1.15)
height=int(GetSystemMetrics(1)/1.05)
pos_x=int((GetSystemMetrics(0)-width)/2)
pos_y=int((GetSystemMetrics(1)-height)/2)
root.geometry(f"{width}x{height}+{pos_x}+{pos_y}")
root.wm_resizable(0,0)
root.overrideredirect(1)
root.wm_attributes("-topmost",1)

style=ttk.Style()
style.configure("TMenubutton",font=("Verdana",12),foreground='#2b2b2b')

background_img=Image.open("./images/HomeBackground.gif")
background_img=background_img.resize((width,height), Image.ANTIALIAS)
background_img=ImageTk.PhotoImage(background_img,master=root)

brown_img=Image.open("./images/HomeBackground.gif")
brown_img=brown_img.resize((300,100), Image.ANTIALIAS)
brown_img=ImageTk.PhotoImage(brown_img,master=root)

appbar_img=Image.open("./images/FOOTER.gif")
appbar_img=appbar_img.resize((width,int(height/9)), Image.ANTIALIAS)
appbar_img=ImageTk.PhotoImage(appbar_img,master=root)

green_img=Image.open("./images/FOOTER.gif")
green_img=green_img.resize((500,100), Image.ANTIALIAS)
green_img=ImageTk.PhotoImage(green_img,master=root)

back_canvas=Canvas(root)
back_canvas.place(relx=0,rely=0,relwidth=1,relheight=1)
back_canvas.create_image(0,0,anchor='nw',image=background_img)

logout_img=PhotoImage(file='./images/logout.png')

appbar=Canvas(back_canvas,highlightthickness=0)
appbar.place(relx=0,rely=0,relwidth=1,relheight=0.1)
appbar.create_image(0,0,anchor='nw',image=appbar_img)

appname_lbl=ttk.Label(appbar,text='Eastern Apartments MS',font=("Lucida Calligraphy",24),image=green_img,compound='center',background='#338033',foreground='orange')
appname_lbl.pack(side='top')

close_lbl=ttk.Label(appbar,text="X",font=("Bahnschrift Light SemiCondensed",18),foreground='beige',cursor='hand2',background='#338033',image=green_img,compound='center')
close_lbl.place(relx=0.95,rely=0.2,relheight=0.6,relwidth=0.05)

minimize_lbl=ttk.Label(appbar,text="__\n",font=("Bahnschrift Light SemiCondensed",14),foreground='beige',cursor='hand2',background='#338033',image=green_img,compound='center')
minimize_lbl.place(relx=0.899,rely=0.2,relheight=0.6,relwidth=0.05)


menubar=ttk.Label(root)
menubar.place(relx=0,rely=0.1,relwidth=1,relheight=0.04)

# home_menu_btn=Menubutton(menubar,text="Home",font=("Bahnschrift Light SemiCondensed",14),cursor='hand2')
# home_menu_btn.pack(side='left')

admin_menu_btn=ttk.Menubutton(menubar,text="Admin",cursor='hand2')
admin_menu_btn.pack(side='left')

caretaker_menu_btn=ttk.Menubutton(menubar,text="Care Taker",cursor='hand2')
caretaker_menu_btn.pack(side='left')

tenants_menu_btn=ttk.Menubutton(menubar,text="Tenants",cursor='hand2')
tenants_menu_btn.pack(side='left')

# Dashboard Area

dashboard=Canvas(root)
dashboard.place(relx=0,rely=0.14,relwidth=1,relheight=0.86)
dashboard.create_image(0,0,anchor='nw',image=background_img)

logout_lbl=ttk.Label(dashboard,background='#CC8066',image=logout_img,compound='center',cursor='hand2')
logout_lbl.pack(side='right',anchor='nw',pady=30,padx=10)

user_lbl=Label(dashboard,background='beige',text='Session User: Chege Mwangi',foreground='#214665',justify='left',font=("Bahnschrift Light SemiCondensed",14),border=5,relief='groove')
user_lbl.place(relx=0.01,rely=0.05)

numbers_canvas=Canvas(dashboard,highlightthickness=0)
numbers_canvas.place(relx=0.009,rely=0.15,relwidth=0.35,relheight=0.83)
numbers_canvas.create_image(0,0,anchor='nw',image=background_img)

active_tenants=Label(numbers_canvas,text="Total Tenants",background='#338033',foreground='beige',font=("Bahnschrift Light SemiCondensed",14),border=4,relief='groove')
active_tenants.place(relx=0.01,rely=0.01,relwidth=0.43,relheight=0.31)

totaldebts_tenants=Label(numbers_canvas,text="Total Debts",background='#551A8B',foreground='beige',font=("Bahnschrift Light SemiCondensed",14),border=4,relief='groove')
totaldebts_tenants.place(relx=0.48,rely=0.01,relwidth=0.43,relheight=0.31)

t_rooms=Label(numbers_canvas,text="Total Rooms",background='#FFCD42',foreground='black',font=("Bahnschrift Light SemiCondensed",14),border=4,relief='groove')
t_rooms.place(relx=0.01,rely=0.34,relwidth=0.43,relheight=0.31)

empty_rooms=Label(numbers_canvas,text="Empty Rooms",background='#007ACC',foreground='beige',font=("Bahnschrift Light SemiCondensed",14),border=4,relief='groove')
empty_rooms.place(relx=0.48,rely=0.34,relwidth=0.43,relheight=0.31)

t_workers=Label(numbers_canvas,text="Total Workers",background='#9EC862',foreground='black',font=("Bahnschrift Light SemiCondensed",14),border=4,relief='groove')
t_workers.place(relx=0.01,rely=0.68,relwidth=0.43,relheight=0.31)

p_bills=Label(numbers_canvas,text="Pending Bills",background='#FF7F0E',foreground='beige',font=("Bahnschrift Light SemiCondensed",14),border=4,relief='groove')
p_bills.place(relx=0.48,rely=0.68,relwidth=0.43,relheight=0.31)

chart_canvas=Canvas(dashboard,highlightthickness=0)
chart_canvas.place(relx=0.359,rely=0.15,relwidth=0.63,relheight=0.83)
chart_canvas.create_image(0,0,anchor='nw',image=background_img)

month_checkins=Label(chart_canvas,text="64 registered tenants this month in 26 rooms",background='#323233',foreground='beige',font=("Bahnschrift Light SemiCondensed",14,'bold'),border=4,relief='groove')
month_checkins.place(relx=0,rely=0,relheight=0.1)

chart_canvas_real=Canvas(chart_canvas,highlightthickness=0)
chart_canvas_real.place(relx=0,rely=0.2,relwidth=1,relheight=0.79)
chart_canvas_real.create_image(0,0,anchor='nw',image=background_img)

data1 = {'Month': ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC'],
                 'Customers': [random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500),random.randint(0,500)]}
df1 = DataFrame(data1, columns=['Month', 'Customers'])

figure1 = Figure(facecolor="beige")
pyplot.rcParams.update({'font.size': 8})

# print(pyplot.rcParams.keys())
ax1 = figure1.add_subplot(111)

bar1 = FigureCanvasTkAgg(figure1, chart_canvas_real)
bar1.get_tk_widget().place(relx=0,rely=0,relwidth=1,relheight=1)
df1 = df1[['Month', 'Customers']].groupby('Month').sum()
df1.plot(kind='bar', legend=True, ax=ax1)
ax1.tick_params(axis='x', labelrotation=20)
ax1.set_title('Income Per Month this year')

# resizer=ttk.Sizegrip(root).pack(side='bottom',anchor='se')

try:
    lastClickX = 0
    lastClickY = 0

    def save_last_pos(event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y

    def dragging(event):
        x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+{0}+{1}".format(x, y))

    appbar.bind('<Button-1>', save_last_pos)
    appbar.bind('<B1-Motion>', dragging)
    appname_lbl.bind('<Button-1>', save_last_pos)
    appname_lbl.bind('<B1-Motion>', dragging)
    def minimize_window(event):
        root.wm_state('withdrawn')
        root.overrideredirect(0)
        root.iconify()

    def show_windoww():
        if  root.state() == 'normal':
            root.overrideredirect(1)
        root.after(1, show_windoww)
    show_windoww()
    close_lbl.bind("<ButtonPress>",lambda event:root.destroy())
    minimize_lbl.bind("<ButtonPress>",minimize_window)
except:
    pass

root.mainloop()