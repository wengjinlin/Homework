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

# 添加初始数据
Session_class = sessionmaker(bind=engine)
Session = Session_class()
# # user_profile
user = model.UserProfile(username='sublime', password='123')
# # remote_user
ru1 = model.RemoteUser(username='root', password='sublime123', auth_type='ssh-password')
ru2 = model.RemoteUser(username='sublime', password='sublime123', auth_type='ssh-password')
# # host
h1 = model.Host(hostname='ubuntu-1', ip='192.168.1.9', port='22')
h2 = model.Host(hostname='ubuntu-2', ip='192.168.1.10', port='22')
# # host_group
g1 = model.HostGroup(name='group-1')
g2 = model.HostGroup(name='group-2')
g3 = model.HostGroup(name='group-3')
# # bind_host
bh1 = model.BindHost()
bh2 = model.BindHost()
bh3 = model.BindHost()
# # 建立关联关系
# ## 外键关联
bh1.host = h1
bh1.remote_user = ru1
bh2.host = h2
bh2.remote_user = ru1
bh3.host = h2
bh3.remote_user = ru2
# ## 多对多关联
user.host_groups = [g1]
user.bind_hosts = [bh3]
g1.bind_hosts = [bh1]
g2.bind_hosts = [bh1, bh2]
g3.bind_hosts = [bh1, bh3]

Session.add_all([user, ru1, ru2, h1, h2, g1, g2, g3, bh1, bh2, bh3])
Session.commit()
