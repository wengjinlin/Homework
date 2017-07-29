import os
while True:
    print("1.查询员工工资\n2.修改员工工资\n3.增加新员工记录\n4.退出")
    choice = input("请输入选择序号>>:")
    if choice == "1":
        #查询
        query_staff = input("请输入要查询的员工姓名（例如：Alex）：")
        staff_find = False
        with open("info.txt", "r") as f_r:
            for line in f_r:
                if query_staff in line:
                    wage = line[line.find(" ")+1:].strip()
                    staff_find = True
                    break
        if staff_find:
            print("{name}的工资是：{wage}。".format(name=query_staff,wage=wage))
        else:
            print("没有该员工信息")
    elif choice == "2":
        #修改
        modify_staff = input("请输入要修改的员工姓名和工资，用空格分隔（例如：Alex 10）：")
        staff = modify_staff[:modify_staff.find(" ")].strip()
        staff_find = False
        with open("info.txt","r") as f_r,\
             open("info_new.txt","w") as f_w:
            for line in f_r:
                if staff in line:
                    staff_find = True
            if staff_find:
                f_r.seek(0)
                for line in f_r:
                    if staff in line:
                        f_w.write(modify_staff+"\n")
                    else:
                        f_w.write(line)
            else:
                print("没有该员工")
        if staff_find:
            os.remove("info.txt")
            os.rename("info_new.txt","info.txt")
            print("修改成功！")
        else:
            os.remove("info_new.txt")
    elif choice == "3":
        #增加
        add_staff = input("请输入要增加的员工姓名和工资，用空格分割（例如：Eric 100000）：")
        with open("info.txt","a") as f_a:
            f_a.write(add_staff+"\n")
        print("增加成功！")
    elif choice == "4":
        #退出
        print("再见！")
        break
    else:
        print("输入错误！")
