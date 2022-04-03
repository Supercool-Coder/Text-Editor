import cx_Freeze
import sys
import os
base = None

if sys.platform == 'win32':
    base = "win32GUI"

os.environ['TCL_LIBRARY']=r"C:\Python 3.9.6\tcl"
os.environ['TK_LIBRARY']=r"C:\Python 3.9.6\tcl"

executable = [cx_Freeze.Executable("vpad.py",base=base, icon="icon.ico")]

cx_Freeze.setup(
    name = "Text Editor",
    options = {"build_exe" : {"packages":['tkinter','os'],"include_files":["icon.ico",'tcl86t.dll','tk86t.dll','icon2']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )