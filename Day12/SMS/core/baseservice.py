import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Teacher, Classes, Student, Record, Homework


class BaseService(object):
    # 基础服务类，建立表结构，操作数据
    def __init__(self):
        engine = create_engine(config.db_con(), echo=False)
        Session_class = sessionmaker(bind=engine)
        self.Session = Session_class()

    def select_teacher(self, name):
        # 查询教师
        teacher = self.Session.query(Teacher).filter(Teacher.name == name).first()
        return teacher

    def select_student(self, name):
        # 查询学生
        student = self.Session.query(Student).filter(Student.name == name).first()
        return student

    def select_student_by_qq(self, qq):
        # 通过QQ查询学生
        student = self.Session.query(Student).filter(Student.qq == qq).first()
        return student

    def select_student_by_id(self, id):
        # 通过id查询学生
        student = self.Session.query(Student).filter(Student.id == id).first()
        return student

    def select_classes(self, name):
        # 查询班级
        classes = self.Session.query(Classes).filter(Classes.name == name).first()
        return classes

    def add_classes(self, teacher, classes_name):
        # 添加班级
        classes = Classes(name=classes_name)
        teacher.classes.append(classes)
        self.Session.commit()

    def add_record(self, classes, day):
        # 添加上课记录,同时添加学生的逻辑关联对象Homework
        record = Record(Day=day)
        classes.record.append(record)
        for student in classes.student:
            homework = Homework(student_id=student.id, submit=False, score=None)
            record.homework.append(homework)
        self.Session.commit()

    def relationship_classes_to_student(self, classes, student_list):
        # 添加班级与学生的关联对象
        for student in student_list:
            student.classes.append(classes)
        self.Session.commit()

    def update(self):
        # 更新数据
        self.Session.commit()

# test = BaseService()
# test.select_teacher("sdfs")
# a= None
# print(a)

