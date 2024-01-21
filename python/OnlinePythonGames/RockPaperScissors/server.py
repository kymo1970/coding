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


def readPos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


def makePos(tup):
    return str(tup[0]) + "," + str(tup[1])      


pos = [(0, 0), (400, 400)]
def threadedClient(conn, player):
    conn.send(str.encode(makePos(pos[player])))
    reply = ""
    while True:
        try:
            data = readPos(conn.recv(2048).decode())
            print(data)
            pos[player] = data
            # reply = data.decode("utf-8")
            
            if not data:
                print("Disconnected")
                break
            else:
                if pos[player] == 1:
                    reply = pos[0]
                else:
                    reply = pos[1]
                        
                print("Received: ", data)
                print("Sending: ", reply)
                
            conn.sendall(str.encode(makePos(reply)))
        except:
            break        
    
    print("Lost Connection!")
    conn.close()        

currentPlayer = 0
while True:
    conn, addr = sock.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threadedClient, (conn, currentPlayer))
    
    currentPlayer += 1
    
