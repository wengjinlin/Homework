# RPC程序说明

> - 用Python3.0及以上解释器运行，运行环境保证编码为UTF-8
> - 程序控制端入口为：RPC\control\bin\control.py
> - 程序客户端入口为：RPC\client\bin\client.py
> - 控制端可以控制多个客户端执行命令，采用rabbitmq消息队列进行通信
> - 客户端通过self.ip = socket.gethostbyname_ex(socket.gethostname())\[2][0]语句进行不同ip模拟多台主机共同在线（测试主机含多个虚拟网卡）
> - 客户端功能：
>   - 启动后自动向约定Queue发送注册信息
>   - 注册成功后等待命令
>   - 接收命令后执行并向指定Queue返回命令结果
> - 控制端功能：
>   - 从约定Queue接收主机注册信息，可在程序界面打印主机列表
>   - 发送命令并返回task值以供查询
>   - 执行命令如果无--hosts后缀，即循环在线主机列表，发送给所有主机该命令，有后缀，则循环后缀并指定发送
>   - 用户发出查询命令后，从约定Queue中获取结果并保存到本地内存，从本地内存查询具体结果并打印
>   - 每次输入命令后，均接收一次所有Queue中的消息，主要确保新注册的主机能接收消息，同时有几率接收之前执行命令后还没来得及接收的命令结果
> - 具体测试用例见test.md