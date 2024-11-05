# Напишите генератор, которая вернет результат generate_dates и generate_dow в виде кортежа (день, месяц, год,
# день недели). Опять же, может быть, вам покажется полезным оператор yield from.

import datetime

def generate_dates(day, month, year):
    try:
        current = datetime.datetime(year, month, day)
    except ValueError:
        raise ValueError("Invalid date")

    while True:
        yield current
        current += datetime.timedelta(days=1)


def generate_dow(month, day, year):
    try:
        current_date = datetime.date(year, month, day)
    except ValueError:
        raise ValueError("Invalid date")
    while True:
        yield current_date.strftime('%A')
        current_date += datetime.timedelta(days=1)


def generate_date_and_dow(day, month, year):
    date_gen = generate_dates(day, month, year)
    dow_gen = generate_dow(month, day, year)

    for date, dow in zip(date_gen, dow_gen):
        yield (date.day, date.month, date.year, dow)


for i, result in zip(range(7), generate_date_and_dow(1, 11, 2024)):
    print(result)