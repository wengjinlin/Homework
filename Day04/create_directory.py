#软件基本目录
import os
path = os.path.dirname(os.path.abspath(__file__))
pro_name = "staff_info"
#创建目录
os.makedirs(pro_name+"/bin")
os.makedirs(pro_name+"/conf")
os.makedirs(pro_name+"/core")
os.makedirs(pro_name+"/db")
os.makedirs(pro_name+"/log")
#创建文件
with open(path+"/"+pro_name+"/readme.md","w"):
    pass
with open(path+"/"+pro_name+"/bin/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/conf/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/core/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/db/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/log/__init__.py","w"):
    pass

