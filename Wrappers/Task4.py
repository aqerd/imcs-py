# Напишите декоратор retry:
# декоратор вызовает функцию, которая иногда возвращает исключение. При сбое декоратор должен подождать и повторить
# попытку выполнения функции. При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой.
# Если у декоратора заканчиваются попытки, он сдается и возвращает исключение. Если все же функция выполнилась без
# исключительных ситуаций, то декоратор возвращает результат исходной функции.
# Не забывайте использовать functools.wraps для сохранения свойств исходной (декорируемой) функции.

# Пример декоратора с параметром

# def decorator_factory(argument):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             # raise NotImplementedError
#
#         return wrapper
#     return decorator

# (еще варианты на https://stackoverflow.com/questions/5929107/decorators-with-parameters)

import functools
import time
from random import random

def retry(max_retries=5, initial_delay=1, factor=2):
    print(type(max_retries))
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            delay = initial_delay
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise
                    else:
                        print(f'Attempt {attempt + 1} terminated by error: "{e}". Repeating process in {delay} seconds.')
                        time.sleep(delay)
                        delay *= factor
        return wrapper
    return decorator

@retry
def unstable_function():
    if random.randint(0, 10) < 5:
        raise ValueError("Error")
    return "Success!"

try:
    result = unstable_function()
    print(f"Result: {result}")
except Exception as e:
    print(f"Function ended with exception: {e}")
