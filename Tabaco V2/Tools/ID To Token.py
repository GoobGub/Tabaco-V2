# Modules importation
import os
import base64
try:
    from colorama import Fore, init
except:
    os.system("py -m pip install colorama")
    from colorama import Fore, init
init()

userid = input("ID : ")
encodedBytes = base64.b64encode(userid.encode("utf-8"))
encodedStr = str(encodedBytes, "utf-8")
print(f'\n  FIRST PART : {encodedStr}')
print("Control + C To Go back to Menu")
os.system('pause >nul') 