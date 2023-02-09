# Задача №23.
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import os
os.system('cls')

from random import randint

my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
print(my_list)

new_lict = [f'{my_list[i]} > {my_list[i-1]}' for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
print(*new_lict, sep='; ')
print(len(new_lict))

# from random import randint

# my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
# print(my_list)

# counter = 0
# for i in range(1, len(my_list)):
# if my_list[i] > my_list[i-1]:
# counter += 1
