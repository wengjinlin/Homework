import socket

def get_connect(ip_port):
    sk = socket.socket()
    sk.connect(ip_port)
    return sk