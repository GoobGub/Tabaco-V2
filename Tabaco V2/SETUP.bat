@echo off

pip install --upgrade pip

setlocal

set PYTHON38_URL=https://www.python.org/ftp/python/3.8.12/python-3.8.12-amd64.exe
set PYTHON39_URL=https://www.python.org/ftp/python/3.9.12/python-3.9.12-amd64.exe
set PYTHON310_URL=https://www.python.org/ftp/python/3.10.2/python-3.10.2-amd64.exe

rem Check if Python 3.8 is installed
python3.8 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python 3.8 is already installed.
) else (
    echo Installing Python 3.8...
    msiexec /i %PYTHON38_URL% /qn
    echo Python 3.8 installation complete.
)

rem Check if Python 3.9 is installed
python3.9 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python 3.9 is already installed.
) else (
    echo Installing Python 3.9...
    msiexec /i %PYTHON39_URL% /qn
    echo Python 3.9 installation complete.
)

rem Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% equ 0 (
    echo pip is already installed.
) else (
    echo Installing pip...
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    echo pip installation complete.
)

rem Check if Python 3.10 is installed
python3.10 --version >nul 2>&1
if %errorlevel% equ 0 (
    echo Python 3.10 is already installed.
) else (
    echo Installing Python 3.10...
    msiexec /i %PYTHON310_URL% /qn
    echo Python 3.10 installation complete.
)

echo Installing required packages...

pip install pysocks
pip install smtplib
pip install requests
pip install random-package
pip install colorama
pip install discord
pip install threading
pip install asyncio
pip install aiohttp
pip install pathlib
pip install psutil
pip install colored
pip install termcolor
pip install webbrowser
pip install httpx
pip install pyotp
pip install psutil
pip install pypiwin32
pip install pycryptodome
pip install roblox
pip install roblox-mod
pip install pyinstaller>=5.0
pip install PIL-tools
pip install asyncio
pip install ctypes
pip install json
pip install ntpath
pip install os
pip install random
pip install re
pip install shutil
pip install sqlite3
pip install subprocess
pip install threading
pip install winreg
pip install zipfile
pip install fade
pip install colorama
pip install fake-useragent
pip install aiohttp
pip install urllib3
pip install requests
pip install beautifulsoup4
pip install pythonping
pip install httpagentparser
pip install cloudscraper
pip install opentele
pip install pyautogui
pip install keyboard
pip install pystyle
pip install pyfiglet
pip install PyJWT
pip install Scapy
pip install socket
pip install pyinstaller
pip install pygame

echo All packages installed successfully.
