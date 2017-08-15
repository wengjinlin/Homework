#删除实现
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def delete(staff_id):
    with open(BASE_DIR+"/db/staff_table", "r") as d_f, \
          open(BASE_DIR + "/db/staff_table_new", "w") as d_f_b:
        for line in d_f:
            if staff_id != line.split(",")[0]:
                d_f_b.write(line)
    os.remove(BASE_DIR+"/db/staff_table")
    os.rename(BASE_DIR + "/db/staff_table_new", BASE_DIR+"/db/staff_table")
