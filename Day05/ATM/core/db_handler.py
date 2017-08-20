# -*- coding: utf-8 -*-
import os,json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def existence(user_name):
    #根据用户名判定该用户是否已存在
    with open(BASE_DIR + "/db/account", "r") as f_r:
        for line in f_r:
            if user_name in line:
                return True
    return False
def save(user):
    #持久化用户信息
    with open(BASE_DIR + "/db/accounts/"+user["user_name"]+".json", "w") as f_w:
        f_w.write(json.dumps(user))
def add(user_name):
    #添加新用户到account表
    with open(BASE_DIR + "/db/account", "a") as f_a:
        f_a.write(user_name+"\n")
def getuser(user_name):
    #根据用户名获取用户
    with open(BASE_DIR + "/db/accounts/"+user_name+".json", "r") as f_r:
        user = json.loads(f_r.read())
    return user
def print_bill(user_name,date):
    with open(BASE_DIR + "/log/transactions.log", "r",encoding="utf8") as f_r:
        for line in f_r:
            if user_name in line and date in line:
                print(line.strip())
def mall_existence(user_name):
    # 根据用户名判定该用户是否已存在
    with open(BASE_DIR + "/db/mall/account", "r") as f_r:
        for line in f_r:
            if user_name in line:
                return True
    return False
def mall_getuser(user_name):
    # 根据用户名获取用户
    with open(BASE_DIR + "/db/mall/accounts/" + user_name + ".json", "r") as f_r:
        user = json.loads(f_r.read())
    return user
def mall_print_history(user_name):
    with open(BASE_DIR + "/log/mall/transactions.log", "r",encoding="utf8") as f_r:
        for line in f_r:
            if user_name in line:
                print(line.strip())