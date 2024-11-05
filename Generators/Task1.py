# Напишите генератор, которые выводит простые числа или другую рекуррентную числовую последовательность

def fib_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for fib in fib_generator():
    if fib <= 100000:
        print(fib, end=" ")
    else:
        break