import func
while True:
    func.menu_print()
    choice = input(">>:")
    if choice == "2":
        break
    if choice == "1":
        formula = input("请输入公式：")
        formula = formula.replace(" ", "").strip()
        res = func.calculation(formula)
        print("计算结果为："+res)
        py_res = eval(formula)
        print("Python运行公式结果为："+str(py_res))
