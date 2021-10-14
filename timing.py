import time

def calculate_time(func):
    '''
    Calculate the run time of the input function.

    Parameters
    ----------
    func : function
            The function to be calculating run time on.

    return
    ----------
    string
            The run time of the input function
    '''
    def wrapper():
        x = time.time()
        func()
        print(f"Total time {time.time() - x}")
    return wrapper

@calculate_time
def sleep():
    time.sleep(2)

sleep()