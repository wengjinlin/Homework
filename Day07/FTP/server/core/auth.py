def login_if(login_user):
    def middle(func):
        def inside(*args,**kwargs):
            if login_user.NAME == "tourist":
                args[0].sendall("login_fail".encode("utf-8"))
            else:
                args[0].sendall("login_success".encode("utf-8"))
                return func(*args,**kwargs)
        return inside
    return middle