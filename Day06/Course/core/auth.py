import db_handler,Student,Teacher

def login(login,type):
    def login_1(func):
        def login_2(*args, **kwargs):
            if type == "Student":
                if not isinstance(login[type], Student.Student):
                    name = input("学员用户名：")
                    while not db_handler.if_student(name):
                        print("\033[31;1m该学员不存在，请重新输入！\033[0m")
                        name = input("学员用户名：")
                    student = db_handler.get_student(name)
                    password = input("密码：")
                    while password != student.PASSWORD:
                        print("\033[31;1m密码错误，请重新输入！\033[0m")
                        password = input("密码：")
                    login[type] = student
            if type == "Teacher":
                if not isinstance(login[type], Teacher.Teacher):
                    name = input("讲师用户名：")
                    while not db_handler.if_teacher(name):
                        print("\033[31;1m该讲师不存在，请重新输入！\033[0m")
                        name = input("讲师用户名：")
                    teacher = db_handler.get_teacher(name)
                    password = input("密码：")
                    while password != teacher.PASSWORD:
                        print("\033[31;1m密码错误，请重新输入！\033[0m")
                        password = input("密码：")
                    login[type] = teacher
            if type == "manager":
                if login["manager"] != "admin":
                    password = input("管理员密码:")
                    while password != "admin":
                        print("\033[31;1m密码错误，请重新输入！\033[0m")
                        password = input("密码：")
                    login[type] = "admin"
            return func(*args, **kwargs)
        return login_2
    return login_1
