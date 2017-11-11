from service import Service


class SMS(object):
    def __init__(self):
        self.service = Service()
        self.login_user = {"role": None,
                           "user": None}

    def login_teacher(self):
        # 教师登录
        username = input('用户名>>:').strip()
        password = input('密码>>:').strip()
        message, teacher = self.service.login('teacher', username, password)
        if message == 'login_success':
            self.login_user["role"] = 'teacher'
            self.login_user["user"] = teacher
        print(message)

    def login_student(self):
        # 学生登录
        username = input('用户名>>:').strip()
        password = input('密码>>:').strip()
        message, student = self.service.login('student', username, password)
        if message == 'login_success':
            self.login_user["role"] = 'student'
            self.login_user["user"] = student
        print(message)

    def create_classes(self):
        # 新建班级
        print('/*********创建班级*********/')
        name = input("班级名字>>:").strip()
        message = self.service.create_classes(self.login_user["user"], name)
        print(message)

    def choice_classes(self):
        # 选择将要操作的班级
        classes_name_list = []
        # 打印该教师所教班级
        i = 0
        for classes in self.login_user["user"].classes:
            if i % 3 == 0 and i != 0:
                print()
            classes_name_list.append(classes.name)
            print(classes.name, end="  ")
            i += 1
        print()
        print()
        # 输入选择
        while True:
            classes_name = input('班级名称>>:').strip()
            if classes_name not in classes_name_list:
                print("Input error")
            else:
                break
        for classes in self.login_user["user"].classes:
            if classes_name == classes.name:
                return classes

    def choice_record(self, classes):
        # 选择将要操作的上课记录
        record_list = []
        if not classes.record:
            # 还未添加上课记录
            print('This class has no record')
        else:
            print('/********该班级上课记录********/')
            # 显示已创建的上课记录
            i = 0
            for record in classes.record:
                if i % 7 == 0 and i != 0:
                    print()
                print(record.Day, end="  ")
                record_list.append(record.Day)
                i += 1
            print()
            print()
        while True:
            record_day = input('选择上课记录>>:').strip()
            if record_day not in record_list:
                print("The choice is error")
            else:
                break
        for record in classes.record:
            if record_day == record.Day:
                return record

    def choice_student(self, classes):
        # 选择将要分配的学员列表
        choice_student_list = []
        qq_list = []  # 保证不重复添加学员
        if classes.student:
            for student in classes.student:
                qq_list.append(student.qq)
        print("输入学员QQ号，每个QQ号跟回车，输入“OK”结束输入")
        while True:
            qq = input('>>:').strip()
            if qq == "OK" or qq == "ok" or qq == "Ok" or qq == "oK":
                if len(choice_student_list) == 0:
                    print('You should enter at least one student')
                    continue
                break
            if qq in qq_list:
                print("Don't repeat")
            else:
                student = self.service.get_student_by_qq(qq)
                if student is None:
                    print("QQ number is error")
                else:
                    choice_student_list.append(student)
                    qq_list.append(qq)
        return choice_student_list

    def distribution_student(self):
        # 分配学员
        print('/********分配学员********/')
        choice_classes = self.choice_classes()  # 选择将要分配学员的班级
        choice_student_list = self.choice_student(choice_classes)  # 选择将要分配的学员列表
        message = self.service.distribution_student(choice_classes, choice_student_list)
        print(message)

    def management_classes(self):
        # 管理班级
        while True:
            print('********管理班级********')
            print('1.创建新班级')
            print('2.分配学员')
            print('3.返回')
            choice = input(">>:").strip()
            if choice == '1':
                self.create_classes()
            elif choice == '2':
                self.distribution_student()
            elif choice == '3':
                break

    def create_record(self):
        # 创建上课记录
        record_list = []
        print('********添加上课记录********')
        choice_classes = self.choice_classes()  # 选择将要添加记录的班级
        # 判断该班级是否有学员
        if not choice_classes.student:
            print('This class has no student')
        else:
            if not choice_classes.record:
                # 还未添加上课记录
                print('This class has no record')
            else:
                print('/********该班级已有记录********/')
                # 显示已创建的上课记录
                i = 0
                for record in choice_classes.record:
                    if i % 7 == 0 and i != 0:
                        print()
                    print(record.Day, end="  ")
                    record_list.append(record.Day)
                    i +=1
                print()
                print()
            while True:
                record_day = input('新上课记录>>:').strip()
                if record_day in record_list:
                    print("Don't repeat")
                else:
                    break
            message = self.service.create_record(choice_classes, record_day)
            print(message)

    def correcting_homework(self):
        # 批改作业
        print('********批改作业********')
        choice_classes = self.choice_classes()  # 选择将要批改的班级
        # 判断该班级是否有学员
        if not choice_classes.student:
            print('This class has no student')
        else:
            record = self.choice_record(choice_classes)  # 选择将要批改的上课记录
            for homework in record.homework:
                # 开始批改作业
                if homework.submit and homework.score is None:
                    # 只批改已提交且未被批改的作业
                    student = self.service.get_student_by_id(homework.student_id)
                    description = "学生：%s QQ：%s (打分：0-100的整数)" % (student.name, student.qq)
                    print(description)
                    while True:
                        score_str = input(">>:").strip()
                        try:
                            score = int(score_str)
                            break
                        except Exception as e:
                            print("Enter is error")
                    homework.score = score
                    self.service.save()
            print("Correction completed")

    def get_classes(self):
        # 学生选择班级
        classes_list = []
        print("/********已参加班级********/")
        i = 0
        for classes in self.login_user["user"].classes:
            if i % 3 == 0 and i != 0:
                print()
            print(classes.name, end="  ")
            classes_list.append(classes.name)
            i += 1
        print()
        print()
        while True:
            choice_classes = input('选择班级>>:').strip()
            if choice_classes in classes_list:
                break
            print("Enter is error")
        for classes in self.login_user["user"].classes:
            if classes.name == choice_classes:
                return classes

    def get_record(self, classes, no):
        # 学生选择上课记录,no=-1表示获取最新的
        record_list = []
        if len(classes.record) == 0:
            return None
        else:
            if no == -1:
                return classes.record[len(classes.record)-1]
            else:
                print("/********上课记录********/")
                i = 0
                for record in classes.record:
                    if i % 7 == 0 and i != 0:
                        print()
                    print(record.Day, end="  ")
                    record_list.append(record.Day)
                    i += 1
                print()
                print()
                while True:
                    record_day = input("选择上课日期>>:").strip()
                    if record_day not in record_list:
                        print("Enter is error")
                    else:
                        break
                for record in classes.record:
                    if record.Day == record_day:
                        return record

    def submit_homework(self):
        # 提交作业
        choice_homework = None
        print('********提交作业********')
        classes = self.get_classes()
        record = self.get_record(classes, -1)
        if record is None:
            print("This class has no record")
        else:
            for homework in record.homework:
                if homework.student_id == self.login_user["user"].id:
                    choice_homework = homework
                    break
            if choice_homework.submit:
                print("Homework already submitted")
            else:
                print("Are you sure?(y/n)")
                while True:
                    cmd = input(">>:").strip()
                    if cmd == "y" or cmd == "Y":
                        # 提交作业
                        choice_homework.submit = True
                        self.service.save()
                        print("Success")
                        break
                    elif cmd == "n" or cmd == "N":
                        break

    def check_homework(self):
        # 查看作业成绩
        choice_homework = None
        print('********查看成绩********')
        classes = self.get_classes()
        if len(classes.record) == 0:
            print("This class has no record")
        else:
            print("/********%s 成绩列表********/" % classes.name)
            for record in classes.record:
                for homework in record.homework:
                    if homework.student_id == self.login_user["user"].id:
                        choice_homework = homework
                        break
                if choice_homework.submit:
                    print("%s：%s" % (record.Day, choice_homework.score))
                else:
                    print("%s：%s" % (record.Day, "未提交"))

    def check_ranking(self):
        # 查看排名
        print('********查看成绩排名********')
        classes = self.get_classes()
        if len(classes.record) == 0:
            print("This class has no record")
        else:
            ranking = self.service.get_ranking(classes, self.login_user["user"].id)
            print("The ranking in %s is %s" % (classes.name, str(ranking)))

    def show_menu(self):
        role = self.login_user["role"]
        while True:
            print('/-----------当前用户：%s[%s]-----------/'
                  % (role, self.login_user["user"].name))
            if role == 'teacher':
                # 教师视图
                print('1.管理班级')
                print('2.添加上课记录')
                print('3.批改作业')
                print('4.退出登录')
                choice = input(">>:").strip()
                if choice == '1':
                    self.management_classes()
                elif choice == '2':
                    self.create_record()
                elif choice == '3':
                    self.correcting_homework()
                elif choice == '4':
                    self.login_out()
                    break
            elif role == "student":
                # 学生视图
                print('1.提交作业')
                print('2.查看作业成绩')
                print('3.查看排名')
                print('4.退出登录')
                choice = input(">>:").strip()
                if choice == '1':
                    self.submit_homework()
                elif choice == '2':
                    self.check_homework()
                elif choice == '3':
                    self.check_ranking()
                elif choice == '4':
                    self.login_out()
                    break

    def login_out(self):
        # 退出登录
        self.login_user = {"role": None,
                           "user": None}

    def run(self):
        while True:
            print("-----------学生管理系统-----------")
            print("1.教师登录")
            print("2.学生登录")
            print("3.退出系统")
            choice = input(">>:").strip()
            if choice == "1":
                self.login_teacher()
            elif choice == '2':
                self.login_student()
            elif choice == "3":
                break
            else:
                continue
            if self.login_user["role"] is None:
                print("请重新登录")
            else:
                self.show_menu()
