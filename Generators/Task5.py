# Напишите аналог POSIX-утилиты head для показа строк из файлов (https://linuxfaq.ru/page/komanda-head)
# используя операторы for и yield. Для работы с параметрами командной стоки можно использовать argparse
# (https://docs.python.org/3/library/argparse.html) или click (https://click.palletsprojects.com/en/stable/)

# How to run this task:
# python Generators/Task5.py -n 3 Generators/TextT5.txt

import click

def head(lines_count, file):
    with open(file, 'r', encoding="utf-8") as f:
        for current_line, line in enumerate(f):
            if current_line < lines_count:
                yield line.rstrip()
            else:
                break

@click.command()
@click.option('-n', default=10, help="Number of lines")
@click.argument('file', type=click.Path(exists=True))
def hello(n, file):
    """ The head utility shall copy its input files to the standard output,
        ending the output for each file at a designated point.
        Copying shall end at the point in each input file indicated by the -n number option.
        The option-argument number shall be counted in units of lines"""
    for line in head(n, file):
        click.echo(line)


if __name__ == '__main__':
    hello()
