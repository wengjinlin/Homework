#修改实现
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import select_impl
def modify(update):
    #查询获取where结果
    str_set = update.split(" ")[2]
    str_where = update.split(" ")[6]
    str_set_data = update[update.find(str_set) + 4:update.find(str_where) - 1]
    data = str_set_data.split(" ")[2]
    data = data.replace("'", "")
    data = data.replace('"', "")
    res = select_impl.select_where(update[update.find(str_where) + 6:])
    #修改结果
    for i in range(res[0]):
        res[i+1][str_set_data.split(" ")[0]] = data
    #持久化数据
    with open(BASE_DIR+"/db/staff_table", "r") as d_f, \
          open(BASE_DIR + "/db/staff_table_new", "w") as d_f_b:
        for line in d_f:
            find_if = 0
            for i in range(res[0]):
                if res[i + 1]["staff_id"] == line.split(",")[0]:
                    info = ",".join(list(res[i + 1].values()))+"\n"
                    d_f_b.write(info)
                    find_if = 1
                    break
            if find_if == 0:
                d_f_b.write(line)
    os.remove(BASE_DIR+"/db/staff_table")
    os.rename(BASE_DIR + "/db/staff_table_new", BASE_DIR+"/db/staff_table")