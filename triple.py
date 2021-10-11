def tripler(func):
    def wrapper():
        func()
        func()
        func()
    return wrapper