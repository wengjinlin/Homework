import paramiko
import os
import threading
import queue

class Fabric(object):

    def __init__(self):
        # 获取主机或主机组信息
        self.computer_list = self.get_computers()
        self.groups = self.get_computers_groups()
        # 指定主机或主机组
        self.ex_computers = []
        # 执行结果队列
        self.result = queue.Queue()

    def get_computers(self):
        # 获取文件中的所有主机列表
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db")
        computer_list = {}
        computer = {}
        with open(os.path.join(path, "computers.txt"), "r") as f_computers:
            for line in f_computers:
                data = line.strip()
                computer["hostname"] = data.split()[0]
                computer["port"] = int(data.split()[1])
                computer["name"] = data.split()[2]
                computer["password"] = data.split()[3]
                computer_list[data.split()[0]] = computer
                computer = {}
        return computer_list

    def get_computers_groups(self):
        # 获取文件中主机分组信息
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "db")
        groups = []
        with open(os.path.join(path, "groups.txt"), "r") as f_g:
            for line in f_g:
                group_s = []
                data = line.strip()
                with open(os.path.join(path, data + ".txt"), "r") as f_g_s:
                    for line_2 in f_g_s:
                        data_2 = line_2.strip()
                        group_s.append(data_2)
                groups.append(group_s)
        return groups

    def print_computers_list(self):
        print("--------主机列表--------")
        for c in self.computer_list:
            print(c)

    def print_groups(self):
        print("--------主机组--------")
        i = 1
        for group in self.groups:
            print("******group:%s******" %i)
            for c in group:
                print(c)
            i += 1

    def print_menu(self):
        print("/********Fabric********/")
        print("1.指定主机")
        print("2.指定主机组")
        print("3.退出系统")

    def do(self):
        # 用户可操作选项
        # print(self.ex_computers)
        while True:
            print("1.执行命令")
            print("2.传输文件")
            print("3.重新选择主机")
            choose = input(">>:").strip()
            if choose == "1":
                self.execute_cmd()
            elif choose == "2":
                self.transmission_file()
            elif choose == "3":
                break

    def transmission_file(self):
        # 文件传输
        while True:
            print("----传输文件----")
            cmd = input(">>:").strip()
            if cmd == "exit":
                break
            if cmd == "help":
                print("***help***")
                print("upload:put filename(abspath) new_name(abspath)")
                print("download:get filename(abspath) new_name(just new_filename)")
            cm = cmd.split()[0]
            if cm != "put" and cm != "get":
                print("命令有误，输入help查看帮助")
                continue
            count = 0
            for i in self.ex_computers:
                computer = self.computer_list[i]
                t = threading.Thread(target=self._file, args=(computer, cm, cmd.split()[1], cmd.split()[2]))
                t.start()
                count += 1
            print("--------命令结果--------")
            for i in range(count):
                print(self.result.get())

    def _file(self, computer, cmd, file1, file2):
        # 文件传输具体实现
        transport = paramiko.Transport((computer["hostname"], computer["port"]))
        transport.connect(username=computer["name"], password=computer["password"])

        sftp = paramiko.SFTPClient.from_transport(transport)
        # 将location.py 上传至服务器 /tmp/test.py
        # sftp.put('/tmp/location.py', '/tmp/test.py')
        # 将remove_path 下载到本地 local_path
        # sftp.get('remove_path', 'local_path')
        path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "file")
        if cmd == "put":
            sftp.put(file1, file2)
        if cmd == "get":
            sftp.get(file1, os.path.join(path, "from_%s_%s" % (computer["hostname"], file2)))
        result = "%s is ok" % computer["hostname"]
        self.result.put(result)
        transport.close()

    def execute_cmd(self):
        # 执行命令
        while True:
            print("----执行命令----")
            cmd = input(">>:").strip()
            if cmd == "exit":
                break
            count = 0
            for i in self.ex_computers:
                computer = self.computer_list[i]
                t = threading.Thread(target=self._cmd, args=(computer, cmd,))
                t.start()
                count += 1
            for i in range(count):
                print(self.result.get())

    def _cmd(self, computer, cmd):
        # 执行命令具体实现
        transport = paramiko.Transport((computer["hostname"], computer["port"]))
        transport.connect(username=computer["name"], password=computer["password"])

        ssh = paramiko.SSHClient()
        ssh._transport = transport

        stdin, stdout, stderr = ssh.exec_command(cmd)

        result = ""
        if stderr:
            result = stderr.read()
        if stdout:
            result = stdout.read()
        # print("--------命令结果：%s--------" % computer["hostname"])
        # print(result.decode())
        a = "--------命令结果：%s--------\n" % computer["hostname"]
        self.result.put(a+result.decode())
        transport.close()

    def run(self):
        # 主执行流程
        while True:
            self.print_menu()
            cmd = input(">>:").strip()
            if cmd == "1":
                self.print_computers_list()
                choose = input(">>:").strip()
                if choose in self.computer_list.keys():
                    self.ex_computers.append(choose)
                else:
                    print("指定主机不存在！")
            elif cmd == "2":
                self.print_groups()
                choose = input(">>:").strip()
                if int(choose) <= len(self.groups):
                    for c in self.groups[int(choose)-1]:
                        self.ex_computers.append(c)
                else:
                    print("指定主机组不存在！")
            elif cmd == "3":
                break
            if self.ex_computers:
                self.do()
                self.ex_computers = []



