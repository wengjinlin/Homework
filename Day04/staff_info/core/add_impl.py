#添加实现
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def add(satff_id,name,age,phone,dept,enroll_date):
    info = satff_id+","+name+","+age+","+phone+","+dept+","+enroll_date+"\n"
    with open(BASE_DIR+"/db/staff_table", "a") as a_f:
        a_f.write(info)
