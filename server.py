'''
Created on Mar 8, 2022

@author: kymo1
'''
import socket
import threading

HEADER = 128
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handleClient(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")
    
    connected = True
    while connected:
        msgLength = conn.recv(HEADER).decode(FORMAT)
        if msgLength:
            msgLength = int(msgLength)
            msg = conn.recv(msgLength).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("Message recieved".encode(FORMAT))


    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    
    listening = True
    while listening:
        conn, addr = server.accept()
        thread = threading.Thread(target = handleClient, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server is starting!")
start()
