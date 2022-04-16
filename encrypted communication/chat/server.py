# SERVER CODE
# Update 1.1 AES Encryption Now Included :p
# AES Block Cipher 16 bytes block size as supported by pyaes
# You Can Change the Port Server Listens by passing argument in command line directly
# Server Code To be Started before Client, or Connection will be refused

import os
try:
    import pyaes
except ImportError:
    print("Install pyaes library!")
    print("windows : python -m pip insatll pyaes")
    print("linux   : pip install pyaes ")
    exit()
# import statements
import sys
import socket
import threading
import hashlib
import json
from datetime import datetime


HOST = '0.0.0.0'
if(len(sys.argv)==1):
    PORT = 5555
elif(len(sys.argv)==2):
    PORT=int(sys.argv[1])


print("[+] Server Running ")
print("[+] Allowing All Incoming Connections ")
print("[+] PORT "+str(PORT))
print("[+] Waiting For Connection...")
# Creating socket instance
# with input parameters AF_INETwhich refers to address family ipv4 and
#SOCK_STREAM for connection oriented TCP protocol


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print('[+] Connected by ', addr)


key = str(input('[+] AES Pre-Shared-Key for the Connection : '))
# Creating secure hash algorithm using sha256 constructor to create SHA256 hash


hashed = hashlib.sha256(key.encode()).digest()
aes = pyaes.AES(hashed)


def verify_and_display(recv_dict):


