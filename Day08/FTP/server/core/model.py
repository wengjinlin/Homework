class User(object):
    def __init__(self, name, password, home_content, space, limit_space):
        self.name = name
        self.password = password
        self.home_content = home_content
        self.space = space
        self.limit_space = limit_space

    def get_space(self):
        return self.space

    def get_limit_space(self):
        return self.limit_space

    def set_limit_space(self, capacity):
        self.limit_space = self.limit_space - capacity

    def get_home_content(self):
        return self.home_content
