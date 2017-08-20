import accounts
def buy(commodity,account,tra_log,mall_log):
    message = "购买成功"
    power = float(account["atm"]["data"]["quota"]) + float(account["atm"]["data"]["balance"])
    if power >= float(commodity[1]) :
        account["atm"]["data"]["balance"] = str(float(account["atm"]["data"]["balance"]) - float(commodity[1]))
        accounts.save(account["atm"]["data"])
        #日志
        tra_log.info("[%s]商城消费[%s]"%(account["atm"]["data"]["user_name"],commodity[1]))
        mall_log.info("[%s]购买了[%s],价格为[%s]"%(account["mall"]["data"]["user_name"],commodity[0],commodity[1]))
    else:
        message = "余额不足,购买失败"
    return message