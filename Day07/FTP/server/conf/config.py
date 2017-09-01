import socket

ip = "192.168.1.3"
port = 9999

def get_socket():
    ip_port = (ip, port)
    sk = socket.socket()
    sk.bind(ip_port)
    sk.listen(5)
    return sk
