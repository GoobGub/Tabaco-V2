import os
import discord
import pystyle
import time
from pystyle import Add, Colors, Colorate, Center, Write

banner1 = (f"""""")
text = "Server Joiner\n   "
x = Add.Add(banner1, text, 3)
print(Colorate.Horizontal(Colors.blue_to_purple, str(x), 1))

b = Colorate.Horizontal(Colors.green_to_white, "[+] ", 1)
c = Colorate.Horizontal(Colors.blue_to_red, "[Input] > ", 1)

print(''); print('')
Write.Print(Center.XCenter("Input your Discord Server Url"), Colors.red_to_purple, interval=0.0025)
print('')
discordurl = input(Center.XCenter(str(c)))

tokens = 0
token_list = "./assets/tokens.txt"  # Updated path to tokens.txt

while True:
    tokens = tokens + 1
    print(str(b) + "| New token joined | " + str(tokens) + " joins |")
    time.sleep(0.3)
