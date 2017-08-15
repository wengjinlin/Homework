# staff_info程序说明

> - 用Python3.0及以上解释器运行staff_info\bin\staff_info.py，运行环境保证编码为UTF-8
>
> - 系统实现查询，修改、增加和删除功能
>
> - 程序由staff_info进入，调用main主程序，main负责调用各个功能模块，各功能模块在实现之前均调用验证模块进行语法或数据的基本验证，最后调用功能底层实现模块
>
> - 添加功能：会验证输入的phone值是否是唯一，只有phone唯一，才会添加成功
>
> - 删除功能：通过id删除，删除之前会验证该id是否存在，只有存在才会删除
>
> - 修改功能：通过命令语句进行操作，格式：UPDATE staff_table SET dept="Market" where dept = "IT"，关键字（如：update,set,where）不分大小写，where后面的条件可以是任意表内字段数据的约束条件，set内容可以是除staff_id以外的任意内容
>
> - 查询功能：通过命令语句进行操作，关键字（如：update,set,where）不分大小写，格式：
>
>   select name,age from staff_table where age > 22
>
>   select  * from staff_table where dept = "IT"
>
>   select  * from staff_table where enroll_date like "2013"
>
>   select后面的搜索内容可以是任意表内字段，where后面的条件可以是除staff_id以外任意表内字段数据的约束条件，同时支持模糊查询（like需小写）
>
> - 具体测试用例见test.md

