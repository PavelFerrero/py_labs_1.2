from itertools import product

def first():
    """"
    >>> first()
    100
    """
    first_two = ['X', 'Z']
    last_two = ['A', 'B', 'C', 'D', 'E']
    # Генерация всех возможных комбинаций
    count = 0
    for p in product(first_two, repeat=2):
        for q in product(last_two, repeat=2):
            count += 1
    return count

print(first())

def second():
    """"
    >>> second()
    18
    """
    x = 49**10 + 7**30 - 49
    s = ''
    while x != 0: 
        s += str(x % 7)
        x //= 7
    s = s[::-1]
    return(s.count("6"))
print(second())

def thirst():
    """"
    >>> thirst()
    1 2 4 78157 156314 312628
    1 3 9 34739 104217 312651
    """
    for x in range(312614,312652):
        d = [1,x]
        k = 0
        for i in range (2,x//2+1):
            if x%i==0:
                d.append(i)
                k+=1
                if k>4:
                    break
        if k==4:
            d.sort()
            print(*d)
    return('_')
print(thirst())

import doctest
doctest.testmod()