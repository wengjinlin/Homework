#FTP程序的测试

## 开始测试

###1.多用户同时登陆

#### 	1).测试数据

```
user1 123
user2 123
```


#### 	2).测试结果

![](test\test1.png)
![](test\test2.png)

###2.用户空间配额限制

#### 	1).测试数据

```
ul E:\美剧\11.mkv
```


#### 	2).测试结果

![](test\test3.png)

###3.查看用户目录及文件

#### 	1).测试数据

```
ls
cd dir1
ls
cd dir1_1
cd ..
cd dir1_2
cd
```


#### 	2).测试结果

![](test\test4.png)

###4.上传下载文件

#### 	1).测试数据

```
dl 111.jpg
cd dir2
ls
ul C:\Users\Administrator\Documents\Homework\Day08\FTP\client\download\user1\111.jpg
```


#### 	2).测试结果

![](test\test5.png)

