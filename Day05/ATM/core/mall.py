import db_handler
def getcommodities():
    #获取商品信息
    commodities = [["Iphone", "5000"], ["Computer", "8000"], ["Television", "3000"],
                   ["Refrigerator", "2300"], ["Motorcycle", "6500"]]
    return commodities
def gethistory(user):
    #获取用户历史记录并打印
    db_handler.mall_print_history(user["user_name"])