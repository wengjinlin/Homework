#查询实现
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def select_phone(phone):
    #phone的唯一性验证，通过返回自增ID，不通过返回-1
    with open(BASE_DIR + "/db/staff_table", "r") as s_f:
        for line in s_f:
            if phone in line:
                return -1
        id = int(line.split(",")[0]) + 1
    return id
def select_staff_id(staff_id):
    #验证ID是否存在
    with open(BASE_DIR+"/db/staff_table", "r") as d_f:
        for line in d_f:
            if staff_id == line.split(",")[0]:
                return True
    return False
def select_where(str_data):
    #根据查询语句查询，返回dict
    search = {"name": search_name_phone_dept_date,
              "age": search_age,
              "phone": search_name_phone_dept_date,
              "dept": search_name_phone_dept_date,
              "enroll_date": search_name_phone_dept_date}
    return search[str_data.split(" ")[0]](str_data)
def search_all():
    res = {}
    count = 0
    with open(BASE_DIR + "/db/staff_table", "r") as d_f:
        for line in d_f:
            line_f = line.strip()
            count += 1
            res[count] = {"staff_id": line_f.split(",")[0],
                          "name": line_f.split(",")[1],
                          "age": line_f.split(",")[2],
                          "phone": line_f.split(",")[3],
                          "dept": line_f.split(",")[4],
                          "enroll_date": line_f.split(",")[5]}
    res[0] = count
    return res
def search_name_phone_dept_date(str_data):
    where = ('name', 'age', 'phone', 'dept', 'enroll_date')
    where_id = where.index(str_data.split(" ")[0])+1
    pd = str_data.split(" ")[1]
    data = str_data.split(" ")[2].replace("'", "")
    data = data.replace('"', "")
    res = {}
    count = 0
    with open(BASE_DIR+"/db/staff_table", "r") as d_f:
        for line in d_f:
            line_f = line.strip()
            if pd == "=":
                if data == line_f.split(",")[where_id]:
                    count += 1
                    res[count] = {"staff_id":line_f.split(",")[0],
                                  "name": line_f.split(",")[1],
                                  "age": line_f.split(",")[2],
                                  "phone": line_f.split(",")[3],
                                  "dept": line_f.split(",")[4],
                                  "enroll_date": line_f.split(",")[5]}
            elif pd == "like":
                if data in line_f.split(",")[where_id]:
                    count += 1
                    res[count] = {"staff_id":line_f.split(",")[0],
                                  "name":line_f.split(",")[1],
                                  "age": line_f.split(",")[2],
                                  "phone": line_f.split(",")[3],
                                  "dept": line_f.split(",")[4],
                                  "enroll_date": line_f.split(",")[5]}
    res[0] = count
    return res
def search_age(str_data):
    pd = str_data.split(" ")[1]
    data = int(str_data.split(" ")[2])
    res = {}
    count = 0
    with open(BASE_DIR + "/db/staff_table", "r") as d_f:
        for line in d_f:
            line_f = line.strip()
            age_f = int(line_f.split(",")[2])
            if pd == "=":
                if data == age_f:
                    count += 1
                    res[count] = {"staff_id":line_f.split(",")[0],
                                  "name": line_f.split(",")[1],
                                  "age": line_f.split(",")[2],
                                  "phone": line_f.split(",")[3],
                                  "dept": line_f.split(",")[4],
                                  "enroll_date": line_f.split(",")[5]}
            elif pd == ">":
                if data < age_f:
                    count += 1
                    res[count] = {"staff_id":line_f.split(",")[0],
                                  "name": line_f.split(",")[1],
                                  "age": line_f.split(",")[2],
                                  "phone": line_f.split(",")[3],
                                  "dept": line_f.split(",")[4],
                                  "enroll_date": line_f.split(",")[5]}
            elif pd == "<":
                if data > age_f:
                    count += 1
                    res[count] = {"staff_id":line_f.split(",")[0],
                                  "name": line_f.split(",")[1],
                                  "age": line_f.split(",")[2],
                                  "phone": line_f.split(",")[3],
                                  "dept": line_f.split(",")[4],
                                  "enroll_date": line_f.split(",")[5]}
    res[0] = count
    return res
# def search_phone(str_data):
#     pd = str_data.split(" ")[1]
#     data = str_data.split(" ")[2]
#     res = {}
#     count = 0
#     with open(BASE_DIR + "/db/staff_table", "r") as d_f:
#         for line in d_f:
#             line_f = line.strip()
#             if pd == "=":
#                 if data == line_f.split(",")[3]:
#                     count += 1
#                     res[count] = {"staff_id":line_f.split(",")[0],
#                                   "name": line_f.split(",")[1],
#                                   "age": line_f.split(",")[2],
#                                   "phone": line_f.split(",")[3],
#                                   "dept": line_f.split(",")[4],
#                                   "enroll_date": line_f.split(",")[5]}
#             elif pd == "like":
#                 if data in line_f.split(",")[3]:
#                     count += 1
#                     res[count] = {"staff_id":line_f.split(",")[0],
#                                   "name": line_f.split(",")[1],
#                                   "age": line_f.split(",")[2],
#                                   "phone": line_f.split(",")[3],
#                                   "dept": line_f.split(",")[4],
#                                   "enroll_date": line_f.split(",")[5]}
#     res[0] = count
#     return res
# def search_dept(str_data):
#     pd = str_data.split(" ")[1]
#     data = str_data.split(" ")[2]
#     res = {}
#     count = 0
#     with open(BASE_DIR + "/db/staff_table", "r") as d_f:
#         for line in d_f:
#             line_f = line.strip()
#             if pd == "=":
#                 if data == line_f.split(",")[4]:
#                     count += 1
#                     res[count] = {"staff_id":line_f.split(",")[0],
#                                   "name": line_f.split(",")[1],
#                                   "age": line_f.split(",")[2],
#                                   "phone": line_f.split(",")[3],
#                                   "dept": line_f.split(",")[4],
#                                   "enroll_date": line_f.split(",")[5]}
#             elif pd == "like":
#                 if data in line_f.split(",")[4]:
#                     count += 1
#                     res[count] = {"staff_id":line_f.split(",")[0],
#                                   "name": line_f.split(",")[1],
#                                   "age": line_f.split(",")[2],
#                                   "phone": line_f.split(",")[3],
#                                   "dept": line_f.split(",")[4],
#                                   "enroll_date": line_f.split(",")[5]}
#     res[0] = count
#     return res
# def search_date(str_data):
#     pd = str_data.split(" ")[1]
#     data = str_data.split(" ")[2]
#     res = {}
#     count = 0
#     with open(BASE_DIR + "/db/staff_table", "r") as d_f:
#         for line in d_f:
#             line_f = line.strip()
#             date_f = line_f.split(",")[5]
#             if pd == "=":
#                 if data == date_f:
#                     count += 1
#                     res[count] = {"staff_id":line_f.split(",")[0],
#                                   "name": line_f.split(",")[1],
#                                   "age": line_f.split(",")[2],
#                                   "phone": line_f.split(",")[3],
#                                   "dept": line_f.split(",")[4],
#                                   "enroll_date": line_f.split(",")[5]}
#             elif pd == "like":
#                 if data in line_f.split(",")[5]:
#                     count += 1
#                     res[count] = {"staff_id":line_f.split(",")[0],
#                                   "name": line_f.split(",")[1],
#                                   "age": line_f.split(",")[2],
#                                   "phone": line_f.split(",")[3],
#                                   "dept": line_f.split(",")[4],
#                                   "enroll_date": line_f.split(",")[5]}
#     res[0] = count
#     return res
