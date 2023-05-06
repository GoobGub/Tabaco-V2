import random
import string
import pathlib
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
import colorama
from colorama import Fore, init, Back, Style
from datetime import date

def Spinner():
	l = ['|', '/', '-', '\\']
	for i in l+l+l:
		sys.stdout.write('\r' + Fore.GREEN +'TokenGen is Starting...'+i)
		sys.stdout.flush()
		time.sleep(0.2)

Spinner()

count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
	
print(Fore.WHITE +Fore.RED +"-\ "+Fore.BLUE+"     TokenGen -\-\-")
print(Fore.WHITE +Fore.RED +"-\ [1] "+Fore.BLUE+"Token Generator \-")
print(Fore.WHITE +Fore.RED +"-\ [2] "+Fore.BLUE+"Exit \-")                                                                                             
opcion = input("\nChoice: ")
if opcion=='1':
	cantidad = input("\nAmount to generate: ")
	while int(count)<int(cantidad):
		Generated = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
		f= open(current_path +"/"+str("Generated")+str("")+".txt","a")
		f.write(Generated+"\n")
		print(Fore.GREEN +" "+ Fore.RESET + Generated)
		count+=1
		if int(count)==int(cantidad):
			print("\n" + Fore.CYAN +Fore.RED +"Tokens generated successfully!")
			print(Fore.WHITE +Fore.RED +"Tokens saved in Generated.txt")
			input(Fore.RED +Fore.RED +"\nPress enter to exit")
			os.system("cls")
			time.sleep(2)
			sys.exit()