import json
import os

os.system("color 2")

# Read the configuration file
with open('Tools/NG/config/config.json', 'r') as f:
    config = json.load(f)

# Ask the user to input the webhook URL
webhook_url = input("Enter the webhook URL: ")

# Update the URL in the configuration file
config["url"] = webhook_url

# Write the updated configuration file
with open('Tools/NG/config/config.json', 'w') as f:
    json.dump(config, f)

# Ask the user if they want to run the script
run_script = input("Do you want to run the script? (y/n) ")

if run_script.lower() == "y":
    # Change directory to the NG folder
    os.chdir('Tools/NG')

    # Run the main.py script
    os.system('python main.py')