import School,db_handler,Teacher,Student,auth,time,C_class

# S1 = School.School("School in beijing","北京")
# S2 = School.School("School in shanghai","上海")
S1 = db_handler.get_school("School in beijing")
S2 = db_handler.get_school("School in shanghai")

loggin = {"Student":object,
            "Teacher":object,
            "manager":""}

def menu(choice):
    if choice == "1":
        student_view()
    elif choice == "2":
        teacher_view()
    elif choice == "3":
        manager_view()
    elif choice == "4":
        # 退出程序
        return False
    #显示菜单
    print("/------选课系统------/")
    print("1.学生界面")
    print("2.教师登录")
    print("3.管理员登录")
    print("4.退出系统")
    return True

def student_view():
    #学员视图
    while True:
        print("------学员界面------")
        print("1.新学员注册")
        print("2.老学员登录")
        print("3.退出学员界面")
        choice = input(">>:")
        if choice == "1":
            name = input("学员用户名：")
            while db_handler.if_student(name):
                print("\033[31;1m该学员已存在，请重新输入！\033[0m")
                name = input("学员用户名：")
            password = input("密码：")
            psd = input("重复密码：")
            while password != psd:
                print("\033[31;1m两次密码不同，请重新输入！\033[0m")
                password = input("密码：")
                psd = input("重复密码：")
            print("选择学校：")
            print("\t1.%s" % S1.NAME)
            print("\t2.%s" % S2.NAME)
            student = object
            choice_2 = -1
            while choice_2 == -1:
                choice_2 = input(">>:")
                if choice_2 == "1":
                    student = Student.Student(name, password, S1)
                elif choice_2 == "2":
                    student = Student.Student(name, password, S2)
                else:
                    choice_2 = -1
            db_handler.add_student(name)
            db_handler.save_student(student)
        elif choice == "2":
            old_student()
        elif choice == "3":
            break

@auth.login(loggin,"Teacher")
def teacher_view():
    teacher = loggin["Teacher"]
    #教师登录
    while True:
        print("------教师界面------")
        print("1.上课班级")
        print("2.查看班级学员列表")
        print("3.修改学员成绩")
        print("4.退出教师界面")
        choice = input(">>:")
        if choice == "1":
            print("*****教师：%s*****" % teacher.NAME)
            print("***所教班级如下***")
            for c in teacher.C_CLASSES:
                print(c.NAME)
        elif choice == "2":
            print("*****查询班级学员*****")
            c_class_in = input("班级：")
            c_class = object
            while not isinstance(c_class,C_class.C_class):
                for c in teacher.C_CLASSES:
                    if c_class_in == c.NAME:
                        c_class = c
                if not isinstance(c_class,C_class.C_class):
                    print("\033[31;1m输入错误，请重新输入！\033[0m")
                    c_class_in = input("班级：")
            for s in c_class.STUDENTS:
                print(s.NAME)
        elif choice == "3":
            print("*****修改学员成绩*****")
            c_class_in = input("班级：")
            c_class = object
            while not isinstance(c_class, C_class.C_class):
                for c in teacher.C_CLASSES:
                    if c_class_in == c.NAME:
                        c_class = c
                if not isinstance(c_class, C_class.C_class):
                    print("\033[31;1m输入错误，请重新输入！\033[0m")
                    c_class_in = input("班级：")
            print("***该班学员成绩***")
            for s in c_class.STUDENTS:
                print("\t%s : %s" % (s.NAME,s.SCORE))
            student_in = input("学员：")
            student = object
            while not isinstance(student, Student.Student):
                for s in c_class.STUDENTS:
                    if student_in == s.NAME:
                        student = s
                if not isinstance(student, Student.Student):
                    print("\033[31;1m输入错误，请重新输入！\033[0m")
                    student_in = input("学员：")
            score = input("修改为：")
            student.set_score(score)
            db_handler.save_student(student)
            db_handler.save_teacher(teacher)
            print("\033[31;1m修改成功！\033[0m")
        elif choice == "4":
            loggin["Teacher"] = object
            break

