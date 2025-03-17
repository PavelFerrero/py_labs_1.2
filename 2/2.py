def count_base7():
    value = 49**10 + 7**30 - 49
    base7 = []
    while value > 0:
        base7.append(value % 7)
        value = value // 7
    return base7.count(6)

print(count_base7())