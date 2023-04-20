import tkinter as tk
from tkinter import messagebox, font, filedialog, PhotoImage, ttk, BitmapImage
import tkinter.ttk as ttk
import ttkthemes as ttkh
APP_MAIN = ttkh.ThemedTk()
APP_MAIN.geometry("900x530")
APP_MAIN.wm_resizable(width=1, height=1)
APP_MAIN.title("RoXpeed Downloader Build 1.0.0")
APP_MAIN.wm_iconbitmap('assets/ico.ico')

APP_MAIN.set_theme('clam')

app_main_menu = tk.Menu(APP_MAIN)

menu_tasks = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan', fg='bisque')
menu_downloads = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan',
                         fg='bisque')
menu_queue = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan', fg='bisque')
menu_category = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan',
                        fg='bisque')
menu_view = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan', fg='bisque')
menu_help = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan', fg='bisque')
menu_settings = tk.Menu(app_main_menu, font=("Raleway", 10), tearoff=False, bg='#2B2B2B', selectcolor='cyan',
                        fg='bisque')

app_main_menu.add_cascade(label='Initiate Tasks', menu=menu_tasks)
app_main_menu.add_cascade(label='File Settings', menu=menu_settings)
app_main_menu.add_cascade(label='Downloads', menu=menu_downloads)
app_main_menu.add_cascade(label='Scheduler', menu=menu_queue)
app_main_menu.add_cascade(label='Category', menu=menu_category)
app_main_menu.add_cascade(label='View', menu=menu_view)
app_main_menu.add_cascade(label='Help', menu=menu_help)

# Downloads Dropdown
menu_downloads.add_command(label='Paste url', accelerator='Ctrl+V')
menu_downloads.add_command(label='Re-download', accelerator='Ctrl+Alt+R')
menu_downloads.add_separator()
menu_downloads.add_separator()
menu_downloads.add_command(label='Pause', accelerator='Ctrl+P')
menu_downloads.add_command(label='Pause All', accelerator='Ctrl+Alt+P')
menu_downloads.add_separator()
menu_downloads.add_separator()
menu_downloads.add_command(label='Resume All', accelerator='Ctrl+Shift+Space')
menu_downloads.add_command(label='Resume', accelerator='Ctrl+Space')
menu_downloads.add_separator()
menu_downloads.add_separator()
menu_downloads.add_command(label='Stop', accelerator='Ctrl+Q')
menu_downloads.add_command(label='Stop All', accelerator='Ctrl+Shift+Q')
menu_downloads.add_separator()
menu_downloads.add_command(label='Delete', accelerator='Ctrl+Del')
menu_downloads.add_command(label='Delete All', accelerator='Ctrl+Alt+Del')

# Settings Dropdown
menu_settings.add_checkbutton(label='Multi-Downloading', accelerator='Ctrl+Alt+T')
menu_settings.add_checkbutton(label='Use proxies', accelerator='Ctrl+Q')
menu_settings.add_separator()
menu_settings.add_separator()
menu_settings.add_command(label='Tweak defaults', accelerator='Ctrl+T')
menu_settings.add_command(label='Change Saving Folder', accelerator='Ctrl+S')
menu_settings.add_separator()
menu_settings.add_command(label='Quit', accelerator='Ctrl+Q')

# View Dropdown
menu_view.add_command(label='Full Download History', accelerator='Ctrl+Alt+H')
menu_view.add_command(label='Completed Downloads', accelerator='Ctrl+Shift+C')
menu_view.add_command(label='Interrupted Downloads', accelerator='Ctrl+I')
menu_view.add_separator()
menu_view.add_separator()
menu_view.add_command(label='Queues', accelerator='Shift+U')
menu_view.add_separator()
menu_view.add_command(label='Compiled tweaks', accelerator='Ctrl+Alt+C')
menu_view.add_command(label='Browser Grabber', accelerator='Shift+G')

# Help Dropdown
menu_help.add_command(label='Help', accelerator='Ctrl+H')
menu_help.add_command(label='About', accelerator='Alt+A')

# Tasks Dropdown
menu_tasks.add_command(label='Add New Download', accelerator='Ctrl+N')
menu_tasks.add_command(label='Add Batch from Clipboard', accelerator='Alt+C')
menu_tasks.add_command(label='Add from Clipboard', accelerator='Ctrl+I')
menu_tasks.add_command(label='Halt All', accelerator='Ctrl+Alt+Q')
menu_tasks.add_separator()
menu_tasks.add_command(label='Exit', accelerator='Ctrl+Q')

