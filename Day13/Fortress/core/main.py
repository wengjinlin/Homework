from service import Service
import ssh


class Fortress(object):
    def __init__(self):
        self.service = Service()
        self.user = None

    def auth(self):
        # 登录
        username = input('username:').strip()
        password = input('password:').strip()
        user = self.service.login(username, password)
        if user is not None:
            self.user = user
            print('login success')
        else:
            print('username or password is wrong')

    def cmd(self, bind_host):
        ssh.run(bind_host, self.user, self.service)

    def show_hosts(self, choice):
        # 显示有权限的主机
        if choice == 'all':
            if self.user.bind_hosts:
                print('z.ungroupped(%s)' % len(self.user.bind_hosts))
            if self.user.host_groups:
                for index, group in enumerate(self.user.host_groups):
                    print('%s.%s(%s)' % (index, group, len(group.bind_hosts)))
        else:
            if choice == 'z':
                if self.user.bind_hosts:
                    print('/---------------Group:ungroupped hosts---------------/')
                    for index, bind_host in enumerate(self.user.bind_hosts):
                        print('%s.%s' % (index, bind_host))
                    choice_hosts = input("[%s______]:" % self.user).strip()
                    try:
                        ch = int(choice_hosts)
                        if self.user.bind_hosts[ch]:
                            self.cmd(self.user.bind_hosts[ch])
                        else:
                            print('choice error')
                    except:
                        print('Input error')
                else:
                    print('You have no ungroupped host')
            else:
                try:
                    c = int(choice)
                    if self.user.host_groups[c]:
                        print('/---------------Group:%s hosts---------------/' % self.user.host_groups[c])
                        for index, bind_host in enumerate(self.user.host_groups[c].bind_hosts):
                            print('%s.%s' % (index, bind_host))
                        choice_hosts = input("[%s______]:" % self.user).strip()
                        try:
                            ch = int(choice_hosts)
                            if self.user.host_groups[c].bind_hosts[ch]:
                                self.cmd(self.user.host_groups[c].bind_hosts[ch])
                            else:
                                print('choice error')
                        except:
                            print('Input error')
                    else:
                        print('choice error')
                except:
                    print('Input error')

    def run(self):
        while self.user is None:
            print("---------------Fortress---------------")
            self.auth()
        while True:
            print("---------------Fortress:%s---------------" % self.user)
            self.show_hosts('all')
            choice = input("[%s]:" % self.user).strip()
            if len(choice) == 0:
                continue
            if choice == "exit":
                break
            self.show_hosts(choice)
