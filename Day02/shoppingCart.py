while True:
    try:
        salay = int(input("请输入金额："))
        break
    except:
        print("输入有误，请输入整数数字！")
        continue
commodities = [["Iphone", "5000"], ["Computer", "8000"], ["Television", "3000"],
               ["Refrigerator", "2300"], ["Motorcycle", "6500"]]
shopping_cart = []
while True:
    print("---------商品列表---------")
    no = 1
    for i in commodities:
        print("{no}.{name}:{price}".format(no=no,name=i[0],price=i[1]))
        no += 1
    buy_no = input("请选择购买商品的序号(或输入Q退出)：")
    if buy_no == "q" or buy_no == "Q":
        print("您已购买如下商品:")
        for i in shopping_cart:
            print("{name}:{price}".format(name=i[0],price=i[1]))
        print("所剩余额为：{balance}".format(balance=salay))
        break
    else:
        try:
            com_no = int(buy_no)
            if salay < int(commodities[com_no - 1][1]):
                print("余额不足，请重新选择...\t所剩余额为：{_salay}".format(_salay=salay))
                continue
            print("已添加商品{name}到购物车...".format(name=commodities[com_no - 1][0]))
            shopping_cart.append(commodities[com_no - 1])
            salay = salay - int(commodities[com_no - 1][1])
        except:
            print("选择错误，请重新选择商品编号...")
            continue
