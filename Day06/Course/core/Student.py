class Student(object):
    #学生基类
    def __init__(self,name,password,school):
        #自有属性
        self.NAME = name
        self.PASSWORD = password
        self.SCHOOL = school
        self.PAY = False
        self.SCORE = ""
        self.C_CLASS = object

    def choice_c_class(self,c_class):
        #选择班级并关联
        self.C_CLASS = c_class

    def pay(self):
        #缴费
        self.PAY = True

    def set_score(self,score):
        #修改成绩
        self.SCORE = score