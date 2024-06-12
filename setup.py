# from cx_Freeze import setup, Executable
# setup(name="Generador de Claves",
#     options = {"build_exe":{"packages":["tkinter","pyperclip","csv"],
#     "include_files":[]}},
#     version="1.0",
#     description="Generador de Claves",
#     executables=[Executable(r"/home/alexander/Escritorio/Python/PhytonScripts/main.py")],
#     icon=r"/home/alexander/Escritorio/Python/PhytonScripts/siap_icon.ico",
#     shorcutName="Generador de Claves",
#     shortcutDir="DesktopFolder",
#     base="Win32GUI"
#     )


# from cx_Freeze import setup, Executable

# setup(
#     name="Generador de Claves",
#     options={
#         "build_exe": {
#             "packages": ["tkinter", "pyperclip", "csv"],
#             "include_files": []
#         }
#     },
#     version="1.0",
#     description="Generador de Claves",
#     executables=[Executable("main.py")],
# )

import cx_Freeze, sys

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("main.py", base=base)]

cx_Freeze.setup(
    name="generador",
    options={"build_exe": {"packages": ["tkinter", "csv", "pyperclip"], "include_files": []}},
    version="1.0",
    description="Generador de claves",
    executables=executables
)
