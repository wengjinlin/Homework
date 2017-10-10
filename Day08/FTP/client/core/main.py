import os, sys, socket, pickle
from conf import config
from service import Service
from baseservice import BaseService

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)

def run():
    ip = "192.168.1.3"
    port = 9999
    ip_port = (ip, port)
    client = config.get_connect(ip_port)
    service = Service(client)
    login_user = service.auth()
    path = login_user.get("user").name
    while True:
        cmd = input(path+">>:").strip()
        if not cmd:
            continue
        if cmd == "exit":
            break
        path = service.cmd(cmd, path)
    client.close()
