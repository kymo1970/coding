'''
Created on Mar 8, 2022

@author: kymo1
'''
import socket

HEADER = 128
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "127.0.1.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msgLength = len(message)
    sendLength = str(msgLength).encode(FORMAT)
    sendLength += b' ' * (HEADER - len(sendLength))
    client.send(sendLength)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World, Eat My Dust!!")
#send(DISCONNECT_MESSAGE)
