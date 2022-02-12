import socket

#каким образом будем принимать данные (inet, bluetooth or etc)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # 2 = protocol TCP/ip

server.bind(("127.0.0.1", 12345))


server.listen()


while True:
    user, address = server.accept()

    user.send(input().encode("utf-8"))

    data = user.recv(1024)

    print(data.decode("utf-8"))