import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table

Base = declarative_base()

# 学生和班级的多对多关联表
classes_m2m_student = Table('classes_m2m_student', Base.metadata,
                            Column('classes_id', Integer, ForeignKey('classes.id')),
                            Column('student_id', Integer, ForeignKey('student.id')),
                            )


class Teacher(Base):
    # 教师表
    __tablename__ = 'teacher'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))


class Student(Base):
    # 学生表
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))
    qq = Column(String(20))

    classes = relationship('Classes', secondary=classes_m2m_student, backref='student')


class Classes(Base):
    # 班级表，与教师表建立外键关联
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))

    teacher = relationship('Teacher', backref='classes')


class Record(Base):
    # 上课记录表，与班级表建立外键关联
    __tablename__ = 'record'
    id = Column(Integer, primary_key=True)
    Day = Column(String(8))
    classes_id = Column(Integer, ForeignKey('classes.id'))

    classes = relationship('Classes', backref='record')


class Homework(Base):
    # 作业表，与上课记录表建立外键关联
    __tablename__ = 'homework'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer)
    submit = Column(Boolean)
    score = Column(Integer)
    record_id = Column(Integer, ForeignKey('record.id'))

    record = relationship('Record', backref='homework')




