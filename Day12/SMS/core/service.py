from baseservice import BaseService


class Service(BaseService):
    # 业务逻辑服务类
    def login(self, role, username, password):
        # 用户登录
        message = ""
        obj = None
        # 根据username查询数据
        if role == 'teacher':
            obj = self.select_teacher(username)
        elif role == 'student':
            obj = self.select_student(username)
        if obj is None:
            # 用户不存在
            message = "user does not exist"
        else:
            # 用户存在
            if password == obj.password:
                # 登录成功
                message = "login_success"
            else:
                # 密码错误
                message = "password error"
        return message, obj

    def create_classes(self, teacher, name):
        # 创建班级
        obj = self.select_classes(name)
        if obj is None:
            # 该班级名字可用,添加班级
            self.add_classes(teacher, name)
            message = 'Class creation completed'
        else:
            # 该班级名字已存在
            message = 'The class name is already exist'
        return message

    def get_student_by_qq(self, qq):
        # 通过QQ查询学员
        student = self.select_student_by_qq(qq)
        return student

    def get_student_by_id(self, id):
        # 通过ID查询学员
        student = self.select_student_by_id(id)
        return student

    def distribution_student(self, classes, student_list):
        # 分配学员
        self.relationship_classes_to_student(classes, student_list)
        return 'Success'

    def create_record(self, classes, day):
        # 创建上课记录
        self.add_record(classes, day)
        return 'Success'

    def save(self):
        # 保存数据
        self.update()

    def get_ranking(self, classes, student_id):
        # 获取排名
        ranking_list_without = []
        rank_dict = {}
        for record in classes.record:
            for homework in record.homework:
                if homework.score is not None:
                    rank_dict[homework.student_id] = 0
        for record in classes.record:
            for homework in record.homework:
                if homework.score is not None:
                    rank_dict[homework.student_id] += int(homework.score)
        for i in rank_dict.keys():
            if i != student_id:
                ranking_list_without.append(rank_dict[i])
        # 排序
        ranking_list_without.sort(reverse=True)
        rank = rank_dict[student_id]
        count = len(ranking_list_without)
        for i in range(count):
            if rank > ranking_list_without[i]:
                return i+1
        return count+1
