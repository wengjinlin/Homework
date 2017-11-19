def db_con():
    ip = "localhost"
    database = "fortress"
    con = "mysql+pymysql://root:@"+ip+"/"+database+"?charset=utf8"
    return con