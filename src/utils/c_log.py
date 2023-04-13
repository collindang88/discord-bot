import datetime
from termcolor import cprint
from functools import wraps

def log(message, log_condition=None):
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            if log_condition is None or log_condition(*args, **kwargs):
                cprint(f'[{str(datetime.datetime.now())}]', 'yellow', end=' ')
                print(message)
            return await func(*args, **kwargs)
        return wrapper
    return decorator