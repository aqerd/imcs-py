import functools

def prime_filter(func):
    """Дан список целых чисел, возвращайте только простые целые числа"""
    @functools.wraps(func)
    def wrapper(**args):
        numbers = func(**args)
        print(numbers)
        for i in numbers:
            if i > 1:
                for j in range(2 * i, len(numbers), i):
                    numbers[j] = 0
        numbers = [x for x in numbers if x]
        return numbers
    return wrapper

@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]

if __name__ == "__main__":
    print(numbers(from_num=2, to_num=20))