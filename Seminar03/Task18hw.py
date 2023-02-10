# Задача 18: Требуется найти в массиве A[1..N]
# самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число
# N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X
# Например:
# 5
# 1 2 3 4 5
# 6
# -> 5

import os
os.system('cls')

my_list = [int(input('Введите элемент: '))
            for i in range(int(input('Введите количество элементов: ')))]
x = int(input('Введите число: '))
print(my_list)
my_list.append(x)
print(my_list)
list.sort(my_list)
print(my_list)
if x == my_list[0]:
    print(my_list[1])
elif x == my_list[-1]:
    print(my_list[-2])
else:
    b = my_list.index(x)
    b0 = b - 1
    b1 = b + 1
    if x - my_list[b0] < my_list[b1]-x:
        print(my_list[b0])
    elif x - my_list[b0] > my_list[b1]-x:
        print(my_list[b1])
    else:
        print(my_list[b0], my_list[b1])
