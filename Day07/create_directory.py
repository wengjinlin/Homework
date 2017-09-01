#软件基本目录
import os
path = os.path.dirname(os.path.abspath(__file__))
pro_name = "FTP"
pro_server_name = "server"
pro_client_name = "client"
#创建目录
os.makedirs(os.path.join(pro_name,pro_server_name,"bin"))
os.makedirs(os.path.join(pro_name,pro_server_name,"conf"))
os.makedirs(os.path.join(pro_name,pro_server_name,"core"))
os.makedirs(os.path.join(pro_name,pro_server_name,"db"))
os.makedirs(os.path.join(pro_name,pro_server_name,"log"))

os.makedirs(os.path.join(pro_name,pro_client_name,"bin"))
os.makedirs(os.path.join(pro_name,pro_client_name,"conf"))
os.makedirs(os.path.join(pro_name,pro_client_name,"core"))
os.makedirs(os.path.join(pro_name,pro_client_name,"db"))
os.makedirs(os.path.join(pro_name,pro_client_name,"log"))
#创建文件
os.path.join(path,pro_name,"readme.md")
with open(os.path.join(path,pro_name,"readme.md"),"w"):
    pass
with open(os.path.join(path,pro_name,pro_server_name,"bin","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,pro_server_name,"conf","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,pro_server_name,"core","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,pro_client_name,"bin","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,pro_client_name,"conf","__init__.py"),"w"):
    pass
with open(os.path.join(path,pro_name,pro_client_name,"core","__init__.py"),"w"):
    pass
