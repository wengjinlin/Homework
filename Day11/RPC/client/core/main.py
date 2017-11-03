import pika
import socket
import subprocess


class RPCclient(object):
    def __init__(self):
        # 初始化
        self.ip = socket.gethostbyname_ex(socket.gethostname())[2][0]
        # 连接RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
        self.channel = connection.channel()
        # 声明exchange
        self.channel.exchange_declare(exchange='cmd', exchange_type="direct")  # 执行命令的exchange
        # 声明Q
        self.channel.queue_declare(queue="online")  # 注册在线主机的Q
        result = self.channel.queue_declare(exclusive=True)  # 获取命令的随机Q
        q_get_cmd = result.method.queue
        # 绑定Q
        self.channel.queue_bind(exchange="cmd", queue=q_get_cmd, routing_key=self.ip)
        # 声明消费
        self.channel.basic_consume(self.do_cmd, queue=q_get_cmd, no_ack=True)
        # 注册控制器
        self.if_register = False

    def register_self(self):
        # 注册本机
        self.channel.basic_publish(exchange="", routing_key="online", body=self.ip)
        self.if_register = True

    def do_cmd(self, channel, method, props, body):
        # 执行命令
        cmd = body.decode()
        print("run :", cmd)
        result = subprocess.getoutput(cmd)
        # 返回结果
        channel.basic_publish(exchange='',
                              routing_key=props.reply_to,
                              body=result,
                              properties=pika.BasicProperties(
                                  correlation_id=props.correlation_id,
                                  app_id=self.ip,
                              ),)

    def run(self):
        # 主程序执行流程
        if not self.if_register:
            self.register_self()
        # self.channel.basic_consume(self.on_request, queue=self.queue_name)
        print(" %s waiting command" % self.ip)
        self.channel.start_consuming()
