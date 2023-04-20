import win32print

printer_info = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

printer_names = [name for (flgs, description, name, comment) in printer_info]
printer_list = []

for i, name in enumerate(printer_names):
    printer_list.append(name)
    print(name)
defaultPrinter = win32print.GetDefaultPrinter()
# if defaultPrinter in printer_list:
#     print(defaultPrinter, "[IN PRINTER LIST] Is the default Printer")


def selectDefaultPrinter(printer_name):
    try:
        win32print.SetDefaultPrinter(printer_name)
    except Exception as msg:
        pass
