# Задача 26: Напишите программу, 
# которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B 
# с помощью рекурсии.
# Пример:
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

import os
os.system('cls')

def Exponentiation(a, b):
    if b == 0:
        return 1
    if b == 1:
        return a
    if b != 1:
        return a * Exponentiation(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(f'Число {a} в степени {b} = {Exponentiation(a, b)}')