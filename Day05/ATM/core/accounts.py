# -*- coding: utf-8 -*-
import db_handler
def add(user):
    #添加用户，返回信息
    message = "添加成功"
    if db_handler.existence(user["user_name"]):
        message = "该用户已存在！"
    else:
        db_handler.add(user["user_name"])
        db_handler.save(user)
    return message
def select(user_name):
    #根据用户名查找用户并返回，如不存在，返回空字典
    user = {}
    if db_handler.existence(user_name):
        user = db_handler.getuser(user_name)
    return user
def save(user):
    #保存用户信息
    db_handler.save(user)
def getbill(user,date):
    #打印用户账单
    db_handler.print_bill(user["user_name"],date)
def mall_select(user_name):
    # 根据用户名查找用户并返回，如不存在，返回空字典
    user = {}
    if db_handler.mall_existence(user_name):
        user = db_handler.mall_getuser(user_name)
    return user