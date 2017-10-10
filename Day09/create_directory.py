#软件基本目录
import os
path = os.path.dirname(os.path.abspath(__file__))
pro_name = "Fabric"
#创建目录
os.makedirs(os.path.join(pro_name,"bin"))
os.makedirs(os.path.join(pro_name,"conf"))
os.makedirs(os.path.join(pro_name,"core"))
os.makedirs(os.path.join(pro_name,"db"))
os.makedirs(os.path.join(pro_name,"log"))

#创建文件
with open(os.path.join(path,pro_name,"bin","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,"conf","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,"core","__init__.py"),"w"):
    pass

