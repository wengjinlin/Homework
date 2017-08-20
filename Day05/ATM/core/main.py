# -*- coding: utf-8 -*-
import transaction,manage,auth,logger,mall,shopping
account = {"atm":{"role":"tourist",
                  "login":"fail",
                  "message":"",
                  "data":{}},
           "mall":{"role":"tourist",
                  "login":"fail",
                  "message":"",
                  "data":{}}
           }
acc_log = logger.logger("access")
tra_log = logger.logger("transactions")
mall_log = logger.logger("mall")
def menu(choice):
    if choice == "1":
        sys_atm()
    elif choice == "2":
        sys_atm_manage()
    elif choice == "3":
        sys_shopping_mall()
    elif choice == "4":
        # 退出程序
        return False
    #显示菜单
    menu_top()
    print("1.进入银行系统")
    print("2.进入银行管理系统")
    print("3.进入电子商城")
    print("4.退出系统")
    return True
@auth.login_if(account,sys="atm")#登录判定
@auth.atm_role(account["atm"],role="user")#权限判定
def sys_atm():
    while True:
        sys_menu("atm")
        choice = input(">>:")
        if choice == "1":
            transaction.drawing(account["atm"]["data"],acc_log,tra_log)
        elif choice == "2":
            transaction.repayment(account["atm"]["data"],acc_log,tra_log)
        elif choice == "3":
            transaction.transfer_accounts(account["atm"]["data"],acc_log,tra_log)
        elif choice == "4":
            transaction.check_balance(account["atm"]["data"],acc_log)
        elif choice == "5":
            transaction.check_billing(account["atm"]["data"],acc_log)
        elif choice == "6":
            break
@auth.login_if(account,sys="atm")#登录判定
@auth.atm_role(account["atm"],role="admin")#权限判定
def sys_atm_manage():
    while True:
        sys_menu("manage")
        choice = input(">>:")
        if choice == "1":
            manage.add_account(acc_log)
        elif choice == "2":
            manage.modify_quota(acc_log)
        elif choice == "3":
            manage.lock_account(acc_log)
        elif choice == "4":
            manage.unlock_account(acc_log)
        elif choice == "5":
            break
@auth.login_if(account,sys="mall")#登录判定
def sys_shopping_mall():
    commodities = mall.getcommodities()
    while True:
        print("---------商品列表---------")
        no = 1
        for i in commodities:
            print("{no}.{name}:{price}".format(no=no, name=i[0], price=i[1]))
            no += 1
        print("S.查询历史记录")
        print("Q.退出系统")
        choice = input(">>：")
        if choice == "q" or choice == "Q":
            break
        elif choice == "s" or choice == "S":
            mall.gethistory(account["mall"]["data"])
        list = []
        for i in range(no-1):
            list.append(str(i+1))
        if choice in list:
            buy_interface(commodities[int(choice)-1],tra_log,mall_log)
def sys_menu(sys):
    if sys == "atm":
        print("------bank------")
        print("1.提款")
        print("2.还款")
        print("3.转账")
        print("4.查询余额")
        print("5.账单查询")
        print("6.退出")
    elif sys == "manage":
        print("------manage------")
        print("1.添加账户")
        print("2.更改用户额度")
        print("3.冻结账户")
        print("4.解冻账户")
        print("5.退出")
    elif sys == "mall":
        pass
def menu_top():
    print("/------------当前用户------------/")
    if account["atm"]["role"] == "user":
        print("/----银行：\033[34;1m{name}\033[0m----/".format(name=account["atm"]["data"]["user_name"]))
    else:
        print("/----银行：\033[34;1m{name}\033[0m----/".format(name=account["atm"]["role"]))
    if account["mall"]["role"] == "user":
        print("/----商城：\033[34;1m{name}\033[0m----/".format(name=account["mall"]["data"]["user_name"]))
    else:
        print("/----商城：\033[34;1m{name}\033[0m----/".format(name=account["mall"]["role"]))
@auth.login_if(account,sys="atm")#登录判定
@auth.atm_role(account["atm"],role="user")#权限判定
def buy_interface(commodity,tra_log,mall_log):
    message = shopping.buy(commodity,account,tra_log,mall_log)
    print("\033[31;1m%s\033[0m" % message)