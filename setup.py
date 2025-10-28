import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["tkinter", "lr2testing"],
    "include_files": [],
    "excludes": []
}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="GenerateNum",
    version="1.0",
    description="Генератор случайных чисел",
    options={"build_exe": build_exe_options},
    executables=[Executable("gui.py", base=base, target_name="GenerateNum.exe")]
)