# Queue Dropdown
menu_queue.add_command(label='Enqueue', accelerator='Ctrl+Enter')
menu_queue.add_command(label='Enqueue Batch from Clipboard', accelerator='Alt+Enter')
menu_queue.add_separator()
menu_queue.add_separator()
menu_queue.add_command(label='Dequeue', accelerator='Ctrl+D')
menu_queue.add_command(label='Dequeue All', accelerator='Ctrl+Shift+D')
menu_queue.add_separator()
menu_queue.add_command(label='Start Queue', accelerator='Ctrl+Space+Alt')
menu_queue.add_command(label='Stop Queue', accelerator='Ctrl+S+Space')

# Category Dropdown
menu_category.add_radiobutton(label='Grouped')
menu_category.add_radiobutton(label='Compressed')
menu_category.add_radiobutton(label='Video')
menu_category.add_radiobutton(label='Documents')
menu_category.add_radiobutton(label='Programs')
menu_category.add_radiobutton(label='Others')
im = PhotoImage(file='assets/Tpp.png')

MAIN_FRAME = tk.Frame(APP_MAIN, bg='grey')
MAIN_FRAME.place(relwidth=0.99, relheight=0.99, relx=0.005, rely=0.005)

APP_BANNER = tk.Label(MAIN_FRAME, text='RoXpeed Downloader', image=im, bg='grey', fg='#3B4B2E', compound=tk.LEFT,
                      font=("Algerian", 18))
APP_BANNER.pack(side=tk.RIGHT, anchor=tk.NE, padx=30)

APP_INFO = tk.Label(MAIN_FRAME, text='Download files and videos from the internet including youtube videos/audio and '
                                     'other files as well and at a high speed', wrap=450, bg='grey', fg='indigo',
                    compound=tk.LEFT, font=("Raleway", 11))
APP_INFO.pack(side=tk.LEFT, anchor=tk.NW, padx=15, pady=20)

FRAME_TABS = tk.Frame(MAIN_FRAME, bg='grey')
FRAME_TABS.place(rely=0.17, relheight=0.83, relwidth=1)

FRAME_TABS1 = tk.Frame(FRAME_TABS, bg='silver')
FRAME_TABS1.place(rely=0.005, relheight=0.99, relwidth=0.995, relx=0.0025)

DOWNLOADER_NOTEBOOK = ttk.Notebook(FRAME_TABS1)

FRAME_FILES = tk.Frame(DOWNLOADER_NOTEBOOK, bg='#2B2B2B')
FRAME_FILES.place(relwidth=1, relheight=1)

FRAME_YOUTUBE = tk.Frame(DOWNLOADER_NOTEBOOK, bg='#2B2B2B')

frame_ytb_left = tk.Frame(FRAME_YOUTUBE, bg='grey')
imy = PhotoImage(file='assets/ytb10.png')
imy1 = PhotoImage(file='assets/view3.png')
lbl_img_ytb = tk.Label(frame_ytb_left, image=imy, bg='grey')
lbl_img_ytb.pack(side=tk.TOP)

lbl0 = tk.Label(frame_ytb_left, text="Paste Url", fg='black', bg='grey')
lbl0.place(y=80, x=2)

txtpasteyt = tk.Entry(frame_ytb_left, font=("Raleway", 11), fg='maroon', bg='beige')
txtpasteyt.place(y=78, x=65, relwidth=0.7)

FRMT = tk.StringVar()

cmbformat = ttk.Menubutton(frame_ytb_left, textvariable=FRMT, compound=tk.RIGHT)
formatmenu = tk.Menu(cmbformat, tearoff=0)
cmbformat['menu'] = formatmenu
alignments = ['MKV 720p', 'MP3', 'MP4 1020p']
for text in alignments:
    formatmenu.add_radiobutton(label=text, variable=FRMT, value=text, indicatoron=1)
cmbformat.place(y=105, x=10, relwidth=0.70)

btntest = tk.Button(frame_ytb_left, image=imy1, activeforeground='lime', compound=tk.LEFT, activebackground='#2F2B2E',
                    relief=tk.FLAT, fg='black', text="Check", bg='beige')
btntest.place(y=103, relx=0.76)

lbltitle = tk.Label(frame_ytb_left, text="Title", fg='#2B2B2B', bg='grey')
lbltitle.place(y=132, x=2)
lbltitleans = tk.Label(frame_ytb_left, text="Me at the zoo", fg='maroon', bg='grey')
lbltitleans.place(y=132, x=65)

