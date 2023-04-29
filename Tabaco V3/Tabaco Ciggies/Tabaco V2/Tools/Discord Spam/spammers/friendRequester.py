import requests
from .assetsManager import *
from .color import color

def friend_request(token : str , userid : str , userAgent: str , proxies : str) -> str:
	"""Sends a friend request to the person whose ID you enter"""
	headers = {"content-type": "application/json",	"authorization": token , "User-Agent" : userAgent}
	proxies = {"http" : proxies}
	try:
		x = requests.put(f"https://discordapp.com/api/v7/users/@me/relationships/{userid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ERROR: {color.RESET_ALL} {err}")
	if x.status_code == 204:
		print(f"{color.GREEN}[+] Friend request sent successfully. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Failed to send friend request {color.RESET_ALL} {x.json()}")
