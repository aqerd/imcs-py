# Напишите генератор с именем generate_dates и параметрами month, day, year, который позволит генерировать
# последовательные даты, начинающиеся с заданного месяца, дня, года. (Возможно, вам поможет стандартный модуль datetime)

import datetime

def generate_dates(day, month, year):
    try:
        current = datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError("Invalid date")

    while True:
        yield current
        current += datetime.timedelta(days=1)

for i, date in zip(range(365), generate_dates(10, 11, 2024)):
    print(date)