lblviews = tk.Label(frame_ytb_left, text="Views", fg='#2B2B2B', bg='grey')
lblviews.place(y=155, x=2)
lblviewsans = tk.Label(frame_ytb_left, text="106602383", fg='maroon', bg='grey')
lblviewsans.place(y=155, x=65)

lblPublished = tk.Label(frame_ytb_left, text="Published", fg='#2B2B2B', bg='grey')
lblPublished.place(y=180, x=2)
lblPublishedans = tk.Label(frame_ytb_left, text="23/04/2005", fg='maroon', bg='grey')
lblPublishedans.place(y=180, x=65)

lblDuraton = tk.Label(frame_ytb_left, text="Duration", fg='#2B2B2B', bg='grey')
lblDuraton.place(y=205, x=2)
lblDuratonans = tk.Label(frame_ytb_left, text="0:18", fg='maroon', bg='grey')
lblDuratonans.place(y=205, x=65)

lblLikes = tk.Label(frame_ytb_left, text="Likes", fg='#2B2B2B', bg='grey')
lblLikes.place(y=230, x=2)
lblLikesans = tk.Label(frame_ytb_left, text="3825489", fg='maroon', bg='grey')
lblLikesans.place(y=230, x=65)

lblType = tk.Label(frame_ytb_left, text="Format", fg='#2B2B2B', bg='grey')
lblType.place(y=255, x=2)
lblTypeans = tk.Label(frame_ytb_left, text="Video/MP4", fg='maroon', bg='grey')
lblTypeans.place(y=255, x=65)

lblSize = tk.Label(frame_ytb_left, text="Size", fg='#2B2B2B', bg='grey')
lblSize.place(y=280, x=2)
lblSizeans = tk.Label(frame_ytb_left, text="100 Mb", fg='maroon', bg='grey')
lblSizeans.place(y=280, x=65)

lblchanel = tk.Label(frame_ytb_left, text="Channel", fg='#2B2B2B', bg='grey')
lblchanel.place(y=305, x=2)
lblchanelans = tk.Label(frame_ytb_left, text="WWE Forever", fg='maroon', bg='grey')
lblchanelans.place(y=305, x=65)

lblUrl = tk.Label(frame_ytb_left, text="Url", fg='#2B2B2B', bg='grey')
lblUrl.place(y=330, x=2)
lblUrlans = tk.Label(frame_ytb_left, text="https://www.youtube.com/channel/UC4QobU6STFB0P71PMvOGN5A", wrap=200,
                     fg='maroon', bg='grey')
lblUrlans.place(y=330, x=65)

imgstat = PhotoImage(file='assets/download.png')
imgpause = PhotoImage(file='assets/pause.png')
imgcancel = PhotoImage(file='assets/cancel.png')

frame_ytb_left.place(relheight=1, relwidth=0.3)

frame_ytb_right = tk.Frame(FRAME_YOUTUBE, bg='grey')
frame_ytb_right.place(relheight=1, relwidth=0.7, relx=0.3)

YT_DOWNLOADS_NOTEBOOK = ttk.Notebook(frame_ytb_right)

frame_downloads_yt = tk.Frame(YT_DOWNLOADS_NOTEBOOK, bg='silver')
frame_downloads_yt.pack(fill=tk.BOTH)

YT_DOWNLOADS_NOTEBOOK.add(frame_downloads_yt, image=imy1, compound=tk.LEFT, text="Downloads")
YT_DOWNLOADS_NOTEBOOK.place(relwidth=0.995, relheight=0.99, relx=0.0025, rely=0.005)

YT_TREEVIEW = ttk.Treeview(frame_downloads_yt, columns=(0, 1, 2, 3, 4, 5, 6), displaycolumns='#all')
YT_TREEVIEW.place(relwidth=0.995, relheight=0.92, relx=0.0025, y=40)

YT_TREEVIEW.heading('#0', text="Id")
YT_TREEVIEW.heading(0, text="Title")
YT_TREEVIEW.heading(1, text="Queue")
YT_TREEVIEW.heading(2, text="Last Try")
YT_TREEVIEW.heading(3, text="Status")
YT_TREEVIEW.heading(4, text="Size")
YT_TREEVIEW.heading(5, text="Speed")
YT_TREEVIEW.heading(6, text="Category")

