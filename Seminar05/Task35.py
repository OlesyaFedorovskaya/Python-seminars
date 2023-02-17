# Задача №35.
# Напишите функцию, которая 
# принимает одно число и проверяет, 
# является ли оно простым
# Напоминание: Простое число - это число, 
# которое имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

import os
os.system('cls')

def simple_num(x):
    num = list(range(2,x))
    print(num)
    for i in num:
        if x % i == 0:
            return 'NO'
    return 'YES'

n = int(input('Введите число: '))
print(simple_num(n))
