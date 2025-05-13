# This is a program manager for Project Professional.
# It Is A CLI But When Type In a command It Will Open A GUI

# This Function Is For Checking The Python Version

import sys
from tkinter import messagebox

def check_python_version():
    if sys.version_info.major == 3 and sys.version_info.minor == 14:
        print("This Python Version Is Good")
        return True
    else:
        print("This Python Version Is Not Good")
        print("Please Use Python 3.14")
        return False

def program_manager():
    while True:
        program_manager_command = input("Program Manager > ")
        if program_manager_command == "about":
            messagebox.showinfo("Program Manager For Project Professional", "This Is A Program Manager For Project Professional" "\n VERSION: MAY 13TH BETA")


if __name__ == "__main__":
    if check_python_version():
        program_manager()
    else:
        print("Please Use Python 3.14")
        sys.exit(1)