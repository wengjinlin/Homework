# Login程序的测试

## 文件初始内容

### 1.可登陆用户管理文件（user）
```text
admin
123
user1
456
user2
789
user3
123
user4
123
user5
123
user6
123
user7
123
```

### 2.被锁定用户管理文件（locked_user）

```text

```

## 开始测试

### 1.用户admin成功登陆

#### 	1).测试数据

```
admin 123
```

#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test1.png)

### 2.用户admin不被锁定

#### 	1).测试数据

```
admin sdf 123
admin sdf sdf 123
```

#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test2.png)
### 3.用户admin被锁定

#### 	1).测试数据

```
admin sdf sdf sdf
admin 123
```

#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test3.png)
### 4.用户user1输错1次密码(该密码存在文件中，但不是user1的密码)

#### 	1).测试数据

```
user1 123
user1 456
```

#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test4.png)
### 5.用户user1被锁定，再次登陆时无论密码对否直接显示用户被锁定

#### 	1).测试数据

```
user1 sdf sdf sdf
user1 sdf
```


#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test5.png)
### 6.非法用户登录，显示用户不存在

#### 	1).测试数据

```
wer wer
```


#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test6.png)

## 程序结束后文件内容

### 1.可登陆用户管理文件（user）
```text
admin
123
user1
456
user2
789
user3
123
user4
123
user5
123
user6
123
user7
123
```

### 2.被锁定用户管理文件（locked_user）

```text
admin
user1
```

















# 3levelMenu程序的测试

## 开始测试

### 1.进入各层级及各层级返回功能

#### 	1).测试数据

```
B 浙江省 杭州市 b b 江苏省 南京市 B 无锡市
```


#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test7.png)
### 2.各层级退出功能
#### 	1).测试数据

```
Q
福建省 q
江苏省 徐州市 q
```


#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test8.png)
![](C:\Users\Administrator\Documents\Homework\Day01\test\test9.png)
![](C:\Users\Administrator\Documents\Homework\Day01\test\test10.png)
### 3.各层级非法输入拦截功能
#### 	1).测试数据

```
sdfs 浙江省 水电费 杭州市 水电费 Q
```


#### 	2).测试结果

![](C:\Users\Administrator\Documents\Homework\Day01\test\test11.png)