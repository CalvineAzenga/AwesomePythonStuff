import cx_Freeze
import sys
import os

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\CALVOKILROY\AppData\Local\Programs\Python\Python38\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\CALVOKILROY\AppData\Local\Programs\Python\Python38\tcl\tk8.6"

executables = [cx_Freeze.Executable("Skribol.py", base=base, icon="ico.ico")]

cx_Freeze.setup(
    name="Skribol Text Editor",
    options={"build_exe": {"packages": ["tkinter", "os"],"include_files": ["ico.ico", 'tcl86t.dll', 'tk86t.dll', 'assets']}},
    version="1.0.0",
    description="Skribol Text Editor",
    executables=executables
)
