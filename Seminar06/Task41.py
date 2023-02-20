# Задача №41. Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит
# количество элементов, у которых два соседних n,
# при этом оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива.
# Массив состоит из целых чисел.
# Ввод:           Ввод:
# 5               5
# 1 2 3 4 5       1 5 1 5 1
# Вывод:          Вывод:
# 0               2
# (каждое число вводится с новой строки)

import os
os.system('cls')

n = 5
numm_list = [1, 5, 1, 5, 1]

count = 0
for i in range(len(numm_list)-2):
    test_trio = numm_list[i:i+3]
    if test_trio[0] < test_trio[1] > test_trio[2]:
        count += 1
print(count)



# arr=list(int(input(f"Enter {i+1} your num:")) for i in range(int(input("Enter num len:"))))
# n=len(arr)
# result=0
# for i in range(1,n-1):
#     if arr[i+1] < arr[i] > arr[i-1]:
#         result+=1
# print(f'Кол-во парных элементов списка = {result}')