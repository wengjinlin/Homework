#消费状态
bought_before = [0,0,0,0,0]
bought_this = [0,0,0,0,0]
salay = 0
username = input("请输入用户名：")
try:
    user_file = open("user\{user_file}".format(user_file=username),"r")
    password_user = user_file.readline().strip()
    while True:
        password = input("请输入密码：")
        if password == password_user:
            salay = int(user_file.readline().strip())
            for i in range(5):
                bought_before[i] = int(user_file.readline().strip())
            break
        else:
            print("密码错误，请重新输入！")
    user_file.close()

except:
    while True:
        password_first = input("第一次登录，请设置密码：")
        password_second = input("请重复密码：")
        if password_first == password_second:
            password_user = password_first
            break
        else:
            print("两次密码不一致，请重新设置！")
    print("欢迎登录本商城")
    while True:
        try:
            salay = int(input("请输入工资："))
            break
        except:
            print("输入有误，请输入整数数字！")
            continue
commodities = [["Iphone", "5000"], ["Computer", "8000"], ["Television", "3000"],
               ["Refrigerator", "2300"], ["Motorcycle", "6500"]]
while True:
    print("---------商品列表---------")
    no = 1
    for i in commodities:
        print("{no}.{name}:{price}".format(no=no,name=i[0],price=i[1]))
        no += 1
    print("S.查询历史记录")
    print("Q.退出系统")
    buy_no = input("请选择购买商品的序号：")
    if buy_no == "q" or buy_no == "Q":
        bought_if = False
        for i in range(5):
            if bought_this[i] != 0:
                bought_if = True
                break
        if bought_if:
            print("您已购买如下商品:")
            no = 0
            for i in commodities:
                if bought_this[no] != 0:
                    print("{name}\t*\t{count}".format(name=i[0],count=bought_this[no]))
                no += 1
        else:
            print("您没有购买任何商品！")
        print("\033[1m")
        print("所剩余额为：{balance}".format(balance=salay))
        print("\033[0m")
        #将用户信息存入文件
        user_to_file = open("user\{filename}".format(filename=username), "w")
        user_to_file.write(password_user+"\n")
        user_to_file.write(str(salay)+"\n")
        for i in range(5):
            user_to_file.write(str(bought_this[i]+bought_before[i])+"\n")
        user_to_file.close()
        break
    elif buy_no == "s" or buy_no == "S":
        try:
            if password_first != None:
                print("您是第一次登录系统，暂无历史记录！")
        except:
            bought_if = False
            for i in range(5):
                if bought_before[i] != 0:
                    bought_if = True
                    break
            if bought_if:
                print("您的历史记录如下：")
                no = 0
                for i in commodities:
                    if bought_before[no] != 0:
                        print("{name}\t*\t{count}".format(name=i[0], count=bought_before[no]))
                    no += 1
            else:
                print("您还没有购买过任何商品！")
            print("\033[1m")
            print("所剩余额为：{balance}".format(balance=salay))
            print("\033[0m")
        wait = input("按回车返回系统...")
    else:
        try:
            com_no = int(buy_no)
            if salay < int(commodities[com_no - 1][1]):
                print("\033[1m")
                print("余额不足，请重新选择...\n所剩余额为：{_salay}".format(_salay=salay))
                print("\033[0m")
                continue
            print("\033[1m")
            print("已添加商品{name}到购物车...".format(name=commodities[com_no - 1][0]))
            print("\033[0m")
            bought_this[com_no - 1] += 1
            salay = salay - int(commodities[com_no - 1][1])
        except:
            print("选择错误，请重新选择商品编号...")
            continue
