# Method 1
# import subprocess

# data=subprocess.check_output(['wmic', 'printer' ,'list' ,'brief']).decode('utf-8').split('\r\r\n')

# data=data[1:] # To get rid of the first row

# for line in data:
#     for printername in line.split("  "): # Two spaces to avoid splitting the printer names with spaces in them
#         if printername!="":
#             print(printername)
#             break # To get the first column value only

# Method 2- Efficient

import win32print

printer_info=win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

printer_names=[name for(flgs, description,name,comment) in printer_info]


for i, name in enumerate(printer_names):
    print(name)
