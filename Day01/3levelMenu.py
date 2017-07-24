#初始化菜单数据
menu = {
    "浙江省": {
        "杭州市": ["上城区","下城区","江干区"],
        "宁波市": ["鄞州区","余姚市","慈溪市"],
        "温州市": ["鹿城区","龙湾区","瓯海区"]
    },
    "江苏省": {
        "南京市": ["玄武区","秦淮区","鼓楼区"],
        "无锡市": ["崇安区","北塘区","江阴市"],
        "徐州市": ["云龙区","泉山区","铜山区"]
    },
    "福建省": {
        "福州市": ["台江区","仓山区","马尾区"],
        "厦门市": ["思明区","湖里区","同安区"],
        "莆田市": ["城厢区","涵江区","荔城区"]
    }
}
#初始化菜单显示状态
level = 1
upper_level = ""
top_level = ""
choice = ""
while True:
    if level == 1:
        #打印一级菜单
        for i in menu:
            print(i)
    elif level == 2:
        #打印二级菜单
        try:
            for i in menu[upper_level]:
                print("\t", i)
        except:
            print("输入的菜单内容有误，请重新输入...")
            level -= 1
            upper_level = top_level
            top_level = ""
            continue
    elif level == 3:
        #打印三级菜单
        try:
            for i in menu[top_level][upper_level]:
                print("\t\t",i)
        except:
            print("输入的菜单内容有误，请重新输入...")
            level -= 1
            upper_level = top_level
            top_level = ""
            continue
    #if choice == "":
    choice = input("选择进入（或输入Q退出、输入B返回）：")
    if choice == "q" or choice == "Q":
        #退出系统
        break
    elif choice == "b" or choice == "B":
        #返回上一级
        if level > 1:
            level -= 1
            upper_level = top_level
            top_level = ""
    else:
        if level == 3:
            print("系统菜单只有3层，请选择返回或退出...")
            continue
        top_level = upper_level
        upper_level = choice
        level +=1
