import pika
import random


class RPCcontrol(object):
    def __init__(self):
        # 初始化
        # 连接RabbitMQ
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        # 声明exchange
        self.channel.exchange_declare(exchange='cmd', exchange_type="direct")  # 执行命令的exchange
        # 声明Q
        self.channel.queue_declare(queue="online")  # 接收注册在线主机的Q
        # 声明消费
        self.channel.basic_consume(self.get_online, queue="online", no_ack=True)

        self.result_dict = {}  # 命令结果集
        self.online = []  # 在线主机

    def get_online(self, ch, method, props, body):
        # 注册在线主机
        pc = body.decode()
        if pc not in self.online:
            self.online.append(pc)

    def get_result(self, ch, method, props, body):
        # 获取命令执行结果
        # print("in the get_result")
        self.result_dict[props.correlation_id][props.app_id] = body.decode()
        # print(self.result)
        # print(props.app_id)
        # print("end the get_result")

    def get_task(self):
        # 创建唯一task值
        while True:
            task = str(random.randint(1000, 9999))
            if task in self.result_dict.keys():
                continue
            else:
                break
        return task

    def receive_message(self):
        # 接收消息
        self.connection.process_data_events()

    def do_cmd(self, cmd):
        # 分析cmd
        do = cmd.split(" ")[0]
        if do == "check_task":
            # 查询结果
            self.receive_message()
            task = cmd.split(" ")[1]
            if task in self.result_dict.keys():
                if self.result_dict[task]:
                    print("/-------------task id: %s-------------/" % task)
                    print("/-------task cmd: %s-------/" % self.result_dict[task+"_cmd"])
                    for key in self.result_dict[task]:
                        print("/****from_pc: %s****/" % key)
                        print(self.result_dict[task][key])
                else:
                    print("暂时没有命令结果，请稍后查询!")
            else:
                print("该task不存在！")
        elif do == "run":
            # 分解run命令
            command = cmd.split("\"")[1]
            cmd_pc = []
            if "--hosts" in cmd:
                # 指定主机
                cmd_pc = cmd[cmd.find("--hosts")+8:].split(" ")
            else:
                # 在线所有主机
                if self.online:
                    cmd_pc = self.online
                else:
                    print("无主机在线，无法执行命令")
                    return
            # 发送命令
            result = self.channel.queue_declare(exclusive=True)
            callback_queue = result.method.queue  # 接收命令结果的随机Q
            self.channel.basic_consume(self.get_result, no_ack=True, queue=callback_queue)  # 每个命令的接收Q都需要声明消费
            task = self.get_task()  # 每个命令分配一个task值
            self.result_dict[task] = {}  # 定义对应task的结果集
            self.result_dict[task+"_cmd"] = command  # 保存对应cmd指令
            for pc in cmd_pc:
                self.send_cmd(pc, command, callback_queue, task)
            # 给用户返回供查询结果的task值
            print("task id:", task)
        else:
            print("命令错误！")

    def send_cmd(self, pc, command, callback_queue, task):
        # 根据主机地址发送命令消息
        self.channel.basic_publish(exchange="cmd",
                                   routing_key=pc,
                                   body=command,
                                   properties=pika.BasicProperties(
                                       reply_to=callback_queue,
                                       correlation_id=task,
                                   ),)

    def run(self):
        # 主程序执行流程
        while True:
            print("------------RPC------------")
            print("1.在线主机")
            print("2.执行命令")
            print("3.退出系统")
            choice = input(">>:").strip()
            if choice == "1":
                # 获取在线主机
                self.receive_message()
                if self.online:
                    print("******在线主机******")
                    for pc in self.online:
                        print(pc)
                else:
                    print("当前无在线主机")
            elif choice == "2":
                print("******执行命令(back命令返回主菜单)******")
                while True:
                    cmd = input(">>:").strip()
                    if cmd == "back":
                        break
                    # 每执行一次命令前，刷新一次在线主机列表，或者获取之前命令的返回结果
                    self.receive_message()  # 主要作用是刷新在线主机列表，在当前界面不断获取新添加的主机
                    self.do_cmd(cmd)
            elif choice == "3":
                break
