# Задача №9.
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N
# (произведение всех чисел от 1 до N)
# 0! = 1
# Решить задачу используя цикл while
# Input: 5
# Output: 120

import os
os.system('cls')

n = int(input('Введите целое неотрицательное число'))
while n < 0:
    print('Введеные неверные данные')
    n = int(input('Введите целое неотрицательное число: '))


def factorial_number(number):
    factorial = 1
    # i = 1
    # while i <= n:
    #     factorial*= i
    #     i+=1
    for i in range(1, n+1):
        factorial *= i
    return factorial

factorial_n = factorial_number(n)
print(factorial_n)


# n = int(input('Введите целое неотрицательное число'))
# factorial = 1
# while N > 1:
#     factorial *= N
#     N -= 1
# print(factorial)
