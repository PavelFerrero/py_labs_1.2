from itertools import product

def count_words():
    first_two = ['X', 'Z', 'A', 'B', 'C', 'D', 'E']
    last_two = ['A', 'B', 'C', 'D', 'E']
    
    # X и Z только на первых двух позициях
    first_two_filtered = ['X', 'Z', 'A', 'B', 'C', 'D', 'E']
    
    # Генерация всех возможных комбинаций
    count = 0
    for p in product(first_two_filtered, repeat=2):
        for q in product(last_two, repeat=2):
            count += 1
    return count

print(count_words())