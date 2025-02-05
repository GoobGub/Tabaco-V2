import os
import time
import subprocess
from colorama import init, Fore, Style

os.system("color 2")

def load_proxies():
    print("Loading proxies...")
    for i in range(5):
        time.sleep(0.1)
        print(".", end='', flush=True)
    time.sleep(1)
    print("\nProxies loaded successfully!")
    time.sleep(0.5)
    print("Activating proxies...")
    for i in range(5):
        time.sleep(0.1)
        print(".", end='', flush=True)
    time.sleep(1)
    print("\nProxies activated!")
    time.sleep(0.5)

with open('Tools/proxies.txt') as f:
    proxies = f.readlines()
    
load_proxies()

init(autoreset=True)


options = [
    "TokenBruteforce",
    "WebhookSpam",
    "NitroCheck",
    "Vanity Checker",
    "Gmail BruteForce",
    "Server Nuker",
    "Email Spam",
    "ImageLogger",
    "TokenLogger",
    "DDOS",
    "NitroGen",
    "ServerJoiner",
    "TokenGen",
    "Discord Spam",
    "ID To Token",
    "Token Checker",
    "BotNetDDOS",
    "Stresser",
    "IP Pinger"
]

print(F"{Fore.LIGHTGREEN_EX}████████╗ █████╗ ██████╗  █████╗  ██████╗ ██████╗ ")
print(F"{Fore.GREEN}╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔═══██╗")
time.sleep(0.1)
print(F"{Fore.LIGHTGREEN_EX}   ██║   ███████║██████╔╝███████║██║     ██║   ██║")
time.sleep(0.1)
print(F"{Fore.GREEN}   ██║   ██╔══██║██╔══██╗██╔══██║██║     ██║   ██║")
time.sleep(0.1)
print(F"{Fore.LIGHTGREEN_EX}   ██║   ██║  ██║██████╔╝██║  ██║╚██████╗╚██████╔╝")
time.sleep(0.1)
print(F"{Fore.GREEN}   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ")
time.sleep(0.1)
print(F"{Fore.LIGHTGREEN_EX}HAWK TAWW!")
print(F"{Fore.RED}SKIBIDI TOLIET")
time.sleep(2)                                     

os.system("color 2")

print("If Your Done Using a Tool Press Control + C To Go back to Menu")

print("made bye me and only me")

def menu():
    while True:
        
        print(Fore.LIGHTGREEN_EX + "\nChoose an option:\n")
        for i in range(len(options)):
            print(Fore.LIGHTGREEN_EX + str(i+1) + ". " + options[i])

        # Get the user's choice
        choice = input(Fore.LIGHTGREEN_EX + "\nEnter the number of your choice: ")

        # Run the chosen script, if it exists
        try:
            script_name = options[int(choice)-1]
            subprocess.call(["python", f"Tools/{script_name}.py"])
                
        except:
            print

if __name__ == "__main__":
    menu()
