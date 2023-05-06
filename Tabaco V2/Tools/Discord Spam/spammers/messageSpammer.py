import requests
from .assetsManager import *
from .color import color

def send_message(token : str , channelid : str , message : str , userAgent: str , proxies : str) -> str:
	"""It sends the message you want to the channel whose ID you entered."""
	headers = {"content-type": "application/json",	"authorization": token , "User-Agent" : userAgent , "content" : message , "tts" : "false"}
	proxies = {"http" : proxies}
	try:
		x = requests.post(f"https://discordapp.com/api/v7/channels/{channelid}/messages" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ERROR: {color.RESET_ALL} {err}")
	if x.status_code == 200:
		print(f"{color.GREEN}[+] Message sent successfully. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Message could not be sent. {color.RESET_ALL} {x.json()}")
