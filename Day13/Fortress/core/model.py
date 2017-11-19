from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, Table, DateTime
from sqlalchemy_utils import ChoiceType

Base = declarative_base()


class Host(Base):
    # 主机表
    __tablename__ = 'host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(64), unique=True)
    ip = Column(String(64), unique=True)
    port = Column(Integer, default=22)

    def __repr__(self):
        return self.hostname


class HostGroup(Base):
    # 主机分组表
    __tablename__ = 'host_group'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)

    bind_hosts = relationship('BindHost', secondary='bindhost_m2m_hostgroup', backref='host_groups')

    def __repr__(self):
        return self.name


class RemoteUser(Base):
    # 主机用户(root, web, mysql)
    __tablename__ = 'remote_user'
    id = Column(Integer, primary_key=True)
    AuthTypes = [('ssh-password', 'SSH/Password'), ('ssh-key', 'SSH/KEY')]
    auth_type = Column(ChoiceType(AuthTypes))
    username = Column(String(32))
    password = Column(String(128))

    def __repr__(self):
        return self.username


class UserProfile(Base):
    # 堡垒机用户
    __tablename__ = 'user_profile'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    password = Column(String(128))

    bind_hosts = relationship('BindHost', secondary='user_m2m_bindhost', backref='user_profiles')
    host_groups = relationship('HostGroup', secondary='userprofile_m2m_hostgroup', backref='user_profiles')

    def __repr__(self):
        return self.username


class BindHost(Base):
    '''
    192.168.1.12   web
    192.168.1.12   mysql
    '''
    __tablename__ = 'bind_host'
    id = Column(Integer, primary_key=True)
    host_id = Column(Integer, ForeignKey('host.id'))
    remoteuser_id = Column(Integer, ForeignKey('remote_user.id'))

    host = relationship('Host', backref='bind_hosts')
    remote_user = relationship('RemoteUser', backref='bind_hosts')

    def __repr__(self):
        return '<%s -- %s -- %s>' % (self.host, self.host.ip, self.remote_user.username)


class AuditLog(Base):
    # 日志
    __tablename__ = 'audit_log'
    id = Column(Integer, primary_key=True)
    userprofile_id = Column(Integer, ForeignKey('user_profile.id'))
    bindhost_id = Column(Integer, ForeignKey('bind_host.id'))
    action = Column(String(64))
    date = Column(DateTime)

    user_profile = relationship('UserProfile', backref='audit_logs')
    bind_host = relationship('BindHost', backref='audit_logs')

    def __repr__(self):
        return '%s -- %s -- %s --%s' % (self.date, self.user_profile, self.bind_hosts, self.action)


# 堡垒机用户与绑定主机表的多对多关联表
user_m2m_bindhost = Table('user_m2m_bindhost', Base.metadata,
                          Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                          Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                          )


# 绑定主机表与主机组的多对多关联表
bindhost_m2m_hostgroup = Table('bindhost_m2m_hostgroup', Base.metadata,
                               Column('bindhost_id', Integer, ForeignKey('bind_host.id')),
                               Column('hostgroup_id', Integer, ForeignKey('host_group.id')),
                               )


# 堡垒机用户与主机组的多对多关联表
userprofile_m2m_hostgroup = Table('userprofile_m2m_hostgroup', Base.metadata,
                               Column('userprofile_id', Integer, ForeignKey('user_profile.id')),
                               Column('hostgroup_id', Integer, ForeignKey('host_group.id')),
                               )
