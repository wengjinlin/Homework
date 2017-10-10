import pickle, os, hashlib
from baseservice import BaseService

class Service(BaseService):
    # 服务类，业务服务

    def __init__(self, conn):
        self.client = conn

    def auth(self):
        # 登录功能
        while True:
            super(Service, self).auth()
            self.set_send(self.data)
            request_data = self.get_recv()
            if request_data.get("login") == "success":
                print("\033[31;1m登录成功!\033[0m")
                break
            else:
                print("\033[31;1m"+request_data.get("msg")+"\033[0m")
        self.user = request_data.get("user")
        return request_data

    def cmd(self, cmd, path):
        # 命令选择器
        cmd_com = cmd.split()[0]
        if hasattr(self, "_%s" % cmd_com):
            path = getattr(self, "_%s" % cmd_com)(cmd, path)
        else:
            print("\033[31;1m无效命令(输入help获得帮助)！\033[0m")
        return path

    def _help(self, cmd, path):
        # 帮助菜单
        super(Service, self)._help()
        return path

    def _cd(self, cmd, path):
        # 切换目录命令
        data = super(Service, self)._cd(cmd, path)
        self.set_send(data)
        dict = self.get_recv()
        if not dict.get("res"):
            # 命令执行失败
            print("\033[31;1m%s\033[0m" % dict.get("msg"))
        return dict.get("path")

    def _ls(self, cmd, path):
        # 显示目录下文件及子目录
        data = super(Service, self)._ls(cmd, path)
        self.set_send(data)
        dict = self.get_recv()
        if dict.get("total") == 0:
            print("\033[31;1m目录为空\033[0m")
        else:
            if dict.get("dir").__len__() == 0:
                print("\033[31;1m没有子目录\033[0m")
            else:
                print("\033[31;1m子目录为:\033[0m")
                print("", end="    ")
                for i in dict["dir"]:
                    print(i, end="  ")
                print()
            if dict.get("file").__len__() == 0:
                print("\033[31;1m没有文件\033[0m")
            else:
                print("\033[31;1m文件为:\033[0m")
                print("", end="    ")
                for i in dict["file"]:
                    print(i, end="  ")
                print()
        return path

    def _dl(self, cmd, path):
        # 下载文件
        data = super(Service, self)._dl(cmd, path)
        if not data.get("cmd_sec"):
            # 命令不全
            print("\033[31;1m请输入当前目录下的文件名\033[0m")
        else:
            # 发送下载命令
            self.set_send(data)
            dict = self.get_recv()
            if not dict["start"]:
                # 无法开始下载
                print("\033[31;1m%s\033[0m" % dict.get("msg"))
                return path
            # 开始下载
            self.set_send("ready")
            self.receive_file(path.split("\\")[0], data.get("cmd_con"), dict.get("file_size_total"))
        return path

    def _ul(self, cmd, path):
        # 上传文件
        data = super(Service, self)._ul(cmd, path)
        if not data.get("cmd_sec"):
            # 命令不全
            print("\033[31;1m请输入要上传的文件路径及文件名\033[0m")
        else:
            file_size_total = os.stat(data.get("cmd_con")).st_size
            if self.user.get_limit_space() >= file_size_total:
                # 空间配额足够
                data["file_size_total"] = file_size_total
                # 发送前置数据
                self.set_send(data)
                if self.get_recv() == "ready":
                    self.send_file(data.get("cmd_con"), file_size_total)
            else:
                print("\033[31;1m服务器空间余额不足,无法上传!\033[0m")
        return path

    def get_recv(self):
        # 获取数据到data
        data = self.client.recv(1024).strip()
        format_data = pickle.loads(data)
        return format_data

    def set_send(self, data):
        # 发送data数据
        self.client.sendall(pickle.dumps(data))

    def receive_file(self, username, filename, file_size_total):
        # 接收文件
        m = hashlib.md5()
        file_size = 0
        path = self.get_temp_dir()
        self.init_cent()
        with open(os.path.join(path, filename), "wb") as f_w:
            while file_size < file_size_total:
                if file_size_total - file_size > 1024:
                    size = 1024
                else:
                    size = file_size_total - file_size
                line = self.client.recv(size)
                m.update(line)
                f_w.write(line)
                file_size += len(line)
                self.show_bar(file_size_total, file_size)
        server_m = self.get_recv()
        if file_size == file_size_total:
            if server_m == m.hexdigest():# 验证MD5值
                self.move_file(filename, path, self.get_user_path(username))
                print("\033[31;1m下载完成！\033[0m")

    def show_bar(self, total, now):
        # 打印进度条
        per_cent = int((now / total) * 100)
        if self.cent[per_cent]:
            if per_cent < 10:
                print("%s   %%[" % per_cent, end="")
            elif per_cent == 100:
                print("%s %%[" % per_cent, end="")
            else:
                print("%s  %%[" % per_cent, end="")
            print("=" * per_cent, end="")
            print(" " * (100 - per_cent), end="")
            print("]")
            self.cent[per_cent] = False

    def init_cent(self):
        # 初始化需要显示的百分比控制列表
        self.cent = []
        for i in range(101):
            if i % 10 == 0:
                self.cent.append(True)
            else:
                self.cent.append(False)

    def send_file(self, path, file_size_total):
        # 发送文件
        m = hashlib.md5()
        self.init_cent()
        size = 0
        with open(path, "rb") as f_r:
            for line in f_r:
                m.update(line)
                self.client.sendall(line)
                size += len(line)
                self.show_bar(file_size_total, size)
        self.set_send(m.hexdigest())
        if self.get_recv() == "success":
            self.user.set_limit_space(file_size_total)
            print("\033[31;1m上传完成！\033[0m")
        else:
            print("\033[31;1m上传失败！\033[0m")