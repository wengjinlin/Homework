class Teacher(object):
    #教师基类
    def __init__(self,name,password,school):
        #自有属性
        self.NAME = name
        self.PASSWORD = password
        self.SCHOOL = school
        self.C_CLASSES = []

    def add_c_classes(self,c_class):
        #增加班级
        self.C_CLASSES.append(c_class)

