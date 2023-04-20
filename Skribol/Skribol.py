import tkinter as tk
from tkinter import font, colorchooser, filedialog, messagebox
from tkinter import ttk
import os
import threading

app_main = tk.Tk()
app_main.geometry('1200x710')
app_main.title('Skribol Text Editor')
app_main.configure(background='#2B2B2B')
app_main.wm_iconbitmap('ico.ico')


########################################## Main Menu start ########################################
main_menu = tk.Menu(app_main)
# File icons
new_icon = tk.PhotoImage(file='assets/filenew.png')
open_icon = tk.PhotoImage(file='assets/fileopen.png')
save_icon = tk.PhotoImage(file='assets/filesave.png')
save_as_icon = tk.PhotoImage(file='assets/filesaveas.png')
exit_icon = tk.PhotoImage(file='assets/exit.png')

file = tk.Menu(main_menu, tearoff=False)

# Edit
# edit icons
copy_icon = tk.PhotoImage(file='assets/editcopy.png')
paste_icon = tk.PhotoImage(file='assets/editpaste.png')
cut_icon = tk.PhotoImage(file='assets/editcut.png')
clear_icon = tk.PhotoImage(file='assets/history_clear.png')
find_icon = tk.PhotoImage(file='assets/searchreplace.png')

edit = tk.Menu(main_menu, tearoff=False)

##### view icons
tool_bar_icon = tk.PhotoImage(file='assets/attributebar41.png')
status_bar_icon = tk.PhotoImage(file='assets/attributebar51.png')

view = tk.Menu(main_menu, tearoff=False)

# Color theme
light_default_icon = tk.PhotoImage(file='assets/pointblue.png')
blue_theme_icon = tk.PhotoImage(file='assets/pointblue.png')
red_theme_icon = tk.PhotoImage(file='assets/pointred.png')
dark_theme_icon = tk.PhotoImage(file='assets/pointblack.png')

color_theme = tk.Menu(main_menu, tearoff=False)

theme_choice = tk.StringVar()
color_icons = (light_default_icon, blue_theme_icon, red_theme_icon, dark_theme_icon)

color_dict = {
    'Light theme': ('black', 'beige'),
    'Blue theme': ('red', '#669B9B'),
    'Red theme': ('lime', '#3F0000'),
    'Dark theme': ('#80FFFF', '#2B2B2B'),
}

# cascade
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color theme', menu=color_theme)

# -------------------------------------------%%%%End main menu%%%%%%%-------------------

########################################## ToolBar start ########################################
tool_bar = tk.Label(app_main, bg='#3C3F41')
tool_bar.pack(side=tk.TOP, fill=tk.X)

#  font box
font_tuple = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar, background='silver', font=("Courier New", 11, "bold"), width=30,
                        textvariable=font_family, state='readonly')
font_box['values'] = font_tuple
font_box.current(font_tuple.index('Courier New'))
font_box.grid(row=0, column=0, padx=6, pady=5)

# size box
size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar, font=("Courier New", 11, "bold"), textvariable=size_var, state='readonly')
font_size['values'] = tuple(range(8, 81, 2))
font_size.current(4)
font_size.grid(row=0, column=1, pady=5)

# Bold button
bold_icon = tk.PhotoImage(file='assets/bold.gif')
bold_button = tk.Button(tool_bar, image=bold_icon)
bold_button.grid(row=0, column=2, pady=5, padx=6)

# italic btn
italic_icon = tk.PhotoImage(file='assets/italic.gif')
italic_button = tk.Button(tool_bar, image=italic_icon)
italic_button.grid(row=0, column=3, pady=5)

# underline btn
underline_icon = tk.PhotoImage(file='assets/underline.gif')
underline_button = tk.Button(tool_bar, image=underline_icon)
underline_button.grid(row=0, column=4, pady=5, padx=6)

# Font color btn
font_color_icon = tk.PhotoImage(file='assets/colorpicker3.png')
font_color_btn = tk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, pady=5)

# Align left
align_left_icon = tk.PhotoImage(file='assets/alignl.png')
align_left_btn = tk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, pady=5, padx=6)