try:
    for row in range(0, 50):
        YT_TREEVIEW.insert('', row, text=row + 1)
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=0, value='Drake-Do you Love me.mkv')
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=1, value=(row % 9) * (96 - row))
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=2, value='12/08/2020')
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=3, value='Complete')
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=4, value='100 Mb')
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=5, value='324kb/s')
        YT_TREEVIEW.set(YT_TREEVIEW.get_children()[row], column=6, value='Video')

except:
    pass

# print(YT_TREEVIEW.get_children())


YT_TREEVIEW.column('#0', width=55)
YT_TREEVIEW.column(0, width=180)
YT_TREEVIEW.column(1, width=45)
YT_TREEVIEW.column(2, width=70)
YT_TREEVIEW.column(3, width=60)
YT_TREEVIEW.column(4, width=50)
YT_TREEVIEW.column(5, width=50)
YT_TREEVIEW.column(6, width=100)

btndownloadyt = tk.Button(frame_downloads_yt, image=imgstat, activeforeground='lime', compound=tk.LEFT,
                          activebackground='#2F2B2E',
                          relief=tk.FLAT, text="Start", bg='beige')
btndownloadyt.place(y=10, x=12)

btnpauseyt = tk.Button(frame_downloads_yt, image=imgpause, activeforeground='green', compound=tk.LEFT,
                       activebackground='#2F2B2E',
                       relief=tk.FLAT, text="Pause", bg='beige')
btnpauseyt.place(y=10, x=95)

btncancelyt = tk.Button(frame_downloads_yt, image=imgcancel, activeforeground='red', compound=tk.LEFT,
                        activebackground='#2F2B2E',
                        relief=tk.FLAT, text="Cancel", bg='beige')
btncancelyt.place(y=10, x=175)

FRAME_YOUTUBE.place(relwidth=1, relheight=1)

im1 = PhotoImage(file='assets/ytb3.png')
im2 = PhotoImage(file='assets/goo1.png')

DOWNLOADER_NOTEBOOK.add(FRAME_YOUTUBE, text="Youtube Download")
DOWNLOADER_NOTEBOOK.add(FRAME_FILES, text="Other Files Download")
DOWNLOADER_NOTEBOOK.place(relwidth=0.995, relheight=0.99, relx=0.0025, rely=0.005)
DOWNLOADER_NOTEBOOK.tab(tab_id=0, image=im1, compound=tk.LEFT)
DOWNLOADER_NOTEBOOK.tab(tab_id=1, image=im2, compound=tk.LEFT)

scroll_bar1 = ttk.Scrollbar(YT_TREEVIEW, orient='vertical')
scroll_bar1.pack(side=tk.RIGHT, fill=tk.Y)
scroll_bar1.config(command=YT_TREEVIEW.yview)
YT_TREEVIEW.configure(yscrollcommand=scroll_bar1.set)

scroll_bar2 = ttk.Scrollbar(YT_TREEVIEW, orient='horizontal')
scroll_bar2.pack(side=tk.BOTTOM, fill=tk.X)
scroll_bar2.config(command=YT_TREEVIEW.xview)
YT_TREEVIEW.configure(xscrollcommand=scroll_bar2.set)


def popUpMenu(event=None):
    # print(YT_TREEVIEW.identify(component='item',x=event.x_root, y=event.y_root))
    # print(YT_TREEVIEW.selection())
    YT_TREEVIEW.selection_add(YT_TREEVIEW.identify(component='item', x=event.x, y=event.y))
    popup = tk.Menu(app_main_menu, font=("Arial", 9), tearoff=False, bg='beige', fg='#2B2B2B')
    popup.add_command(label='Resume')
    popup.add_separator()
    popup.add_command(label='Stop')
    popup.add_separator()
    popup.add_command(label='Start')
    popup.add_separator()
    popup.add_command(label='Re-download')
    popup.add_separator()
    popup.add_command(label='Open')
    popup.add_separator()
    popup.add_command(label='Reload Url')
    popup.add_separator()
    popup.add_command(label='Move/Rename')
    popup.add_separator()
    popup.add_command(label='Remove from queue')
    popup.add_separator()
    popup.add_command(label='Delete')
    popup.add_separator()
    popup.add_command(label='Properties')

    popup.post(event.x_root, event.y_root)


YT_TREEVIEW.bind("<Button-3>", popUpMenu)

APP_MAIN.tk_setPalette('#fff')
APP_MAIN.config(menu=app_main_menu)
APP_MAIN.mainloop()
