import Course,C_class
class School(object):
    #学校基类
    def __init__(self,name,address):
        #自有属性
        self.NAME = name
        self.ADDRESS = address
        self.COURSES = []
        self.C_CLASSES = []

    def create_course(self,name,cycle,price):
        #创建课程，并关联
        course = Course.Course(name,cycle,price)
        self.COURSES.append(course)

    def create_c_class(self,name,teacher,course):
        #创建班级，并关联
        c_class = C_class.C_class(name,teacher,course)
        self.C_CLASSES.append(c_class)


