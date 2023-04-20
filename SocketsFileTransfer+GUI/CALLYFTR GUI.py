import tkinter as tk
from tkinter import messagebox as msg, filedialog as fd, font, ttk
import os
import socket
import threading
import time
import sys

VERSION="1.0.0"
WINDOW = tk.Tk()
WINDOW.minsize(450, 530)
WINDOW.maxsize(450, 530)
WINDOW.title('                       CALLYFTR OFFLINE GUI Version '+VERSION)
WINDOW.configure(background='#2B2B2B')

try:
    WINDOW.wm_iconbitmap('assets/bitmp.ico')
except:
    pass

url = ""
s = None
f = None

try:
    def forHaltBtn():
        btnfile.config(state='normal')
        lbl_lbl.config(state='normal')
        cmb_conn.config(state='normal')
        global url, f
        try:
            url = ""
            socket.socket.close(s)
            socket.socket.close(s)
            btnsend.config(state='normal')
            btnrecv.config(state='normal')
            f = False
            cmb_conn['values'] = ""
            cmb_conn.set("")
            conn_details.config(text="")
        except:
            conn_details.config(text="")
            btnfile.config(state='normal')
            btnsend.config(state='normal')
            btnrecv.config(state='normal')
            pass


    def folderNameUpdater():
        while True:
            if os.path.exists('Downloads'):
                pass
            else:
                os.makedirs('Downloads')
            try:
                if os.path.exists('CFOL/vaimba.dat'):
                    with open('CFOL/vaimba.dat', 'r', encoding="utf-8") as myf:
                        saveloc23 = str(myf.read())
                        if os.path.exists(saveloc23):
                            lblsavingfolder.config(text="Saving to -> {}/".format(saveloc23))
                        else:
                            lblsavingfolder.config(text="Saving to -> {}/Downloads/".format(os.getcwd()))
                else:
                    lblsavingfolder.config(text="Saving to -> {}/Downloads/".format(os.getcwd()))

            except:
                pass
            time.sleep(0)


    def fileSelect():
        global url
        url = fd.askopenfilename(title='CALVOFTR GUI || Select file to send')


    def startServer():
        btnsend.config(state='disabled')
        btnrecv.config(state='disabled')
        thred1 = threading.Thread(target=Server)
        thred1.daemon = True
        thred1.start()


    def startClient():
        btnsend.config(state='disabled')
        thred2 = threading.Thread(target=Client)
        thred2.daemon = True
        thred2.start()


    def Server():
        def getFile(name, sock):
            sock.send((str(socket.gethostname())+" IP Addr: "+str(socket.gethostbyname(socket.gethostname()))).encode("utf-8"))
            global url
            global f
            try:
                if os.path.isfile(url):
                    filesize = int(os.path.getsize(url))
                    if filesize <= 1024:
                        filesizetoprint = "{0:.2f} bytes".format(float(filesize))
                    if filesize > 1024:
                        filesizetoprint = "{0:.2f} Kb".format(float(filesize / 1024))
                    if filesize > 1048576:
                        filesizetoprint = "{0:.2f} Mb".format(float(filesize / (1024 * 1024)))
                    if filesize > 1073741824:
                        filesizetoprint = "{0:.2f} Gb".format(float(filesize / (1024 * 1024 * 1024)))
                    sock.send(("EXISTS " + str(os.path.getsize(url))).encode("utf-8"))
                    userResponse = sock.recv(65536)
                    if userResponse[:2] == 'OK'.encode("utf-8"):
                        realfilename = str(os.path.basename(url))
                        realfilename2short = realfilename.replace("b'", "").replace("'", "")
                        if len(realfilename) > 25:
                            realfilename2short = realfilename[0:23] + "... ." + realfilename[
                                                                                len(realfilename) - 3:]
                        sock.send(realfilename.replace("b'", "").replace("'", "").encode("utf-8"))
                        with open(url, 'rb') as f:
                            bytesToSend = f.read(65536)
                            sock.send(bytesToSend)
                            bytesToSend2 = 65536
                            while bytesToSend2 < filesize:
                                bytesToSend = f.read(65536)
                                bytesToSend2 = bytesToSend2 + len(bytesToSend)
                                sock.send(bytesToSend)
                                percent = ((bytesToSend2) / filesize) * 100
                                progressbar.configure(value=percent)
                                lbl_lbl2.config(
                                    text="Sending {0} {1}".format(realfilename2short, filesizetoprint))
                                lbl_percentage.config(text="{0:.2f}%".format(percent))
                                WINDOW.update()
                            lbl_lbl2.config(text="Sent {0} {1}".format(realfilename2short, filesizetoprint))
                            lbl_percentage.config(text="")
                            progressbar.config(value=0)
                            WINDOW.update()
                else:
                    sock.send("".encode("utf-8"))
                sock.close()
                btnsend.config(state='disabled')
            except:
                pass
            url = ""

        def Main():
            global s
            host = socket.gethostname()
            port = 25937

            s = socket.socket()
            try:
                s.bind((host, port))
            except:
                btnsend.config(state='normal')
                btnrecv.config()
                msg.showerror("Conflict of ports!","Ensure no other services are running\n on port {25937} and only one "
                                                   "instance \nof this application is running, \nthen retry starting "
                                                   "the "
                                                   "server")

            s.listen(10)

            def lblstat():
                lblserverstat2.config(text="Server is up, time for clients to connect!", fg="green")
                time.sleep(15)
                lblserverstat2.config(text="")

            thred3 = threading.Thread(target=lblstat)
            thred3.daemon = True
            thred3.start()
            while True:
                allConnections = []
                allAddresses = []
                conn, addr = s.accept()
                # print("Client connected ip:< " + str(addr) + ">")
                allConnections.append(conn)
                allAddresses.append(
                    str(addr).replace(" ", "  @ port ").replace("('", "IP ").replace("'", "").replace(")", ""))
                cmb_conn['values'] = tuple(allAddresses)
                cmb_conn.current(0)
                updatelabels()
                t = threading.Thread(target=getFile, args=("retrThread", allConnections[cmb_conn.current()]))
                t.start()

            s.close()

        Main()


    def chooseFolder():
        directori = fd.askdirectory(title='CALVOFTR GUI || Choose a Saving Location')
        if os.path.exists('CFOL'):
            pass
        else:
            os.makedirs('CFOL')
        with open('CFOL/vaimba.dat', 'w', encoding="utf-8") as filetowrite:
            filetowrite.write(directori)


    global saveloc


    def Client():
        if os.path.exists('CFOL/vaimba.dat'):
            with open('CFOL/vaimba.dat', 'r', encoding="utf-8") as myf:
                saveloc1 = str(myf.read())
                if os.path.exists(saveloc1):
                    saveloc = saveloc1
                else:
                    saveloc = "Downloads"
        else:
            saveloc = "Downloads"

        try:

            def tryConnecting():
                MYVAR = 0
                while MYVAR < 1:
                    host = socket.gethostname()
                    port = 25937

                    s = socket.socket()
                    s.connect((host, port))

                    btnfile.config(state='disabled')
                    lbl_lbl.config(state='disabled')
                    cmb_conn.config(state='disabled')
                    btnhalt.update()
                    sender = str(s.recv(65536).decode("utf-8"))
                    conn_details.config(text="Connected to Server " + sender)
                    data = s.recv(65536)
                    if data[:6] == 'EXISTS'.encode("utf-8"):
                        filesize = int(data[6:])
                        filesizetoprint = filesize
                        if filesize < 1024:
                            filesizetoprint = "{0:.2f} bytes".format(float(filesize))
                        if filesize > 1024:
                            filesizetoprint = "{0:.2f} Kb".format(float(filesize / 1024))
                        if filesize > 1048576:
                            filesizetoprint = "{0:.2f} Mb".format(float(filesize / (1024 * 1024)))
                        if filesize > 1073741824:
                            filesizetoprint = "{0:.2f} Gb".format(float(filesize / (1024 * 1024 * 1024)))
                        message = 'Y'
                        if message == 'Y':

                            s.send('OK'.encode("utf-8"))
                            realfilename = s.recv(65536)
                            realfilename2 = realfilename.decode("utf-8").replace("\"", "")
                            if os.path.exists("{}/{}".format(saveloc, realfilename2)):
                                lblserverstat.config(
                                    text="Incoming file {0} already in location, delete if not complete! ".format(
                                        realfilename2[0:23] + "... ." + realfilename2[
                                                                        len(realfilename2) - 3:]),
                                    fg="red")
                                time.sleep(5)
                                progressbar.configure(value=0)
                                lbl_percentage.config(text="")
                                lblserverstat.config(text="")

                            else:
                                f = open('{0}/{1}'.format(saveloc, realfilename2), 'wb')

                                data = s.recv(65536)
                                totalRecv = len(data)
                                f.write(data)
                                realfilename2short = realfilename2
                                if len(realfilename2) > 25:
                                    realfilename2short = realfilename2[0:23] + "... ." + realfilename2[
                                                                                         len(realfilename2) - 3:]
                                btnrecv.config(state='disabled')
                                btnfile.config(state='disabled')
                                btnhalt.config(state='disabled')
                                while totalRecv < filesize:
                                    data = s.recv(65536)
                                    totalRecv += len(data)
                                    f.write(data)
                                    percent = totalRecv / float(filesize) * 100
                                    progressbar.configure(value=percent)
                                    lbl_lbl2.config(
                                        text="Receiving {0} {1}".format(realfilename2short, filesizetoprint))
                                    lbl_percentage.config(text="{0:.2f}%".format(percent))
                                    WINDOW.update()
                                btnrecv.config(state='normal')
                                btnfile.config(state='normal')
                                btnhalt.config(state='normal')
                                lbl_lbl2.config(text="Received {0} {1}".format(realfilename2short, filesizetoprint))
                                lbl_percentage.config(text="")
                                progressbar.config(value=0)
                                WINDOW.update()

                    else:
                        # print("File does not exist on server")

                        s.close()
                    MYVAR = 2

            tryConnecting()

        except:
            btnfile.config(state='normal')
            lbl_lbl.config(state='normal')
            cmb_conn.config(state='normal')
            msg.showerror("Error Occurred", "Wait for Server for you to connect")


    exit_icon = tk.PhotoImage(file='assets/logout.png')

    IPSTRING = tk.StringVar()
    IPSTRING = 'Host name: [{0}]\t\tHost Address: [{1}]'.format(socket.gethostname(),
                                                                socket.gethostbyname(socket.gethostname()))

    menu_bar = tk.Label(WINDOW, bg='#3C3F41', height=2)
    menu_bar.pack(side=tk.TOP, fill=tk.X)

    btnsettings = tk.Button(menu_bar, bg='#3C3F41', fg='white', text='Set Folder', font=("Arial", 11),
                            command=chooseFolder)
    btnsettings.grid(row=0, column=0, padx=4, pady=1)

    btnfile = tk.Button(menu_bar, bg='#3C3F41', fg='white', text='Choose File', font=("Arial", 11), command=fileSelect)
    btnfile.grid(row=0, column=1, padx=4, pady=1)

    btnsend = tk.Button(menu_bar, bg='#3C3F41', fg='white', text='Start Server', font=("Arial", 11),
                        command=startServer)
    btnsend.grid(row=0, column=2, padx=4, pady=1)

    btnrecv = tk.Button(menu_bar, bg='#3C3F41', fg='white', text='Receive', font=("Arial", 11), command=startClient)
    btnrecv.grid(row=0, column=3, padx=4, pady=1)


    def closeApp():
        INTEXIT = msg.askyesnocancel("Sure to Exit?", "Confirm system Exit?")
        if INTEXIT == 1:
            sys.exit(0)


    btnexit = tk.Button(menu_bar, bg='#3C3F41', fg='white', image=exit_icon, command=closeApp)
    btnexit.grid(row=0, column=4, padx=50, pady=1)

    menu_my_details = tk.Label(WINDOW, bg='#3D3A41', font=("Arial", 10, 'bold'), fg="CYAN", text=IPSTRING, height=2)
    menu_my_details.pack(side=tk.TOP, fill=tk.X)

    conn_details = tk.Label(WINDOW, bg='#3D3A41', font=("Arial", 11), fg="LIME", height=2)
    conn_details.pack(side=tk.TOP, fill=tk.X)

    menu_conn_list = tk.Label(WINDOW, bg='#2B2B2B', font=("Arial", 10, 'bold'), fg="CYAN", height=4)
    menu_conn_list.pack(side=tk.TOP, fill=tk.X, pady=10)

    CONNECTIONCHOICE = tk.StringVar()

    lbl_lbl = tk.Label(menu_conn_list, bg='#2B2B2B', text="Choose connection:", font=("Arial", 11, "bold"), fg='ORANGE')
    lbl_lbl.grid(row=0, column=0, padx=5, pady=0)

    cmb_conn = ttk.Combobox(menu_conn_list, background="black", foreground='ORANGE', font=("Arial", 12, 'bold'),
                            state='readonly',
                            textvariable=CONNECTIONCHOICE, width=28)
    cmb_conn.grid(row=0, column=1, pady=5, padx=10)


    def updatelabels(event=None):
        conn_details.config(text="Connected to Client " + cmb_conn.get())


    cmb_conn.bind("<<ComboboxSelected>>", updatelabels)

    lbl_lbl2 = tk.Label(WINDOW, bg='#2B2B2B', text="", font=("Arial", 10), fg='LIME')
    lbl_lbl2.pack(side=tk.TOP, fill=tk.X, pady=10)

    lbl_progressbar = tk.Label(WINDOW, bg='#1B150E', font=("Arial", 10, 'bold'), fg="CYAN", height=10)
    lbl_progressbar.pack(side=tk.TOP, fill=tk.X, pady=20)

    progressbar = ttk.Progressbar(lbl_progressbar, mode='determinate', orient='horizontal', value=0, maximum=100,
                                  length=410)
    progressbar.pack(side=tk.TOP, pady=30, padx=40)

    lbl_percentage = tk.Label(lbl_progressbar, bg='#1B150E', font=("Arial", 10), fg='LIME')
    lbl_percentage.pack(side=tk.RIGHT, padx=20)

    lbl_halt = tk.Label(WINDOW, bg='#2B2B2B', font=("Arial", 10, 'bold'), fg="CYAN", height=4)
    lbl_halt.pack(side=tk.TOP, fill=tk.X, pady=5)

    lblserverstat = tk.Label(WINDOW, bg='#2B2B2B', font=("Arial", 10), wrap=300, fg='RED')
    lblserverstat.pack(side=tk.TOP, fill=tk.X, pady=1)

    lblserverstat2 = tk.Label(WINDOW, bg='#2B2B2B', font=("Arial", 10), fg='RED')
    lblserverstat2.pack(side=tk.TOP, fill=tk.X, pady=1)

    lblsavingfolder = tk.Label(lbl_halt, wrap=320, bg='#2B2B2B', font=("Courier", 9), fg='BEIGE')
    lblsavingfolder.pack(side=tk.LEFT, fill=tk.X, pady=0, padx=0)

    lblaboutme = tk.Label(WINDOW, text='Developer: Calvine Museywa Azenga - 0700666848 @MUT', bg='#2B2B2B',
                          font=("Raleway", 9), fg='CYAN')
    lblaboutme.pack(side=tk.TOP, fill=tk.X, pady=0)

    lblaboutme2 = tk.Label(WINDOW, text='muscalazems@gmail.com', bg='#2B2B2B', font=("Raleway", 9), fg='CYAN')
    lblaboutme2.pack(side=tk.TOP, fill=tk.X, pady=0)

    btnhalt = tk.Button(lbl_halt, bg='#3C3F41', fg='white', text='Halt process', font=("Arial", 11), command=forHaltBtn)
    btnhalt.pack(side=tk.RIGHT, pady=1, padx=10)

    try:
        thredupdet = threading.Thread(target=folderNameUpdater)
        thredupdet.daemon = True
        thredupdet.start()
    except:
        pass
    # try:
    #     image = tk.PhotoImage(file='assets/b.png')
    #     lblimage=tk.Canvas(lblaboutme,bg="#2B2B2B",height=50,width=50)
    #     lblimage.create_image(50,50,anchor=tk.SE, image=image)
    #     lblimage.pack(side=tk.RIGHT,padx=10)
    # except:
    #     pass

    WINDOW.mainloop()
except:
    msg.showerror("CALVOFTR GUI || FATAL ERROR!", "A fatal Error occurred!, \nPlease try restarting CALVOFTR GUI "
                                                  "OFFLINE\nIf the error persists, try reinstalling the application")