# Align center
align_center_icon = tk.PhotoImage(file='assets/alignc.png')
align_center_btn = tk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=7, pady=5)

# Align right
align_right_icon = tk.PhotoImage(file='assets/alignr.png')
align_right_btn = tk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=8, pady=5, padx=6)

# Align none
align_none_icon = tk.PhotoImage(file='assets/alignn.png')
align_none_btn = tk.Button(tool_bar, image=align_none_icon)
align_none_btn.grid(row=0, column=9, pady=5)

# -------------------------------------------%%%%End toolbar%%%%%%%-------------------

########################################## Text editor start ########################################


skrib_editor = tk.Text(app_main)
skrib_editor.config(wrap='word', fg='#80FFFF', insertbackground='beige', insertofftime=0, highlightthickness=0,
                    highlightcolor='beige', bg='#2B2B2B', relief=tk.SUNKEN, bd=1)

scroll_bar1 = tk.Scrollbar(app_main, troughcolor="silver", bg="#2B2B2B")
scroll_bar1.pack(side=tk.RIGHT, fill=tk.Y)
scroll_bar1.pack(side=tk.RIGHT, fill=tk.Y)
skrib_editor.focus_set()
skrib_editor.pack(fill=tk.BOTH, expand=True)
scroll_bar1.config(command=skrib_editor.yview)
skrib_editor.config(yscrollcommand=scroll_bar1.set)

# Font family and size functionality
current_font_family = 'Courier New'
current_font_size = 16


def change_font(event=None):
    global current_font_family
    current_font_family = font_family.get()
    skrib_editor.configure(font=(current_font_family, current_font_size))


def change_fontsize(event=None):
    global current_font_size
    current_font_size = size_var.get()
    skrib_editor.configure(font=(current_font_family, current_font_size))


font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_fontsize)


# Buttons Functionality

# Bold btn functionality

