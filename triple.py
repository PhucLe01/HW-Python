def tripler(func):
    '''
    Run the input function three times.

    Parameters
    ----------
    func : function
            The function ti be run three times
    '''
    def wrapper():
        func()
        func()
        func()
    return wrapper

@tripler
def threeTimes():
    print("hi")

threeTimes()