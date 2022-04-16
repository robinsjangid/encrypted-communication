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


