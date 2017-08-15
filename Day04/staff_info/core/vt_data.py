#数据验证实现
import select_impl
def add(phone):
    return select_impl.select_phone(phone)
def delete(staff_id):
    return select_impl.select_staff_id(staff_id)
def select(str_pr,str_table,str_data):
    message = "OK"
    str_print2 = "name,age,phone,dept,enroll_date"
    #select内容
    if str_pr != "*":
        for i in range(str_pr.count(",")):
            st = str_pr.split(",")[i]
            if st not in str_print2:
                message = message + ",select内容不存在"
                break
        if str_pr.split(",")[str_pr.count(",")] not in str_print2:
            message = message + ",select内容不存在"
    #table内容
    if str_table != "staff_table":
        message = message + ",所查表不存在"
    #where内容
    if str_data.split(" ")[0] not in str_print2:
        message = message + ",where内容不存在"
    else:
        if str_data.split(" ")[0] == "age":
            if str_data.split(" ")[1] != "=" and str_data.split(" ")[1] != ">" and str_data.split(" ")[1] != "<":
                message = message + ",where条件不支持该查询"
            try:
                int(str_data.split(" ")[2])
            except:
                message = message + ",age内容有误"
        else:
            if str_data.split(" ")[1] != "=" and str_data.split(" ")[1] != "like":
                message = message + ",where条件不支持该查询"
    #返回message
    if "," in message:
        return message[3:]
    return message
def select_nowhere(str_pr, str_table):
    message = "OK"
    str_print2 = "name,age,phone,dept,enroll_date"
    # select内容
    if str_pr != "*":
        for i in range(str_pr.count(",")):
            st = str_pr.split(",")[i]
            if st not in str_print2:
                message = message + ",select内容不存在"
                break
        if str_pr.split(",")[str_pr.count(",")] not in str_print2:
            message = message + ",select内容不存在"
    # table内容
    if str_table != "staff_table":
        message = message + ",所查表不存在"
    #返回message
    if "," in message:
        return message[3:]
    return message
def modify(str_table, str_set_data, str_where_data):
    message = "OK"
    str_print2 = "name,age,phone,dept,enroll_date"
    #set内容
    if str_set_data.split(" ")[0] not in str_print2:
        message = message + ",set内容不存在"
    else:
        if str_set_data.split(" ")[0] == "age":
            try:
                int(str_set_data.split(" ")[2])
            except:
                message = message + ",age应为数字"
        if str_set_data.split(" ")[0] == "phone":
            if select_impl.select_phone(str_set_data.split(" ")[2]) == -1:
                message = message + ",phone已存在"
    # table内容
    if str_table != "staff_table":
        message = message + ",所查表不存在"
    # where内容
    if str_where_data.split(" ")[0] not in str_print2:
        message = message + ",where内容不存在"
    else:
        if str_where_data.split(" ")[0] == "age":
            if str_where_data.split(" ")[1] != "=" \
                    and str_where_data.split(" ")[1] != ">" \
                    and str_where_data.split(" ")[1] != "<":
                message = message + ",where条件不支持该查询"
            try:
                int(str_where_data.split(" ")[2])
            except:
                message = message + ",age内容有误"
        else:
            if str_where_data.split(" ")[1] != "=" and str_where_data.split(" ")[1] != "like":
                message = message + ",where条件不支持该查询"
    # 返回message
    if "," in message:
        return message[3:]
    return message
