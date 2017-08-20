# -*- coding: utf-8 -*-
import accounts
def drawing(user,acc_log,tra_log):
    print("********提款********")
    print("账户额度：%s" % user["quota"])
    print("账户余额：%s" % user["balance"])
    limit = "0"
    if float(user["balance"]) >= 0:
        limit = str(float(user["balance"])+float(user["quota"])/2)
    if float(user["balance"]) < 0:
        limit = str((float(user["balance"]) + float(user["quota"]))/2)
    print("提现额度：%s" % limit)
    drawing_num = input("提款金额：")
    if float(drawing_num) > float(limit):
        print("\033[31;1m超限！提款失败！\033[0m")
    else:
        user["balance"] = str(float(user["balance"]) - float(drawing_num)*1.05)
        accounts.save(user)
        print("\033[31;1m提款成功！\033[0m")
        acc_log.info("用户[%s]提款[%s]"%(user["user_name"],drawing_num))
        tra_log.info("用户[%s]提款[%s]" % (user["user_name"], drawing_num))
def repayment(user,acc_log,tra_log):
    print("********还款********")
    print("账户额度：%s" % user["quota"])
    print("账户余额：%s" % user["balance"])
    repay = input("还款金额：")
    user["balance"] = str(float(user["balance"]) + float(repay))
    accounts.save(user)
    print("\033[31;1m还款成功！\033[0m")
    acc_log.info("用户[%s]还款[%s]" % (user["user_name"], repay))
    tra_log.info("用户[%s]还款[%s]" % (user["user_name"], repay))
def transfer_accounts(user,acc_log,tra_log):
    print("********转账********")
    print("账户额度：%s" % user["quota"])
    print("账户余额：%s" % user["balance"])
    limit = "0"
    if float(user["balance"]) >= 0:
        limit = str(float(user["balance"]) + float(user["quota"]) / 2)
    if float(user["balance"]) < 0:
        limit = str((float(user["balance"]) + float(user["quota"])) / 2)
    print("转账额度：%s" % limit)
    transfer_num = input("转账金额：")
    if float(transfer_num) > float(limit):
        print("\033[31;1m超限！转账失败！\033[0m")
    else:
        transfer_to_user_name = input("对方账户：")
        transfer_to_user = accounts.select(transfer_to_user_name)
        if transfer_to_user:
            if transfer_to_user["locked"] == "1":
                print("\033[31;1m目标账户已被冻结！转账失败！\033[0m")
            else:
                user["balance"] = str(float(user["balance"]) - float(transfer_num) * 1.05)
                accounts.save(user)
                transfer_to_user["balance"] = str(float(transfer_to_user["balance"]) + float(transfer_num))
                accounts.save(transfer_to_user)
                print("\033[31;1m转账成功！\033[0m")
                acc_log.info("用户[%s]向用户[%s]转账[%s]" % (user["user_name"],
                            transfer_to_user["user_name"],transfer_num))
                tra_log.info("用户[%s]向用户[%s]转账[%s]" % (user["user_name"],
                                                      transfer_to_user["user_name"], transfer_num))
        else:
            print("\033[31;1m目标账户不存在！转账失败！\033[0m")
def check_balance(user,acc_log):
    print("********查询余额********")
    print("账户额度：%s" %user["quota"])
    print("账户余额：%s" %user["balance"])
    acc_log.info("用户[%s]查询了余额" % (user["user_name"]))
def check_billing(user,acc_log):
    print("********账单查询********")
    date = input("所查询日期(20xx-xx):")
    accounts.getbill(user, date)
    acc_log.info("用户[%s]查询了[%s]的账单" % (user["user_name"],date))