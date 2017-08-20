#软件基本目录
import os
path = os.path.dirname(os.path.abspath(__file__))
pro_name = "ATM"
sub_pro1 = "atm"
sub_pro2 = "shopping_mall"
#创建目录
os.makedirs(pro_name+"/"+sub_pro1+"/bin")
os.makedirs(pro_name+"/"+sub_pro1+"/conf")
os.makedirs(pro_name+"/"+sub_pro1+"/core")
os.makedirs(pro_name+"/"+sub_pro1+"/db")
os.makedirs(pro_name+"/"+sub_pro1+"/log")
os.makedirs(pro_name+"/"+sub_pro2)
#创建文件
with open(path+"/"+pro_name+"/readme.md","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro1+"/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro2+"/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro1+"/bin/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro1+"/conf/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro1+"/core/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro1+"/db/__init__.py","w"):
    pass
with open(path+"/"+pro_name+"/"+sub_pro1+"/log/__init__.py","w"):
    pass

