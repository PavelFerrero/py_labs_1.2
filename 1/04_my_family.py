#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ["Отец","Мама","Кошка"]


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ["Иван",180],["Виктория",167],["Теззи",42]
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см
print("Рост отца - ",str(my_family_height[0][1])," см")
# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
print("Общий рост моей семьи - ", my_family_height[0][1]+my_family_height[1][1]+my_family_height[2][1])
print(my_family_height[0][1],my_family_height[1][1],my_family_height[2][1])