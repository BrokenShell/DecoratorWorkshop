import pickle


class FuncCache:

    def __init__(self, func):
        self.cache = {}
        self.func = func
        self.__doc__ = func.__doc__

    def __call__(self, *args, **kwargs):
        key = (pickle.dumps(args), pickle.dumps(kwargs))
        if key not in self.cache:
            self.cache[key] = self.func(*args, **kwargs)
        return self.cache[key]


@FuncCache
def fib(n):
    """ Fibonacci with recursion """
    if n in {0, 1}:
        return n
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    help(fib)
