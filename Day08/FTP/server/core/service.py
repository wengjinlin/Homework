import socketserver, pickle, os, hashlib
from core.baseservice import BaseService


class FTPService(socketserver.BaseRequestHandler):

    def handle(self):
        print(self.client_address[0] + " has connected...")
        self.service = BaseService()
        while True:
            # 用户登录
            self.login_data = self.service.auth(self.get_request())
            self.send_response(self.login_data)
            if self.login_data.get("login") == "success":
                print("登录用户：", self.login_data.get("user").name)
                break
        while True:
            # 用户命令
            try:
                self.data = self.get_request()
            except ConnectionResetError as e:
                print(self.client_address[0] + " has lost...")
                print("用户退出：", self.login_data.get("user").name)
                break
            if not self.data:
                print(self.client_address[0] + " has closed...")
                print("用户退出：", self.login_data.get("user").name)
                break
            self.cmd(self.data)

    def get_request(self):
        # 获取数据到data
        data = self.request.recv(1024).strip()
        if not data:
            return
        format_data = pickle.loads(data)
        return format_data

    def send_response(self, data):
        # 发送data数据
        response = data
        self.request.sendall(pickle.dumps(response))

    def cmd(self, cmd):
        # 命令选择器
        cmd_com = cmd.get("cmd_com")
        getattr(self, "_%s" % cmd_com)(cmd)

    def _cd(self, cmd):
        # 切换目录命令
        dict = {"res": True}
        path = cmd.get("path")
        if cmd.get("cmd_sec"):
            # 有二级命令
            if cmd.get("cmd_con") == "..":
                # 返回上一层目录
                index = path.index(path.split("\\")[path.split("\\").__len__() - 1])
                path = path[:index - 1]
            else:
                # 进入指定目录
                into_path = os.path.join(self.service.get_path(cmd.get("path")), cmd.get("cmd_con"))
                if os.path.isdir(into_path):
                    # 存在指定目录
                    path = path + "\\" + cmd.get("cmd_con")
                else:
                    # 指定目录不存在
                    dict["res"] = False
                    dict["msg"] = "指定目录不存在!"
        else:
            # 返回家目录
            path = self.login_data.get("user").name
        dict["path"] = path
        self.send_response(dict)

    def _ls(self, cmd):
        # 显示目录下文件及子目录
        path = self.service.get_path(cmd.get("path"))
        data = os.listdir(path)
        dict = {"total": data.__len__(),
                "dir": [],
                "file": []}
        for i in data:
            if os.path.isfile(os.path.join(path, i)):
                dict["file"].append(i)
            if os.path.isdir(os.path.join(path, i)):
                dict["dir"].append(i)
        self.send_response(dict)

    def _dl(self, cmd):
        # 下载文件
        dict = {"start": True}
        path = self.service.get_path(cmd.get("path"))
        if not os.path.isfile(os.path.join(path, cmd.get("cmd_con"))):
            # 文件不存在
            dict["start"] = False
            dict["msg"] = "当前目录不存在该文件！"
            self.send_response(dict)
            return
        # 开始下载前必要数据传送
        dict["file_size_total"] = os.stat(os.path.join(path, cmd.get("cmd_con"))).st_size
        self.send_response(dict)
        if self.get_request() == "ready":
            # 开始下载
            self.send_file(os.path.join(path, cmd.get("cmd_con")))

    def _ul(self, cmd):
        # 上传文件
        # 接收前置数据
        self.send_response("ready")
        # 接收文件
        self.receive_file(cmd.get("path"), cmd.get("filename"), cmd.get("file_size_total"))

    def send_file(self, path):
        # 发送文件
        m = hashlib.md5()
        with open(path, "rb") as f_r:
            for line in f_r:
                m.update(line)
                self.request.sendall(line)
        self.send_response(m.hexdigest())

    def receive_file(self, path, filename, file_size_total):
        # 接收文件
        m = hashlib.md5()
        file_size = 0
        path = self.service.get_path(path)
        with open(os.path.join(path, filename), "wb") as f_w:
            while file_size < file_size_total:
                if file_size_total - file_size > 1024:
                    size = 1024
                else:
                    size = file_size_total - file_size
                line = self.request.recv(size)
                m.update(line)
                f_w.write(line)
                file_size += len(line)
        client_m = self.get_request()
        if file_size == file_size_total:
            if client_m == m.hexdigest():# 验证MD5值
                self.send_response("success")
                # 保存用户信息（剩余空间减少）
                self.login_data.get("user").set_limit_space(file_size_total)
                self.service.save_user(self.login_data.get("user"))
                return
        os.remove(os.path.join(path, filename))
        self.send_response("fail")
