import socket
import threading
import os
import time

class ftp_client(object):
    def __init__(self):
        self.ip = "192.168.1.3"
        self.port = 8888
        self.client = socket.socket()
        self.client.connect((self.ip, self.port))

    def run(self):
        while True:
            msg = input(">>:").strip()
            if msg.split()[0] == "dl":
                self.client.send(msg.encode("utf-8"))
                self.download(msg.split()[1])
            elif msg.split()[0] == "ul":
                self.upload(msg.split()[1])
            else:
                self.client.send(str(msg).encode("utf-8"))
                rec = self.client.recv(1024)
                print(rec)

    def upload(self, file_name):
        # 上传文件
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file", file_name)
        total_size = os.stat(path).st_size
        print(total_size)
        msg = "ul " + file_name + " " + str(total_size)
        self.client.send(msg.encode("utf-8"))
        self.init_cent()
        send_size = 0
        with open(path, "rb") as f:
            for line in f:
                self.client.sendall(line)
                send_size += len(line)
                self.show_bar(total_size, send_size)
        if send_size == total_size:
            print("上传成功！")
        else:
            print("上传失败！")

    def download(self, file_name):
        # 下载文件
        total_size = int(self.client.recv(1024).decode("utf-8"))
        recv_size = 0
        size = 0
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file", file_name)
        self.init_cent()
        with open(path, "wb") as f_w:
            while recv_size < total_size:
                if total_size - recv_size > 1024:
                    size = 1024
                else:
                    size = total_size - recv_size
                line = self.client.recv(size)
                f_w.write(line)
                recv_size += len(line)
                self.show_bar(total_size, recv_size)
            else:
                print("下载完成！")

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


if __name__ == '__main__':
    client = ftp_client()
    client.run()
    # cl = []
    # t = []
    # for i in range(500):
    #     cl.append(ftp_client())
    #     t.append(threading.Thread(target=cl[i].run, args=(i,)))
    #     t[i].start()

