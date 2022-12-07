import functools


def solution(no=1):
    def decorator_solution(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{no}: {result}")
            return result

        return wrapper

    return decorator_solution