def change_bold():
    text_property = tk.font.Font(font=skrib_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        skrib_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        skrib_editor.configure(font=(current_font_family, current_font_size, 'normal'))


bold_button.configure(command=change_bold)


# italic btn functionality

def change_italic():
    text_property = tk.font.Font(font=skrib_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        skrib_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        skrib_editor.configure(font=(current_font_family, current_font_size, 'roman'))


italic_button.configure(command=change_italic)


# Underline btn functionality

def change_underline():
    text_property = tk.font.Font(font=skrib_editor['font'])
    if text_property.actual()['underline'] == 0:
        skrib_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        skrib_editor.configure(font=(current_font_family, current_font_size, 'normal'))


underline_button.configure(command=change_underline)


# Font color functionality
def change_font_color():
    color_var = tk.colorchooser.askcolor()
    skrib_editor.configure(fg=color_var[1])


font_color_btn.configure(command=change_font_color)


# Align functionality
# Align Left
def align_left():
    text_content = skrib_editor.get(1.0, 'end')
    skrib_editor.tag_config('left', justify=tk.LEFT)
    skrib_editor.delete(1.0, tk.END)
    skrib_editor.insert(tk.INSERT, text_content, 'left')


align_left_btn.configure(command=align_left)


# Align center
def align_center():
    text_content = skrib_editor.get(1.0, 'end')
    skrib_editor.tag_config('center', justify=tk.CENTER)
    skrib_editor.delete(1.0, tk.END)
    skrib_editor.insert(tk.INSERT, text_content, 'center')


align_center_btn.configure(command=align_center)


# Align Right
def align_right():
    text_content = skrib_editor.get(1.0, 'end')
    skrib_editor.tag_config('right', justify=tk.RIGHT)
    skrib_editor.delete(1.0, tk.END)
    skrib_editor.insert(tk.INSERT, text_content, 'right')


align_right_btn.configure(command=align_right)


# Align None
def align_none():
    text_content = skrib_editor.get(1.0, 'end')
    skrib_editor.tag_config('left', justify=tk.LEFT)
    skrib_editor.delete(1.0, tk.END)
    skrib_editor.insert(tk.INSERT, text_content, 'left')


align_none_btn.configure(command=align_none)

skrib_editor.configure(font=('Courier New', 16))

# -------------------------------------------%%%%End text editor%%%%%%%-------------------

########################################## Main status bar start ########################################

status_bar = tk.Label(skrib_editor, text='Status bar', bg='#3C3F41', fg='silver')
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

text_changed = False


def changed(event=None):
    if skrib_editor.edit_modified():
        words = len(skrib_editor.get(1.0, 'end-1c').split())
        chars = len(skrib_editor.get(1.0, 'end-1c').replace(' ', ''))
        status_bar.config(text=f'Characters : [{chars}]  Words : [{words}]')

        skrib_editor.edit_modified(False)


skrib_editor.bind('<<Modified>>', changed)

# -------------------------------------------%%%%End main status bar%%%%%%%-------------------

########################################## Main Menu functionlity start ########################################


## Variable
url = ''


# New fuctionality
def new_file(event=None):
    global url
    url = ''
    skrib_editor.delete(1.0, tk.END)
    app_main.title('Skribal Text Editor')


# Open fuctionality
def open_file(event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Skribol Text file',
                                     filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
    try:
        with open(url, 'r') as fr:
            skrib_editor.delete(1.0, tk.END)
            skrib_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        app_main.title('Skribal Text Editor')
        return
    except:
        app_main.title('Skribal Text Editor')
        return
    app_main.title(url)


# Save fuctionality
def save_file(event=None):
    global url, text_changed
    try:
        if url:
            content = str(skrib_editor.get(1.0, tk.END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
            content2 = skrib_editor.get(1.0, tk.END)
            url.write(content2)
            url.close()
    except:
        app_main.title('Skribal Text Editor')
        return
    text_changed = False
    app_main.title(url.name)


# Save As functionality
def save_as(event=None):
    global url, text_changed
    try:
        content = str(skrib_editor.get(1.0, tk.END))
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                       filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
        url.write(content)
        url.close()
    except:
        app_main.title('Skribal Text Editor')
        return
    text_changed = False
    app_main.title(url.name)


## Exit Functionality

def exit_function(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = skrib_editor.get(1.0, tk.END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        app_main.destroy()
                else:
                    content2 = str(skrib_editor.get(1.0, tk.END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                                   filetypes=(('Text File', '*.txt'), ('All Files', '*.*')))
                    url.write(content2)
                    url.close()
                    app_main.destroy()
            elif mbox is False:
                app_main.destroy()
        else:
            app_main.destroy()
    except:
        return


# file commands

file.add_command(label='New', command=new_file, image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N')
file.add_command(label='Open', command=open_file, image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O')
file.add_command(label='Save', command=save_file, image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S')
file.add_command(label='Save As', command=save_as, image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S')

file.add_separator()

file.add_command(label='Exit', command=exit_function, image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q')

# Find & Replace functionality
global matches
global word
matches=0
word=""


def find_func(event=None):
    def find():
        word = find_input.get()
        skrib_editor.tag_remove('match', '1.0', tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = skrib_editor.search(word, start_pos, stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                skrib_editor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                skrib_editor.tag_config('match', foreground='red', background='lime')
        matches_found_lbl.config(text="{} match(es) of [{}] found".format(matches, word))

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = skrib_editor.get(1.0, tk.END)
        new_content = content.replace(word, replace_text)
        skrib_editor.delete(1.0, tk.END)
        skrib_editor.insert(1.0, new_content)

    find_dialogue = tk.Toplevel(bg="#2B2B2B")
    find_dialogue.geometry('450x300+500+200')
    find_dialogue.title('Find / Replace')
    find_dialogue.wm_iconbitmap('ico.ico')
    find_dialogue.resizable(0, 0)

    def findThread():
        thread1=threading.Thread(target=find)
        thread1.daemon=True
        thread1.start()
    def replaceThread():
        thread2=threading.Thread(target=replace)
        thread2.daemon=True
        thread2.start()

    ## frame
    find_frame = tk.LabelFrame(find_dialogue, bg="#2B2B2B", fg="#D4FFFF", text='Find/Replace', font=("Courier New", 13))
    find_frame.pack(pady=30)

    # Labels
    text_find_label = tk.Label(find_frame, bg="#2B2B2B", fg="#D4FFFF", text='Find : ', font=("Courier New", 13))
    text_replace_label = tk.Label(find_frame, bg="#2B2B2B", fg="#D4FFFF", text='Replace : ', font=("Courier New", 13))

    # Entry
    find_input = tk.Entry(find_frame, bg="beige", fg="#652C90", width=30, font=("Courier New", 12))
    replace_input = tk.Entry(find_frame, bg="beige", fg="#652C90", width=30, font=("Courier New", 12))

    # Buttons
    find_btn = tk.Button(find_frame, bg="#2B2B2B", fg="#D4FFFF", text='Find', command=findThread, font=("Courier New", 12))
    replace_btn = tk.Button(find_frame, bg="#2B2B2B", fg="#D4FFFF", text='Replace', command=replaceThread,
                            font=("Courier New", 13))

    # Label grid
    text_find_label.grid(row=0, column=0, padx=4, pady=4)
    text_replace_label.grid(row=1, column=0, padx=4, pady=4)

    # Entry grid
    find_input.grid(row=0, column=1, padx=4, pady=4)
    replace_input.grid(row=1, column=1, padx=4, pady=4)

    matches_found_lbl = tk.Label(find_frame, bg="#2B2B2B", fg="beige", font=("Courier New", 11))
    matches_found_lbl.grid(row=2, column=1, pady=4)

    # Button grid
    find_btn.grid(row=3, column=0, padx=8, pady=8)
    replace_btn.grid(row=3, column=1, padx=8, pady=8)

    find_dialogue.mainloop()


# Edit commands

edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C',
                 command=lambda: skrib_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V',
                 command=lambda: skrib_editor.event_generate("<Control v>"))
edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X',
                 command=lambda: skrib_editor.event_generate("<Control x>"))
edit.add_command(label='Clear All', image=clear_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X',
                 command=lambda: skrib_editor.delete(1.0, tk.END))
edit.add_separator()

edit.add_command(label='Find and Replace', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command=find_func)

# view check buttons

show_statusbar = tk.BooleanVar()
show_statusbar.set(True)
show_toolbar = tk.BooleanVar()
show_toolbar.set(True)


def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar = False
    else:
        skrib_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP, fill=tk.X)
        skrib_editor.pack(fill=tk.BOTH, expand=True)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        show_toolbar = True


def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar = False
    else:
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        show_statusbar = True


view.add_checkbutton(label='Tool Bar', variable=show_toolbar, command=hide_toolbar, onvalue=True, offvalue=0,
                     image=tool_bar_icon, compound=tk.LEFT)
view.add_separator()

view.add_checkbutton(label='Status Bar', variable=show_statusbar, command=hide_statusbar, onvalue=1, offvalue=False,
                     image=status_bar_icon, compound=tk.LEFT)


# color theme

def change_theme():
    chosen_theme = theme_choice.get()
    color_tuple = color_dict.get(chosen_theme)
    fg_color, bg_color = color_tuple[0], color_tuple[1]
    skrib_editor.config(background=bg_color, fg=fg_color)


count = 0
for i in color_dict:
    if count > 0:
        color_theme.add_separator()
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT,
                                command=change_theme)
    count += 1

# -------------------------------------------%%%%End main menu functionality%%%%%%%-------------------

app_main.config(menu=main_menu)
# Bind Shortcut keys
app_main.bind("<Control-N>", new_file)
app_main.bind("<Control-O>", open_file)
app_main.bind("<Control-S>", save_file)
app_main.bind("<Control-Alt-S>", save_as)
app_main.bind("<Control-Q>", exit_function)
app_main.bind("<Control-F>", find_func)

app_main.bind("<Control-n>", new_file)
app_main.bind("<Control-o>", open_file)
app_main.bind("<Control-s>", save_file)
app_main.bind("<Control-Alt-s>", save_as)
app_main.bind("<Control-q>", exit_function)
app_main.bind("<Control-f>", find_func)

app_main.mainloop()
