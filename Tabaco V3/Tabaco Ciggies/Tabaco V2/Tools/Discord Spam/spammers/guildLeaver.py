import requests
from .assetsManager import *
from .color import color

def leave_guild(token : str , guildid : str , userAgent: str , proxies : str) -> str:
	"""It leaves the server where you entered the ID."""
	headers = {"content-type": "false",	"authorization": token , "User-Agent" : userAgent}
	proxies = {"http" : proxies}
	try:
		x = requests.delete(f"https://discordapp.com/api/v7/invite/{guildid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ERROR: {color.RESET_ALL} {err}")
	if x.status_code == 204:
		print(f"{color.GREEN}[+] Successfully left the server. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Could not leave the server. {color.RESET_ALL} {x.json()}")
