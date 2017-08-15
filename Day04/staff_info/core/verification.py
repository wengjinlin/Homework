#验证模块
import vt_data,vt_grammar
def add(phone):
    #add功能只验证phone的数据是否存在，不验证语法及数据合法性
    return vt_data.add(phone)
def delete(staff_id):
    # delete功能只验证id是否存在，不验证语法及数据合法性
    return vt_data.delete(staff_id)
def modify(update):
    # modify功能验证语法和数据
    if update.count(" ") != 9:
        return "语句错误！请检查空格"
    else:
        str_update = update.split(" ")[0]
        str_table = update.split(" ")[1]
        str_set = update.split(" ")[2]
        str_where = update.split(" ")[6]
        str_set_data = update[update.find(str_set) + 4:update.find(str_where)-1]
        str_where_data = update[update.find(str_where) + 6:]
    # 验证语法
    message = vt_grammar.modify(str_update, str_set, str_where)
    if message == "OK":
        # 验证数据
        return vt_data.modify(str_table, str_set_data, str_where_data)
    else:
        return message
def select(search):
    #select功能验证语法和数据
    if search.count(" ") != 3 and search.count(" ") != 7:
            return "语句错误！请检查空格"
    elif search.count(" ") == 7:
        str_select = search.split(" ")[0]
        str_pr = search.split(" ")[1]
        str_from = search.split(" ")[2]
        str_table = search.split(" ")[3]
        str_where = search.split(" ")[4]
        str_data = search[search.find(str_where) + 6:]
        #验证语法
        message = vt_grammar.select(str_select,str_from,str_where)
        if message == "OK":
            #验证数据
            return vt_data.select(str_pr,str_table,str_data)
        else:
            return message
    else:
        str_select = search.split(" ")[0]
        str_pr = search.split(" ")[1]
        str_from = search.split(" ")[2]
        str_table = search.split(" ")[3]
        # 验证语法
        message = vt_grammar.select_nowhere(str_select, str_from)
        if message == "OK":
            # 验证数据
            return vt_data.select_nowhere(str_pr, str_table)
        else:
            return message