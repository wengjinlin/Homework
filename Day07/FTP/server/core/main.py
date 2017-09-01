import os
import sys
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(BASE_DIR)
db_path = os.path.join(os.path.dirname(BASE_DIR), "db")

from conf import config
from user import User
import socket,pickle,db_handler,auth,os

login_user = User("tourist","")
menu = ["/------命令式FTP------/",
        "login",
        "check",
        "upload",
        "download",
        "exit"]

def run():
    server = config.get_socket()
    while True:
        conn, addr = server.accept()
        if conn.recv(1024) == b"start":
            conn.sendall(pickle.dumps(menu))
        login_user.NAME = "tourist"
        while True:
            order = conn.recv(1024)
            if not order:
                print("client has lost...")
                break
            if order == b"login":
                login(conn)
            elif order == b"check":
                check(conn)
            elif order == b"upload":
                upload(conn)
            elif order == b"download":
                download(conn)
        conn.close()
    server.close()

def login(conn): #登录
    user_msg = pickle.loads(conn.recv(1024))
    msg = db_handler.login_user(user_msg[0],user_msg[1])
    conn.sendall(msg.encode("utf-8"))
    if msg == "登录成功":
        login_user.NAME = user_msg[0]
        login_user.PASSWORD = user_msg[1]

@auth.login_if(login_user)
def check(conn): #查看目录
    list = os.listdir(os.path.join(db_path, login_user.NAME))
    conn.sendall(pickle.dumps(list))

@auth.login_if(login_user)
def upload(conn): #上传
    file_path = pickle.loads(conn.recv(1024))
    file_name = os.path.basename(file_path)
    with open(os.path.join(db_path, login_user.NAME,file_name), "wb") as f_w:
        while True:
            line = conn.recv(1024)
            if line == b"finish":
                conn.sendall(b"success")
                break
            else:
                f_w.write(line)

@auth.login_if(login_user)
def download(conn): #下载
    list = os.listdir(os.path.join(db_path, login_user.NAME))
    conn.sendall(pickle.dumps(list))
    file_name = conn.recv(1024).decode("utf-8")
    with open(os.path.join(db_path, login_user.NAME, file_name), "rb") as f_r:
        for line in f_r:
            conn.sendall(line)
    conn.sendall(b"finish")