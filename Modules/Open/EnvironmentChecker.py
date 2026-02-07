"""
This code was written by SpinnySpiwal
This code checks if the user has the required libraries installed for the project to run.
"""
import os
import subprocess
import platform

def findVirtualEnvironment():
    for path in os.listdir("."):
        if os.path.isdir(path):
            print(path)
            path_contents = os.listdir(path)
            if "include" in path_contents:
                include_contents = os.listdir(path + "/include")
                for file in include_contents:
                    if "python" in file:
                        return path + "/include/" + file


def checkInstalledLibraries(listOfLibraries):
    libraries = {}
    for library in listOfLibraries:
        try:
            __import__(library.replace("BeautifulSoup4", "bs4").replace("-", "_"))
            libraries[library] = True
        except Exception:
            libraries[library] = False

    return libraries

libraries = checkInstalledLibraries(["requests", "bson", "xmltodict", "BeautifulSoup4", "werkzeug", "pypresence", "pywidevine", "cryptography", "aws-encryption-sdk", "brotli"])

settings = {"enabled": True, "logLevel": 3}

keys = {
    "reset": 0,
    "bright": 1,
    "dim": 2,
    "underline": 4,
    "blink": 5,
    "reverse": 7,
    "hidden": 8,
    "black": 30,
    "pink": 91,
    "red": 31,
    "green": 32,
    "yellow": 33,
    "blue": 34,
    "magenta": 35,
    "cyan": 36,
    "grey": 37,
    "gray": 37,
    "white": 97,
    "blackbg": 40,
    "redbg": 41,
    "greenbg": 42,
    "yellowbg": 43,
    "bluebg": 44,
    "magentabg": 45,
    "cyanbg": 46,
    "greybg": 47,
    "graybg": 47,
    "whitebg": 107,
}

escape_string = "\x1b[%dm"

def escape_number(number):
    return escape_string % number

def colors(string, *args):
    if not settings["enabled"]:
        return string

    string = str(string or "")
    escapes = [escape_number(keys[name]) for name in args]

    return (
        escape_number(keys["reset"])
        + "".join(escapes)
        + string
        + escape_number(keys["reset"])
    )

def colorsPrint(string, *args):
    print(colors(string, *args))

def logPrint(text, color, levelToPrint=1):
    if levelToPrint <= settings["logLevel"]:
        colorsPrint(text, color)




colorsPrint("Checking installed libraries...", "yellow")
notInstalled=[]
for library, installed in libraries.items():
    if not installed:
        colorsPrint(f"Library {library} is not installed. Please install it using 'pip install {library}'.", "red")
        notInstalled.append(library)
notInstalledString = " ".join(notInstalled) + " -y"

if len(notInstalled) > 0:
    is_windows = platform.system() == "Windows"
    
    if is_windows:
        # On Windows, use system pip directly without virtual environment
        colorsPrint("Would you like to automatically install the missing libraries?", "yellow")
        answer = input("Answer: ")
        if answer == "yes":
            libraries_to_install = []
            for lib in notInstalled:
                if lib == "BeautifulSoup4":
                    libraries_to_install.append("beautifulsoup4")
                else:
                    libraries_to_install.append(lib)
            subprocess.run(["py", "-m", "pip", "install"] + libraries_to_install, check=True)
        else:
            colorsPrint("Please install the missing libraries manually.", "red")
            exit(1)
    else:
        # On non-Windows systems, check for virtual environment
        virtualEnvironment = findVirtualEnvironment()
        if virtualEnvironment is not None:
            colorsPrint("A virtual environment has been found. Would you like to automatically install the missing libraries?", "yellow")
            answer = input("Answer: ")
            if answer == "yes":
                # Fix the pip path construction and library name replacement
                pip_path = os.path.join(os.path.dirname(virtualEnvironment).split("/")[0], "bin", "pip")
                libraries_to_install = []
                for lib in notInstalled:
                    if lib == "BeautifulSoup4":
                        libraries_to_install.append("bs4")
                    else:
                        libraries_to_install.append(lib)
                subprocess.run([pip_path, "install"] + [lib.replace("-", "_") for lib in libraries_to_install], check=True)
            else:
                colorsPrint("Please install the missing libraries manually.", "red")
                exit(1)
        else:
            colorsPrint("No virtual environment found. Please create one using 'virtualenv venv'.", "red")
            exit(1)