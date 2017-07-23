while True:
    username = input("username:")
    # 在PyCharm中测试方便，采用明文密码
    password = input("password:")
    #调用文件locked_user
    print("调用文件locked_user")
    if username == "locked":
        print("用户已被锁定，请联系管理员！")
        quit_sis = input("是否退出系统（y/n）？")
        if quit_sis != "n":
            break
        else:
            continue
    else:
        #调用文件user
        print("调用文件user")
        #用户名验证成功
        if username == "success" :
            #密码验证成功
            if password == "success":
                print("欢迎{_username}成功登陆系统".format(_username=username))
                quit_sis = input("是否退出系统（y/n）？")
                if quit_sis != "n":
                    break
                else:
                    continue
            #密码验证失败
            else:
                #最多还有2次输入机会
                print("密码输入错误，你还有2次机会！")
                for i in range(2):
                    password = input("password:")
                    if password == "success":
                        print("欢迎{_username}成功登陆系统".format(_username=username))
                        break
                    else:
                        if i == 0:
                            print("密码输入错误，你还有1次机会！")
                else:
                    #写入文件，锁定用户
                    print("密码连续输入错误已达3次，用户被锁定，请联系管理员！")
                    username = "locked"
                    print("写入文件，锁定用户")
                quit_sis = input("是否退出系统（y/n）？")
                if quit_sis != "n":
                    break
                else:
                    continue
        #用户名验证失败
        else:
            print("用户不存在！")
            quit_sis = input("是否退出系统（y/n）？")
            if quit_sis != "n":
                break
            else:
                continue