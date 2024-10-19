# Напишите декоратор retry:
# декоратор вызовает функцию, которая иногда возвращает исключение. При сбое декоратор должен подождать и повторить
# попытку выполнения функции. При повторных неудачах декоратор должен ждать дольше между каждой последующей попыткой.
# Если у декоратора заканчиваются попытки, он сдается и возвращает исключение. Если все же функция выполнилась без
# исключительных ситуаций, то декоратор возвращает результат исходной функции.
#
# Не забывайте использовать functools.wraps для сохранения свойств исходной (декорируемой) функции.
#
# Пример декоратора с параметром
#
# def decorator_factory(argument):
#     def decorator(function):
#         def wrapper(*args, **kwargs):
#             # raise NotImplementedError
#
#         return wrapper
#     return decorator
#
# (еще варианты на https://stackoverflow.com/questions/5929107/decorators-with-parameters)

import functools

def retry(func):
    @functools.wraps(func)
    def wrapper(*args):
        res = func(args)
        return args
    return wrapper