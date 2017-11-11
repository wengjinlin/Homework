def db_con():
    ip = "localhost"
    database = "sms"
    con = "mysql+pymysql://root:@"+ip+"/"+database+"?charset=utf8"
    return con