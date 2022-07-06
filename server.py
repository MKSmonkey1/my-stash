import socket
#Server's host and port number
host = '192.168.1.35'
port = 23

#server ko bata rha hu ki internet ka socket use karna hai or TCP steam use karmi hai

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#server ko ip or port se bind kana kyunki fir pata chalega ki server kosa hai
server.bind((host,port))

#listening for inward connevtion on port(here 23)
server.listen()

print(f"server is listening on port = {port}")

#jab tak true hai connection established rahega while ni hoga to connect hote  hi disconnect ho jayega
while True:
    conn,addr = server.accept( )
    print(f"connecttion socket info is {conn},\n client address is {addr}")
