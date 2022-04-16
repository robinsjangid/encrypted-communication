# CLIENT CODE
# Update 1.1 AES Encryption Now Included :p
# AES Block Cipher 16 bytes block size as supported by pyaes
# Server Code Must Be Running Before Starting Client or Connection will be refused

import os
try:
    import pyaes
except ImportError:
    print("Install pyaes library!")
    print("windows : python -m pip insatll pyaes")
    print("linux   : pip install pyaes ")
    exit()
# importing socket library
import socket
import threading
import hashlib
import json
from datetime import datetime


print("[+] Client Running ")
#
HOST = str(input('[+] Enter Destination IP   : '))
PORT = int(input('[+] Enter Destination Port : '))
try:
# Creating socket instance
# with input parameters AF_INETwhich refers to address family ipv4 and
#SOCK_STREAM for connection oriented TCP protocol


    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
