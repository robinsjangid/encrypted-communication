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
# Catching an exception
except ConnectionError:
    print('Could Not Connect !')
    exit(-1)
key = str(input('[+] AES Pre-Shared-Key For Connection :'))
# Creating secure hash algorithm using sha256 constructor to create SHA256 hash
hashed = hashlib.sha256(key.encode()).digest()
aes = pyaes.AES(hashed)
def process_bytes(bytess):
    ret = []
# Iterate till length of bytes is greater than or equal to 16
    while(len(bytess)>=16):
        if(len(bytess)>=16):
            byts = bytess[:16]
            ret.append(byts)
            bytess = bytess[16:]
        else:
            print("Block Size Mismatch ")
    return ret
def process_text(data): #take data in as a string return 16 bytes block of bytes list
    streams = []
    while (len(data)>0):
        if(len(data)>=16):
            stream = data[:16]
            data = data[16:]
        else:
            stream = data + ("~"*(16-len(data)))
            data = ''
        stream_bytes = [ ord(c) for c in stream]
        streams.append(stream_bytes)
    return streams