# SELECT_FTP程序说明

> - 用Python3.0及以上解释器运行，运行环境保证编码为UTF-8
> - 程序服务器端入口为：select_ftp\server\ftp_server.py
> - 程序客户端入口为：select_ftp\client\ftp_client.py
> - 服务器端可以接收多个客户端的连接，采用select进行单线程并发，实现多客户端同时进行通信效果
> - 上传功能：
>   - 多客户端可同时进行文件上传
> - 下载功能：
>   - 多客户端可同时进行文件下载
> - 具体测试用例见test.md