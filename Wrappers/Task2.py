import functools

def prime_filter(func):
    """Дан список целых чисел, возвращайте только простые целые числа"""
    @functools.wraps(func)
    def wrapper(**args):
        numbers = func(**args)
        sieve = [1] * (max(numbers) + 1)
        sieve[0], sieve[1] = 0, 0
        for i in range(2, int(len(sieve) ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, len(sieve), i):
                    sieve[j] = 0
        return [num for num in numbers if sieve[num]]
    return wrapper

@prime_filter
def numbers(from_num, to_num):
    return [num for num in range(from_num, to_num)]

if __name__ == "__main__":
    print(numbers(from_num=2, to_num=20))