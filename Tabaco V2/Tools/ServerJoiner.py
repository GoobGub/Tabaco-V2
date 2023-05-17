import os
import discord
import time

def join_server(token, server_url):
    client = discord.Client()

    @client.event
    async def on_ready():
        try:
            await client.accept_invite(server_url)
            print(f"Joined server with token: {token}")
        except discord.errors.HTTPException:
            print(f"Failed to join server with token: {token}")

        await client.logout()

    client.run(token)

token_file = "Tools/WORKED TOKENS.txt"  # Path to tokens.txt
server_url = input("Enter the Discord server URL: ")

with open(token_file, "r") as file:
    tokens = file.read().splitlines()

for token in tokens:
    join_server(token, server_url)
    time.sleep(1)  # Add a delay between joining with different tokens
