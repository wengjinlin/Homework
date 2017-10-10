import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from core.model import User
from core.baseservice import BaseService

service = BaseService()

def home_content(username):
    #返回用户家目录
    path = os.path.join(BASE_DIR, "home", username)
    os.makedirs(path)
    return path

def add_user(username):
    #保存新用户到用户信息表
    path = os.path.join(BASE_DIR, "db", "user.txt")
    with open(path, "a", newline="\n") as f:
        f.write(username+"\n")

if __name__ == '__main__':
    #初始化用户
    u1 = User("user1", "123", home_content("user1"), 1*1024*1024, 1*1024*1024)
    u2 = User("user2", "123", home_content("user2"), 10*1024*1024, 10*1024*1024)
    u3 = User("user3", "123", home_content("user3"), 100*1024*1024, 100*1024*1024)
    u4 = User("user4", "123", home_content("user4"), 500*1024*1024, 500*1024*1024)
    u = (u1, u2, u3, u4)
    for i in range(4):
        service.save_user(u[i])
        add_user(u[i].name)
