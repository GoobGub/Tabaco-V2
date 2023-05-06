import spammers as s
from spammers import color

s.banner(text="")

print("""



1: Friend Request Sender
2: Guild Leaver
3: Message Sender
4: Shows the help message.
5: Exit

""")

while True:
	_input = str(input(f"{color.YELLOW}[?] > {color.RESET_ALL}").lower())

	if _input == "1":
		userid = input(f"{color.YELLOW}[?] Enter the ID of the user you want to send a friend request to > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.friend_request(token = tokens , userid = userid , userAgent = s.userAgent() , proxies = s.proxies())
		print(f"{color.GREEN}The transaction is finished. {color.RESET_ALL}")

	elif _input == "10000":
		print("Not working unless you have hCaptcha bypass")



	elif _input == "2":
		guildid = input(f"{color.YELLOW}[?] Enter the ID of the server you want to leave > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.leave_guild(token = tokens , guildid=guildid , userAgent=s.userAgent() , proxies=s.proxies())
		print(f"{color.GREEN}The transaction is finished. {color.RESET_ALL}")


	elif _input == "3":
		channelid = input(f"{color.YELLOW}[?] Enter the ID of the channel you will message > {color.RESET_ALL}").lower()
		message = input(f"{color.YELLOW}[?] enter message > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.send_message(token = tokens , channelid = channelid , message = message , userAgent = s.userAgent() , proxies=s.proxies())
		print(f"{color.GREEN}The transaction is finished. {color.RESET_ALL}")

	elif _input == "4":
		print("Simply put the tokens in the ./assets/tokens.txt file.")

	elif _input == "5":
		quit()

	else:
		print(f"{color.RED}[-]Invalid options. {color.RESET_ALL}")
