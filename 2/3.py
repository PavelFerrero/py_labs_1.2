def get_divisors(n):
    divisors = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.add(i)
            divisors.add(n // i)
    return sorted(divisors)

def find_numbers(start, end):
    result = []
    for num in range(start, end + 1):
        divisors = get_divisors(num)
        if len(divisors) == 6:
            result.append(divisors)
    return result

start = 312614
end = 312651
numbers = find_numbers(start, end)
for divisors in numbers:
    print(divisors)