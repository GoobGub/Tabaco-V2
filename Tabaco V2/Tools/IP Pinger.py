import socket, threading
import colorama
import os
import sys
import fade
import time

faded_gui=fade.brazil(gui)
print(faded_gui)
def tcpping(ip,port):
    try:
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect((ip,port))
        print(f"                {m}[{w}OK{m}] {g}Connection to {y}{ip} {lg}in port {y}{port} {lb}[{y}By Noxius{lb}] {m}[{w}OK{m}]")
    except:
        print(f"                        {m}[{w}HIT{m}] {r}Oops {y}{ip} {r}is down {lb}[{y}By Noxius{lb}]")

ip = input(f"{m}[{w}>>>{m}] {black}IP:{y} ")
print("")
port = input(f"{m}[{w}>>>{m}] {black}Port:{y} ")
print("")
while True:
    try:
        os.system(f"Ping to {ip} in port {port} -")
        tcpping(ip,int(port))
        time.sleep(0.25)
    except KeyboardInterrupt:
        exit(0)