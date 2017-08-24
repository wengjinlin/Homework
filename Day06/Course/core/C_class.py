class C_class(object):
    #班级基类
    def __init__(self,name,teacher,course):
        #自有属性
        self.NAME = name
        self.TEACHER = teacher
        self.COURSE = course
        self.STUDENTS = []

    def add_student(self,student):
        #添加学生
        self.STUDENTS.append(student)