@auth.login(loggin,"manager")
def manager_view():
    #管理员视图
    while True:
        print("------管理视图------")
        print("1.创建讲师")
        print("2.创建班级")
        print("3.创建课程")
        print("4.退出管理视图")
        choice = input(">>:")
        if choice == "1":
            print("*****创建讲师*****")
            name = input("讲师姓名：")
            if db_handler.if_teacher(name):
                print("\033[31;1m该讲师已存在！\033[0m")
            else:
                password = input("密码：")
                psd = input("重复密码：")
                while password != psd:
                    print("\033[31;1m两次密码不同，请重新输入！\033[0m")
                    password = input("密码：")
                    psd = input("重复密码：")
                print("所属学校：")
                print("\t1.%s" % S1.NAME)
                print("\t2.%s" % S2.NAME)
                choice_2 = -1
                while choice_2 == -1:
                    choice_2 = input(">>:")
                    if choice_2 == "1":
                        teacher = Teacher.Teacher(name,password,S1)
                    elif choice_2 == "2":
                        teacher = Teacher.Teacher(name, password, S2)
                    else:
                        choice_2 = -1
                db_handler.add_teacher(teacher.NAME)
                db_handler.save_teacher(teacher)
                print("\033[31;1m创建成功！\033[0m")
        elif choice == "2":
            print("*****创建班级*****")
            print("所属学校：")
            print("\t1.%s" % S1.NAME)
            print("\t2.%s" % S2.NAME)
            choice_2 = "0"
            school = object
            while choice_2 == "0":
                choice_2 = input(">>:")
                if choice_2 == "1":
                    school = S1
                elif choice_2 == "2":
                    school = S2
                else:
                    choice_2 = "0"
            print("该校课程如下，请输入选择：")
            list = {}
            for a in school.COURSES:
                list[a.NAME] = a
                print("\t%s" % a.NAME,end="\t")
            print("")
            course_in = input("课程名：")
            while course_in not in list:
                print("\033[31;1m课程名输入错误，请重新输入！\033[0m")
                course_in = input("课程名：")
            course = list[course_in]
            while True:
                teacher_in = input("教师：")
                if not db_handler.if_teacher(teacher_in):
                    print("\033[31;1m不存在该教师，请重新输入！\033[0m")
                    continue
                else:
                    teacher = db_handler.get_teacher(teacher_in)
                    if school.NAME != teacher.SCHOOL.NAME:
                        print("\033[31;1m该教师不在本校任职，请重新输入！\033[0m")
                        continue
                break
            name = input("班级名称：")
            list = []
            for a in school.C_CLASSES:
                list.append(a.NAME)
            while name in list:
                print("\033[31;1m班级已存在，请重新输入！\033[0m")
                name = input("班级名称：")
            school.create_c_class(name,teacher,course)
            teacher.add_c_classes(school.C_CLASSES[-1])
            teacher.SCHOOL = school
            db_handler.save_teacher(teacher)
            print("\033[31;1m创建成功！\033[0m")
        elif choice == "3":
            print("*****创建课程*****")
            name = input("课程名称：")
            cycle = input("课程周期：")
            price = input("课程价格：")
            print("开设学校：")
            print("\t1.%s" % S1.NAME)
            print("\t2.%s" % S2.NAME)
            choice_2 = -1
            while choice_2 == -1:
                choice_2 = input(">>:")
                if choice_2 == "1":
                    S1.create_course(name,cycle,price)
                    db_handler.save_school(S1)
                elif choice_2 == "2":
                    S2.create_course(name, cycle, price)
                    db_handler.save_school(S2)
                else:
                    choice_2 = -1
            print("\033[31;1m创建成功！\033[0m")
        elif choice == "4":
            loggin["manager"] = ""
            break

@auth.login(loggin,"Student")
def old_student():
    student = loggin["Student"]
    while True:
        print("------学员%s已登录------" % student.NAME)
        print("1.交学费")
        print("2.选择班级")
        print("3.退出登录")
        choice = input(">>:")
        if choice == "1":
            if student.PAY:
                print("\033[31;1m学费已交!\033[0m")
            else:
                try:
                    price = student.C_CLASS.COURSE.PRICE
                    print("正在交学费，请稍等...")
                    time.sleep(2)
                    student.pay()
                    db_handler.save_student(student)
                    print("\033[31;1m缴费成功!缴费：%s\033[0m" % price)
                except:
                    print("\033[31;1m请先选择班级!\033[0m")
        elif choice == "2":
            try:
                classname = student.C_CLASS.NAME
                classcourse = student.C_CLASS.COURSE.NAME
                #已选择班级
                print("*****当前班级：%s*****" % classname)
            except:
                #第一次选择班级
                print("*****本学校开设如下班级*****")
                for a in student.SCHOOL.C_CLASSES:
                    print(a.NAME)
                c_class = object
                while not isinstance(c_class,C_class.C_class):
                    choice_class = input("输入选择班级：")
                    for a in student.SCHOOL.C_CLASSES:
                        if choice_class == a.NAME:
                            c_class = a
                    if not isinstance(c_class, C_class.C_class):
                        print("\033[31;1m输入错误！\033[0m")
                c_class.add_student(student)
                student.choice_c_class(c_class)
                db_handler.save_student(student)
                print("\033[31;1m选择完成\033[0m")
        else:
            loggin["Student"] = object
            break
