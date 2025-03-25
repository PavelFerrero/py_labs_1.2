# Проверка палиндрома

# Без рекурсии
def pal(s):
    res = s == s[::-1]
    return res

print(pal([1, 2, 3, 2, 1]))  
print(pal('spam'))           

# С рекурсией
def pal_rec(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    res = pal_rec(s[1:-1])
    return res

print(pal_rec([1, 2, 3, 2, 1]))  
print(pal_rec('spam'))            

# Вычисление последовательности

# Без рекурсии
def seq(n):
    if n <= 3:
        return 1
    nums = [1, 1, 1]
    for i in range(3, n):
        next_num = nums[i-1] + nums[i-3]
        nums.append(next_num)
    return nums[-1]

print(seq(4))  
print(seq(6))  

# С рекурсией
def seq_rec(n):
    if n <= 3:
        return 1
    return seq_rec(n-1) + seq_rec(n-3)

print(seq_rec(4))  
print(seq_rec(6))  
