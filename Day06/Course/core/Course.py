class Course(object):
    #课程基类
    def __init__(self,name,cycle,price):
        #自有属性
        self.NAME = name
        self.CYCLE = cycle
        self.PRICE = price

    def print_info(self):
        #打印课程信息
        print("课程名称：%s" % self.NAME)
        print("课程周期：%s" % self.CYCLE)
        print("课程价格：%s" % self.PRICE)