import functools

def reverse_string(func):
    """Если результат функции - строка, то ее нужно перевернуть. Иначе вернуть None."""
    @functools.wraps(func)
    def wrapper():
        result = func()
        if isinstance(result, str):
            return result[::-1]
    return wrapper

@reverse_string
def get_university_name():
    return "Western Institute of Technology and Higher Education"

@reverse_string
def get_university_founding_year():
    return 1957

if __name__ == "__main__":
    print(
        get_university_name(),
        get_university_founding_year(),
        sep="\n"
    )