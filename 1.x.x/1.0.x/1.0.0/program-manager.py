# This is a program manager for Project Professional.
# It Is A CLI But When Type In a command It Will Open A GUI

# This Fuction Is For Checkign The Python Version

import sys
import os

def check_python_version():
    if sys.version_info.major == 3 and sys.version_info.minor == 14:
        print("This Python Version Is Good")
        return True
    else:
        print("This Python Version Is Not Good")
        print("Please Use Python 3.14")
        return False