import random

def userAgent():
    """UserAgents"""
    with open("./assets/userAgents.txt" , encoding="utf-8") as f:
        return random.choice(f.readlines()).split("\n")[0]

def proxies():
    """Proxies"""
    with open("./assets/proxies.txt" , encoding="utf-8") as f:
        return random.choice(f.readlines()).split("\n")[0]

def tokens():
	"""Tokens"""
	tokens = []
	with open("./assets/tokens.txt" , encoding="utf-8") as f:
		for i in f.readlines():
			tokens.append(i.split("\n")[0])
		return tokens 