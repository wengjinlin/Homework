#Fabric程序的测试

## 开始测试

###1.主机或主机组列表

#### 	1).测试数据

```
1
2
3
```


#### 	2).测试结果

![](test\test1.png)
![](test\test2.png)
![](test\test3.png)
![](test\test4.png)
![](test\test5.png)
![](test\test6.png)

###2.对选定主机或主机组执行命令

#### 	1).测试数据

```
ls
ifconfig
```


#### 	2).测试结果

![](test\test7.png)
![](test\test8.png)
![](test\test9.png)

###3.上传下载文件

#### 	1).测试数据

```
ls /tmp
put C:\Users\Administrator\Documents\Homework\Day09\Fabric\file\1.jpg /tmp/picture_from_win.jpg
ls /tmp
help
get /tmp/picture_from_win.jpg new_picture.jpg
```


#### 	2).测试结果

![](test\test10.png)
![](test\test11.png)
![](test\test12.png)
