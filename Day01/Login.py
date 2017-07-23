while True:
    username = input("username:")
    # 在PyCharm中测试方便，采用明文密码
    password = input("password:")
    #用户锁定状态指示器
    user_locked = False
    #调用文件locked_user
    fp_locked_user = open("locked_user", "r")
    for line in fp_locked_user:
        if username == line.strip():
            user_locked = True
            break
    fp_locked_user.close()
    if user_locked:
        print("用户已被锁定，请联系管理员！")
    else:
        #调用文件user
        fp_user = open("user","r")
        #计数器，隔行验证用户名
        count = 0
        #用户名密码验证器
        username_su = False
        password_su = False
        for line in fp_user:
            if username_su:
                #用户名验证成功的下一次循环，就是该用户的密码
                password_in_file = line.strip()
                if password == password_in_file:
                    #验证密码成功
                    password_su = True
                #只验证一行，跳出循环
                break
            if count%2 == 0:
                if username == line.strip():
                    # 用户名验证成功
                    username_su = True
            count += 1
        fp_user.close()
        if username_su:
            #用户名验证成功
            if password_su:
                # 密码验证成功
                print("欢迎{_username}成功登陆系统".format(_username=username))
            else:
                # 密码验证失败
                #最多还有2次输入机会
                print("密码输入错误，你还有2次机会！")
                for i in range(2):
                    password = input("password:")
                    if password == password_in_file:
                        print("欢迎{_username}成功登陆系统".format(_username=username))
                        break
                    else:
                        if i == 0:
                            print("密码输入错误，你还有1次机会！")
                else:
                    print("密码连续输入错误已达3次，用户被锁定，请联系管理员！")
                    # 写入文件，锁定用户
                    fp_locked_user = open("locked_user", "a")
                    fp_locked_user.write(username+"\n")
                    fp_locked_user.close()
        else:
            # 用户名验证失败
            print("用户不存在！")
    quit_sis = input("是否退出系统（y/n）？")
    if quit_sis != "n":
        break
    else:
        continue
