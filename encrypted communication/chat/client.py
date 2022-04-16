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


def verify_and_display(recv_dict):
    # Assigning 'timestamp','hash','message' from input parameter recv_dict and creating a secure
    # hash algorithm using SHA256
    timestamp = recv_dict['timestamp']
    recv_hash = recv_dict['hash']
    message = recv_dict['message']
    mess_hash = hashlib.sha256(str(message).encode('utf-8')).hexdigest()
    SET_LEN = 80
    if (mess_hash == recv_hash):
        tag = str('☑')
    else:
        tag = str('☒')
    spaces = SET_LEN - len(str(message)) - len('Received : ') - 1
    if spaces > 0:
        space = ' ' * spaces
        sentence = 'Received : ' + str(message) + space + tag + '  ' + timestamp
        print(sentence)


class myThread(threading.Thread):
    def __init__(self, id):
        threading.Thread.__init__(self)
        self.threadID = id

    def stop(self):
        self.is_alive = False

    def run(self):
        print("[+] Listening On Thread " + str(self.threadID))
        while 1:
            try:

                data = s.recv(1024)
                if (data != ""):
                    mess = ''
                    processed_data = process_bytes(data)
# iterating processed_date from return of process_bytes method
                #    for dat in processed_data
# decrypting with AES CRYPT
                        decrypted = aes.decrypt(dat)
                        for ch in decrypted:
                            if(chr(ch)!='~'):
                                mess+=str(chr(ch))
                    try:
# Parsing json string and converting to Python dictionary
                        data_recv = json.loads(mess)
                        #message = str(data_recv['message'])
                        verify_and_display(data_recv)
#Handling exception
                    except:
                        print('Unrecognised Data or Broken PIPE ')
            except ConnectionResetError:
                print('Broken PIPE!')
# creating a daemon thread and starting a thread
Listening_Thread = myThread(1)
Listening_Thread.daemon = True
Listening_Thread.start()


while 1:
    try:
        sending_data = str(input(""))
    except KeyboardInterrupt:
        s.close()
        exit(-1)
    if(sending_data=="quit()"):
        Listening_Thread.stop()
        s.close()
        exit()
    timestamp = str(datetime.now())[11:19]
    mess_hash = hashlib.sha256(str(sending_data).encode('utf-8')).hexdigest()
    send_data = {
        "timestamp" : timestamp,
        "message"   : sending_data,
        "hash"      : mess_hash
    }