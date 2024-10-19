import math
from collections import defaultdict, Counter

WORD = "связана"

def getTF(file):
    wordCounter = defaultdict(int)
    n = 0
    TF = 0
    for line in file:
        words = line.strip().split()
        for i in words:
            i = i.lower()
            wordCounter[i] += 1
            n += 1
    array = Counter(wordCounter)
    for k in array:
        # print(f'{k} = {array[k]}')
        if k == WORD and n != 0:
            TF = array[k] / n
    return TF

def getIDF(res1, res2):
    d = 2
    k = 0
    for i in [res1, res2]:
        if i != 0:
            k += 1
    IDF = math.log(abs(d) / abs(k))
    return IDF

with open('first.txt', 'r', encoding="utf-8") as f1, open('second.txt', 'r', encoding="utf-8") as f2:
    res1 = getTF(f1)
    print(f'Term frequency of word "{WORD}" in 1st file is {res1}')
    res2 = getTF(f2)
    IDF = getIDF(res1, res2)
    print(f'IDF for 1st file is {IDF}')
    print(f'TF-IDF is {res1 * IDF}')