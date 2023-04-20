import win32ui

import win32print, pywintypes, win32con, win32gui, win32api


class POSPrinter:
    def __init__(self):
        self.defaultPrinter = self.getDefaultPrinter()
        self.printers = []

    def setDefaultPrinter(self):
        try:
            win32print.SetDefaultPrinter(self.defaultPrinter)
        except Exception as msg:
            pass

    def getDefaultPrinter(self) -> str:
        self.defaultPrinter = win32print.GetDefaultPrinter()
        return self.defaultPrinter

    def installed_printers(self) -> list:
        printer_info = win32print.EnumPrinters(win32print.PRINTER_ENUM_LOCAL | win32print.PRINTER_ENUM_CONNECTIONS)

        printer_names = [name for (flags, description, name, comment) in printer_info]

        for i, name in enumerate(printer_names):
            self.printers.append(name)

        return self.printers

    def PrintText(self, text):
        printer_name = self.defaultPrinter
        print(printer_name)
        hDC = win32ui.CreateDC()
        hDC.CreatePrinterDC(printer_name)

        hDC.StartDoc("file_name")
        hDC.StartPage()
        textLines = str(text).split("\n")
        x = 0
        y = 0

        for line in textLines:
            # hDC.MoveTo(x, y)
            hDC.TextOut(x, y, line)
            y += 100

        hDC.EndPage()
        hDC.EndDoc()
        hDC.DeleteDC()

    def print2(self, txt):
        job = None
        printer_name = self.defaultPrinter
        p = win32print.OpenPrinter("Microsoft XPS Document Writer")
        print(printer_name)
        try:
            job = win32print.StartDocPrinter(p, 1, ("pos_receipt", None, "RAW"))
            try:
                file = txt.encode()
                win32print.StartPagePrinter(p)

                win32print.WritePrinter(p, file)
                win32print.EndPagePrinter(p)
            finally:
                win32print.EndDocPrinter(p)

        finally:
            print("Printing: %s" % job)
            win32print.ClosePrinter(p)

    def print4(self, txt):

        pass
