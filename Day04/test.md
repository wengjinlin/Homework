# staff_info程序的测试

## 开始测试

### 1.查询功能测试

#### 	1).测试数据

```
dsfgsdggdgg
sdfsdf sdfdsf sdf sdf sdfsdf sdff
sdfsdf sdfsdf sdf sdfsf sdfsdf sdfsdf sdfsf sdfsdf
select name,age,phone from staff_table where age > 30
select * from staff_table where dept = 'IT'
select * from staff_table where enroll_date like '2017'
select * from staff_table
```


#### 	2).测试结果

![](test\test1.png)
![](test\test2.png)
![](test\test3.png)
![](test\test4.png)
### 2.删除功能测试

#### 	1).测试数据

```
0
6
10
3
15
15
select * from staff_table
```


#### 	2).测试结果

![](test\test5.png)
![](test\test6.png)
![](test\test7.png)
### 3.添加功能测试

#### 	1).测试数据

```
Huang Gai
35
13611111112
HR
2017-03-21
13611111121
13678945612
select * from staff_info
select * from staff_table
```


#### 	2).测试结果

![](test\test8.png)
![](test\test9.png)

### 4.修改功能测试

#### 	1).测试数据

```
select * from staff_table
UPDATE staff_table SET dept='Market' WHERE dept = 'IT'
select * from staff_table
```


#### 	2).测试结果

![](test\test10.png)
![](test\test11.png)