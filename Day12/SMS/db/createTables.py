import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from conf import config
from core import model
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 创建表结构
engine = create_engine(config.db_con(), echo=True)
model.Base.metadata.create_all(engine)

# 添加初始数据（老师和学生数据）
Session_class = sessionmaker(bind=engine)
Session = Session_class()
# #教师数据
t1 = model.Teacher(name='sublime', password='123')
t2 = model.Teacher(name='alex', password='123')
# #学生数据
s1 = model.Student(name='s1', password='123', qq='11111111')
s2 = model.Student(name='s2', password='123', qq='22222222')
s3 = model.Student(name='s3', password='123', qq='33333333')
s4 = model.Student(name='s4', password='123', qq='44444444')
s5 = model.Student(name='s5', password='123', qq='55555555')
s6 = model.Student(name='s6', password='123', qq='66666666')
s7 = model.Student(name='s7', password='123', qq='77777777')
s8 = model.Student(name='s8', password='123', qq='88888888')
Session.add_all([t1, t2, s1, s2, s3, s4, s5, s6, s7, s8])
Session.commit()
