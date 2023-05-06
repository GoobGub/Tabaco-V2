import webbrowser


url1 = "https://www.youtube.com/watch?v=rFbiW2x4HEw"
url2 = "https://github.com/dekrypted/discord-image-logger"


while True:
    response = input("This will take you to the download and setup for the image logger are you sure you want to procced (Y/N)").lower()
    if response == 'y':
        break
    elif response == 'n':
        print("Exiting script...")
        exit()
    else:
        print("Invalid response. Please enter 'Y' or 'N'.")


webbrowser.open_new_tab(url1)
webbrowser.open_new_tab(url2)


print("The image logger is made by my friend dekrypt.")
