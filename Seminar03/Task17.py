# Задача №17.
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

import os
os.system('cls')

my_list = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(my_list)))
my_list = set(my_list)
print(len(my_list))