#语法验证实现
def select(str_select,str_from,str_where):
    #带条件查询语句验证
    message = "OK"
    if str_select != "select" and str_select != "SELECT":
        message = message + ",必须以select开头"
    if str_from != "from" and str_from != "FROM":
        message = message + ",缺少from"
    if str_where != "where" and str_where != "WHERE":
        message = message + ",缺少where"
    if "," in message:
        return message[3:]+",关键字必须用空格分割"
    return message
def select_nowhere(str_select, str_from):
    #不带条件查询语句验证
    message = "OK"
    if str_select != "select" and str_select != "SELECT":
        message = message + ",必须以select开头"
    if str_from != "from" and str_from != "FROM":
        message = message + ",缺少from"
    if "," in message:
        return message[3:] + ",关键字必须用空格分割"
    return message
def modify(str_update, str_set, str_where):
    # 修改语句验证
    message = "OK"
    if str_update != "update" and str_update != "UPDATE":
        message = message + ",必须以select开头"
    if str_set != "set" and str_set != "SET":
        message = message + ",缺少from"
    if str_where != "where" and str_where != "WHERE":
        message = message + ",缺少where"
    if "," in message:
        return message[3:] + ",关键字必须用空格分割"
    return message
