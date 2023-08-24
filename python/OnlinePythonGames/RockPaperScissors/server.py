import socket
from _thread import *
import sys

server = "192.168.12.192"
port = 5555

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.bind((server, port))
except socket.error as e:
    str(e)

sock.listen(2)
print("Waiting for connection, Server has been started.")        


def threadedClient(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
                
            conn.sendall(str.encode(reply))
        except:
            break        


while True:
    conn, addr = sock.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threadedClient, conn)
    
    
    