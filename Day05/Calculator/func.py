import func_impl
def menu_print():
    #菜单打印
    func_impl.menu()
def calculation(formula):
    #去括号，先乘除，再加减,返回计算结果
    while "(" in formula:
        formula = func_impl.cutbrackets(formula)
    res = func_impl.calculation_nobk(formula)
    # print(res)
    return res