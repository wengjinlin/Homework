import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(BASE_DIR,"db")

def login_user(name,password):
    #用户登录
    path_user = os.path.join(path,"user")
    with open(path_user,"r",encoding="utf8") as f_r:
        for line in f_r:
            x = line.strip()[:line.strip().index(" ")]
            y = line.strip()[line.strip().index(" ") + 1:]
            if name == x and password == y:
                return "登录成功"
    return "用户名或密码错误"


