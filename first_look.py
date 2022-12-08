from functools import wraps


def logger(func):
    @wraps(func)
    def worker(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}: {result}")
        return result
    return worker


@logger
def add_one(n: int) -> int:
    """ Takes an int adds 1 and returns the result """
    return n + 1


@logger
def add_two(n: int) -> int:
    """ Takes an int adds 2 and returns the result """
    return n + 2


if __name__ == '__main__':
    print(add_two(10))
