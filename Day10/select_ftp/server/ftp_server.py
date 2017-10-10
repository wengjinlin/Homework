
import select
import socket
import sys
import queue
import os

class ftp_server(object):

    def __init__(self):
        # 建立链接
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.setblocking(False)

        # 绑定端口
        server_address = ('0.0.0.0', 8888)
        self.server.bind(server_address)

        # 监听链接
        self.server.listen(5)

        # 读取的链接
        self.inputs = [self.server]

        # 发送的链接
        self.outputs = []

        # 数据
        self.message_queues = {}

        # 上传链接字典
        self.upload_dict = {}

    def download(self, file_name, s):
        # 客户端请求下载文件
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file", file_name)
        total_size = os.stat(path).st_size
        self.message_queues[s].put(str(total_size).encode("utf-8"))
        f = open(path, 'rb')
        for line in f:
            self.message_queues[s].put(line)
        # Add output channel for response
        if s not in self.outputs:
            self.outputs.append(s)

    def upload(self, s, data):
        # 客户端请求上传文件
        data_size = len(data)
        if self.upload_dict[s]["recv_size"] + data_size < self.upload_dict[s]["total_size"]:
            self.upload_dict[s]["file"].write(data)
            self.upload_dict[s]["recv_size"] += data_size
        else:
            size = self.upload_dict[s]["total_size"] - self.upload_dict[s]["recv_size"]
            self.upload_dict[s]["file"].write(data[0:size])
            self.upload_dict[s]["recv_size"] += len(data[0:size])
        if self.upload_dict[s]["recv_size"] == self.upload_dict[s]["total_size"]:
            # 上传完成
            self.upload_dict[s]["file"].close()
            del self.upload_dict[s]

    def handle_inputs(self, readable):
        # Handle inputs
        for s in readable:
            if s is self.server:
                # 新连接
                connection, client_address = s.accept()
                print('new connection from', client_address)
                connection.setblocking(False)
                self.inputs.append(connection)

                # Give the connection a queue for data we want to send
                self.message_queues[connection] = queue.Queue()
            else:
                try:
                    data = s.recv(1024)
                    if data:
                        # 有数据
                        if s in self.upload_dict.keys():
                            # 该数据是上传的文件数据
                            self.upload(s, data)
                        else:
                            data = data.decode("utf-8")
                            if data.split()[0] == "dl":
                                # 客户端请求下载文件
                                self.download(data.split()[1], s)
                            elif data.split()[0] == "ul":
                                # 客户端请求上传文件
                                # self.upload(data.split()[1], data.split()[2], s)
                                path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file", data.split()[1])
                                total_size = int(data.split()[2])
                                self.upload_dict[s] = {}
                                # self.upload_dict[s]["path"] = path
                                self.upload_dict[s]["total_size"] = total_size
                                self.upload_dict[s]["recv_size"] = 0
                                self.upload_dict[s]["file"] = open(path, "wb")
                            else:
                                self.message_queues[s].put(data.encode("utf-8"))
                                # Add output channel for response
                                if s not in self.outputs:
                                    self.outputs.append(s)
                    else:
                        # 客户端正常退出机制
                        print('closing after reading no data')
                        # Stop listening for input on the connection
                        if s in self.outputs:
                            self.outputs.remove(s)  # 既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                        self.inputs.remove(s)  # inputs中也删除掉
                        s.close()  # 把这个连接关闭掉

                        # Remove message queue
                        del self.message_queues[s]
                except ConnectionResetError as e:  # windows客户端强制关闭机制
                    print('lost...')
                    # Stop listening for input on the connection
                    if s in self.outputs:
                        self.outputs.remove(s)  # 既然客户端都断开了，我就不用再给它返回数据了，所以这时候如果这个客户端的连接对象还在outputs列表中，就把它删掉
                    self.inputs.remove(s)  # inputs中也删除掉
                    s.close()  # 把这个连接关闭掉

                    # Remove message queue
                    del self.message_queues[s]

    def handle_outputs(self, writable):
        # Handle outputs
        for s in writable:
            try:
                next_msg = self.message_queues[s].get_nowait()
            except queue.Empty:
                # No messages waiting so stop checking for writability.
                print('output queue for', s.getpeername(), 'is empty')
                self.outputs.remove(s)
            else:
                # print('sending "%s" to %s' % (next_msg, s.getpeername()))
                s.send(next_msg)

    def handle_exceptional(self, exceptional):
        # Handle "exceptional conditions"
        for s in exceptional:
            print('handling exceptional condition for', s.getpeername())
            # Stop listening for input on the connection
            self.inputs.remove(s)
            if s in self.outputs:
                self.outputs.remove(s)
            s.close()

            # Remove message queue
            del self.message_queues[s]

    def run(self):
        while self.inputs:
            # 等待下一个已准备好的连接
            readable, writable, exceptional = select.select(self.inputs, self.outputs, self.inputs)

            self.handle_inputs(readable)
            self.handle_outputs(writable)
            self.handle_exceptional(exceptional)


if __name__ == '__main__':
    server = ftp_server()
    server.run()