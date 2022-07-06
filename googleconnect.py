import socket
import sys

port = 80
try:
    S = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("socket successfully created")
except:
    err = socket.error()
    print(err)


host = socket.gethostbyname("www.google.com")


S.connect((host,port))

print(f'google has this ip == {host}')
