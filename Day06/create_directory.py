#软件基本目录
import os
path = os.path.dirname(os.path.abspath(__file__))
pro_name = "Course"
#创建目录
os.makedirs(pro_name+os.sep+"bin")
os.makedirs(pro_name+os.sep+"conf")
os.makedirs(pro_name+os.sep+"core")
os.makedirs(pro_name+os.sep+"db")
os.makedirs(pro_name+os.sep+"log")
#创建文件
file_addr = path+os.sep+pro_name+os.sep
with open(file_addr+"readme.md","w"):
    pass
with open(file_addr+os.sep+"bin"+os.sep+"__init__.py","w"):
    pass
with open(file_addr+os.sep+"conf"+os.sep+"__init__.py","w"):
    pass
with open(file_addr+os.sep+"core"+os.sep+"__init__.py","w"):
    pass
