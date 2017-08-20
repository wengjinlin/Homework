# -*- coding: utf-8 -*-
import accounts
def login_if(account,sys):#登录判定装饰器
    def login(func):
        def login_role(*args, **kwargs):
            if account[sys]["role"] == "tourist":
                if sys == "atm":
                    #atm系统登录
                    atm_sign_in(account[sys])
                if sys == "mall":
                    #mall系统登录
                    mall_sign_in(account[sys])
                if account[sys]["login"] == "fail":
                    print("\033[31;1m%s\033[0m" %account[sys]["message"])
                    return None
                print("\033[31;1m登录成功！\033[0m")
            return func(*args, **kwargs)
        return login_role
    return login
def atm_role(account_atm,role):#权限判定装饰器
    def atm_role_sys(func):
        def role_determine(*args, **kwargs):
            if role == account_atm["role"]:
                return func(*args, **kwargs)
            print("\033[31;1m当前用户没有该权限，请重新登录！\033[0m")
            atm_sign_in(account_atm)
            if account_atm["login"] == "fail":
                print("\033[31;1m%s\033[0m" % account_atm["message"])
                return None
            print("\033[31;1m登录成功！\033[0m")
        return role_determine
    return atm_role_sys
def atm_sign_in(account_2):
    print("****银行登录系统****")
    while True:
        print("1.普通用户登录")
        print("2.管理员登录")
        print("3.暂不登录")
        choice = input(">>:")
        if choice == "1":
            atm_user_login(account_2)
            break
        elif choice == "2":
            atm_admin_login(account_2)
            break
        elif choice == "3":
            account_2["login"] = "fail"
            account_2["message"] = "用户放弃登录"
            break
def atm_user_login(account_2):
    #普通用户登录
    user_name = input("账号：")
    user_password = input("密码：")
    user = accounts.select(user_name)
    if user:
        if user["locked"] == "0":
            if user_password == user["user_password"]:
                account_2["login"] = "success"
                account_2["role"] = "user"
                account_2["data"] = user
            else:
                account_2["login"] = "fail"
                account_2["message"] = "密码错误！"
        else:
            account_2["login"] = "fail"
            account_2["message"] = "该账号已被冻结！请联系管理员!"
    else:
        account_2["login"] = "fail"
        account_2["message"] = "用户不存在！"
def atm_admin_login(account_2):
    #管理员登录
    admin_name = input("管理员账号：")
    admin_password = input("管理员密码：")
    if admin_name == "admin" and admin_password == "admin":
        account_2["role"] = "admin"
        account_2["login"] = "success"
    else:
        account_2["login"] = "fail"
        account_2["message"] = "管理员账号密码错误！"
def clean_account(account):
    #初始化account数据
    account = {"atm": {"role": "tourist",
                       "login": "fail",
                       "message": "",
                       "data": {}},
               "mall": {"role": "tourist",
                        "login": "fail",
                        "message": "",
                        "data": {}}
               }
def mall_sign_in(account_mall):
    print("****电子商城登录系统****")
    while True:
        print("1.普通用户登录")
        print("2.暂不登录")
        choice = input(">>:")
        if choice == "1":
            mall_user_login(account_mall)
            break
        elif choice == "2":
            account_mall["login"] = "fail"
            account_mall["message"] = "用户放弃登录"
            break
def mall_user_login(account_mall):
    # mall普通用户登录
    user_name = input("账号：")
    user_password = input("密码：")
    user = accounts.mall_select(user_name)
    if user:
        if user_password == user["user_password"]:
            account_mall["login"] = "success"
            account_mall["role"] = "user"
            account_mall["data"] = user
        else:
            account_mall["login"] = "fail"
            account_mall["message"] = "密码错误！"
    else:
        account_mall["login"] = "fail"
        account_mall["message"] = "用户不存在！"