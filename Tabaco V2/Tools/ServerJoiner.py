import os
import discord
import time

banner1 = (f"""""")
text = "Server Joiner\n   "
x = banner1 + text * 1
print("\033[32m" + x + "\033[0m")

b = "\033[32m[+] \033[0m"
c = "\033[32m[Input] > \033[0m"

print('')
print('Input your Discord Server Url')
print('')
discordurl = input(str(c))

tokens = 0
token_list = "Tools/WorkedTokens.txt"  # Updated path to tokens.txt

with open(token_list, "r") as file:
    token_lines = file.read().splitlines()

if len(token_lines) == 0:
    print("There's nothing in the tokens file.")
else:
    num_tokens = len(token_lines)
    for i in range(num_tokens):
        tokens += 1
        print(str(b) + "| New token joined | " + str(tokens) + " joins |")
        time.sleep(0.01)
