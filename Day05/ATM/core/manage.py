# -*- coding: utf-8 -*-
import accounts
def add_account(acc_log):
    print("****添加账户****")
    user_name = input("用户名：")
    user_password = input("密码：")
    user = {"user_name":user_name,
            "user_password":user_password,
            "balance":"0",
            "quota":"15000",
            "locked":"0"}
    message = accounts.add(user)
    if message == "添加成功":
        acc_log.info("管理员添加银行新用户[%s]" % user_name)
    print("\033[31;1m%s\033[0m" %message)
def modify_quota(acc_log):
    print("****更改用户额度****")
    user_name = input("账户名：")
    user = accounts.select(user_name)
    if user:
        if user["locked"] == "1":
            print("\033[31;1m该账户已被冻结！\033[0m")
        else:
            print("账户原额度：%s" %user["quota"])
            modify = input("更改为:")
            user["quota"] = modify
            accounts.save(user)
            print("\033[31;1m修改成功！\033[0m")
            acc_log.info(u"管理员将[%s]的信用卡额度更改为[%s]"%(user_name,modify))
    else:
        print("\033[31;1m该用户不存在!\033[0m")
def lock_account(acc_log):
    print("****冻结账户****")
    user_name = input("账户名：")
    user = accounts.select(user_name)
    if user:
        if user["locked"] == "1":
            print("\033[31;1m该账户已被冻结！\033[0m")
        else:
            user["locked"] = "1"
            accounts.save(user)
            print("\033[31;1m冻结成功！\033[0m")
            acc_log.info("管理员冻结了用户[%s]"%user_name)
    else:
        print("\033[31;1m该用户不存在!\033[0m")
def unlock_account(acc_log):
    print("****解冻账户****")
    user_name = input("账户名：")
    user = accounts.select(user_name)
    if user:
        if user["locked"] == "0":
            print("\033[31;1m该账户未被冻结！\033[0m")
        else:
            user["locked"] = "0"
            accounts.save(user)
            print("\033[31;1m解冻成功！\033[0m")
            acc_log.info("管理员解除了对[%s]的冻结"%user_name)
    else:
        print("\033[31;1m该用户不存在!\033[0m")