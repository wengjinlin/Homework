import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from conf import config
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model import Host,HostGroup, RemoteUser, UserProfile, BindHost, AuditLog
import datetime


class Service(object):
    def __init__(self):
        engine = create_engine(config.db_con(), echo=False)
        Session_class = sessionmaker(bind=engine)
        self.Session = Session_class()

    def login(self, username, password):
        # 验证用户登录
        user = self.Session.query(UserProfile).filter(UserProfile.username == username).first()
        if user is not None and password == user.password:
            return user
        return None

    def log(self, user, bind_host, action):
        # 记录操作日志
        if action == 'login':
            log = AuditLog(action='login', date=datetime.datetime.now())
        else:
            log = AuditLog(action='cmd:'+action, date=datetime.datetime.now())
        log.user_profile = user
        log.bind_host = bind_host
        self.Session.add(log)
        self.Session.commit()

