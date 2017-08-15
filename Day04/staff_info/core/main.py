import verification,add_impl,delete_impl,select_impl,modify_impl
def menu(choice):
    if choice == "1":
        add()
    elif choice == "2":
        delete()
    elif choice == "3":
        modify()
    elif choice == "4":
        select()
    elif choice == "5":
        #退出程序
        return False
    #显示菜单
    print("/-----员工信息系统-----/")
    print("1.增加员工信息")
    print("2.删除员工信息")
    print("3.修改员工信息")
    print("4.查询员工信息")
    print("5.退出系统")
    return True

def add():
    print("增加员工信息：")
    name = input("姓名：")
    age = input("年龄：")
    phone = input("电话：")
    dept = input("部门：")
    enroll_date = input("入职时间(20XX-XX-XX)：")
    staff_id = verification.add(phone)
    while staff_id == -1:
        print("该电话已存在，请重新输入！")
        phone = input("电话：")
        staff_id = verification.add(phone)
    add_impl.add(str(staff_id),name,age,phone,dept,enroll_date)
    print("添加成功！")
def delete():
    staff_id = input("员工ID：")
    while not verification.delete(staff_id):
        print("不存在该ID，请核对后重新输入！")
        staff_id = input("员工ID：")
    delete_impl.delete(staff_id)
    print("删除成功！")
def modify():
    print("是否显示查询帮助信息？")
    while True:
        if_help = input("Y/N?")
        if if_help == "Y" or if_help == "y":
            print("本修改系统仅支持以下语法：")
            print("UPDATE staff_table SET dept='Market' WHERE dept = 'IT'")
            break
        if if_help == "N" or if_help == "n":
            break
    update = input("请输入修改语句：")
    update = format_input(update)
    message = verification.modify(update)
    while message != "OK":
        print(message)
        update = input("请输入修改语句：")
        update = format_input(update)
        message = verification.modify(update)
    res = modify_impl.modify(update)
    print("修改成功！")
def select():
    print("是否显示查询帮助信息？")
    while True:
        if_help = input("Y/N?")
        if if_help == "Y" or if_help == "y":
            print("本查询系统支持单条件查询和模糊查询，示例：")
            print("select * from staff_table")
            print("select name,age from staff_table where age > 22")
            print("select * from staff_table where dept = 'IT'")
            print("select * from staff_table where enroll_date like '2017'")
            break
        if if_help == "N" or if_help == "n":
            break
    search = input("请输入查询语句：")
    search = format_input(search)
    message = verification.select(search)
    while message != "OK":
        print(message)
        search = input("请输入查询语句：")
        search = format_input(search)
        message = verification.select(search)
    str_where = search.split(" ")[4]
    if str_where in search:
        res = select_impl.select_where(search[search.find(str_where) + 6:])
    else:
        res = select_impl.search_all()
    print_out(res,search)
def format_input(line):
    #格式化语句
    line = line.replace(">", " > ")
    line = line.replace("<", " < ")
    line = line.replace("=", " = ")
    for i in range(10):
        line = line.replace("  ", " ")
        line = line.replace(" ,", ",")
        line = line.replace(", ", ",")
    return line
def print_out(res,search):
    str_pr = search.split(" ")[1]
    for i in range(res[0]):
        if str_pr != "*":
            if str_pr.find(",") == -1:
                #单显示内容
                print(res[i+1][str_pr])
            else:
                for j in range(str_pr.count(",")):
                    st = str_pr.split(",")[j]
                    print(res[i + 1][st], end=",")
                print(res[i+1][str_pr.split(",")[str_pr.count(",")]])
        else:
            print(res[i + 1]["staff_id"], end=",")
            print(res[i + 1]["name"], end=",")
            print(res[i + 1]["age"], end=",")
            print(res[i + 1]["phone"], end=",")
            print(res[i + 1]["dept"], end=",")
            print(res[i + 1]["enroll_date"])
    print("共查询到{x}条记录：".format(x=res[0]))