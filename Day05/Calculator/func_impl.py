import re
def menu():
    #菜单打印实现
    print("-----计算器-----")
    print("1.公式计算")
    print("2.退出")
def cutbrackets(formula):
    #去最里层括号，计算结果放回公式并返回该公式
    formula_mbk = re.search(r"\([^()]+\)",formula).group()
    formula_mbk_index = formula.index(formula_mbk)
    res = calculation_nobk(formula_mbk[1:-1])
    formula = formula.replace(formula_mbk,res)
    if res[0] == "-":
        if formula_mbk_index-1 > 0:
            if formula[formula_mbk_index-1] != "(":
                formula = format_formula(formula_mbk_index,formula)
    # print("取括号："+formula_mbk)
    # print("括号内结果："+res)
    # print("返回公式："+formula)
    return formula
def calculation_nobk(formula):
    #计算无括号的公式,返回计算结果
    res = calculation_mulp(formula)
    res = calculation_plus(res)
    return res
def calculation_plus(formula):
    #计算公式内的加减法
    times = formula.count("+")
    times = times + formula.count("-")
    if formula[0] == "-":
        times -= 1
    for j in range(times):
        for i in range(len(formula)):
            if formula[i] == "+":
                a = getbefor(i, formula)
                b = getafter(i, formula)
                replace = a + "+" + b
                res = str(float(a) + float(b))
                formula = formula.replace(replace, res)
                break
            if formula[i] == "-":
                if i == 0:
                    continue
                a = getbefor(i, formula)
                b = getafter(i, formula)
                replace = a + "-" + b
                res = str(float(a) - float(b))
                formula = formula.replace(replace, res)
                break
    return formula
def calculation_mulp(formula):
    #计算公式内的乘除法
    times = formula.count("*")
    times = times + formula.count("/")
    for j in range(times):
        for i in range(len(formula)):
            if formula[i] == "*":
                a = getbefor(i, formula)
                b = getafter(i, formula)
                replace = a + "*" + b
                res = str(float(a) * float(b))
                formula = formula.replace(replace,res)
                break
            if formula[i] == "/":
                a=getbefor(i, formula)
                b=getafter(i, formula)
                replace = a + "/" + b
                res = str(float(a) / float(b))
                formula = formula.replace(replace,res)
                break
    return formula
def getbefor(i,formula):
    for j in range(i-1,-1,-1):
        if formula[j] == "+":
            break
        elif formula[j] == "-":
            break
        elif formula[j] == "*":
            break
        elif formula[j] == "/":
            break
    if j == 0:
        return formula[0:i]
    else:
        return formula[j+1:i]
def getafter(i,formula):
    for j in range(i+1,len(formula)):
        if formula[j] == "+":
            break
        elif formula[j] == "-":
            break
        elif formula[j] == "*":
            break
        elif formula[j] == "/":
            break
    if j == len(formula)-1:
        return formula[i+1:]
    else:
        return formula[i+1:j]
def format_formula(formula_mbk_index,formula):
    if "+-" in formula:
        return formula.replace("+-", "-")
    if "--" in formula:
        if formula[0] == "-":
            return formula.replace("--", "")
        return formula.replace("--", "+")
    for j in range(formula_mbk_index-1,-1,-1):
        if formula[j] == "+":
            return formula[:j] + "-" + formula[j + 1:]
        elif formula[j] == "-":
            if j == 0:
                return formula[1:]
            return formula[:j] + "+" + formula[j + 1:]
        elif formula[j] == "*":
            formula = formula.replace("*-", "*")
            continue
        elif formula[j] == "/":
            formula = formula.replace("/-", "*")
            continue