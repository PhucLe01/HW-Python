import time

def calculate_time(func):
    def wrapper():
        x = time.time()
        func()
        print(f"Total time {time.time() - x}")
    return wrapper

@calculate_time
def sleep():
    time.sleep(2)

sleep()