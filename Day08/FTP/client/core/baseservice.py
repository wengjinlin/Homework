import os, shutil

class BaseService(object):
    #基础服务类，提供业务基础服务

    def auth(self):
        username = input("用户名：").strip()
        password = input("密码：").strip()
        self.data = {"username": username,
                     "password": password}

    # def cmd(self, cmd):
    #     #命令选择器
    #     cmd_com = cmd.split()[0]
    #     if hasattr(self, "_%s" % cmd_com):
    #         func = getattr(self, "_%s" % cmd_com)
    #     else:
    #         print("\033[31;1m无效命令(输入help获得帮助)！\033[0m")
    #     return func

    def _help(self):
        #帮助菜单
        msg = '''
        /*************************help*************************/
        cd : change the dir |cd     : home dir
                             cd ..  : upper dir
                             cd dir : into the dir,must be in this dir
        ls : show all files and dirs
        dl : download file |dl file : must be in this dir
        ul : upload file |ul path+file : must use the absolute address
        exit : quit
        '''
        print("\033[34;1m" + msg + "\033[0m")

    def _cd(self, cmd, path):
        # 切换目录命令
        data = {"cmd_com": cmd.split()[0],
                "cmd_sec": False,
                "path": path}
        if cmd.split().__len__() > 1:
            # 有二级命令：
            data["cmd_sec"] = True
            data["cmd_con"] = cmd.split()[1]
        return data

    def _ls(self, cmd, path):
        # 显示目录下文件及子目录
        data = {"cmd_com": cmd.split()[0],
                "path": path}
        return data

    def _dl(self, cmd, path):
        # 下载文件
        data = {"cmd_com": cmd.split()[0],
                "cmd_sec": False,
                "path": path}
        if cmd.split().__len__() > 1:
            # 有二级命令：
            data["cmd_sec"] = True
            data["cmd_con"] = cmd.split()[1]
        return data

    def _ul(self, cmd, path):
        # 上传文件
        data = {"cmd_com": cmd.split()[0],
                "cmd_sec": False,
                "path": path}
        if cmd.split().__len__() > 1:
            # 有二级命令：
            data["cmd_sec"] = True
            data["cmd_con"] = cmd.split()[1]
            data["filename"] = os.path.basename(cmd.split()[1])
        return data

    def get_temp_dir(self):
        # 获取临时文件夹路径
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        download_path = os.path.join(path, "download", "temp")
        return download_path

    def move_file(self, file, from_path, to_path):
        # 将临时文件夹中下载完成的文件移动到用户文件夹下
        if not os.path.isdir(to_path):
            os.makedirs(to_path)
        shutil.move(os.path.join(from_path, file), to_path)
        # 强制删除原文件
        if os.path.isfile(os.path.join(from_path, file)):
            os.remove(os.path.join(from_path, file))

    def get_user_path(self, username):
        # 获取用户下载文件夹路径
        path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        user_path = os.path.join(path, "download", username)
        return user_path
