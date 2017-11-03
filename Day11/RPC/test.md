#RPC程序的测试

## 开始测试

###1.查看在线主机

#### 	1).测试数据

```
只开启控制端，无在线主机，开启两个终端后自动注册，显示主机IP
```


#### 	2).测试结果

![](test\test1.png)
![](test\test2.png)
![](test\test3.png)
![](test\test4.png)

###2.执行命令

#### 	1).测试数据

```
run "net user" --hosts 192.168.1.3
run "dir"
开启第三个主机
run "cd"
check_task 8704
check_task 3552
check_task 9916
```


#### 	2).测试结果

![](test\test6.png)
![](test\test5.png)
![](test\test11.png)
![](test\test7.png)
![](test\test8.png)
![](test\test9.png)
![](test\test10.png)
![](test\test12.png)
![](test\test13.png)
![](test\test14.png)
