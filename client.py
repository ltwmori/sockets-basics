from multiprocessing.connection import Client
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 2 = protocol TCP/ip


client.connect(("127.0.0.1", 12345))


while True:
    data = client.recv(1024)
    print(data.decode("utf-8")) 


    client.send(input().encode("utf-8"))