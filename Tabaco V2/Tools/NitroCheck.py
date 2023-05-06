import requests
import random
import string

print("This will take a few seconds..")
print("If you see many *'s that means most are invalid or all are invalid")

with open("tools/workedcodes.txt") as file:
    for line in file.readlines():
        nitro = line.strip("\n")

        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f"\n\n Valid | {nitro}\n\n") 
        else:
            print(f"*", end = "")
