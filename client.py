import socket 

print("THIS IS A CLIENT")

addr = ('')
port = 1457

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.bind((addr,port))

client.listen()
print('listening to the port %s' %port)

while True:
     conn, addr = client.accept()
     print(f"connected to {addr}")
     rec = conn.recv(1024)
     print(rec.decode('utf-8'))
     break


