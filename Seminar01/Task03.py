# Задача №3. В некоторой школе решили 
# набрать три новых математических класса 
# и оборудовать кабинеты для них новыми партами. 
# За каждой партой может сидеть два учащихся. 
# Известно количество учащихся в каждом из трех классов. 
# Выведите наименьшее число парт, 
# которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

import os
os.system('cls')

print('Введите количество учеников: ')
n = int(input('в 1м классе = '))
m = int(input('в 2м классе = '))
o = int(input('в 3м классе = '))
print(f'Количество необходимых парт: {(((n+m+o)+((n+m+o)%2))//2)}')

# a = int(input("Student number "))
# b = int(input("Student number "))
# c = int(input("Student number "))


# def Tables(a):
# return a//2+a % 2

# print("Количество парт для покупки", Tables(a) + Tables(b) + Tables(c))

# print(a//2 + a%2 + b//2 + b%2 + c//2 + c%2)