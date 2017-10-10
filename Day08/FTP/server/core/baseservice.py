# from model import User
import os, pickle

class BaseService(object):
    # 基础服务类，负责底层数据交互

    def __init__(self):
        self.BASEPATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def auth(self, data):
        # 用户登录
        path = os.path.join(self.BASEPATH, "db")
        find_user = 0
        login_data = {}
        with open(os.path.join(path, "user.txt"), "r", encoding="utf8") as f:
            for line in f:
                if data.get("username") == line.split()[0]:
                    find_user = 1
                    break
        if find_user:
            # 该用户存在
            user = self.get_user(data.get("username"))
            if data.get("password") == user.password:
                # 登录成功
                login_data["login"] = "success"
                login_data["user"] = user
            else:
                # 密码错误
                login_data["login"] = "fail"
                login_data["msg"] = "密码错误!"
        else:
            # 该用户不存在
            login_data["login"] = "fail"
            login_data["msg"] = "用户不存在!"
        return login_data

    def save_user(self, user):
        # 保存用户信息
        path = os.path.join(self.BASEPATH, "db", "user")
        with open(os.path.join(path, user.name+".pickle"), "wb") as f:
            user = pickle.dump(user, f)

    def get_user(self, username):
        # 根据唯一用户名获取用户实例
        path = os.path.join(self.BASEPATH, "db", "user")
        with open(os.path.join(path, username+".pickle"), "rb") as f:
            user = pickle.load(f)
        return user

    def get_path(self, path):
        # 返回目录绝对地址
        cmd_path_list = path.split("\\")
        dir_path = os.path.join(self.BASEPATH, "home", cmd_path_list[0])
        if cmd_path_list.__len__() > 1:
            for i in range(cmd_path_list.__len__() - 1):
                dir_path = os.path.join(dir_path, cmd_path_list[i + 1])
        return dir_path



