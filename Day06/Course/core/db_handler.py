import os,pickle

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR+os.sep+"db"+os.sep

import C_class

def save_school(school):
    #持久化学校信息
    path_school = path+"schools"+os.sep+school.NAME
    with open(path_school,"wb")  as f_w:
        f_w.write(pickle.dumps(school))

def get_school(name):
    #获取学校信息到内存
    path_school = path + "schools" + os.sep + name
    with open(path_school, "rb")  as f_w:
        return pickle.load(f_w)

def if_teacher(name):
    #判断是否存在该教师
    path_teacher = path + "teachers" + os.sep + "teachers"
    with open(path_teacher,"r",encoding="utf8") as f_a:
        for line in f_a:
            if name in line:
                return True
    return False

def save_teacher(teacher):
    #持久化教师信息
    path_teacher = path+"teachers"+os.sep+teacher.NAME
    with open(path_teacher,"wb")  as f_w:
        f_w.write(pickle.dumps(teacher))
    save_school(teacher.SCHOOL)

def add_teacher(name):
    #添加教师名字到教师表
    path_teacher = path + "teachers" + os.sep + "teachers"
    with open(path_teacher, "a")  as f_w:
        f_w.write(name+"\n")

def get_teacher(name):
    #获取教师信息到内存
    path_teacher = path + "teachers" + os.sep + name
    with open(path_teacher, "rb")  as f_w:
        teacher = pickle.load(f_w)
    teacher.SCHOOL = get_school(teacher.SCHOOL.NAME)
    if teacher.C_CLASSES:
        list = []
        for tc in teacher.C_CLASSES:
            for sc in teacher.SCHOOL.C_CLASSES:
                if tc.NAME == sc.NAME:
                    list.append(sc)
                    break
        teacher.C_CLASSES = list
    return teacher

def save_student(student):
    #持久化学生信息
    path_student = path+"students"+os.sep+student.NAME
    with open(path_student,"wb")  as f_w:
        f_w.write(pickle.dumps(student))
    save_school(student.SCHOOL)

def add_student(name):
    #添加学生名字到学生表
    path_student = path + "students" + os.sep + "students"
    with open(path_student, "a")  as f_w:
        f_w.write(name+"\n")

def if_student(name):
    #判断是否存在该学生
    path_student = path + "students" + os.sep + "students"
    with open(path_student,"r",encoding="utf8") as f_a:
        for line in f_a:
            if name in line:
                return True
    return False

def get_student(name):
    #获取学生信息到内存
    path_student = path + "students" + os.sep + name
    with open(path_student, "rb")  as f_w:
        student = pickle.load(f_w)
    student.SCHOOL = get_school(student.SCHOOL.NAME)
    if isinstance(student.C_CLASS,C_class.C_class):
        student.C_CLASS = get_c_class(student.C_CLASS.NAME,student.SCHOOL.NAME)
    return student

def get_c_class(classname,schoolname):
    school = get_school(schoolname)
    for c in school.C_CLASSES:
        if c.NAME == classname:
            return c