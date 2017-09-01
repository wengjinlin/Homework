import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
download_path = os.path.join(os.path.dirname(BASE_DIR),"download")

from conf import config
import socket,pickle,os


def run():
    ip = input("服务器IP：").strip()
    port = input("端口号：").strip()
    ip_port = (ip,int(port))
    client = config.get_connect(ip_port)
    client.sendall(b"start")
    menu = pickle.loads(client.recv(1024))
    while True:
        print_menu(menu)
        msg = input(">>:").strip()
        if msg == "exit":
            break
        if msg not in menu:
            continue
        client.sendall(msg.encode("utf-8"))
        if msg == "login":
            login(client)
        elif msg == "check":
            check(client)
        elif msg == "upload":
            upload(client)
        elif msg == "download":
            download(client)
    client.close()

def print_menu(menu):
    for i in menu:
        print("\033[34;1m%s\033[0m" % i)

def login(client):
    user_name = input("用户名：").strip()
    user_password = input("密码：").strip()
    user_msg = [user_name,user_password]
    client.sendall(pickle.dumps(user_msg))
    answer = client.recv(1024)
    print(answer.decode())

def check(client):
    answer = client.recv(1024)
    if answer == b"login_fail":
        print("请先登录")
    if answer == b"login_success":
        list = pickle.loads(client.recv(1024))
        if list:
            print("\033[31;1m*****目录文件*****\033[0m")
            for i in list:
                print(i)
        else:
            print("\033[31;1m目录为空\033[0m")

def upload(client):
    answer = client.recv(1024)
    if answer == b"login_fail":
        print("请先登录")
    if answer == b"login_success":
        while True:
            file = input("上传文件路径(带文件名完整路径)：")
            if os.path.isfile(file):
                client.sendall(pickle.dumps(file))
                print("\033[34;1m文件上传中...\033[0m")
                with open(file, "rb") as f_r:
                    for line in f_r:
                        client.sendall(line)
                client.sendall(b"finish")
                break
            else:
                print("\033[31;1m文件不存在\033[0m")
        if client.recv(1024) == b"success":
            print("\033[31;1m上传成功\033[0m")
        else:
            print("\033[31;1m上传失败\033[0m")

def download(client):
    answer = client.recv(1024)
    if answer == b"login_fail":
        print("\033[31;1m请先登录\033[0m")
    if answer == b"login_success":
        list = pickle.loads(client.recv(1024))
        if list:
            print("\033[31;1m*****目录文件*****\033[0m")
            for i in list:
                print(i)
            while True:
                file_name = input("文件名：")
                if file_name not in list:
                    print("\033[31;1m文件名输入错误\033[0m")
                else:
                    client.sendall(file_name.encode("utf-8"))
                    break
            print("\033[34;1m文件下载中...\033[0m")
            with open(os.path.join(download_path, file_name), "wb") as f_w:
                while True:
                    line = client.recv(1024)
                    if line == b"finish":
                        print("\033[31;1m下载完成\033[0m")
                        break
                    else:
                        f_w.write(line)
        else:
            print("\033[31;1m目录为空,无可下载文件\033[0m")