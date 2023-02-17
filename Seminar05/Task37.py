# Задача №37.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы 
# и использовать циклы (даже для ввода и вывода).
# Input: 2 -> 3 4
# Output: 4 3

import os
os.system('cls')

# from random import randint

# n = int(input('Введите число: '))

# def recurs(a):
#     if a == 0:
#         print()
#         return
         
#     number = randint(0, 10)

#     print(number, end=' ')
#     recurs(a - 1)
#     print(number, end=' ')

# recurs(n)

# альтернативное решение

def print_numbers(n):
    if n > 0:
        numb = int(input('Введите число: '))
        print_numbers(n-1)
        print(numb, end=' ')
    else:
        print('Чиcла в обратном порядке: ')

N = int(input('Введите количество чисел: '))
print_numbers(N)