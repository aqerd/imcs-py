# Напишите генератор с именем generate_dow и параметрами month, day, year, который будет генерировать последовательные
# дни недели (в виде строк), начинающиеся с данного месяца, дня, года. Например, если месяц, день, год, это 10, 21, 2020
# соответственно, он вернет «Среда», «Четверг», «Пятница» и так далее.

import datetime

def generate_dow(month, day, year):
    try:
        current = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date")
    while True:
        yield current.strftime('%A')
        current += datetime.timedelta(days=1)

dow_gen = generate_dow(11, 1, 2024)
for _ in range(5):
    print(next(dow_gen))
