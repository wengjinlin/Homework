# Fortress程序说明

> - 用Python3.0及以上解释器运行，运行环境保证编码为UTF-8
> - 程序入口为：Fortress\bin\Fortress.py
> - 数据库表创建文件为：Fortress\db\createTables.py
> - 数据库连接参数设置：Fortress\conf\config.py
> - 日志文件：Fortress\log\ssh.log，数据库audit_log表
> - 程序功能：
>   - 用户登录后即可见已被绑定的主机和主机组
>   - 选择未分组主机（如果有）或主机组（如果有）后显示具体主机
>   - 选择主机后根据已分配的权限账户进行远程登录
>   - 连接远程主机后可操作命令
>   - 系统自动记录连接操作的ssh日志以及用户操作命令的日志记录
>   - 用户被分配的主机和主机组以及各主机的权限，均由管理员事先分配并绑定，用户只能选择和登录进行相应权限的操作
> - 具体测试用例见test.md